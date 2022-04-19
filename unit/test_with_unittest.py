# -*- coding: utf-8 -*-

from unittest import TestCase

import pytest


@pytest.mark.skip('old version')
class TryTesting(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

    def test_always_fails(self):
        self.assertTrue(False)
