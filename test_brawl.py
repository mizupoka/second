import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from brawl import greet, farewell

def test_greet():
    assert greet("Alice") == "Hello, Alice!"

def test_farewell():
    assert farewell("Bob") == "Goodbye, Bob!"
