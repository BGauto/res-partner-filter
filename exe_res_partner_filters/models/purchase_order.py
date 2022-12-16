# -*- coding: utf-8 -*-

from odoo import models, fields, api
import json


class PurchaseOrderFilter(models.Model):
    _inherit = 'purchase.order'

    partner_id_domain = fields.Char(
        compute="_compute_partner_id_domain",
        readonly=True,
        store=False,
    )

    # @api.multi
    @api.depends('partner_id')
    def _compute_partner_id_domain(self):
        for rec in self:
            rec.partner_id_domain = json.dumps(
                [('supplier_rank', '>', 0)]
            )