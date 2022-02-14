from unicodedata import decimal
import code_191_number_of_1_bits as c

def test_example_1():
    s = c.Solution()
    assert s.hammingWeight(11) == 3

def test_example_2():
    s = c.Solution()
    assert s.hammingWeight(128) == 1

def test_example_3():
    s = c.Solution()
    assert s.hammingWeight(4294967293) == 31
    