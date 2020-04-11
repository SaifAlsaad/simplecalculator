print("Welcome to Saif's calculator")
num1=input("Enter any number: ")
op=input("Choose any symbole + - * ** / % // == != < > <= >= = : ")
num2=input("last step to see the results: ")
num1=float(num1)
num2=float(num2)
if op=="+":
    pls=num1 + num2
    print(pls)
elif op=="-":
    sub=num1-num2
    print(sub)
elif op=="*":
    multi=num1*num2
    print(multi)
elif op=="**":
    power=num1**num2
    print(power)
elif op=="/":
    divide=num1/num2
    print(divide)
elif op=="%":
    Modulus=num1%num2
    print(Modulus)
elif op=="//":
    Floor_Division=num1//num2
    print(Floor_Division)
elif op=="==":
    equal=num1==num2
    print(equal)
elif op==">":
    left_op=num1>num2
    print(left_op)
elif op=="<":
    Right_op=num1<num2
    print(Right_op)
elif op=="<=":
    left_eq=num1<=num2
    print(left_eq)
elif op==">=":
    right_eq=num1>=num2
    print(right_eq)
elif op=="!=":
    EQ_OP=num1!=num2
    print(EQ_OP)
elif op=="=":
    EQ=num1=num2
    print(EQ)
else:
    print("use + - / * ** % // == < > <= >= != = only")
