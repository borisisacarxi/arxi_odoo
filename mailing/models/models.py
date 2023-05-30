# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class exercise12(models.Model):
#     _name = 'exercise12.exercise12'
#     _description = 'exercise12.exercise12'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class MailingList(models.Model):
	_name = 'mailinglist.mailinglist'
	_description = 'mailing list New Contacts 2023'

	name = fields.Char(string = 'Name')
	gender = fields.Selection([
        ('M', 'Male'),
        ('F', 'Female')
    ], string='Gender')

	email = fields.Char(string = 'Email')
	phone = fields.Char(string = 'Phone')

	picture = fields.Binary(string = 'Picture', attachment = True)

	street = fields.Char(string = 'Street')
	city = fields.Char(string = 'City')
	state = fields.Char(string = 'State')
	country = fields.Char(string = 'Country')
	postcode = fields.Char(string = 'Post Code')
