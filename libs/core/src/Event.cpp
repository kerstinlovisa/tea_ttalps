//  Event.cpp
//
//  Created by Jeremi Niedziela on 04/08/2023.

#include "Event.hpp"
#include "Helpers.hpp"

using namespace std;

Event::Event() {}

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

void Event::AddExtraCollections(shared_ptr<ConfigManager> config) {
  map<string, ExtraCollection> extraEventCollections;
  config->GetExtraEventCollections(extraEventCollections);

  for (auto &[name, extraCollection] : extraEventCollections) {
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

        if (passes) newCollection->push_back(physicsObject);
      }
    }
    extraCollections.insert({name, newCollection});
  }
}