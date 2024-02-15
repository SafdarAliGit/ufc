frappe.ui.form.on('Job Card', {
    supplier: function (frm) {
        var bom_no = frm.doc.bom_no;
        var operation = frm.doc.operation;
        get_operating_cost(frm, bom_no, operation);
    },

});

function get_operating_cost(frm, bom_no, operation) {
    // Call the whitelisted server-side function
    frappe.call({
        method: 'ufc.ufc.doctype.utils.get_bom_and_operations.get_bom_and_operations',
        args: {'bom_id': bom_no, 'operation': operation}, // Replace 'your_bom_id' with the actual ID of the BOM
        callback: function (response) {
            var data = response.message;

            if (data) {
                var operating_cost = data.operating_cost;
                frm.set_value('operating_cost', operating_cost);
            }
        }
    });

}

