import pytest


def test_dummy():
    x=10
    y=10
    assert  x == y

def test_second():
    name="Selenium"
    title="Its framework in Selenium"
    assert name in title
@pytest.mark.smoke
def comments():
    print("Checkingg!!!!")

@pytest.mark.regression
def comments():
    print("Checkingg datas!!!")