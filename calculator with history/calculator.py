HISTORY_FILE = "history.txt"

def show_history():
    """For showing the history if exists."""
    try:
        with open(HISTORY_FILE, "r") as file:
            lines = file.readlines()
        if len(lines) == 0:
            print("No history found.")
        else:
            for line in reversed(lines):
                print(line.strip())
    except FileNotFoundError:
        print("No history found.")

def clear_history():
    """Clear the history file."""
    with open(HISTORY_FILE, "w"):
        pass
    print("History Cleared successfully!")

def save_to_history(equation, result):
    """Save the equation and result to history."""
    with open(HISTORY_FILE, "a") as file:
        file.write(equation + " = " + str(result) + "\n")

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input format. Use 'number operator number'. eg(8 + 8)")
        return

    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid numbers. Please enter valid numbers.")
        return

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operator. Supported operators are +, -, *, /.")
        return

    if int(result) == result:
        result = int(result)
    print("Result:", result)
    save_to_history(user_input, result)

def main():
    print("Welcome to the Calculator!")

    while True:
        user_input = input("Enter calculation eg(8 + 8) or 'history' to view history, 'clear' to clear history, 'exit' to quit: ")
        if user_input.lower() == "exit":
            print("Exiting the calculator. Goodbye!")
            break
        elif user_input.lower() == "history":
            show_history()
        elif user_input.lower() == "clear":
            clear_history()
        else:
            calculate(user_input)

if __name__ == "__main__":
    main()