import argparse
import importlib.util
import uuid
import os
from SubmissionManager import SubmissionManager, SubmissionSystem

from Logger import *

def get_args():
  parser = argparse.ArgumentParser(description="Submitter")

  parser.add_argument("--app", type=str, help="name of the app to run", required=True)
  parser.add_argument("--config", type=str, required=True, help="config to be executed by the app")
  
  parser.add_argument("--files_config", type=str, default=None, help="path to a python config with a list of input/output paths")
  
  parser.add_argument("--local", action="store_true", default=False, help="run locally")
  parser.add_argument("--condor", action="store_true", default=False, help="run on condor")
  
  parser.add_argument(
    "--job_flavour", 
    type=str, 
    default="espresso",
    help="condor job flavour: espresso (20 min), microcentury (1h), longlunch (2h), workday (8h), tomorrow (1d), testmatch (3d), nextweek (1w)"
  )
  parser.add_argument(
    "--resubmit_job", 
    type=int,
    default=None,
    help="use this option to resubmitt a specific job"
  )
  
  parser.add_argument("--dry", action="store_true", default=False, help="dry run, without submitting to condor")
  
  args = parser.parse_args()
  return args


def get_files_config(args):
  info(f"Reading files config from path: {args.files_config}")
  spec = importlib.util.spec_from_file_location("files_module", args.files_config)
  files_config = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(files_config)
  return files_config


def update_files_config(path, sample):
  with open(path, "r") as f:
    lines = f.readlines()
  with open(path, "w") as f:
    for line in lines:
      if line.startswith("sample_path"):
        line = f"sample_path = \"{sample}\"\n"
      f.write(line)


def main():
  args = get_args()
  
  submission_system = SubmissionSystem.unknown
  if args.local:
    submission_system = SubmissionSystem.local
  if args.condor:
    submission_system = SubmissionSystem.condor
  
  if submission_system == SubmissionSystem.unknown:
    fatal("Please select either --local or --condor")
    exit()
  
  files_config = get_files_config(args)
  
  
  tmp_files_config_paths = []
  
  if hasattr(files_config, "samples"):
    samples = files_config.samples
    for sample in samples:
      hash_string = str(uuid.uuid4().hex[:6])
      tmp_files_config_path = f"/tmp/files_config_{hash_string}.py"
      
      info(f"Creating a temporary files config: {tmp_files_config_path}")
      os.system(f"cp {args.files_config} {tmp_files_config_path}")
      update_files_config(tmp_files_config_path, sample)
      tmp_files_config_paths.append(tmp_files_config_path)
  else:
    tmp_files_config_paths.append(args.files_config)
  
  for files_config_path in tmp_files_config_paths:
    submission_manager = SubmissionManager(submission_system, args.app, args.config, files_config_path)

    if submission_system == SubmissionSystem.local:  
      submission_manager.run_locally()
    if submission_system == SubmissionSystem.condor:
      submission_manager.run_condor(args.job_flavour, args.resubmit_job, args.dry)
  

if __name__ == "__main__":
  main()
