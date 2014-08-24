#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Showcases *RGB* *colourspaces* computations.
"""

import numpy as np
import pprint
import colour

# Displaying :attr:`colour.RGB_COLOURSPACES` data.
pprint.pprint(sorted(colour.RGB_COLOURSPACES.keys()))

colourspace = colour.RGB_COLOURSPACES['ACES RGB']
print('Name: "{0}"'.format(colourspace.name))
print('Primaries: "{0}"'.format(colourspace.primaries))
print('Normalised primary matrix to "CIE XYZ": "{0}"'.format(
    colourspace.to_XYZ))
print('Normalised primary matrix from "CIE XYZ": "{0}"'.format(
    colourspace.to_RGB))
print('Transfer function: "{0}"'.format(colourspace.transfer_function))
print('Inverse transfer function: "{0}"'.format(
    colourspace.inverse_transfer_function))

# Calculating *ACES RGB* to *sRGB* transformation matrix.
print('"ACES RGB" colourspace to "sRGB" colourspace matrix:')
cat = colour.chromatic_adaptation_matrix(
    colour.xy_to_XYZ(colour.RGB_COLOURSPACES['ACES RGB'].whitepoint),
    colour.xy_to_XYZ(colour.RGB_COLOURSPACES['sRGB'].whitepoint))
print(np.dot(colour.RGB_COLOURSPACES['sRGB'].to_RGB,
             np.dot(cat, colour.RGB_COLOURSPACES['ACES RGB'].to_XYZ)))

# Converting from *sRGB* to *ProPhoto RGB*.
colour.RGB_to_RGB((0.35521588, 0.41, 0.24177934),
                  colour.RGB_COLOURSPACES['sRGB'],
                  colour.RGB_COLOURSPACES['ProPhoto RGB'])