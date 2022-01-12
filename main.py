from cmath import inf

import pytest
import sys
import pytest

#  DICT OPERATIONS


def add_pair_to_dict(dictionary, new_key, new_value):
    dictionary[new_key] = new_value
    return dictionary


def get_value(dictionary, key):
    return dictionary[key]


#   DICT CHECK OPERATIONS


def get_type_key(dictionary):
    if len(dictionary) == 0:
        return None
    return type((dictionary.keys()))


def get_type_value(dictionary):
    if len(dictionary) == 0:
        return None
    return type((dictionary.values()))


@pytest.mark.parametrize("dict_before, key,  value, dict_after", [({0: 1, 1: 2}, 3, 4, {0: 1, 1: 2, 3: 4}),
                                                                  ({"s1": 1, "s2": 2}, "s3", 3, {"s1": 1, "s2": 2, "s3": 3}),
                                                                  ({1: "s", 2 : "s"}, 3, "s", {1: "s", 2: "s", 3: "s"}),
                                                                  ({}, 1, 3, {1: 3})])
def test_good_case(dict_before, key, value, dict_after):
    assert add_pair_to_dict(dict_before, key, value) == dict_after


def test_receive_bad_type_key():
    if type("str") is get_type_key({1: 3}):
        with pytest.raises(TypeError):
            add_pair_to_dict({1: 3}, "str", 4)


def test_receive_bad_type_value():
    if type("str") is get_type_value({1: 3}):
        with pytest.raises(TypeError):
            add_pair_to_dict({1: 3}, 4, "str")


def test_receive_not_allow_key():
    key = "search_tag"
    dictionary = {1: 3}
    if "key" not in dictionary.keys():
        with pytest.raises(KeyError):
            get_value(dictionary, key)


#   FLOAT OPERATIONS


def func(item):
    return float(item)


#   FLOAT OPERATIONS CHECK


@pytest.mark.parametrize("item, answer", [(sys.float_info.max + sys.float_info.max, inf),
                                          (sys.float_info.max, 1.7976931348623157e+308)])
def test_overflow_number(item, answer):
    assert func(item) == answer


@pytest.mark.parametrize("item, answer", [('1.334234', 1.334234),
                                          (0, 0),
                                          (1, 1)])
def test_simple_numbers(item, answer):
    assert func(item) == answer


def test_plus_minus():
    assert func(-3.14) == -3.14


@pytest.mark.parametrize("item, answer", [('12a.3434', ValueError),
                                          ('++12', ValueError),
                                          ('--12', ValueError)])
def test_value_error(item, answer):
    try:
        assert func(item) == answer
    except ValueError:
        pass
