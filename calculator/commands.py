
from calculator.calculation import Calculation


class CalculateCommand:
    def __init__(self, calculation: Calculation, history: list):
        # Store the calculation and shared history.
        self.calculation = calculation
        self.history = history

    def execute(self) -> float:
        # Only save successful calculations.
        result = self.calculation.execute()
        entry = (
            f"{self.calculation.a} "
            f"{self.calculation.operation.__name__} "
            f"{self.calculation.b} = {result}"
        )
        self.history.append(entry)
        return result


class HistoryCommand:
    def __init__(self, history: list):
        self.history = history

    def execute(self) -> list:
        # Return a copy to protect the original history.
        return self.history.copy()
