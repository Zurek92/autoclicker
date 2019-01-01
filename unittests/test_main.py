#!/usr/bin/env python3
from unittest.mock import patch

import pyautogui
import pytest
from click.testing import CliRunner

from main import autoclicker


runner = CliRunner()


@patch('main.mouse_click')
@pytest.mark.parametrize(
    'params_invoke, posx, posy, repeats, time_break, time_different',
    (
        (['-t', 7, '-d', 0.5], 501, 501, 10000, 7, 0.5),
        (['-s', 450, 550, '-r', 5, '-t', 10, '-d', 1], 450, 550, 5, 10, 1),
    ),
)
def test_autoclicker_click(mocked_click, params_invoke, posx, posy, repeats, time_break, time_different):
    pyautogui.moveTo(501, 501)
    result = runner.invoke(autoclicker, ['clicker', *params_invoke])
    mocked_click.assert_called_with(posx, posy, repeats, time_break, time_different)
    assert result.exit_code == 0


@patch('main.mouse_click')
@pytest.mark.parametrize(
    'params_invoke',
    (
        ['-d', 7],
        ['-s', 500, 500, '-d', 2],
        ['-s', 500, '-t', 15],
        ['-s', 450, 'aaa', '-t', 10],
        ['-r', 'aa'],
        ['-t', '123a'],
        ['-t', 20, '-d', '12a'],
        ['-t', -10],
        ['-t', 20, '-d', -5],
    ),
)
def test_autoclicker_click_failed(mocked_click, params_invoke):
    result = runner.invoke(autoclicker, ['clicker', *params_invoke])
    assert mocked_click.call_count == 0
    assert result.exit_code in [1, 2]


def test_autoclicker_scroll():
    result = runner.invoke(autoclicker, ['scroll'])
    assert result.exit_code == 0
