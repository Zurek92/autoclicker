#!/usr/bin/env python3
import time
from unittest.mock import patch

import pytest

from funcs import mouse_click
from funcs import mouse_scroll


@patch('funcs.pyautogui.click')
@pytest.mark.parametrize(
    'posx, posy, repeats, time_break, time_different', ((500, 500, 5, 1, 0.5), (500, 500, 5, 1, 0))
)
def test_mouse_click(mocked_click, posx, posy, repeats, time_break, time_different):
    time_before = time.time()
    mouse_click(posx, posy, repeats, time_break, time_different)
    time_after = time.time()
    mocked_click.assert_called_with(posx, posy)
    assert mocked_click.call_count == repeats
    min_possible_time = (time_break - time_different) * repeats
    max_possible_time = (time_break + time_different) * repeats
    assert round(min_possible_time, 1) <= round(time_after - time_before, 1) <= round(max_possible_time, 1)


@patch('funcs.pyautogui.scroll')
@pytest.mark.parametrize('scrolls, direction', ((5, 1), (-5, -1)))
def test_mouse_scroll(mocked_scroll, scrolls, direction):
    mouse_scroll(scrolls)
    mocked_scroll.assert_called_with(direction)
    assert mocked_scroll.call_count == abs(scrolls)
