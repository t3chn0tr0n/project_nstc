var email = document.getElementById('email');
var phone = document.getElementById('mob_no');

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
  document.getElementById("mob_no_submit").innerHTML = "&nbsp&nbsp&nbsp<span class=\"text-danger\">Phone no must be 10 digit!!</span>&nbsp&nbsp<input type=\"button\" class=\"btn btn-danger btn-sm\" onclick=\"cancel('mob_no_change', 'mob_no_submit', 'mob_no');\" value=\"Cancel\" />";
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
  $("#mob_no_submit").html("");
}

function check_phone() {
  var password = document.getElementById('password').value;
  var mob = document.getElementById('mob_no').value;
  //console.log(password);
  if (password != '') {
    $.ajax({
      type: "POST",
      url: "update_phone/",
      data: {
        password: password,
        mob_no: mob,
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
      },
      success: function (s) {
        if (s == '1') {
          alert("Update successful!!!");
          location.reload();
        } else {
          alert(s);
        }
      }
    });
  } else {
    alert("Please insert the password!!");
  }
}

function check_email() {
  var password = document.getElementById('pass_email').value;
  var email = document.getElementById('email').value;
  var card_no = (document.getElementById('card_no').textContent).trim();
  if (password != '') {
    $.ajax({
      type: "POST",
      url: "update_email/",
      data: {
        password: password,
        email: email,
        card_no: card_no,
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
      },
      success: function (s) {
        if (s == '1') {
          alert("Update successful!!!");
          location.reload();
        } else {
          alert(s);
        }
      }
    });
  } else {
    alert("Please insert the password!!");
  }
}

$(document).ready(function () {
  /*on change phone no*/
  $("#mob_no").keyup(function () {
    var mobile = document.getElementById('mob_no').value;
    if (mobile.length == 10) {
      $("#mob_no_submit").html("");
      document.getElementById("mob_no_submit").innerHTML = "&nbsp<lable class=\"col-1 col-form-label small text-secondary\" style=\"display: inline;\">Password:</lable>&nbsp&nbsp&nbsp<input type=\"password\" name=\"password\" class=\"col-md-4 form-control form-control-sm mb-2\" id=\"password\" style=\"display: inline;\" required />&nbsp&nbsp&nbsp<button type=\"submit\" onclick=\"check_phone()\" class=\"btn btn-success btn-sm\"  id=\"change_mobile_no\">Submit</button>&nbsp&nbsp&nbsp<input type=\"button\" class=\"btn btn-danger btn-sm\" onclick=\"cancel('mob_no_change', 'mob_no_submit', 'mob_no');\" value=\"Cancel\" />";
      document.getElementById("mob_no").disabled = true;
    }
  });
});
