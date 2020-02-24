from __future__ import unicode_literals
from frappe import _


def get_data():
	return {
		'fieldname': 'material_request',
		'transactions': [
			{
				'label': _('Related'),
				'items': ['Request for Quotation', 'Supplier Quotation']
			},
                        {
                                'label': _('Related'),
                                'items': ['Purchase Order', "Stock Entry"]
                        } 
		]
	}
