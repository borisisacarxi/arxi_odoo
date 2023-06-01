from odoo import models, api, fields
import requests, base64
from io import BytesIO


class MailingContact(models.Model):
	_inherit = 'mailing.contact'

	gender = fields.Char(string = 'Gender')

	phone = fields.Char(string = 'Phone')

	picture = fields.Image(string = 'Picture', attachment = True)

	street = fields.Char(string = 'Street')
	city = fields.Char(string = 'City')
	state = fields.Char(string = 'State')
	postcode = fields.Char(string = 'Post Code')


	def delete_all_records(self):
		self.search([]).unlink()
		action = self.env['ir.actions.actions']._for_xml_id('mass_mailing.action_view_mass_mailing_contacts')
		return action


	def load_image_from_url(self, url_img):
		url = url_img  # Replace with your actual URL

		response = requests.get(url)  # save http response for image
		if response.status_code == 200:
			image_data = response.content

			# Store the image data in the binary field
			return base64.b64encode(image_data)
		else:
			# Handle error when the URL is invalid or the image cannot be fetched
			# You can raise an exception or display an error message
			pass

	def create_one_user(self):
		print("***********mailing contact create_one_user************")
		user = {}
		url = 'https://randomuser.me/api'  # read api
		data = requests.get(url).json()  # save dictionario data

		# add information to dictionary. will be easy to save to fields
		user.update({'gender': data['results'][0]['gender']})
		user.update({'name': '{} {} {}'.format(data['results'][0]['name']['title'], data['results'][0]['name']['first'],
		                                       data['results'][0]['name']['last'])})
		user.update({'street': '{} {}'.format(data['results'][0]['location']['street']['name'],
		                                      data['results'][0]['location']['street']['number'])})
		user.update({'city': data['results'][0]['location']['city']})
		user.update({'state': data['results'][0]['location']['state']})
		user.update({'country': data['results'][0]['location']['country']})
		user.update({'postcode': data['results'][0]['location']['postcode']})
		user.update({'email': data['results'][0]['email']})
		user.update({'phone': data['results'][0]['phone']})
		user.update({'avatar': data['results'][0]['picture']['large']})
		user_vals = {
			'name' : user['name'],
			'email' : user['email'],
			'country_id' : self.env["res.country"].search([('name', '=', user['country'])]).id,
			'gender' : user['gender'],
			'phone' : user['phone'],
			'city' : user['city'],
			'street' : user['street'],
			'state' : user['state'],
			'postcode' : user['postcode'],
			'picture': self.load_image_from_url(user['avatar']),
		}

		for k, v in user.items():
			print(k, v)
		return user_vals

	def open_wizard(self):
		action = self.env['ir.actions.actions']._for_xml_id('ex12.quantety_wizard_action')
		action.update(
			{'context': {
				'default_mailing_contact_id': self.id
				}
			})
		return action
