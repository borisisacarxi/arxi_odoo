from odoo import models, api, fields


class ResPartner ( models.Model ) :
	_inherit = "res.partner"

	message = fields.Char ( string = "message" )
	other_message = fields.Char ( string = 'other message' )

	car_count = fields.Integer ( string = 'Count', compute = 'get_car_number' )

	def get_car_number ( self ) :
		for rec in self :
			rec.car_count = self.env['fleet.vehicle'].search_count([('driver_id', '=', self.id)])

	def get_cars ( self ) :
		self.ensure_one ()
		return {
			'type' : 'ir.actions.act_window',
			'name' : 'Cars',
			'view_mode' : 'tree',
			'res_model' : 'fleet.vehicle',
			'domain' : [('driver_id', '=', self.id)],
			'context' : "{'create':False}"
		}
