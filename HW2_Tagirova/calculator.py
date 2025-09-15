# calculator.py 
def add(x, y):
    return x + y

def main():
    num1, op, num2 = input().split()  
    a = float(num1)
    b = float(num2)

    if op == '+':
        res = add(a, b)
    elif op == '-':
        res = subtract(a, b)
    elif op == '*':
        res = multiply(a, b)
    elif op == '/':
        if b == 0:
            print("Ошибка: деление на ноль")
            return
        res = divide(a, b)
    else:
        print(f"Ошибка: неизвестный оператор '{op}'")
        return
    print(int(res) if isinstance(res, float) and res.is_integer() else res)
    
main()
