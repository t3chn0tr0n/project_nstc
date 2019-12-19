function toggle(id1, id2) {
    document.getElementById(id2).hidden = false;
    document.getElementById(id1).hidden = true;
}
function editable() {
    $("#edt").prop('hidden', true)
    $("#generalDetailsForm :input").prop('disabled', false);
}
