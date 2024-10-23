#include <iostream>
#include <vector>

struct Node {
    int value;
    Node* parent;
};

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    int N;
    std::cin >> N;

    std::vector<Node*> history;
    Node* last_solved = nullptr;
    history.push_back(last_solved); // 초기 상태 저장

    for (int i = 0; i < N; ++i) {
        char query_type;
        std::cin >> query_type;

        if (query_type == 'a') {
            int query_value;
            std::cin >> query_value;

            Node* new_node = new Node();
            new_node->value = query_value;
            new_node->parent = last_solved;
            last_solved = new_node;

            std::cout << query_value << "\n";
        } else if (query_type == 's') {
            if (last_solved != nullptr) {
                last_solved = last_solved->parent;
            }

            if (last_solved == nullptr) {
                std::cout << "-1\n";
            } else {
                std::cout << last_solved->value << "\n";
            }
        } else if (query_type == 't') {
            int query_value;
            std::cin >> query_value;
            --query_value; // 0-based 인덱싱

            last_solved = history[query_value];

            if (last_solved == nullptr) {
                std::cout << "-1\n";
            } else {
                std::cout << last_solved->value << "\n";
            }
        }

        history.push_back(last_solved); // 현재 상태 저장
    }

    return 0;
}
