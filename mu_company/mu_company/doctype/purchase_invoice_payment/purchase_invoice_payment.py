# Copyright (c) 2025, Mu and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class PurchaseInvoicePayment(Document):
	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		account: DF.Link | None
		amount: DF.Currency
		base_amount: DF.Currency
		clearance_date: DF.Date | None
		default: DF.Check
		mode_of_payment: DF.Link
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		reference_no: DF.Data | None
		type: DF.ReadOnly | None
	# end: auto-generated types

	pass
