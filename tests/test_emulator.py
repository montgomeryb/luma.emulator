#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Richard Hull and contributors
# See LICENSE.rst for details.

"""
Tests for :py:class:`luma.emulator.device.emulator`.
"""

from luma.emulator.device import emulator

import pytest

import pygame

from PIL import Image, ImageDraw

from helpers import patch


def test_cleanup():
    device = emulator(1, 2, 3, 'RGB', 'none', 6)
    device.cleanup()


def test_alpha():
    w, h = 100, 50
    device = emulator(width=w, height=h, rotate=3, mode='RGB',
        transform='none', scale=6)

    im = Image.new('RGB', (w, h), (255, 0, 0))
    dr = ImageDraw.Draw(im)
    dr.ellipse((w / 2, h / 2, 10, 10), fill='black', outline='blue')
    surf = device.to_surface(im, alpha=0.5)

    assert isinstance(surf, pygame.Surface)


def test_pygame_missing():
    with patch.dict('sys.modules', {'pygame': None}):
        with pytest.raises(RuntimeError) as ex:
            emulator(1, 2, 3, 4, 5, 6)
        assert str(ex.value) == 'Emulator requires pygame to be installed'