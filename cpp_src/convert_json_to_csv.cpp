#include "nlohmann/json.hpp"
#include "csv.hpp"
#include <iostream>
#include <fstream>

using namespace csv;
using namespace std;


// for convenience
using json = nlohmann::json;

int main(){

    // read a JSON file
    std::ifstream i("data.json");
    json j;
    i >> j;

//    std::cout << j["https://www.gla.ac.uk/coursecatalogue/courselist/?code=ACCFIN&name=Accounting+and+Finance"].dump(4) << std::endl;
//    for (json::iterator it = j.begin(); it != j.end(); ++it) {
//      std::cout << *it << '\n';
//    }
//
//    for (auto& element : j) {
//      std::cout << element << '\n';
//    }

    for (json::iterator it = j.begin(); it != j.end(); ++it) {

      auto subj = j[ it.key()];
       for (json::iterator it2 = subj.begin(); it2 != subj.end(); ++it2) {
            std::cout << it2.key()  << "\n";
       }
    }


    std::ofstream ss ("test.csv");

    auto writer = make_csv_writer(ss);

    writer << vector<string>({ "A", "B", "C" })
        << deque<string>({ "I'm", "too", "tired" })
        << list<string>({ "to", "write", "documentation." });

    writer << array<string, 2>({ "The quick brown", "fox", "jumps over the lazy dog" });
    writer << make_tuple(1, 2.0, "Three");

}


