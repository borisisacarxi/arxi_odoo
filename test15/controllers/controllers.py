# -*- coding: utf-8 -*-
# from odoo import http


# class Test7(http.Controller):
#     @http.route('/test7/test7', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test7/test7/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test7.listing', {
#             'root': '/test7/test7',
#             'objects': http.request.env['test7.test7'].search([]),
#         })

#     @http.route('/test7/test7/objects/<model("test7.test7"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test7.object', {
#             'object': obj
#         })
