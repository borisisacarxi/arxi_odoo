from odoo import models, fields, api


class Car ( models.Model ) :
	_name = 'car.car'
	_description = 'Cars'

	name = fields.Char ( string = 'Name' )
	hps_car = fields.Integer ( string = "HP's Car" )
	doors_car = fields.Integer ( string = "Doors's Car" )
	total_spead = fields.Integer ( string = 'Function result', compute = 'say_hello' )

	driver_id = fields.Many2one ( 'res.partner', string = 'Driver' )
	parking_id = fields.Many2one ( 'parking.parking', string = 'Parking Position' )
	feature_ids = fields.Many2many ( 'car.feature', string = 'Features' )
	greating_label = fields.Char ( string = 'Hello', related = "driver_id.name" )
	status = fields.Selection ( [('new', 'New'), ('used', 'Used'), ('sold', 'Sold')], string = 'status',
	                            default = 'new' )
	car_sequence = fields.Char ( string = 'Sequence' )

	@api.model
	def create ( self, vals_list ) :
		result = super ( Car, self ).create ( vals_list )
		return result

	def write ( self, vals_list ) :
		result = super ( Car, self ).write ( vals_list )
		return result
	def unlink(self) :
		return super ( Car, self ).unlink ()

	def say_hello ( self ) :
		for obj in self:
			obj.total_spead = obj.doors_car * obj.hps_car

	def set_status_to_new ( self ) :
		self.status = 'new'

	def set_status_to_used ( self ) :
		self.status = 'used'

	def set_status_to_sold ( self ) :
		self.status = 'sold'
		template_id = self.env.ref ( 'boris_odoo.car_mail_template' )
		if template_id and self.driver_id.email :
			template_id.send_mail (
				self.id,
				force_send = True,
				raise_exception = True,
				email_values = { 'email_to' : self.driver_id.email }
			)
			print ( '*********** ', self.driver_id.email )


class Parking ( models.Model ) :
	_name = 'parking.parking'
	_description = 'parking'

	name = fields.Char ( string = "Parking's position" )
	car_ids = fields.One2many ( 'car.car', 'parking_id' )


class car_features ( models.Model ) :
	_name = 'car.feature'
	_description = 'car_feature'

	name = fields.Char ( string = 'Name' )
