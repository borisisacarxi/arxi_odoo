# -*- coding: utf-8 -*-
# from odoo import http


# class Ex12-3(http.Controller):
#     @http.route('/ex12-3/ex12-3', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ex12-3/ex12-3/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ex12-3.listing', {
#             'root': '/ex12-3/ex12-3',
#             'objects': http.request.env['ex12-3.ex12-3'].search([]),
#         })

#     @http.route('/ex12-3/ex12-3/objects/<model("ex12-3.ex12-3"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ex12-3.object', {
#             'object': obj
#         })
