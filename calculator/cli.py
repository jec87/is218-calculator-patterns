
from calculator.operations import Operations
from calculator.calculation import ArithmeticCalculation
from calculator.commands import CalculateCommand, HistoryCommand


def main():
    history = []

    operations = {
        "add": Operations.add,
        "subtract": Operations.subtract,
        "multiply": Operations.multiply,
        "divide": Operations.divide,
    }

    print("Welcome to the CLI Calculator!")
    print("Commands: add, subtract, multiply, divide, history, exit")

    while True:
        try:
            user_input = input("> ").strip()
        except EOFError:
            print("Goodbye!")
            break

        if not user_input:
            print("Please enter a command.")
            continue

        parts = user_input.split()
        command_name = parts[0].lower()

        if command_name == "exit":
            print("Goodbye!")
            break

        if command_name == "history":
            if len(parts) != 1:
                print("History does not take any operands.")
                continue

            entries = HistoryCommand(history).execute()
            if not entries:
                print("History is empty.")
            else:
                for entry in entries:
                    print(entry)
            continue

        if command_name not in operations:
            print("Unknown command. Try add, subtract, multiply, divide, history, or exit.")
            continue

        if len(parts) != 3:
            print("Please provide exactly two numbers.")
            continue

        try:
            a = float(parts[1])
            b = float(parts[2])
        except ValueError:
            print("Invalid number. Please enter valid numbers.")
            continue

        try:
            # Input -> strategy -> factory -> command -> result
            operation = operations[command_name]
            calculation = ArithmeticCalculation.create(a, b, operation)
            command = CalculateCommand(calculation, history)
            result = command.execute()
            print(result)
        except ValueError as error:
            print(error)

