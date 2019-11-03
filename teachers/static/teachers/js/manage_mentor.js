$(document).ready(function() {
  $("#show").click(function() {
    var content = document.getElementById("content");
    console.log(content);
    var txtarea = document.getElementById("txtarea");
    var mentor_id = document.getElementById("mentor_select").value;
    var batch_id = document.getElementById("batch").value;
    var info = txtarea.value.split(",");
    console.log(info[0]);

    //JSON.stringify(array_s1)
    $.ajax({
      type: "POST",
      url: "mentor_student_show/",
      data: {
        //'student_id': id,
        mentor_id: mentor_id,
        batch_id: batch_id,
        // info: JSON.stringify(info),
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
      },
      success: function(s) {
        //content.style.display = "block";
        //$("#content").show();
        txtarea.value = s;
        console.log(s);
        txtarea.disabled = false;
        var elem = document.getElementById("fuctional_buttons");
        // // elem.parentNode.removeChild(elem);
        // document.getElementById("edit").remove();
        // document.getElementById("gen_cert").remove();
        var button = document.createElement("button");
        button.setAttribute("id", "save_changes");
        button.setAttribute("onclick", "save_changes()");
        button.className = "btn btn-sm btn-outline-success";
        button.innerText = "Save Changes";
        elem.appendChild(button);
      }
    });
  });
});
function save_changes() {
  var conf = confirm(
    "Are you sure you want to generate certificate of this student? Make sure cannot edit any details once the certificate has been generated."
  );
  if (conf == false) {
    return;
  }
  var txtarea = document.getElementById("txtarea");
  var mentor_id = document.getElementById("mentor_select").value;
  var batch_id = document.getElementById("batch").value;
  var info = txtarea.value.split(",");
  if (txtarea.value != "") {
    $.ajax({
      type: "POST",
      url: "mentor_change/",
      data: {
        //'student_id': id,
        mentor_id: mentor_id,
        batch_id: batch_id,
        info: JSON.stringify(info),
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
      },
      success: function(s) {
        txtarea.value = s;
        txtarea.disabled = true;
        document.getElementById("save_changes").remove();
        // var elem = document.getElementById("fuctional_buttons");
        // // elem.parentNode.removeChild(elem);
        // document.getElementById("edit").remove();
        // document.getElementById("gen_cert").remove();
        // var aTag = document.createElement("a");
        // aTag.setAttribute("href", "certificate/" + id.trim());
        // aTag.setAttribute("target", "_blank");
        // aTag.className = "btn btn-sm btn-outline-info";
        // aTag.innerText = "View Certificate";
        // elem.appendChild(aTag);
      }
    });
  } else {
    alert("Textarea cannot be blank");
  }
}
