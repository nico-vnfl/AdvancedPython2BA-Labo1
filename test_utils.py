import pytest
import utils


def test_fact():
    assert utils.fact(0) == 1
    assert utils.fact(5) == 120
    assert utils.fact(3) == 6


def test_fact_negative():
    with pytest.raises(ValueError):
        utils.fact(-1)


def test_roots_two():
    # x² - 3x + 2 = (x-1)(x-2)
    r = utils.roots(1, -3, 2)
    assert set(r) == {1, 2}


def test_roots_one():
    # x² - 2x + 1 = (x-1)²
    r = utils.roots(1, -2, 1)
    assert r == (1,)


def test_roots_none():
    # x² + 1 = 0 → pas de racines réelles
    r = utils.roots(1, 0, 1)
    assert r == ()


def test_integrate():
    result = utils.integrate('x**2 - 1', -1, 1)
    assert pytest.approx(result, 0.01) == -1.333333
