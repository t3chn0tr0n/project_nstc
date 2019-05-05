function filter() {
  var input, filter, table, tr, td, i;
  input = document.getElementById("myInput");

  filter = input.value.toUpperCase();
  //console.log(filter);
  table = document.getElementById("editable_table");
  tr = table.getElementsByTagName("tr");
  for (i = 0; i < tr.length; i++) {
    td_id = tr[i].getElementsByTagName("td")[1];
    td_name = tr[i].getElementsByTagName("td")[2];
    if (td_name) {
      if (
        td_name.innerHTML.toUpperCase().indexOf(filter) > -1 ||
        td_id.innerHTML.toUpperCase().indexOf(filter) > -1
      ) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}
