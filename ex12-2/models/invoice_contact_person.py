from odoo import fields, models


class ContactPersonInvoice(models.Model):
	_inherit = 'res.partner'
	_description = 'Contact person, angariador'

	invoice_contact_person_field = fields.Char(string = 'Contact person')