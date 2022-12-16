# -*- coding: utf-8 -*-

import json
from odoo import models, fields, api


class SaleOrderFilter(models.Model):
    _inherit = 'sale.order'

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
                [('customer_rank', '>', 0)]
            )