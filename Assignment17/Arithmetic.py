def Add(No1,No2):
    Ans = No1 + No2
    return Ans

def Sub(No1,No2):
    Ans = No1 - No2
    return Ans

def Multi(No1,No2):
    Ans = No1 * No2
    return Ans

def Div(No1,No2):
    if No2 == 0:
        print("Error: Division by zero is not allowed.")
        return None
    else:   
        Ans = No1 / No2
        return Ans
