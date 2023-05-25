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

	developer = fields.Many2one ( 'res.partner', string = "Developer" )
	periphery_id = fields.Many2one ( 'periphery.periphery', string = "Perephery" )
	feature_ids = fields.Many2many ( 'pc.feature', string = "Features" )


class Periphery ( models.Model ) :
	_name = 'periphery.periphery'
	_description = 'periphery for pc'

	name = fields.Char ( string = 'Periphery' )
	pc_ids = fields.One2many ( 'pc.pc', 'periphery_id', string = "PC's" )


class PcFeatures ( models.Model ) :
	_name = "pc.feature"
	_description = "many futers fom many pc"

	name = fields.Char ( string = 'Name' )
