from brawl import greet

def test_greet():
    assert greet("Alice") == "Hello, Alice!"

def test_greet_another_name():
    assert greet("Bob") == "Hello, Bob!"
