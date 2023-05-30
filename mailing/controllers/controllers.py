# -*- coding: utf-8 -*-
# from odoo import http


# class Mailing(http.Controller):
#     @http.route('/mailing/mailing', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mailing/mailing/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mailing.listing', {
#             'root': '/mailing/mailing',
#             'objects': http.request.env['mailing.mailing'].search([]),
#         })

#     @http.route('/mailing/mailing/objects/<model("mailing.mailing"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mailing.object', {
#             'object': obj
#         })
