from odoo import fields, models


class ContactPersonCrm(models.Model):
	_inherit = 'crm.lead'
	_description = 'Contact person, angariador'

	crm_contact_person_field = fields.Char(string = 'Contact Person')
