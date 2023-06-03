from odoo import fields, models, api


class ContactPersonCrm(models.Model):
	_inherit = 'crm.lead'
	_description = 'Contact person, angariador'

	crm_contact_person_field = fields.Many2one('res.users', string = 'Contact Person')

	@api.model_create_multi
	def create(self, val_list):
		result = super(ContactPersonCrm, self).create(val_list)
		print('**************', self.env.user.id, self.env.user.name)
		result.crm_contact_person_field = self.env.user.id
		return result

	def _prepare_opportunity_quotation_context(self):
		quatation_info = super(ContactPersonCrm, self)._prepare_opportunity_quotation_context()
		# res = super('crm_lead', self)
		print('***********************************',quatation_info)
		quatation_info['default_sale_contact_person_field'] = self.crm_contact_person_field.id
		print('***********************************', quatation_info)
		return quatation_info
