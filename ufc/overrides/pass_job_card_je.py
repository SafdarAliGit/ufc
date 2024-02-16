import frappe


def pass_job_card_je(self, method):
    voucher_type = "Journal Entry"
    company = frappe.defaults.get_defaults().company
    posting_date = self.posting_date


    total_completed_qty = self.total_completed_qty if self.total_completed_qty else 0
    operating_cost = self.operating_cost if self.operating_cost else 0
    credit_account = 'Creditors - UFC'
    credit_party = self.supplier
    credit_party_type = 'Supplier'
    credit = total_completed_qty * operating_cost

    debit_account = 'Expenses Included In Valuation - UFC'
    debit = credit

    if credit > 0 and debit > 0:
        je = frappe.new_doc("Journal Entry")
        je.posting_date = posting_date
        je.voucher_type = voucher_type
        je.company = company
        je.job_card_id = self.name
        je.append("accounts", {
            'account': credit_account,
            'party_type': credit_party_type,
            'party': credit_party,
            'debit_in_account_currency': 0,
            'credit_in_account_currency': credit
        })
        je.append("accounts", {
            'account': debit_account,
            'debit_in_account_currency': debit,
            'credit_in_account_currency': 0
        })
        je.submit()
    else:
        frappe.throw("Debit or Credit cannot be zero")
