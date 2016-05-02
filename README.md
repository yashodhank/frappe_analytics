## Powerful Analytics for the Frappe Framework

This app works to do two things: enables field history tracking, and provides
advanced reports based on the data it creates.

Field history tracking is enabled on a module-by-module basis in the
"Document Versioning Settings" doctype. Upon changing a document in an enabled
module, the changed field(s) are sorted into a custom doctype named
[doctype] Field History.

Reporting is coming soon....here are some potential reports!
  - See your sales funnel and how quickly leads progress by 'status' field
  - With an 'estimated close date' field, see how many opportunities close
    or push in a given time period
  - Create burndown charts for project tasks
  - Track conversion rates through lead and opportunity stages - i.e.
    10% of Prospects become MQL's, 23% of MQL's become SQL's, etc.

### Contributing

If you have a report you'd like to have, or a better method for the backend,
send a pull request!

Reports should be created as a "page" in the analytics app - and should be kept
plug-and-play with the data provided by Frappe and ERPNext.

If your reports will require a custom field that isn't provided, set it up with
fixtures.

#### One BIG IMPORTANT to-do:
Delete a doc's field history when the doc is deleted.
Currently it won't work with the "on_trash" hook, as that runs after the doc
is deleted.


#### License

MIT
