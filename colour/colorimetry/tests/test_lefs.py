#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Defines unit tests for :mod:`colour.colorimetry.lefs` module.
"""

from __future__ import division, unicode_literals

import numpy as np
import unittest

from colour.colorimetry import (mesopic_weighting_function,
                                mesopic_luminous_efficiency_function)
from colour.utilities import ignore_numpy_errors

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2017 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = [
    'MESOPIC_LEF_SPD_DATA', 'TestMesopicWeightingFunction',
    'TestMesopicLuminousEfficiencyFunction'
]

MESOPIC_LEF_SPD_DATA = (
    0.000423996221042,
    0.000478105586021,
    0.000539901310829,
    0.000612292743837,
    0.000696128469661,
    0.000792943994169,
    0.000907002019269,
    0.001038991062951,
    0.001192298013423,
    0.001370309788741,
    0.001577100133700,
    0.001816732944066,
    0.002094217578858,
    0.002416076568544,
    0.002788832443596,
    0.003219694655734,
    0.003722285106836,
    0.004295769587890,
    0.004953150383591,
    0.005714298941411,
    0.006578479021522,
    0.007565798249134,
    0.008691294922216,
    0.009963802139828,
    0.011405891376328,
    0.013040134056330,
    0.014875060844050,
    0.016931081053406,
    0.019221107382718,
    0.021751183317789,
    0.024534221556937,
    0.027577375342778,
    0.030917278398861,
    0.034514896661912,
    0.038399887696429,
    0.042574431719405,
    0.047107420323755,
    0.051932288874149,
    0.057054111113075,
    0.062546652908218,
    0.068346295876871,
    0.074525532476839,
    0.080944093388470,
    0.087734408501845,
    0.094891523456653,
    0.102273099642187,
    0.109877001609769,
    0.117842125286601,
    0.126031604242477,
    0.134377265167241,
    0.143017004659794,
    0.151812831610346,
    0.160832831284698,
    0.170008823906160,
    0.179272634672297,
    0.188693478005329,
    0.198204129185973,
    0.207803250139006,
    0.217418447891767,
    0.227114713721992,
    0.236819654657020,
    0.246462295387537,
    0.256115392006985,
    0.265716062322745,
    0.275338793469816,
    0.284852031027409,
    0.294464840899776,
    0.303490271989407,
    0.313234753059177,
    0.322325715015028,
    0.331451347544553,
    0.340612983748718,
    0.349811757758196,
    0.358361748146747,
    0.367637792269774,
    0.376267037500552,
    0.384939235443477,
    0.393654052823306,
    0.402407748998520,
    0.411196583327596,
    0.419329893917046,
    0.428180314526271,
    0.436380414469050,
    0.445311711528396,
    0.454294964705678,
    0.462650937976521,
    0.471757050335889,
    0.480930016713931,
    0.490177596952101,
    0.499507550891852,
    0.509614559626605,
    0.519129332097892,
    0.529425904805685,
    0.539131693733156,
    0.549621720283231,
    0.560210336613821,
    0.570219774106467,
    0.581020791225554,
    0.591909355273857,
    0.602868354806121,
    0.613880678377089,
    0.624937372323546,
    0.636061964882719,
    0.646598972109041,
    0.657953823040568,
    0.668784162222337,
    0.679793972609001,
    0.690988775626207,
    0.702382747907381,
    0.713303244319125,
    0.724451313004257,
    0.735847049962440,
    0.746811890694040,
    0.758029423698604,
    0.769496415708862,
    0.780522562977852,
    0.791780560381546,
    0.802612337360557,
    0.813079325993057,
    0.823929780124040,
    0.835225181574250,
    0.845634267482597,
    0.856481883918201,
    0.867692173456598,
    0.878502108708491,
    0.888148910997447,
    0.898640517466401,
    0.907932280953237,
    0.917425551604990,
    0.925773944818251,
    0.935065632506880,
    0.943236567905124,
    0.950906320820545,
    0.958693118011219,
    0.965841393473861,
    0.972282552199726,
    0.977992469040708,
    0.983610660576306,
    0.988346542031548,
    0.992096449883431,
    0.995443641860918,
    0.997620215802517,
    0.999345724088358,
    1.000000000000000,
    0.999649798070971,
    0.999048794086766,
    0.997535634478154,
    0.995761525329390,
    0.993014375646354,
    0.989955936938867,
    0.985874118212809,
    0.981445295294584,
    0.976688569332386,
    0.970936319192731,
    0.964894766246075,
    0.958583260353477,
    0.952011998742489,
    0.944491622775044,
    0.936708904475390,
    0.929350665610349,
    0.921042964190838,
    0.912477248043005,
    0.903660431384556,
    0.894595846967911,
    0.884599956036092,
    0.875050033330603,
    0.865945730653430,
    0.855922407876719,
    0.845684595123427,
    0.835249901264545,
    0.825322906165605,
    0.815207983624290,
    0.804220500547010,
    0.794420922234228,
    0.783746644454823,
    0.773568077475167,
    0.762780824836753,
    0.752271069434583,
    0.741754989619506,
    0.731290980804024,
    0.720798313160170,
    0.710193918959030,
    0.699636273302128,
    0.689065687470055,
    0.678559906736370,
    0.668059341866812,
    0.657569762999898,
    0.647157872557888,
    0.636820835214096,
    0.626487173259215,
    0.616154150851706,
    0.605889614493019,
    0.595700080460271,
    0.585593706535502,
    0.575441266250360,
    0.565388301637279,
    0.555374278353102,
    0.545468087493321,
    0.535597256497158,
    0.525826697054231,
    0.516015244478566,
    0.506232237548814,
    0.496559550172129,
    0.486874671127568,
    0.477329907437551,
    0.467802847366283,
    0.458370440306148,
    0.448972251399137,
    0.439760637410242,
    0.430613136861096,
    0.421544622781150,
    0.412568127724641,
    0.403755029915728,
    0.395035990575763,
    0.386410412793862,
    0.377877749401719,
    0.369440537270578,
    0.361107481350787,
    0.352859660514895,
    0.344705630485531,
    0.336647077772802,
    0.328691712475589,
    0.320841076613668,
    0.313080884593691,
    0.305410539504777,
    0.297822525480953,
    0.290302706156591,
    0.282872778768479,
    0.275531191822063,
    0.268290082505259,
    0.261147799838367,
    0.254117629825878,
    0.247188574621679,
    0.240357052760484,
    0.233605744351966,
    0.226937937143361,
    0.220352731030957,
    0.213846544549470,
    0.207394601159948,
    0.200978993535962,
    0.194581814351080,
    0.188194308912381,
    0.181822635824193,
    0.175498734556038,
    0.169247675364920,
    0.163087659295321,
    0.157025700050094,
    0.151071000005320,
    0.145246954751365,
    0.139584565754938,
    0.134108701934053,
    0.128840802337855,
    0.123766619272101,
    0.118863181142645,
    0.114107516355346,
    0.109476653316060,
    0.104961368330458,
    0.100567919488016,
    0.096292436342783,
    0.092129674606303,
    0.088077824596383,
    0.084130597430525,
    0.080288739247331,
    0.076555990214584,
    0.072936727678744,
    0.069434592322446,
    0.066049096194732,
    0.062779244444135,
    0.059627872397338,
    0.056597078717201,
    0.053689599245262,
    0.050906885990927,
    0.048244432277043,
    0.045695095070067,
    0.043251069286492,
    0.040905236764061,
    0.038653732504820,
    0.036495591265975,
    0.034428544786178,
    0.032450118727706,
    0.030557907444960,
    0.028749627753821,
    0.027023338509577,
    0.025377681739976,
    0.023811304447019,
    0.022322652530592,
    0.020908627975848,
    0.019568807970913,
    0.018305670643421,
    0.017121625428881,
    0.016019287839177,
    0.014998624949462,
    0.014053763109294,
    0.013178438781201,
    0.012366256017720,
    0.011610755153519,
    0.010909796310463,
    0.010258783274767,
    0.009647645070271,
    0.009066521771446,
    0.008505352350642,
    0.007956703372438,
    0.007422984272341,
    0.006909491686943,
    0.006421306227945,
    0.005963729506196,
    0.005537741450392,
    0.005140198329894,
    0.004770003226209,
    0.004426333586668,
    0.004108134205482,
    0.003814898916435,
    0.003545595063702,
    0.003298484428587,
    0.003071843028242,
    0.002863947377246,
    0.002673821526309,
    0.002500026114851,
    0.002340163148156,
    0.002191847872506,
    0.002052667559907,
    0.001920775671288,
    0.001795998699814,
    0.001678462683692,
    0.001568320640552,
    0.001465704482962,
    0.001370202034484,
    0.001281000501467,
    0.001197625742439,
    0.001119582510866,
    0.001046395670422,
    0.000977644493684,
    0.000913102154518,
    0.000852563310843,
    0.000795835861579,
    0.000742713469792,
    0.000692929112612,
    0.000646294076190,
    0.000602683198736,
    0.000561985056886,
    0.000524088227275,
    0.000488865075198,
    0.000456100902232,
    0.000425592157031,
    0.000397124984426,
    0.000370486903095,
    0.000345511126189,
    0.000322107797301,
    0.000300185818831,
    0.000279651295749,
    0.000260410283283,
    0.000242354880318,
    0.000225413417278,
    0.000209548506700,
    0.000194724821881,
    0.000180904975355,
    0.000168036678203,
    0.000156055324297,
    0.000144907947270,
    0.000134542904857,
    0.000124905757365,
    0.000115947828132,
    0.000107630246890,
    0.000099921825045,
    0.000092792011184,
    0.000086209517226,
    0.000080138556943,
    0.000074542690348,
    0.000069382092589,
    0.000064618362399,
    0.000060213148254,
    0.000056133629529,
    0.000052356318257,
    0.000048854801130,
    0.000045601913255,
    0.000042571186609,
    0.000039737093303,
    0.000037085765108,
    0.000034608253334,
    0.000032294917398,
    0.000030137485583,
    0.000028122278208,
    0.000026238700578,
    0.000024479703696,
    0.000022839057899,
    0.000021310391162,
    0.000019886198277,
    0.000018558646686,
    0.000017321059987,
    0.000016166624394,
    0.000015088526124,
    0.000014080323512,
    0.000013137863053,
    0.000012257679587,
    0.000011436518999,
    0.000010671063462,
    0.000009957265824,
    0.000009291440160,
    0.000008670655686,
    0.000008091780515,
    0.000007551893809)  # yapf: disable


class TestMesopicWeightingFunction(unittest.TestCase):
    """
    Defines :func:`colour.colorimetry.lefs.mesopic_weighting_function`
    definition unit tests methods.
    """

    def test_mesopic_weighting_function(self):
        """
        Tests :func:`colour.colorimetry.lefs.mesopic_weighting_function`
        definition.
        """

        self.assertAlmostEqual(
            mesopic_weighting_function(500, 0.2), 0.70522000, places=7)

        self.assertAlmostEqual(
            mesopic_weighting_function(
                500, 0.2, source='Red Heavy', method='LRC'),
            0.90951000,
            places=7)

        self.assertAlmostEqual(
            mesopic_weighting_function(
                700, 10, source='Red Heavy', method='LRC'),
            0.00410200,
            places=7)

    def test_n_dimensional_planck_law(self):
        """
        Tests :func:`colour.colorimetry.lefs.mesopic_weighting_function`
        definition n-dimensional arrays support.
        """

        wl = 500
        Vm = 0.70522000
        np.testing.assert_almost_equal(mesopic_weighting_function(wl, 0.2), Vm)

        wl = np.tile(wl, 6)
        Vm = np.tile(Vm, 6)
        np.testing.assert_almost_equal(mesopic_weighting_function(wl, 0.2), Vm)

        wl = np.reshape(wl, (2, 3))
        Vm = np.reshape(Vm, (2, 3))
        np.testing.assert_almost_equal(mesopic_weighting_function(wl, 0.2), Vm)

        wl = np.reshape(wl, (2, 3, 1))
        Vm = np.reshape(Vm, (2, 3, 1))
        np.testing.assert_almost_equal(mesopic_weighting_function(wl, 0.2), Vm)

    @ignore_numpy_errors
    def test_nan_mesopic_weighting_function(self):
        """
        Tests :func:`colour.colorimetry.lefs.mesopic_weighting_function`
        definition nan support.
        """

        mesopic_weighting_function(
            np.array([-1.0, 0.0, 1.0, -np.inf, np.inf, np.nan]), 0.2),


class TestMesopicLuminousEfficiencyFunction(unittest.TestCase):
    """
    Defines :func:`colour.colorimetry.lefs.\
mesopic_luminous_efficiency_function` definition unit tests methods.
    """

    def test_mesopic_luminous_efficiency_function(self):
        """
        Tests :func:`colour.colorimetry.lefs.\
mesopic_luminous_efficiency_function` definition.
        """

        np.testing.assert_almost_equal(
            mesopic_luminous_efficiency_function(0.2).values,
            MESOPIC_LEF_SPD_DATA,
            decimal=7)


if __name__ == '__main__':
    unittest.main()