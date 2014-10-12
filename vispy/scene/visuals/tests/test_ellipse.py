# -*- coding: utf-8 -*-
# Copyright (c) 2014, Vispy Development Team.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

"""
Tests for EllipseVisual
All images are of size (100,100) to keep a small file size
"""

from vispy import gloo
from vispy.scene import visuals, transforms
from vispy.testing import (requires_application, assert_image_equal,
                           TestingCanvas, run_tests_if_main)


@requires_application()
def test_circle_draw():
    """Test drawing circles without transform using EllipseVisual"""
    with TestingCanvas() as c:
        ellipse = visuals.Ellipse(pos=(75, 35, 0), radius=20,
                                  color=(1, 0, 0, 1))
        c.draw_visual(ellipse)
        assert_image_equal("screenshot", 'visuals/circle1.png')

        gloo.clear()
        ellipse = visuals.Ellipse(pos=(75, 35, 0), radius=20,
                                  color=(1, 0, 0, 1),
                                  border_color=(0, 1, 1, 1))
        c.draw_visual(ellipse)
        assert_image_equal("screenshot", 'visuals/circle2.png')

        gloo.clear()
        ellipse = visuals.Ellipse(pos=(75, 35, 0), radius=20,
                                  border_color=(0, 1, 1, 1))
        c.draw_visual(ellipse)
        assert_image_equal("screenshot", 'visuals/circle3.png')


@requires_application()
def test_ellipse_draw():
    """Test drawing transformed ellipses using EllipseVisual"""
    with TestingCanvas() as c:
        ellipse = visuals.Ellipse(pos=(0., 0.), radius=(20, 15),
                                  color=(0, 0, 1, 1))
        ellipse.transform = transforms.STTransform(scale=(2.0, 3.0),
                                                   translate=(50, 50))
        c.draw_visual(ellipse)
        assert_image_equal("screenshot", 'visuals/ellipse1.png')

        gloo.clear()
        ellipse = visuals.Ellipse(pos=(0., 0.), radius=(20, 15),
                                  color=(0, 0, 1, 1),
                                  border_color=(1, 0, 0, 1))
        ellipse.transform = transforms.STTransform(scale=(2.0, 3.0),
                                                   translate=(50, 50))
        c.draw_visual(ellipse)
        assert_image_equal("screenshot", 'visuals/ellipse2.png')

        gloo.clear()
        ellipse = visuals.Ellipse(pos=(0., 0.), radius=(20, 15),
                                  border_color=(1, 0, 0, 1))
        ellipse.transform = transforms.STTransform(scale=(2.0, 3.0),
                                                   translate=(50, 50))
        c.draw_visual(ellipse)
        assert_image_equal("screenshot", 'visuals/ellipse3.png')


@requires_application()
def test_arc_draw1():
    """Test drawing arcs using EllipseVisual"""
    with TestingCanvas() as c:
        ellipse = visuals.Ellipse(pos=(50., 50.), radius=(20, 15),
                                  start_angle=150., span_angle=120.,
                                  color=(0, 0, 1, 1))
        c.draw_visual(ellipse)
        assert_image_equal("screenshot", 'visuals/arc1.png')

        gloo.clear()
        ellipse = visuals.Ellipse(pos=(50., 50.), radius=(20, 15),
                                  start_angle=90., span_angle=120.,
                                  border_color=(1, 0, 0, 1))
        c.draw_visual(ellipse)
        assert_image_equal("screenshot", 'visuals/arc2.png')


@requires_application()
def test_reactive_draw():
    """Test reactive ellipse attributes"""
    with TestingCanvas() as c:
        ellipse = visuals.Ellipse(pos=[75, 35, 0.], radius=[20, 15],
                                  color='yellow')
        c.draw_visual(ellipse)

        gloo.clear()
        ellipse.pos = [70, 40, 0.]
        c.draw_visual(ellipse)
        assert_image_equal("screenshot", 'visuals/reactive_ellipse1.png')

        gloo.clear()
        ellipse.radius = 25
        c.draw_visual(ellipse)
        assert_image_equal("screenshot", 'visuals/reactive_ellipse2.png')

        gloo.clear()
        ellipse.color = 'red'
        c.draw_visual(ellipse)
        assert_image_equal("screenshot", 'visuals/reactive_ellipse3.png')

        gloo.clear()
        ellipse.border_color = 'yellow'
        c.draw_visual(ellipse)
        assert_image_equal("screenshot", 'visuals/reactive_ellipse4.png')

        gloo.clear()
        ellipse.start_angle = 140.
        c.draw_visual(ellipse)
        assert_image_equal("screenshot", 'visuals/reactive_ellipse5.png')

        gloo.clear()
        ellipse.span_angle = 100.
        c.draw_visual(ellipse)
        assert_image_equal("screenshot", 'visuals/reactive_ellipse6.png')

        gloo.clear()
        ellipse.num_segments = 10.
        c.draw_visual(ellipse)
        assert_image_equal("screenshot", 'visuals/reactive_ellipse7.png')


run_tests_if_main()
