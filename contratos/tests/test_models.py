# Imports
import pytest

#Import Models
from models.data import BaseContract


# Test Base Contract
# def test_contract():
#     c = BaseContract()
#     assert type(c.type) == str
#     assert type(c.source) == str

c = BaseContract()
assert type(c.type) == str
    # assert type(c.source) == str