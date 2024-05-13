def ActualProcessing():
    while True:
        exit_flag = False
        
        line = input()
        
        if (line == '0'):
            break
        
        numberList = list(map(lambda x: int(x), line.split('+')))
        resultString = "";      

        for i in range(len(numberList)):
            passFlag = False            
            
            if (numberList[i] == -100000):
                continue

            for j in range(i + 1, len(numberList)):
                if (numberList[j] == -100000 or numberList[i] == -100000):
                    continue

                if ((int(numberList[i]) + int(numberList[j])) % 10 == 0):
                    resultString += (str(numberList[i]) + "+" + str(numberList[j]) + "+")
                    numberList[i] = -100000
                    numberList[j] = -100000
                    passFlag = True
                    
            if passFlag:
                continue
        
        for i in range(len(numberList)):
            if (numberList[i] == -100000):
                continue
            else:
                resultString += str(numberList[i]) + "+"

        resultString = resultString[0:len(resultString)-1]
        
        print(resultString)


if __name__ == "__main__":
    ActualProcessing()