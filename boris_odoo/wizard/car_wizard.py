from odoo import fields, api, models


class carWizard ( models.TransientModel ) :
	_name = 'car.wizard'
	_description = 'car wizard'

	horse_power_plus = fields.Integer ( string = 'New Horse Power' )

	def submit_hp ( self ) :
		print ( '+++++++++++++++++test wizard FHP' )
		print ( 'car_id', self.env.context.get ( 'active_id' ) )
		print ( 'HP', self.horse_power_plus )

		self.env['car.car'].browse ( self.env.context.get ( 'active_id' ) ).write ( {
			'hps_car' : self.horse_power_plus } )
		return {'type': 'ir.actions.act_window_close'}