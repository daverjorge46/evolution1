from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Evolution Work Orders"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Project",
					"label": _("Work Orders"),
					"description": _("Work Order master."),
				},
				{
					"type": "doctype",
					"name": "Project Update",
				        "label": _("Work Order Update"),
					"description": _("Work Order Update."),
				},
				{
					"type": "doctype",
					"name": "Task",
					"route": "List/Task",
					"description": _("Work Order activity / task."),
				},
				{
					"type": "doctype",
					"name": "Project Type",
					"label": _("Work Order Type"),
					"description": _("Define Work Order type."),
				},
				{
					"type": "report",
					"route": "List/Task/Gantt",
					"doctype": "Task",
					"name": "Gantt Chart",
					"description": _("Gantt chart of all tasks.")
				}
			]
		},
		{
			"label": _("Evolution Modules"),
			"items": [
				{
					"type": "doctype",
					"name": "capabilities",
					"description": _("Capabilities database."),
				},
				{
					"type": "doctype",
					"name": "manuals",
					"description": _("Manual database"),
				},
				{
					"type": "doctype",
					"name": "assets",
					"description": _("Assets database"),
				},
				{
					"type": "doctype",
					"name": "items",
					"description": _("Items database"),
				}
			]
		},
		{
			"label": _("Evolution Time Tracking"),
			"items": [
				{
					"type": "doctype",
					"name": "Timesheet",
					"description": _("Timesheet for tasks."),
				},
				{
					"type": "doctype",
					"name": "Activity Type",
					"description": _("Types of activities for Time Logs"),
				},
				{
					"type": "doctype",
					"name": "Activity Cost",
					"description": _("Cost of various activities"),
				}
			]
		},
		{
			"label": _("Reports"),
			"icon": "fa fa-list",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Daily Timesheet Summary",
					"doctype": "Timesheet"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Work Order wise Stock Tracking",
					"doctype": "Project"
				}
			]
		}
	]
