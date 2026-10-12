
import builtins
import pytest

from calculator.cli import main


def run_cli(monkeypatch, capsys, inputs):
    commands = iter(inputs)
    monkeypatch.setattr(
        builtins,
        "input",
        lambda prompt="": next(commands)
    )
    main()
    return capsys.readouterr().out


def test_all_operations(monkeypatch, capsys):
    output = run_cli(monkeypatch, capsys, [
        "add 5 3",
        "subtract 5 3",
        "multiply 5 3",
        "divide 6 3",
        "exit",
    ])
    assert "8.0" in output
    assert "2.0" in output
    assert "15.0" in output
    assert "Goodbye!" in output


def test_history(monkeypatch, capsys):
    output = run_cli(monkeypatch, capsys, [
        "history",
        "add 5 3",
        "history",
        "exit",
    ])
    assert "History is empty." in output
    assert "5.0 add 3.0 = 8.0" in output


def test_unknown_command(monkeypatch, capsys):
    output = run_cli(monkeypatch, capsys, [
        "hello",
        "exit",
    ])
    assert "Unknown command" in output


def test_wrong_operands(monkeypatch, capsys):
    output = run_cli(monkeypatch, capsys, [
        "add 5",
        "add 5 3 2",
        "history 5",
        "exit",
    ])
    assert output.count("Please provide exactly two numbers.") == 2
    assert "History does not take any operands." in output


def test_invalid_numbers(monkeypatch, capsys):
    output = run_cli(monkeypatch, capsys, [
        "add hello 3",
        "exit",
    ])
    assert "Invalid number" in output


def test_division_by_zero(monkeypatch, capsys):
    output = run_cli(monkeypatch, capsys, [
        "divide 5 0",
        "history",
        "exit",
    ])
    assert "Cannot divide by zero" in output
    assert "History is empty." in output


def test_empty_input(monkeypatch, capsys):
    output = run_cli(monkeypatch, capsys, [
        "",
        "exit",
    ])
    assert "Please enter a command." in output


def test_continues_after_error(monkeypatch, capsys):
    output = run_cli(monkeypatch, capsys, [
        "invalid",
        "add -5 2.5",
        "exit",
    ])
    assert "Unknown command" in output
    assert "-2.5" in output


def test_eof(monkeypatch, capsys):
    def raise_eof(prompt=""):
        raise EOFError

    monkeypatch.setattr(builtins, "input", raise_eof)
    main()
    output = capsys.readouterr().out
    assert "Goodbye!" in output
