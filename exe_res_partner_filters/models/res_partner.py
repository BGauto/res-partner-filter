# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartnerCustomization(models.Model):
    _inherit = 'res.partner'

    def increase_customer_rank_custom(self):
        for rec in self:
            if rec.customer_rank==0:
                rec._increase_rank('customer_rank', n=1)

    def increase_supplier_rank_custom(self):
        for rec in self:
            if rec.supplier_rank==0:
                rec._increase_rank('supplier_rank', n=1)
