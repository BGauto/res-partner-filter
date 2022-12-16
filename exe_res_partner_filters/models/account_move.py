# -*- coding: utf-8 -*-

from odoo import models, fields, api
import json
import logging
log = logging.getLogger(__name__)


class AccountMoveFilter(models.Model):
    _inherit = 'account.move'
    
    
    @api.depends('partner_id')
    def _compute_partner_id_domain(self):
        for rec in self:
            if rec.move_type=='in_invoice':
                rec.partner_id_domain = json.dumps(
                    [('supplier_rank', '>', 0)]
                )
            if rec.move_type=='out_invoice':
                rec.partner_id_domain = json.dumps(
                    [('customer_rank', '>', 0)]
                )
            if rec.move_type !='out_invoice' and rec.move_type !='in_invoice':
                rec.partner_id_domain = json.dumps(
                    [('customer_rank', '>=', 0),('supplier_rank', '>=', 0)]
                )
                
                
    partner_id_domain = fields.Char(
        compute='_compute_partner_id_domain',
        readonly=True,
        store=False,
    )



