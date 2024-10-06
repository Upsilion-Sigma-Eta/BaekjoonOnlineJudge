#include <iostream>
#include <cmath>
#include <cstdint>
#include <algorithm>
#include <stack>
#include <vector>
#include <string>

int OperatorPriority(std::string op) {
    if (op == "(") {
        return 3;
    }
    if (op == "<?" || op == ">?") {
        return 2;
    }
    if (op == "+" || op == "-") {
        return 1;
    }
    return -1;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    std::string equation;
    std::cin >> equation;

    // 파싱하는 부분
    std::vector<std::string> tokens;
    std::string number_token;
    std::string operator_token;

    // 전체 식을 파싱
    for (size_t i = 0; i < equation.length(); ++i) {
        char c = equation[i];
        if (isdigit(c)) {
            if (!operator_token.empty()) {
                tokens.push_back(operator_token);
                operator_token.clear();
            }
            number_token += c;
        } else {
            if (!number_token.empty()) {
                tokens.push_back(number_token);
                number_token.clear();
            }
            if (c == '(' || c == ')' || c == '+' || c == '-') {
                if (!operator_token.empty()) {
                    tokens.push_back(operator_token);
                    operator_token.clear();
                }
                tokens.push_back(std::string(1, c));
            } else {
                operator_token += c;
            }
        }
    }
    if (!operator_token.empty()) {
        tokens.push_back(operator_token);
        operator_token.clear();
    }
    if (!number_token.empty()) {
        tokens.push_back(number_token);
        number_token.clear();
    }

    // 전체 식 파싱 이후에 연산을 위해서 피연산자와 연산자 스택 준비
    std::stack<int> operand_stack;
    std::stack<std::string> operator_stack;

    for (const std::string& token : tokens) {
        if (isdigit(token[0])) {
            int number = std::stoi(token);
            operand_stack.push(number);
        } else if (token == "(") {
            operator_stack.push(token);
        } else if (token == ")") {
            // 닫는 괄호가 나중에 푸쉬되므로 짝이 맞는 열린 괄호가 나올 떄 까지 내부 내용 먼저 계산
            while (!operator_stack.empty() && operator_stack.top() != "(") {
                std::string op = operator_stack.top();
                operator_stack.pop();

                int operand1 = operand_stack.top(); operand_stack.pop();
                int operand2 = operand_stack.top(); operand_stack.pop();

                int result;
                if (op == "+") {
                    result = operand2 + operand1;
                } else if (op == "-") {
                    result = operand2 - operand1;
                } else if (op == "<?") {
                    result = std::min(operand2, operand1);
                } else if (op == ">?") {
                    result = std::max(operand2, operand1);
                }
                operand_stack.push(result);
            }

            if (!operator_stack.empty() && operator_stack.top() == "(") {
                operator_stack.pop();
            }
        } else {
            int current_priority = OperatorPriority(token);
            while (!operator_stack.empty() && OperatorPriority(operator_stack.top()) >= current_priority && operator_stack.top() != "(") {
                std::string op = operator_stack.top();
                operator_stack.pop();

                int operand1 = operand_stack.top(); operand_stack.pop();
                int operand2 = operand_stack.top(); operand_stack.pop();

                int result;
                if (op == "+") {
                    result = operand2 + operand1;
                } else if (op == "-") {
                    result = operand2 - operand1;
                } else if (op == "<?") {
                    result = std::min(operand2, operand1);
                } else if (op == ">?") {
                    result = std::max(operand2, operand1);
                }
                operand_stack.push(result);
            }
            operator_stack.push(token);
        }
    }

    // 남은 연산자와 피연산자 처리
    while (!operator_stack.empty()) {
        std::string op = operator_stack.top();
        operator_stack.pop();

        int operand1 = operand_stack.top(); operand_stack.pop();
        int operand2 = operand_stack.top(); operand_stack.pop();

        int result;
        if (op == "+") {
            result = operand2 + operand1;
        } else if (op == "-") {
            result = operand2 - operand1;
        } else if (op == "<?") {
            result = std::min(operand2, operand1);
        } else if (op == ">?") {
            result = std::max(operand2, operand1);
        }
        operand_stack.push(result);
    }

    int final_result = operand_stack.top();
    std::cout << final_result << "\n";

    return 0;
}
