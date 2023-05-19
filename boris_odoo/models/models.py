from odoo import models, fields


class Car ( models.Model ) :
	_name = 'car.car'
	_description = 'Cars'

	name = fields.Char ( string = 'Name' )
	hps_car = fields.Integer ( string = "HP's Car" )
	doors_car = fields.Integer ( string = "Doors's Car" )

	driver_id = fields.Many2one ( 'res.partner', string = 'Driver' )
	parking_id = fields.Many2one ( 'parking.parking', string = 'Parking Position' )


class Parking ( models.Model ) :
	_name = 'parking.parking'
	_description = 'parking'

	name = fields.Char ( string = "Parking's position" )
	car_ids = fields.One2many ( 'car.car', 'parking_id' )
