# -*- coding: utf-8 -*-
# from odoo import http


# class Ex12(http.Controller):
#     @http.route('/ex12/ex12', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ex12/ex12/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ex12.listing', {
#             'root': '/ex12/ex12',
#             'objects': http.request.env['ex12.ex12'].search([]),
#         })

#     @http.route('/ex12/ex12/objects/<model("ex12.ex12"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ex12.object', {
#             'object': obj
#         })
