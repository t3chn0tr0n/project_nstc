function toggleMiddle(id) {
  var ptr = document.getElementById(id);
  if (ptr.disabled) {
    ptr.disabled = false;
    ptr.required = true;
  } else {
    ptr.disabled = true;
    ptr.required = false;
  }
}

function lat_selected() {
  document.getElementById("is_lat").checked = true;
  document.getElementById("selection").innerHTML =
    "&nbsp;&nbsp;&nbsp;(Lateral is selected)";
  document.getElementById("stream").innerHTML =
    '<option selected disabled value="">Select stream</option><option value="B-TECH">B-TECH</option>';
}

function reg_selected() {
  document.getElementById("is_reg").checked = true;
  document.getElementById("selection").innerHTML =
    "&nbsp;&nbsp;&nbsp;(Regular is selected)";
  document.getElementById("stream").innerHTML =
    '<option selected disabled value="">Select stream</option><option value="B-TECH">B-TECH</option><option value="M-TECH">M-TECH</option><option value="DEPLOMA">DEPLOMA</option>';
}

$(document).ready(function() {
  document.getElementById("upload_db").disabled = true;
  document.getElementById("cancel").disabled = true;

  $("#viewfile").click(function() {
    if (document.getElementById("inputfile").value != "") {
      var batch = document.getElementById("batch").value;
      var Stream = document.getElementById("stream").value;
      var id_card = document.getElementById("Id_card").value;
      var Roll_no = document.getElementById("Roll_no").value;
      var First_Name = document.getElementById("First_Name").value;
      var Middle_Name = document.getElementById("m_name").value;
      var Last_Name = document.getElementById("Last_name").value;
      var Email_column = document.getElementById("email").value;
      var Mentor_id = document.getElementById("mentor_id").value;
      var mid_checked = document.getElementById("customCheck1").checked;
      if (
        batch.trim() != "" &&
        id_card != "" &&
        Stream != "" &&
        Roll_no != "" &&
        First_Name != "" &&
        Last_Name != "" &&
        Email_column != "" &&
        Mentor_id != ""
      ) {
        if (
          (mid_checked && Middle_Name != "") ||
          (!mid_checked && Middle_Name == "")
        ) {
          alert(document.getElementById("customCheck1").checked + Middle_Name);
          $("#error_csv_upload").html(
            '<i class="fas fa-heart-broken"></i> Input fields are incomplete!!!'
          );
        } else {
          $("#error_csv_upload").html("");
          var rdr = new FileReader();
          rdr.onload = function(e) {
            var c = 0;
            var newrow = "";
            var therows = e.target.result.split("\n");
            var col_length = therows[0].split(",");
            col_length = col_length.length;
            if (
              id_card > col_length ||
              Roll_no > col_length ||
              First_Name > col_length ||
              Last_Name > col_length ||
              Email_column > col_length ||
              Mentor_id > col_length
            ) {
              $("#error_csv_upload").append(
                '<i class="fas fa-heart-broken"></i> Entered column no. and columns in CSV does not match!!'
              );
            } else if (
              id_card <= 0 ||
              Roll_no <= 0 ||
              First_Name <= 0 ||
              Last_Name <= 0 ||
              Email_column <= 0 ||
              Mentor_id <= 0
            ) {
              $("#error_csv_upload").append(
                '<i class="fas fa-bug"></i> Column numbers must be greater than 1!!'
              );
            } else {
              document.getElementById("dataTab").hidden = false;
              // document.getElementById('select_file').hidden = true;
              $("#select_file").html("");
              var row = 0;
              if (document.getElementById("is_header").checked) {
                row = 1;
              }
              for (row = row; row < therows.length; row++) {
                var columns = therows[row].split(",");
                var colcount = columns.length;
                console.log(columns);
                if (colcount == 1) {
                  continue;
                }
                if (colcount <= 7) {
                  newrow +=
                    "<tr class='table-danger'><td>" +
                    columns[id_card - 1] +
                    "</td><td>Incorrect number of columns</td><td></td><td></td><td></td><td></td></tr>";
                  c = c + 1;
                  document.getElementById("upload_db").disabled = true;
                } else {
                  if (
                    typeof columns[id_card - 1] == "undefined" ||
                    columns[id_card - 1] == "" ||
                    typeof columns[Roll_no - 1] == "undefined" ||
                    columns[Roll_no - 1] == "" ||
                    typeof columns[First_Name - 1] == "undefined" ||
                    columns[First_Name - 1] == "" ||
                    (!mid_checked &&
                      typeof columns[Middle_Name - 1] == "undefined") ||
                    typeof columns[Last_Name - 1] == "undefined" ||
                    columns[Last_Name - 1] == "" ||
                    typeof columns[Email_column - 1] == "undefined" ||
                    columns[Email_column - 1] == "" ||
                    typeof columns[Mentor_id - 1] == "undefined" ||
                    columns[Mentor_id - 1] == ""
                  ) {
                    newrow += '<tr class="table-danger">';
                    c = c + 1;
                  } else {
                    newrow += "<tr>";
                  }

                  newrow +=
                    "<td>" +
                    columns[id_card - 1] +
                    "</td><td>" +
                    columns[Roll_no - 1] +
                    "</td><td>" +
                    columns[First_Name - 1] +
                    "</td>";
                  if (!mid_checked && Middle_Name != "") {
                    newrow += "<td>" + columns[Middle_Name - 1] + "</td>";
                  } else {
                    newrow += "<td>" + "NULL" + "</td>";
                  }
                  newrow += "<td>" + columns[Last_Name - 1] + "</td>";
                  newrow += "<td>" + columns[Email_column - 1] + "</td>";
                  newrow += "<td>" + columns[Mentor_id - 1] + "</td></tr>";
                }
              } //end of loop
              if (c > 0) {
                $("#error_csv_upload").append(
                  '<i class="fas fa-bug"></i> There are ' + c + " error in csv"
                );
                document.getElementById("upload_db").disabled = true;
                document.getElementById("cancel").disabled = false;
              } else {
                document.getElementById("upload_db").disabled = false;
                document.getElementById("cancel").disabled = false;
              }
              $("#tableMain").append(newrow);
              $("#tableMain").DataTable();
            }
          };
          rdr.readAsText($("#inputfile")[0].files[0]);
        }
      } else {
        $("#error_csv_upload").html(
          '<i class="fas fa-exclamation-triangle"></i> Input fields are incomplete!!!'
        );
      }
    } else {
      $("#error_csv_upload").html(
        '<i class="fas fa-exclamation-triangle"></i> NO FILE IS SELECTED!!!'
      );
    }
  });

  $("#cancel").click(function() {
    location.reload();
  });

  $("#confirmedUpload").click(function() {
    var table = document.getElementById("tableMain");
    var rowCount = table.rows.length;
    var st;
    if (rowCount > 2) {
      var Batch = document.getElementById("batch").value;
      var Stream = document.getElementById("stream").value;

      var Is_lat;
      if (document.getElementById("is_lat").checked) {
        Is_lat = 1;
      } else {
        Is_lat = 0;
      }
      if (Batch != "" && stream != "") {
        var TableData = new Array();
        var arr = new Array(rowCount - 2);
        for (var i = 1; i < rowCount - 1; i++) {
          st = "";
          var objCells = table.rows.item(i).cells;
          for (var j = 0; j < objCells.length; j++) {
            st = st + objCells.item(j).innerHTML + " ";
          }
          arr[i - 1] = st.trimRight();
        }

        $.ajax({
          type: "POST",
          url: "upload_student/",
          data: {
            arr: JSON.stringify(arr),
            Is_lat: Is_lat,
            Stream: Stream,
            Batch: Batch,
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
          },
          success: function(e) {
            alert(e);
            location.reload();
          }
        });
      } else {
        $("#error_csv_upload").html("INPUT FIELDS ARE INCOMPLETE!!!");
      }
    } //end of if
  });
});
