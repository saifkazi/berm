# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import Pool
from . import hsn

__all__ = ['register']


def register():
    Pool.register(
        hsn.HSNCODES,
        module='hsn-sac', type_='model')
    Pool.register(
        module='hsn-sac', type_='wizard')
    Pool.register(
        module='hsn-sac', type_='report')
