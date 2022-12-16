# -*- coding: utf-8 -*-
{
    'name': "Filtros de dominio personalizados",

    'summary': """
        Filtros para contactos (clientes y proveedores) en sale.order, purchase.order y account.move""",

    'description': """
        Filtros para contactos (clientes y proveedores) en sale.order, purchase.order y account.move
    """,

    'author': "Exemax SA - Martin Gonzalez",
    'website': "http://www.exemax.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','account','purchase','web_domain_field'],

    # always loaded
    'data': [
        'views/sale_order.xml',
        'views/purchase_order.xml',
        'views/account_move.xml',
        'views/res_partner.xml'
    ],
    # only loaded in demonstration mode
    'demo': [],
}
