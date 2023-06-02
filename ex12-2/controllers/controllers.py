# -*- coding: utf-8 -*-
# from odoo import http


# class Ex12-2(http.Controller):
#     @http.route('/ex12-2/ex12-2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ex12-2/ex12-2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ex12-2.listing', {
#             'root': '/ex12-2/ex12-2',
#             'objects': http.request.env['ex12-2.ex12-2'].search([]),
#         })

#     @http.route('/ex12-2/ex12-2/objects/<model("ex12-2.ex12-2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ex12-2.object', {
#             'object': obj
#         })
