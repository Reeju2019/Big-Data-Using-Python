"""
Main entry point for the calculator application. Handles user interaction and performs mathematical operations.
"""
from Math_operations.operations import add, subtract, multiply, divide
from Display.printer import show_menu, get_input, show_result

def main() -> None:
    """
    Runs the calculator program in a loop until the user chooses to exit.
    """
    choice: str
    num1: float
    num2: float
    result: float
    operations: dict[str, callable]

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "5":
            print("Exiting calculator.")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("Invalid choice, please try again.")
            continue

        num1 = get_input("Enter first number: ")
        num2 = get_input("Enter second number: ")

        operations = {"1": add, "2": subtract, "3": multiply, "4": divide}
        try:
            result = operations[choice](num1, num2)
            show_result(result)
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
