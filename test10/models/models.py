# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Pc(models.Model):
	_name = "pc.pc"
	_description = "Pc class"

	name = fields.Char(string = "Name")
	brand = fields.Char(string = "Brand")
	ram = fields.Integer(string = "Ram")
	mb = fields.Char(string = "Mother Board")
	cpu = fields.Char(string = "CPU")
	gpu = fields.Char(string = "GPU")

	# ---------------Related Fields---------------------------
	developer = fields.Many2one('res.partner', string = "Developer")
	periphery_id = fields.Many2one('periphery.periphery', string = "Perephery")
	feature_ids = fields.Many2many('pc.feature', string = "Features")

	# ------------Functional fields and Create Form Buttons--------------
	recomended_ram = fields.Char(string = "Recomended RAM", compute = "get_rec_ram")

	def get_rec_ram(self):
		if self.ram < 16:
			self.recomended_ram = "Not Enought"
		elif self.ram == 16:
			self.recomended_ram = "Enought"
		else:
			self.recomended_ram = "More Then Enought"

	# -------------------Functional buttons----------------------
	status = fields.Selection([('new', 'NEW'), ('used', 'USED'), ('broken', 'broken')], string = "Status", default = 'new')

	# -------method for statusbar--------
	def set_new(self):
		self.status = 'new'

	def set_used(self):
		self.status = 'used'

	def set_broken(self):
		self.status = 'broken'


	class Periphery(models.Model):
		_name = 'periphery.periphery'
		_description = 'periphery for pc'

		name = fields.Char(string = 'Periphery')
		pc_ids = fields.One2many('pc.pc', 'periphery_id', string = "PC's")

	class PcFeatures(models.Model):
		_name = "pc.feature"
		_description = "many futers fom many pc"

		name = fields.Char(string = 'Name')

	# class ReportInfoPC(models.Model):
	# 	_name = "reportInfoPc.reportInfoPc"
	# 	_description = "report info about pc in PDF"
	#
	# 	name = fields.Char(string = "Report Info PC")
