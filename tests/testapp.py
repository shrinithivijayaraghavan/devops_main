# tests/test_app.py
from app import add  # Import the add function from app.py

def test_add():
    # Test cases for the add function
    assert add(2, 3) == 5       # Positive numbers
    assert add(-1, 1) == 0      # Positive and negative numbers
    assert add(0, 0) == 0       # Zero values
    assert add(-2, -3) == -5    # Negative numbers
