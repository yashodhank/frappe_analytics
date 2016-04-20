import frappe
from frappe.core.doctype.doctype.doctype import DocType
from frappe.model.document import Document
import json

from .doctype_template import get_analytics_doctype_name, get_change_doctype_json


def sort_changed_field(doc, method):
    """ Gets changed field from doc hook, sorts into correct table, and
    removes doc from Frappe's Changed Fields table"""
    to_doctype_name = get_analytics_doctype_name(doc.changed_doctype)
    make_doctype_maybe(to_doctype_name)
    new_doc = Document(sanitize_document(doc, to_doctype_name))
    new_doc.save()
    doc.delete()


def sanitize_document(from_doc, to_doctype):
    """ Sanitizes document to only contain fields in destination doctype, plus
    the destination doctype"""
    meta = frappe.desk.form.meta.get_meta(to_doctype)
    fields = [field.fieldname for field in meta.fields]
    doc_dict = frappe.client.get(from_doc)
    sanitized_doc =  {k:v for k, v in doc_dict.iteritems() if k in fields}
    sanitized_doc['doctype'] = to_doctype
    return sanitized_doc


def make_doctype_maybe(doctype_name):
    """ Makes doctype for Analytics app, if necessary"""
    try:
        dt = frappe.client.get("DocType", doctype_name)
    except frappe.DoesNotExistError:
        dt = DocType(get_change_doctype_json(doctype_name))
        dt.insert()
