from odoo import fields, models, api


class ContactPersonSales(models.Model):
	# _name = 'blaaa'
	_inherit = 'sale.order'
	_description = 'Contact person, angariador'

	sale_contact_person_field = fields.Many2one('res.users',string = 'Contact Person')

	@api.model_create_multi
	def create(self, val_list):
		result = super(ContactPersonSales, self).create(val_list)
		return result


