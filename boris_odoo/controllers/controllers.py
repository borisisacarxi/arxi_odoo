# -*- coding: utf-8 -*-
# from odoo import http


# class BorisOdoo(http.Controller):
#     @http.route('/boris_odoo/boris_odoo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/boris_odoo/boris_odoo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('boris_odoo.listing', {
#             'root': '/boris_odoo/boris_odoo',
#             'objects': http.request.env['boris_odoo.boris_odoo'].search([]),
#         })

#     @http.route('/boris_odoo/boris_odoo/objects/<model("boris_odoo.boris_odoo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('boris_odoo.object', {
#             'object': obj
#         })
