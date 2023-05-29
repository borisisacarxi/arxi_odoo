from odoo import fields, models, api


class PcWizard(models.TransientModel):
	_name = 'pc.wizard'
	_description = 'Pc Wizard'

	ram_update = fields.Integer("Update RAM")

	def update_new_ram(self):
		print("*************hello world")
		print('pc_id', self.env.context.get('active_id'))
		print('RAM:', self.ram_update)
		self.env['pc.pc'].browse(self.env.context.get('active_id')).write({
			'ram': self.ram_update
		})
		return {'type': 'ir.actions.act_window_close'}
