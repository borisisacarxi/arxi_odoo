from odoo import fields, api, models


class QuantetyWizard(models.TransientModel):
	_name = 'quantety.wizard'
	_description = "quantety wizard"

	quantety_field = fields.Integer(string = "Quantety", default = 1)

	mailing_contact_id = fields.Many2one('mailing.contact')

	# Action For Wizard Quantety
	def quantety_lol(self):
		count = 0
		contact_id = False
		print('***********FUNCTION QUANTETY_LOL', self.quantety_field)
		while count < self.quantety_field:
			vals_list = self.env['mailing.contact'].create_one_user()
			if self.mailing_contact_id.name and not self.env['mailing.contact'].search([('name', '=', vals_list['name'])]):
				contact_id = self.env['mailing.contact'].create(vals_list)
				count += 1
			else:
				self.mailing_contact_id.write(vals_list)
				count += 1
		return {
			'type': 'ir.actions.act_window',
			'name': contact_id.name if contact_id else self.mailing_contact_id.name,
			'view_mode': 'form',
			'views': [(False, "form")],
			'res_id': contact_id.id if contact_id else self.mailing_contact_id.id,
			'res_model': 'mailing.contact',
		}
