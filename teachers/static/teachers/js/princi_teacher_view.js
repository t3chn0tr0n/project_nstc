$(document).ready( function () {
    $("#tableMain").DataTable();
});

function assign_hod(id,btn_id) {
  var is_conform = confirm("ARE YOU SURE U WANT TO ASSIGN HIM/HER AS AN HOD OF THIS DEPARTMENT??");
  if(is_conform == true)
  {
    var mentor_id=document.getElementById(id).value;
    $.ajax({
      type: "POST",
      url: "assign_hod/",
      data: {
        mentor_id: mentor_id,
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
      },
      success: function (e) {
        alert(e);
        location.reload();
      }
    })
  }
}
