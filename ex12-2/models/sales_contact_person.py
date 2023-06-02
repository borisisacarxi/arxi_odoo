from odoo import fields, models


class ContactPersonSales(models.Model):
	# _name = 'blaaa'
	_inherit = 'sale.order'
	_description = 'Contact person, angariador'

	sale_contact_person_field = fields.Char(string = 'Contact Person')
