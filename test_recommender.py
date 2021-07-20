"""
Contains the tests for the recommender module.

The name of this file has to contain the word test. So the filename either has to be test_xxx.py or xxx_test.py
"""

import pytest
from simple_recommender import get_recommendations


def test_output_length():
    """Test if the output of get_recommendations has the right length"""
    output = get_recommendations("Titanic", "5")
    assert len(output) == 3


def test_datatypes():
    """Test that get_recommendations returns the right datatype"""
    output = get_recommendations("Titanic", "2")
    for movie in output:
        assert isinstance(movie, str)


def test_too_many_input_parameters():
    """Test that get_recommendations does not work if the the user passes to many input parameters"""
    with pytest.raises(TypeError):
        output = get_recommendations("Titanic", "2", 2)


# assert statements are used with comparisons
# assert statements return nothing (None) if the comparison is True
# assert 3 == 3

# In contrast, if the assert statement is false, then the assert statement will return an AssertionError
# assert 2 == 3, "2 is most definitely not 3"
