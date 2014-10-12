# -*- coding: utf-8 -*-
# vispy: gallery 30
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
"""
This example demonstrates the use of the SurfacePlot visual.
"""

import sys
import numpy as np

from vispy import app, scene
from vispy.util.filter import gaussian_filter
from vispy.scene.visuals.modular_point import ModularPoint

# vertex positions of data to draw
N = 2000000
x0,x1, y0,y1 = -1, 1, -1, 1
dx, dy = (x1-x0), (y1-y0)
xc, yc = (x0+x1)/2.0, (y0+y1)/2.0
zscale = 10/50.
pos = np.zeros((N, 3), dtype=np.float32)
pos[:, 0] = np.random.normal(size=N, scale=dy, loc=xc).astype(np.float32)
pos[:, 1] = np.random.normal(size=N, scale=dx, loc=yc).astype(np.float32)
pos[:, 2] = np.random.normal(size=N, scale=zscale, loc=zscale/2).astype(np.float32)
colors = np.abs(np.random.normal(size=(N,4)))
points = ModularPoint(pos, color=colors)

canvas = scene.SceneCanvas(keys='interactive')
canvas.show()
view = canvas.central_widget.add_view()
view.set_camera('turntable', mode='ortho', up='z', distance=2)

## Simple surface plot example
## x, y values are not specified, so assumed to be 0:50
# By using the modular_mesh example, it should be possible to put arbitrary colors on the surface.
# need to figure out how to specify faces for a quadrilateral mesh.
z = gaussian_filter(np.random.normal(size=(50, 50)), (1, 1)) * 10
p1 = scene.visuals.SurfacePlot(z=z, color=(0.5, 0.5, 1, 1), shading='smooth')
p1.transform = scene.transforms.AffineTransform()
p1.transform.scale([1/49., 1/49., 0.02])
p1.transform.translate([-0.5, -0.5, 0])

view.add(p1)
view.add(points)

# Add a 3D axis to keep us oriented
axis = scene.visuals.XYZAxis(parent=view.scene)

if sys.flags.interactive == 0:
    app.run()
