import re
import os
import pytest
import inspect
import session9
import datetime

README_CONTENT_CHECK_FOR = ["odd_sec", "authenticate", "logged", "timed_fac", "add"]


def test_readme_exists():
    """                                                                                                                                                                      
    Test funtion to check if README exists.                                                                                                                                  
    """
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    """                                                                                                                                                                      
    Test if README contains atleast 200 words.                                                                                                                               
    """
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert (
        len(readme_words) >= 100
    ), "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    """
    Check if README contains required functions..
    """
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass

    assert (
        READMELOOKSGOOD == True
    ), "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    """
    Test function to check README file formatting.
    """
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    """
    Returns pass if used four spaces for each level of syntactically \
    significant indenting.
    """
    lines = inspect.getsource(session9)
    spaces = re.findall("\n +.", lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert (
            len(re.sub(r"[^ ]", "", space)) % 4 == 0
        ), "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    """
    Test function to check if any function names have any capital letters.
    """
    functions = inspect.getmembers(session9, inspect.isfunction)
    for function in functions:
        assert (
            len(re.findall("([A-Z])", function[0])) == 0
        ), "You have used Capital letter(s) in your function names"


def test_odd_sec():
    """
    Test for decorator that runs a function only if the second is odd.
    """
    temp = session9.odd_sec(session9.add)(1, 2)
    temp_dt = datetime.datetime.now().second

    if temp_dt % 2 == 0:
        assert temp == False
    else:
        assert temp == 3


def test_authenticate():
    """
    Test for authenticate decorator that runs a function only if passwords match.
    """
    temp_pass = session9.authenticate(session9.add, "secret", "secret")(1, 2)
    temp_fail = session9.authenticate(session9.add, "secret", "lol")

    assert temp_pass == 3 and temp_fail == False


def test_logged():
    """
    Test to run a a function n times where n is an integer.
    """
    temp = session9.logged(session9.add)(1, 2)
    temp_dt = datetime.datetime.now().hour

    assert temp == f"{temp_dt}: called {session9.add.__name__} = {3}"


def test_timed_fac():
    """
    Test to run a function n times. 
    """

    assert session9.timed_fac(5)(session9.add)(1, 2) == 3


def test_pr_fac():
    """
    Test to run function with different access levels.
    """
    assert session9.pr_fac(4)(session9.my_func)() == [
        "a",
        "b",
        "c",
        "d",
    ] and session9.pr_fac(2)(session9.my_func)() == ["a", "b"]
