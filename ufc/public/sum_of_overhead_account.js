frappe.ui.form.on('Bom Overhead Account Items', {
    amount: function (frm) {
        calculate_net_total_amount(frm);
    },
    onload: function (frm) {
        calculate_net_total_amount(frm);
    }


});


function calculate_net_total_amount(frm) {
    var net_amount = 0; // Initialize net_amount with a default value
    var total_amount = 0;
    var total_cost = frm.doc.total_cost;

    // Using forEach loop to iterate over each row in the child table
    frm.doc.overhead_account.forEach(function(d) {
        net_amount += flt(d.amount);
        total_amount += flt(d.amount);
    });

    // Set the values of net_amount and total_amount
    frm.set_value("net_amount", net_amount);
    frm.set_value("total_amount", total_amount);
    frm.set_value("total_cost", total_amount + total_cost);
    
}

