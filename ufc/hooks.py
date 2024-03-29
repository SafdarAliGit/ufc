from . import __version__ as app_version

app_name = "ufc"
app_title = "ufc"
app_publisher = "Tech Ventures"
app_description = "This is ufc"
app_email = "safdar211@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ufc/css/ufc.css"
# app_include_js = "/assets/ufc/js/ufc.js"

# include js, css files in header of web template
# web_include_css = "/assets/ufc/css/ufc.css"
# web_include_js = "/assets/ufc/js/ufc.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ufc/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "ufc.utils.jinja_methods",
#	"filters": "ufc.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "ufc.install.before_install"
# after_install = "ufc.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ufc.uninstall.before_uninstall"
# after_uninstall = "ufc.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "ufc.utils.before_app_install"
# after_app_install = "ufc.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "ufc.utils.before_app_uninstall"
# after_app_uninstall = "ufc.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ufc.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"ufc.tasks.all"
#	],
#	"daily": [
#		"ufc.tasks.daily"
#	],
#	"hourly": [
#		"ufc.tasks.hourly"
#	],
#	"weekly": [
#		"ufc.tasks.weekly"
#	],
#	"monthly": [
#		"ufc.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "ufc.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "ufc.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "ufc.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["ufc.utils.before_request"]
# after_request = ["ufc.utils.after_request"]

# Job Events
# ----------
# before_job = ["ufc.utils.before_job"]
# after_job = ["ufc.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"ufc.auth.validate"
# ]


required_apps = ["erpnext"]

doctype_js = {
	"BOM" : "public/sum_of_overhead_account.js",
	"Job Card" : "public/get_bom_and_operations.js"
}

doc_events = {
	"Job Card":{
		"on_submit": "ufc.overrides.pass_job_card_je.pass_job_card_je",
	}
}