import sys

def ActualProcessing():
    input_string = 'start';    

    while (input_string != ''):
        input_string = sys.stdin.readline().split();
    
        if (len(input_string) == 2):
            n = input_string[0];
            m = input_string[1];

            total_room_number = 0;

            for i in range(int(n), int(m) + 1, 1):
                digit_numbers = list(str(i));
                distinct_numbers = set(digit_numbers);

                if (len(distinct_numbers) == len(digit_numbers)):
                    total_room_number = total_room_number + 1;

            sys.stdout.write(str(total_room_number) + '\n');
        else:
            break;


if __name__ == "__main__":
    ActualProcessing()