# -*- coding: utf-8 -*-
# from odoo import http


# class ExeKeclonFilters(http.Controller):
#     @http.route('/exe_keclon_filters/exe_keclon_filters/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/exe_keclon_filters/exe_keclon_filters/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('exe_keclon_filters.listing', {
#             'root': '/exe_keclon_filters/exe_keclon_filters',
#             'objects': http.request.env['exe_keclon_filters.exe_keclon_filters'].search([]),
#         })

#     @http.route('/exe_keclon_filters/exe_keclon_filters/objects/<model("exe_keclon_filters.exe_keclon_filters"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('exe_keclon_filters.object', {
#             'object': obj
#         })
