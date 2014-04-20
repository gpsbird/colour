#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**adobeRgb1998.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	Defines **Color** package *Adobe RGB 1998* colorspace.

**Others:**

"""

#**********************************************************************************************************************
#***	Future imports.
#**********************************************************************************************************************
from __future__ import unicode_literals

#**********************************************************************************************************************
#***    External imports.
#**********************************************************************************************************************
import numpy

#**********************************************************************************************************************
#***	Internal Imports.
#**********************************************************************************************************************
import color.exceptions
import color.illuminants
import color.verbose
from color.colorspaces.colorspace import Colorspace

#**********************************************************************************************************************
#***	Module attributes.
#**********************************************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2013 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["LOGGER",
		   "ADOBE_RGB_1998_PRIMARIES",
		   "ADOBE_RGB_1998_WHITEPOINT",
		   "ADOBE_RGB_1998_TO_XYZ_MATRIX",
		   "XYZ_TO_ADOBE_RGB_1998_MATRIX",
		   "ADOBE_RGB_1998_TRANSFER_FUNCTION",
		   "ADOBE_RGB_1998_INVERSE_TRANSFER_FUNCTION",
		   "ADOBE_RGB_1998_COLORSPACE"]

LOGGER = color.verbose.installLogger()

#**********************************************************************************************************************
#*** *Adobe RGB 1998*
#**********************************************************************************************************************
# http://www.adobe.com/digitalimag/pdfs/AdobeRGB1998.pdf
ADOBE_RGB_1998_PRIMARIES = numpy.matrix([0.6400, 0.3300,
										 0.2100, 0.7100,
										 0.1500, 0.0600]).reshape((3, 2))

ADOBE_RGB_1998_WHITEPOINT = color.illuminants.ILLUMINANTS.get("Standard CIE 1931 2 Degree Observer").get("D65")

# http://www.adobe.com/digitalimag/pdfs/AdobeRGB1998.pdf: 4.3.5.3 Converting RGB to normalized XYZ values
ADOBE_RGB_1998_TO_XYZ_MATRIX = numpy.matrix([0.57666809, 0.18556195, 0.1881985,
											 0.29734449, 0.62737611, 0.0752794,
											 0.02703132, 0.07069027, 0.99117879]).reshape((3, 3))

XYZ_TO_ADOBE_RGB_1998_MATRIX = ADOBE_RGB_1998_TO_XYZ_MATRIX.getI()

def __adobe1998TransferFunction(RGB):
	"""
	Defines the *Adobe RGB 1998* colorspace transfer function.

	Reference: http://www.adobe.com/digitalimag/pdfs/AdobeRGB1998.pdf

	:param RGB: RGB Matrix.
	:type RGB: Matrix (3x1)
	:return: Companded RGB Matrix.
	:rtype: Matrix (3x1)
	"""

	RGB = map(lambda x: x ** (1 / (563. / 256.)), numpy.ravel(RGB))
	return numpy.matrix(RGB).reshape((3, 1))

def __adobe1998InverseTransferFunction(RGB):
	"""
	Defines the *Adobe RGB 1998* colorspace inverse transfer function.

	Reference: http://www.adobe.com/digitalimag/pdfs/AdobeRGB1998.pdf

	:param RGB: RGB Matrix.
	:type RGB: Matrix (3x1)
	:return: Companded RGB Matrix.
	:rtype: Matrix (3x1)
	"""

	RGB = map(lambda x: x ** (563. / 256.), numpy.ravel(RGB))
	return numpy.matrix(RGB).reshape((3, 1))

ADOBE_RGB_1998_TRANSFER_FUNCTION = __adobe1998TransferFunction

ADOBE_RGB_1998_INVERSE_TRANSFER_FUNCTION = __adobe1998InverseTransferFunction

ADOBE_RGB_1998_COLORSPACE = Colorspace("Adobe RGB 1998",
									   ADOBE_RGB_1998_PRIMARIES,
									   ADOBE_RGB_1998_WHITEPOINT,
									   ADOBE_RGB_1998_TO_XYZ_MATRIX,
									   XYZ_TO_ADOBE_RGB_1998_MATRIX,
									   ADOBE_RGB_1998_TRANSFER_FUNCTION,
									   ADOBE_RGB_1998_INVERSE_TRANSFER_FUNCTION)