from odoo import models, fields, api
from datetime import timedelta


# Marcaçao no calendario
class MaintenanceEquipment(models.Model):
	_inherit = "maintenance.equipment"


	@api.onchange('location')
	def _onchange_equipaments(self):#get_equipaments
		equipments = self.env["maintenance.equipment"].search([])
		teams = self.env["maintenance.team"].search([])
		print(teams.read())
		for e in equipments:
			if e.assign_date:
				event = self.env['calendar.event'].create({
					'name': e.name,
					'start': e.assign_date,
					'stop': e.assign_date + timedelta(days = 5),
					# 'maintenance_team_id': prev_team
				})
			# print('\t', e.assign_date, event, e.assign_date + timedelta(days = 2))
			# print(e.read())

	@api.model
	def create(self, val_list):
		prevention_team_today = self.env['maintenance.team'].search([('is_prevention', '=', True)])  #
		res = super(MaintenanceEquipment, self).create(val_list)
		res.maintenance_team_id = prevention_team_today
		return res

