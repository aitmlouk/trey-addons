# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
from openerp import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    subscription_days = fields.Integer(
        string='Subscription days')
