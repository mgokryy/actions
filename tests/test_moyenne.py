import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from moyenne import moyenne



def test_moyenne_simple():
    assert moyenne([2, 4, 6]) == 4

def test_moyenne_un_element():
    assert moyenne([5]) == 5
