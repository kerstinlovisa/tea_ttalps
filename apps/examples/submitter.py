import argparse
import os
import importlib.util

def get_args():
  parser = argparse.ArgumentParser(description="Submitter")

  parser.add_argument("--app", type=str, help="name of the app to run", required=True)
  parser.add_argument("--config", type=str, default="", help="config to be executred by the app")
  
  parser.add_argument("--local", action="store_true", default=False, help="run locally")
  parser.add_argument("--condor", action="store_true", default=False, help="run on condor")
  
  parser.add_argument("--files_config", type=str, default="", help="path to a python config with a list of input/output paths")

  args = parser.parse_args()
  return args

def run_locally_with_files_config(args, files_config):
  app_name = args.app
  executor = f"python " if app_name[-3:] == ".py" else f"./"
  command = f"{executor}{app_name} {args.config}"
  
  spec = importlib.util.spec_from_file_location("files_module", args.files_config)
  files_config = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(files_config)

  # check if files_config contains input_file_list variable
  if hasattr(files_config, "input_file_list"):
    print("Option 1")
    # option 1
    output_dir = files_config.output_dir
    input_file_list = files_config.input_file_list

    if not os.path.exists(output_dir):
      os.makedirs(output_dir)

    for input_file_path in input_file_list:
      input_file_name = input_file_path.strip().split("/")[-1]
      output_file_path = f"{output_dir}/{input_file_name}"
      command_for_file = f"{command} {input_file_path} {output_file_path}"
      
      print(f"\n\nExecuting {command_for_file=}")
      os.system(command_for_file)
  elif hasattr(files_config, "input_output_file_list"):
    print("Option 2")
    # option 2
    for input_file_path, output_file_path in files_config.input_output_file_list:
      command_for_file = f"{command} {input_file_path} {output_file_path}"
      print(f"\n\nExecuting {command_for_file=}")
      os.system(command_for_file)
  elif hasattr(files_config, "dataset"):
    print("Option 3")
    # option 3
    dataset_name = files_config.dataset
    output_dir = files_config.output_dir
    max_files = files_config.max_files
    
    # execute bash command and get output as a list of lines
    das_command = f"dasgoclient -query='file dataset={dataset_name}'"
    print(f"\n\nExecuting {das_command=}")
    input_files = os.popen(das_command).read().splitlines()
    
    for input_file_path in input_files[:max_files]:
      input_file_name = input_file_path.strip().split("/")[-1]
      output_file_path = f"{output_dir}/{input_file_name}"
      command_for_file = f"{command} {input_file_path} {output_file_path}"
      
      print(f"\n\nExecuting {command_for_file=}")
      os.system(command_for_file)
    
    

def main():
  args = get_args()
  
  app_name = args.app
  
  if args.local:
    print("Running locally")
    
    if args.files_config != "":
      run_locally_with_files_config(args, args.files_config)
    else:
      print(f"\n\nExecuting {command=}")
      os.system(command)
  
  elif args.condor:
    if not os.path.exists("error"):
      os.makedirs("error")
    if not os.path.exists("log"):
      os.makedirs("log")
    if not os.path.exists("output"):
      os.makedirs("output")
      
    import uuid
    hash_string = str(uuid.uuid4().hex[:6])
    condor_config_name = f"condor_config_{hash_string}.sub"
    
    os.system(f"cp ../templates/condor_config.template.sub {condor_config_name}")
    
    spec = importlib.util.spec_from_file_location("files_module", args.files_config)
    files_config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(files_config)
    
    
    python_executable = os.popen("which python").read().strip()
    python_executable = python_executable.replace("/", "\/")
    
    dataset_name = files_config.dataset
    das_command = f"dasgoclient -query='file dataset={dataset_name}'"
    print(f"\n\nExecuting {das_command=}")
    input_files = os.popen(das_command).read().splitlines()
    
    # store input_files list in a file
    input_files_file_name = f"input_files_{hash_string}.txt"
    with open(input_files_file_name, "w") as f:
      for input_file_path in input_files:
        f.write(f"{input_file_path}\n")
    
    output_dir = files_config.output_dir.replace("/", "\/")
    
    os.system(f"sed -i 's/<executor>/{python_executable}/g' {condor_config_name}")
    os.system(f"sed -i 's/<app>/{app_name}/g' {condor_config_name}")
    os.system(f"sed -i 's/<config>/{args.config}/g' {condor_config_name}")
    os.system(f"sed -i 's/<input_files_file_name>/{input_files_file_name}/g' {condor_config_name}")
    os.system(f"sed -i 's/<output_dir>/{output_dir}/g' {condor_config_name}")
    os.system(f"sed -i 's/<n_jobs>/{files_config.max_files}/g' {condor_config_name}")
    
    print("Submitting to condor")
    command = f"condor_submit {condor_config_name}"
    # os.system(command)
    
    # remove condor_config_name file
    # os.system(f"rm {condor_config_name}")
    
  else:
    print("Please select either --local or --condor")
    exit()
  

if __name__ == "__main__":
  main()
