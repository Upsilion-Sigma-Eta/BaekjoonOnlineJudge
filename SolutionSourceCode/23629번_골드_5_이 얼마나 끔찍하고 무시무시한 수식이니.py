import sys
import re

def Solution():
    expression = sys.stdin.readline().strip()

    buffer = ""
    converted_expression = []
    for index in range(len(expression)):
        buffer += expression[index]

        if (buffer == "ZERO"):
            converted_expression.append("0")
            buffer = ""
        elif (buffer == "ONE"):
            converted_expression.append("1")
            buffer = ""
        elif (buffer == "TWO"):
            converted_expression.append("2")
            buffer = ""
        elif (buffer == "THREE"):
            converted_expression.append("3")
            buffer = ""
        elif (buffer == "FOUR"):
            converted_expression.append("4")
            buffer = ""
        elif (buffer == "FIVE"):
            converted_expression.append("5")
            buffer = ""
        elif (buffer == "SIX"):
            converted_expression.append("6")
            buffer = ""
        elif (buffer == "SEVEN"):
            converted_expression.append("7")
            buffer = ""
        elif (buffer == "EIGHT"):
            converted_expression.append("8")
            buffer = ""
        elif (buffer == "NINE"):
            converted_expression.append("9")
            buffer = ""
        elif (buffer == "+"):
            converted_expression.append("+")
            buffer = ""
        elif (buffer == "-"):
            converted_expression.append("-")
            buffer = ""
        elif (buffer == "x"):
            converted_expression.append("x")
            buffer = ""
        elif (buffer == "/"):
            converted_expression.append("/")
            buffer = ""
        elif (buffer == "="):
            converted_expression.append("=")
            buffer = ""

    converted_expression_string = "".join(converted_expression)

    separator = "+-/x"

    regex_pattern = "|".join(map(re.escape, separator))

    number_list = re.split(regex_pattern, converted_expression_string[:-1])

    if (number_list.__contains__("")):
        sys.stdout.write("Madness!")
        return

    operator_list = re.findall(regex_pattern, converted_expression_string[:-1])

    for index in range(len(number_list) - 1):
        num_1 = int(number_list[index])
        num_2 = int(number_list[index + 1])

        if (operator_list[index] == "+"):
            number_list[index + 1] = num_1 + num_2
        elif (operator_list[index] == "-"):
            number_list[index + 1] = num_1 - num_2
        elif (operator_list[index] == "x"):
            number_list[index + 1] = num_1 * num_2
        elif (operator_list[index] == "/"):
            number_list[index + 1] = int(num_1 / num_2)

    express_result = str(number_list[-1])

    final_expression = ""
    for i in range(len(express_result)):
        if (express_result[i]) == "1":
            final_expression += "ONE"
        elif (express_result[i]) == "2":
            final_expression += "TWO"
        elif (express_result[i]) == "3":
            final_expression += "THREE"
        elif (express_result[i]) == "4":
            final_expression += "FOUR"
        elif (express_result[i]) == "5":
            final_expression += "FIVE"
        elif (express_result[i]) == "6":
            final_expression += "SIX"
        elif (express_result[i]) == "7":
            final_expression += "SEVEN"
        elif (express_result[i]) == "8":
            final_expression += "EIGHT"
        elif (express_result[i]) == "9":
            final_expression += "NINE"
        elif (express_result[i]) == "0":
            final_expression += "ZERO"
        else:
            final_expression += express_result[i]

    print(converted_expression_string)
    print(final_expression)




if __name__ == "__main__":
    Solution()