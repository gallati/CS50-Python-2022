expression = str(input("Expression: ")).strip()
x, y, z = expression.split(" ")
x, z = int(x), int(z)
match y:
    case "+":
        print(f"{x+z:.1f}")
    case "-":
        print(f"{x-z:.1f}")
    case "*":
        print(f"{x*z:.1f}")
    case "/":
        print(f"{x/z:.1f}")    
