# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "evolution"
app_title = "Evolution"
app_publisher = "Daver Jorge"
app_description = "Evolution MRO Aviation Software"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "daverjorge46@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_js = "assets/js/erpnext.min.js"
app_include_css = "assets/css/erpnext.css"
web_include_js = "assets/js/erpnext-web.min.js"
web_include_css = "assets/css/erpnext-web.css"

domains = {
	'Evolution': 'erpnext.domains.evolution',
	'Distribution': 'erpnext.domains.distribution',
	'Services': 'erpnext.domains.services'
}

website_context = {
	"favicon": 	"/assets/evolution/images/favicon.png",
	"splash_image": "/assets/evolution/images/splash.png"
}

email_brand_image = "assets/erpnext/images/erpnext-logo.jpg"

default_mail_footer = """
	<span>
		Sent via
		<a class="text-muted" href="https://jjaaviation.com" target="_blank">
			Evolution MRO
		</a>
	</span>
  """
# include js, css files in header of desk.html
# app_include_css = "/assets/evolution/css/evolution.css"
# app_include_js = "/assets/evolution/js/evolution.js"

# include js, css files in header of web template
# web_include_css = "/assets/evolution/css/evolution.css"
# web_include_js = "/assets/evolution/js/evolution.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "evolution.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "evolution.install.before_install"
# after_install = "evolution.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "evolution.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"evolution.tasks.all"
# 	],
# 	"daily": [
# 		"evolution.tasks.daily"
# 	],
# 	"hourly": [
# 		"evolution.tasks.hourly"
# 	],
# 	"weekly": [
# 		"evolution.tasks.weekly"
# 	]
# 	"monthly": [
# 		"evolution.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "evolution.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "evolution.event.get_events"
# }
fixtures = ['Terms and Conditions', 'Item Group', 'Letter Head', 'Website Theme', 'Website Settings', 'Web Page', 'Module Def', 'Performance', 'Operation', 'Asset Category', 'Custom Field', 'Custom Script', 'Property Setter', 'Print Settings', 'Print Format','Role Profile', 'Role', 'Report', 'Workflow', 'Workflow State']

