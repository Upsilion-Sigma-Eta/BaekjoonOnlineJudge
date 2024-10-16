#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <thread>
#include <cctype>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    int T = 0;
    std::cin >> T;
    std::cin.ignore();

    for (int _ = 0; _ < T; ++_) {
        std::string word;
        std::string text;

        getline(std::cin, word);
        getline(std::cin, text);

        std::transform(word.begin(), word.end(), word.begin(), [](unsigned char c) { return std::tolower(c); });
        std::transform(text.begin(), text.end(), text.begin(), [](unsigned char c) { return std::tolower(c); });

        std::unordered_map<char, std::vector<int>> pos_map;
        for(char c : word){
            pos_map[c] = std::vector<int>();
        }

        for(int i = 0; i < text.size(); ++i){
            char c = text[i];
            if(pos_map.find(c) != pos_map.end()){
                // 1-based Index
                pos_map[c].push_back(i + 1);
            }
        }

        std::unordered_map<char, int> current_idx;
        for(char c : word){
            current_idx[c] = 0;
        }

        std::vector<int> last_positions;

        while(true){
            int prev = 0;
            std::vector<int> current_positions;
            bool found = true;
            for(char c : word){
                if(current_idx[c] >= pos_map[c].size()){
                    found = false;
                    break;
                }
                auto &vec = pos_map[c];
                int idx = current_idx[c];
                int left = idx;
                int right = vec.size();
                while(left < right){
                    int mid = left + (right - left) / 2;
                    if(vec[mid] > prev){
                        right = mid;
                    }
                    else{
                        left = mid + 1;
                    }
                }
                if(left < vec.size()){
                    int next_pos = vec[left];
                    current_positions.push_back(next_pos);
                    prev = next_pos;
                    current_idx[c] = left + 1;
                }
                else{
                    found = false;
                    break;
                }
            }
            if(found){
                last_positions.push_back(current_positions.back());
            }
            else{
                break;
            }
        }

        int count = last_positions.size();
        if(count == 0){
            std::cout << "0\n";
        }
        else{
            std::cout << count;
            int output_limit = std::min(count, 3);
            for(int i = 0; i < output_limit; ++i){
                std::cout << " " << last_positions[i];
            }
            std::cout << "\n";
        }
    }

    return 0;
}
