# -*- coding: utf-8 -*-
{
	'name': "ex12-2",
	'license': "LGPL-3",

	'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

	'description': """
        Long description of module's purpose
    """,

	'author': "My Company",
	'website': "https://www.yourcompany.com",

	# Categories can be used to filter modules in modules listing
	# Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
	# for the full list
	'category': 'Uncategorized',
	'version': '0.1',

	# any module necessary for this one to work correctly
	'depends': ['base', 'crm', 'sale', 'sale_crm', 'account'],

	# always loaded
	'data': [
		# 'security/ir.model.access.csv',
		'views/views.xml',
		'views/templates.xml',
		'views/crm_inherit.xml',
		'views/sales_inherit.xml',
		'views/invoice_inherit.xml',
		'views/report_sale_order_product_inherit.xml',
	],
	# only loaded in demonstration mode
	'demo': [
		'demo/demo.xml',
	],
}
