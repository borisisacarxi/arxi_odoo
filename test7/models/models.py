# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Pc ( models.Model ) :
	_name = "pc.pc"
	_description = "Pc class"

	name = fields.Char ( string = "Name" )
	brand = fields.Char ( string = "Brand" )
	ram = fields.Integer ( string = "Ram" )
	mb = fields.Char ( string = "Mother Board" )
	cpu = fields.Char ( string = "CPU" )
	gpu = fields.Char ( string = "GPU" )
