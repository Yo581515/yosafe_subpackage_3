from yosafe_packages.yosafe_subpackage_1.yosafe_subpackage_1_functions import yosafe_add, to_capitllal_letters, yosafe_get_yosafe_subpackage_1
from yosafe_packages.yosafe_subpackage_2.yosafe_subpackage_2_functions import to_capitllal_letters_2



def test_yosafe_subpackage_1_add():
    assert yosafe_add(1, 2) == 3


def test_yosafe_subpackage_1_to_capitllal_letters():
    assert to_capitllal_letters("hello") == "HELLO"


def test_yosafe_subpackage_2_to_capitllal_letters():
    assert to_capitllal_letters_2("hello") == "HELLO"


def test_yosafe_subpackage_1_yosafe_get_yosafe_subpackage_1():
    result = yosafe_get_yosafe_subpackage_1()
    print(result)
    assert "Error" not in result
