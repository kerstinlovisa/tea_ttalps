//  Event.cpp
//
//  Created by Jeremi Niedziela on 04/08/2023.

#include "Event.hpp"
#include "Helpers.hpp"
#include "ScaleFactorsManager.hpp"

using namespace std;

#include "Helpers.hpp"

using namespace std;

Event::Event() {
  auto &config = ConfigManager::GetInstance();

  try {
    config.GetExtraEventCollections(extraCollectionsDescriptions);
  } catch (...) {
    info() << "No extra event collections found" << endl;
    hasExtraCollections = false;
  }
}

Event::~Event() {}

void Event::Reset() {
  // for (auto &[key, value] : valuesUint) value = 0;
  // for (auto &[key, value] : valuesInt) value = 0;
  // for (auto &[key, value] : valuesBool) value = 0;
  // for (auto &[key, value] : valuesFloat) value = 0;
  // for (auto &[key, value] : valuesUlong) value = 0;
  // for (auto &[key, value] : valuesUchar) value = 0;

  // for (auto &[name, collection] : collections) {
  //   for (auto element : *collection) element->Reset();
  // }

  extraCollections.clear();
}

void Event::AddExtraCollections() {
  if (!hasExtraCollections) return;

  for (auto &[name, extraCollection] : extraCollectionsDescriptions) {
    auto newCollection = make_shared<PhysicsObjects>();

    for (auto inputCollectionName : extraCollection.inputCollections) {
      auto inputCollection = GetCollection(inputCollectionName);

      int n = 0;
      for (auto physicsObject : *inputCollection) {
        n++;

        bool passes = true;

        for (auto &[branchName, cuts] : extraCollection.selections) {
          float value = physicsObject->Get(branchName);

          if (value < cuts.first || value > cuts.second) {
            passes = false;
            break;
          }
        }

        for (auto &[branchName, flag] : extraCollection.flags) {
          bool value = physicsObject->Get(branchName);

          if (value != flag) {
            passes = false;
            break;
          }
        }

        for (auto &[branchName, option] : extraCollection.options) {
          try {
            UChar_t value = physicsObject->Get(branchName);
            if (value != option) {
              passes = false;
              break;
            }
          } catch (BadTypeException &e) {
            try {
              Int_t value = physicsObject->Get(branchName);
              if (value != option) {
                passes = false;
                break;
              }
            } catch (BadTypeException &e) {
              fatal() << e.what() << endl;
            }
          }
        }

        for (auto &[branchName, cuts] : extraCollection.optionRanges) {
          UChar_t value = physicsObject->Get(branchName);

          if (value < cuts.first || value > cuts.second) {
            passes = false;
            break;
          }
        }

        if (passes) newCollection->push_back(physicsObject);
      }
    }
    extraCollections.insert({name, newCollection});
  }
}

float Event::GetScaleFactor() {
  auto &scaleFactorsManager = ScaleFactorsManager::GetInstance();
  int nVertices = Get("PV_npvsGood");
  return scaleFactorsManager.GetPileupScaleFactor(nVertices);
}