def arithmetic_arranger(problems, bol=None):
    length = len(problems)
    n1, op, n2 = str, str, str
    string_line1 = ""
    string_line2 = ""
    string_line3 = ""
    string_sum = ""
    #First error situation
    if length > 5: 
        return("Error: Too many problems.")
    
    for i in problems: 
        l = (i.split(" "))
        n1 = l[0]
        op = l[1]
        n2 = l[2]

        #Second error situation
        if op != "-" and op != "+":
            return ("Error: Operator must be '+' or '-'.")  
        #Third error situation
        if not n1.isnumeric() or not n2.isnumeric():
            return ("Error: Numbers must only contain digits.")
        else:
            if op == "-":
                sum1 = int(n1) - int(n2)
            else:
                sum1 = int(n1) + int(n2)
        #Fourth Error Situation - receive only 1 to 4 digit numbers
        if len(n1) >= 5 or len(n2) >= 5:
            return ("Error: Numbers cannot be more than four digits.")

        max_len = max(len(n1), len(n2)) + 2
        line1 = str(n1).rjust(max_len)
        line2 = op + str(n2).rjust(max_len - 1)
        line3 = ""
        for p in range(max_len):
            line3 = line3 + "-" 
        line4 = str(sum1).rjust(max_len)
        string_line1 += line1 + "    "
        string_line2 += line2 + "    "
        string_line3 += line3 + "    "
        string_sum += line4 + "    "
        
    string_line1 = string_line1.rstrip()
    string_line2 = string_line2.rstrip()
    string_line3 = string_line3.rstrip()
    string_sum = string_sum.rstrip()

    if bol == True:
        arranged_problems = string_line1 + "\n" + string_line2 + "\n" + string_line3 + "\n" +string_sum
    else:
        arranged_problems = string_line1 + "\n" + string_line2 + "\n" + string_line3
    return (arranged_problems)   

problems = ["32 - 698", "1 - 3801", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems, True))


  