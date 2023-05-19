
from odoo import models, fields


class Car ( models.Model ) :
	_name = 'car.car'
	_description = 'Cars'

	name = fields.Char ( string = 'Model' )
	hps_car = fields.Integer ( string = "HP's Car" )
	doors_car = fields.Integer ( string = "Doors's Car" )
