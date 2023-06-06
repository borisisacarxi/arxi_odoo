from odoo import fields, models, api


class ContactPersonInvoice(models.Model):
	_inherit = 'account.move'
	_description = 'Contact person, angariador'

	invoice_contact_person_field = fields.Many2one('res.users',string = 'Contact person')

	@api.model_create_multi
	def create(self, vals_list):
		info = super(ContactPersonInvoice, self).create(vals_list)
		contact_field = self.env['sale.order'].search([('name', '=', info.invoice_origin)])
		info.invoice_contact_person_field = contact_field.sale_contact_person_field.id
		print(info.read())
		return info