# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class ex13(models.Model):
#     _name = 'ex13.ex13'
#     _description = 'ex13.ex13'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
class ClienteProductNameMapping(models.Model):
	_inherit = "product.product"

	article = fields.Many2one('product.product', string = 'Article')
	customer = fields.Many2one('res.partner', string = 'Customer')

	article_id=fields.Many2one('tabele_one_2_many.tabele_one_2_many', string = 'article_id')

class TableOneToMany(models.Model):
	_name = "tabele_one_2_many.tabele_one_2_many"
	_description = "class for printing all table one to many"

	acticles_ids = fields.One2many('product.product','article_id', string="Article_ids")
