# -*- coding: utf-8 -*-

from __future__ import annotations
import my_module    # The code to test


class TestSrc:
    def test_increment(self) -> None:
        assert my_module.increment(3) == 4

    def test_decrement(self) -> None:
        assert my_module.decrement(3) == 2
