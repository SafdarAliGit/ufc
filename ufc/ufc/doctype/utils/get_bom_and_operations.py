import frappe


@frappe.whitelist()
def get_bom_and_operations(bom_id, operation):
    # Fetch BOM
    bom = frappe.get_doc("BOM", bom_id)
    # Fetch BOM Operation for the specified operation
    bom_operation = frappe.get_all("BOM Operation", filters={"parent": bom_id, "operation": operation},fields=["operating_cost"], limit=1)
    operating_cost = bom_operation[0].get("operating_cost") if bom_operation else None
    return {"operating_cost": operating_cost}

