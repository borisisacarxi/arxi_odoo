# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class boris_odoo(models.Model):
#     _name = 'boris_odoo.boris_odoo'
#     _description = 'boris_odoo.boris_odoo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
