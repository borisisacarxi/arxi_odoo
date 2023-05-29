from odoo import models, fields, api


class ResPartner(models.Model):
	_inherit = "res.partner"

	position_role = fields.Char(string = "Role")

	msg_other_information = fields.Char(string = "Pai toto?" )
