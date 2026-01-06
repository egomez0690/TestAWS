import pytest
from src.handler import handler

def test_ok():
    result = handler({"name": "Eze"}, None)
    assert result["statusCode"] == 200

def test_error():
    try:
        handler({}, None)
        assert False
    except ValueError:
        assert True