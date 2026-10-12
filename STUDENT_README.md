
# CLI Calculator — IS218

## Project Overview

This project is a Python command-line calculator built using object-oriented programming (OOP) and design patterns. It supports addition, subtraction, multiplication, division, and calculation history. It also handles invalid inputs and division by zero without stopping the program.

## Setup

Python 3.12 or newer is required.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Running the Calculator

```bash
python -m calculator
```

Available commands:
- add
- subtract
- multiply
- divide
- history
- exit

## Example Conversation

```text
Welcome to the CLI Calculator!
Commands: add, subtract, multiply, divide, history, exit
> add 5 3
8.0
> subtract 5 3
2.0
> multiply 5 3
15.0
> divide 6 3
2.0
> divide 5 0
Cannot divide by zero
> history
5.0 add 3.0 = 8.0
5.0 subtract 3.0 = 2.0
5.0 multiply 3.0 = 15.0
6.0 divide 3.0 = 2.0
> exit
Goodbye!
```

## Static, Class, and Instance Methods

- Static method: Operations.add() performs addition without needing an object.
- Class method: ArithmeticCalculation.create() creates a new calculation object using cls.
- Instance method: ArithmeticCalculation.execute() uses the object's stored numbers and operation to calculate the answer.

## Factory, Command, and Strategy Patterns

Factory: ArithmeticCalculation.create() creates calculation objects.

Command: CalculateCommand executes calculations and saves successful results to history. HistoryCommand returns a copy of the history list.

Strategy: The CLI selects an arithmetic function from the operations dictionary based on the user's command.

For example, add 5 3 selects Operations.add, creates an ArithmeticCalculation using the factory, passes it to CalculateCommand, executes it, and prints 8.0.

The same calculation execution code works for subtraction, multiplication, and division because the selected operation is passed into the calculation object.

## OOP Principles

Encapsulation: Calculation stores the two numbers and operation together. HistoryCommand returns a copy of the history list to prevent callers from modifying the original through its returned value.

Abstraction: Calculation is an abstract class that requires subclasses to implement execute().

Inheritance: ArithmeticCalculation inherits from Calculation and reuses its create() class method.

Polymorphism: CalculateCommand calls execute() on a Calculation object. Different implementations can be used as long as they follow the same contract.

Composition: CalculateCommand contains a calculation object, and the calculation object contains an operation function.

## SOLID Principles

Single Responsibility: Each class has one main job. Operations performs arithmetic, Calculation represents a calculation, and commands coordinate execution and history.

Open/Closed: New operations can be added without changing ArithmeticCalculation.execute() or CalculateCommand.execute(). The new operation can be registered in the CLI dictionary.

Liskov Substitution: A different Calculation subclass can replace ArithmeticCalculation if it returns a numeric result or raises an appropriate error.

Interface Segregation: Calculation requires only the execute() method instead of unnecessary methods.

Dependency Inversion: CalculateCommand receives a Calculation abstraction rather than creating a specific calculation itself. Calculations receive operation functions instead of hard-coding addition.

## Tests and GitHub Actions

Run tests with:

```bash
python -m pytest --cov=calculator --cov-report=term-missing --cov-fail-under=100
```

Local test results:
- 26 tests passed
- 100% line coverage

GitHub Actions automatically runs the tests on pushes and pull requests.

Successful GitHub Actions run:
ADD SUCCESSFUL ACTIONS URL HERE

## Coverage Exclusions

The abstract Calculation.execute() placeholder is excluded because it only defines the required interface and has no implementation.

The calculator/__main__.py entry point is excluded because it only imports and calls the already-tested main() function. All calculator behavior is tested through the CLI tests.
