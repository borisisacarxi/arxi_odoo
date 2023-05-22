from odoo import models, api, fields


class Res_partner ( models.Model ) :
	_inherit = "res.partner"

	message = fields.Char ( string = "message" )
	other_message = fields.Char ( string = 'other message' )
