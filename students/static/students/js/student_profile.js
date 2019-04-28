var email = document.getElementById('email')
var phone = document.getElementById('mob_no')

function change(div_id_1, div_id_2, id) {
    document.getElementById(div_id_2).style.display = 'inline';
    document.getElementById(div_id_1).style.display = 'none';
    document.getElementById(id).disabled = false;

    if (id == 'email') {
        email = document.getElementById(id).value;
    } else {
        phone = document.getElementById(id).value;
    }
    document.getElementById(id).value = "";
}

function cancel(div_id_1, div_id_2, id) {
    document.getElementById(div_id_1).style.display = 'inline';
    document.getElementById(div_id_2).style.display = 'none';
    if (id == 'email') {
        document.getElementById(id).value = email;
    } else {
        document.getElementById(id).value = phone;
    }
    document.getElementById(id).disabled = true;
}