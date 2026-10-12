
import pytest

from calculator.calculation import ArithmeticCalculation
from calculator.operations import Operations
from calculator.commands import CalculateCommand, HistoryCommand


def test_calculate_command():
    history = []
    calculation = ArithmeticCalculation.create(5, 3, Operations.add)
    command = CalculateCommand(calculation, history)

    assert command.execute() == 8
    assert len(history) == 1
    assert "add" in history[0]


def test_multiple_calculations():
    history = []

    for operation in [Operations.add, Operations.subtract, Operations.multiply]:
        calculation = ArithmeticCalculation.create(5, 3, operation)
        CalculateCommand(calculation, history).execute()

    assert len(history) == 3
    assert "add" in history[0]
    assert "subtract" in history[1]
    assert "multiply" in history[2]


def test_failed_calculation_not_saved():
    history = []
    calculation = ArithmeticCalculation.create(5, 0, Operations.divide)
    command = CalculateCommand(calculation, history)

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        command.execute()

    assert history == []


def test_empty_history():
    history = []
    command = HistoryCommand(history)

    assert command.execute() == []


def test_history_returns_copy():
    history = ["5 add 3 = 8"]
    command = HistoryCommand(history)

    copied_history = command.execute()
    copied_history.append("extra calculation")

    assert history == ["5 add 3 = 8"]
    assert copied_history != history
