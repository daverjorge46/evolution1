from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'heatmap': True,
		'heatmap_message': _('This is based on the Time Sheets created against this Work Order'),
		'fieldname': 'project',
                'non_standard_fieldnames': {
                        'Quotation': 'project'
                },
		'transactions': [
			{
				'label': _('Work Order'),
				'items': ['Task', 'Timesheet', 'Expense Claim', 'Issue' , 'Project Update']
			},
			{
				'label': _('Material'),
				'items': ['Material Request', 'Stock Entry']
			},
			{
				'label': _('Sales'),
				'items': ['Quotation', 'Sales Order', 'Delivery Note', 'Sales Invoice']
			},
			{
				'label': _('Purchase'),
				'items': ['Purchase Order', 'Purchase Receipt', 'Purchase Invoice']
			},
		]
	}
