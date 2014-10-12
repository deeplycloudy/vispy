# -*- coding: utf-8 -*-
# Copyright (c) 2014, Vispy Development Team.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
""" Tests to ensure that base vispy namespace functions correctly,
including configuration options.
"""

from nose.tools import assert_raises, assert_equal, assert_not_equal

import vispy.app
from vispy.testing import requires_application, run_tests_if_main


@requires_application('pyside')
def test_use():
    
    # Set default app to None, so we can test the use function
    vispy.app.use_app()
    default_app = vispy.app._default_app.default_app
    vispy.app._default_app.default_app = None
    
    app_name = default_app.backend_name.split(' ')[0]
    
    try:
        # With no arguments, should do nothing
        assert_raises(TypeError, vispy.use)
        assert_equal(vispy.app._default_app.default_app, None)
        
        # With only gl args, should do nothing to app
        vispy.use(gl='desktop')
        assert_equal(vispy.app._default_app.default_app, None)
        
        # Specify app (one we know works)
        vispy.use(app_name)
        assert_not_equal(vispy.app._default_app.default_app, None)
        
        # Again, but now wrong app
        wrong_name = 'glut' if app_name.lower() != 'glut' else 'pyglet'
        assert_raises(RuntimeError, vispy.use, wrong_name)
        
        # And both
        vispy.use(app_name, 'desktop')
    
    finally:
        # Restore
        vispy.app._default_app.default_app = default_app


run_tests_if_main()
