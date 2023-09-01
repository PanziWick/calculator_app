if __name__ == '__main__':
    input1 = float(input("Enter the first number: "))
    input2 = float(input("Enter the second number: "))
    input3 = str(input("Enter the operator: "))

    if(input3 == "+"):
        sum_result = (input1 + input2)
        print("The sum of", input1, "and", input2, "is", sum_result)
    elif(input3 == "-"):
        sum_result = (input1 - input2)
        print("The sum of", input1, "and", input2, "is", sum_result)
    elif (input3 == "*"):
        sum_result = (input1 * input2)
        print("The sum of", input1, "and", input2, "is", sum_result)
    elif (input3 == "/"):
        sum_result = (input1 / input2)
        print("The sum of", input1, "and", input2, "is", sum_result)
        print(round(sum_result, 3))

