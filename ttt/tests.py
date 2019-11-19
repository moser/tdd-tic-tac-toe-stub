import pytest
from .game import main

def test_failing():
    assert False


def test_integration():
    import io
    stdin = io.StringIO("A1\nexit\n")
    stdout = io.StringIO()

    main(stdin, stdout)
    assert stdout.getvalue() == (
        "Ask player X for input:\n"
        "Player entered: ('A1',)\n"
        "Ask player X for input:\n"
    )
