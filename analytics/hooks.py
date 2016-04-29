# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "analytics"
app_title = "Analytics"
app_publisher = "Alec Ruiz-Ramon"
app_description = "Advanced analytics for Frappe Framework applications"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "alec.ruizramon@me.com"
app_version = "0.0.1"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/analytics/css/analytics.css"
# app_include_js = "/assets/analytics/js/analytics.js"

# include js, css files in header of web template
# web_include_css = "/assets/analytics/css/analytics.css"
# web_include_js = "/assets/analytics/js/analytics.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "analytics.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "analytics.install.before_install"
#after_install = "analytics.analytics.common_methods.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "analytics.notifications.get_notification_config"

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

doc_events = {
    "*": {
        "before_save": "analytics.analytics.common_methods.dump_pre_save_doc",
    },
    "Doc History Temp": {
        "after_insert": "analytics.analytics.common_methods.sort_temp_entries"
    }
}

# Scheduled Tasks
# ---------------

#scheduler_events = {
# 	"all": [
# 		"analytics.analytics.common_methods.sort_temp_entries"
# 	],
# 	"daily": [
# 		"analytics.tasks.daily"
# 	],
# 	"hourly": [
# 		"analytics.tasks.hourly"
# 	],
# 	"weekly": [
# 		"analytics.tasks.weekly"
# 	]
# 	"monthly": [
# 		"analytics.tasks.monthly"
# 	]
#}

# Testing
# -------

# before_tests = "analytics.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "analytics.event.get_events"
# }
