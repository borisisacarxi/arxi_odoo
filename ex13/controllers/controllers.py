# -*- coding: utf-8 -*-
# from odoo import http


# class Ex13(http.Controller):
#     @http.route('/ex13/ex13', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ex13/ex13/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ex13.listing', {
#             'root': '/ex13/ex13',
#             'objects': http.request.env['ex13.ex13'].search([]),
#         })

#     @http.route('/ex13/ex13/objects/<model("ex13.ex13"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ex13.object', {
#             'object': obj
#         })
