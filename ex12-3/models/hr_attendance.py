# -*- coding: utf-8 -*-
import time

from odoo import models, fields, api
import datetime
import pytz

class HrAttendance(models.Model):
	_inherit = 'hr.attendance'

	def check_out_cron(self):
		user = self.env.user
		# print(checked_out_records)
		server_datetime= datetime.datetime.now()
		# print('******** SERVER:', server_datetime)
		attendances_without_checkout = self.env['hr.attendance'].search([('check_out', '=', False)])
		# print('---------------',len(attendances_without_checkout))
		# print(attendances_without_checkout.read())
		attendances_without_checkout.check_and_auto_checkout()

	def check_and_auto_checkout(self):
		# TODO current_datetime deve ser guardada depois de convertida para o fuso horário do funcionário
		# e depois convertida de novo para UTC
		for rec in self.filtered(lambda attendance: attendance.check_out == False):
			user = rec.employee_id.user_id
			tz = pytz.timezone(user.tz)
			current_datetime = fields.datetime.now()
			with_local_tz = current_datetime.astimezone(tz)
			as_utc = with_local_tz.astimezone(pytz.utc).replace(tzinfo = None)
			if with_local_tz.strftime('%H:%M:%S') >= '15:00:00':
				rec.check_out = as_utc
