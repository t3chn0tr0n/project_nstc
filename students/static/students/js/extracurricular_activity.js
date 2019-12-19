// Form 1
$(document).ready(function() {
  $("#submit1").on("click", function() {
    try{ var sftskl_condt = document.getElementById("sftskl_condt").value; } catch (e) { var sftskl_condt = null; }
    try{ var sftskl_attnd = document.getElementById("sftskl_attnd").value; } catch (e) { var sftskl_attnd = null; }
    try{ var apti_condt = document.getElementById("apti_condt").value; } catch (e) { var apti_condt = null; }
    try{ var apti_attnd = document.getElementById("apti_attnd").value; } catch (e) { var apti_attnd = null; }
    try{ var mck_intrvw = document.getElementById("mck_intrvw").value; } catch (e) { var mck_intrvw = null; }
    try{ var iv1_date = document.getElementById("iv1_date").value; } catch (e) { var iv1_date = null; }
    try{ var iv1_place = document.getElementById("iv1_place").value; } catch (e) { var iv1_place = null; }
    try{ var iv2_date = document.getElementById("iv2_date").value; } catch (e) {  var iv2_date = null; }
    try{ var iv2_place = document.getElementById("iv2_place").value; } catch (e) { var iv2_place = null; }
    try{ var onln_tst = document.getElementById("onln_tst").value; } catch (e) {  var onln_tst = null; }
    try{ var gate = document.getElementById("gate").value; } catch (e) { var gate = null; }
    try{ var cat = document.getElementById("cat").value; } catch (e) { var cat = null; }
    $.ajax({
      type: "POST",
      url: "/ea_form1/",
      data: {
        sftskl_condt: sftskl_condt,
        sftskl_attnd: sftskl_attnd,
        apti_condt: apti_condt,
        apti_attnd: apti_attnd,
        mck_intrvw: mck_intrvw,
        iv1_date: iv1_date,
        iv1_place: iv1_place,
        iv2_date: iv2_date,
        iv2_place: iv2_place,
        onln_tst: onln_tst,
        gate: gate,
        cat: cat,
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
      },
      success: function(response) {
        document.getElementById("popupClose").innerHTML = "&times;";
        document.getElementById("popupHead").innerHTML = "";
        document.getElementById("popupContent").innerHTML = response;
      },
      error: function(response) {
        document.getElementById("popupClose").innerHTML = "&times;";
        document.getElementById("popupHead").innerHTML =
          '<h3 class="text-danger">ERROR</h3>';
        document.getElementById("popupContent").innerHTML =
          "Data not submitted or Sever error occurred!";
      }
    });
  });
});

// Form 2
$(document).ready(function() {
  $("#submit2").on("click", function() {
    try{ var swrswti_puja = document.getElementById("swrswti_puja").value; } catch (e) { var swrswti_puja = null; }
    try{ var vswkrma_puja = document.getElementById("vswkrma_puja").value; } catch (e) { var vswkrma_puja = null; }
    try{ var contribs = document.getElementById("contribs").value; } catch (e) { var contribs = null; }
    try{ var ann_mag_pap_pub = document.getElementById("ann_mag_pap_pub").value; } catch (e) {var ann_mag_pap_pub = null; } 
    try{ var ann_mag_evnts = document.getElementById("ann_mag_evnts").value; } catch (e) { var ann_mag_evnts = null; } 
    try{ var wall_mag_evnts = document.getElementById("wall_mag_evnts").value; } catch (e) { var wall_mag_evnts = null; } 
    try{ var wall_mag_pap_pub = document.getElementById("wall_mag_pap_pub").value; } catch (e) { var wall_mag_pap_pub = null; }
    try{ var pap_pub = document.getElementById("papers_pub").value; } catch (e) { var pap_pub = null; } 
    try{ var tech_contst = document.getElementById("tech_contst").value; } catch (e) { tech_contst = null; } 
    try{ var awrds = document.getElementById("awrds").value; } catch (e) { var awrds =  null; }
    $.ajax({
      type: "POST",
      url: "/ea_form2/",
      data: {
        swrswti_puja: swrswti_puja,
        vswkrma_puja: vswkrma_puja,
        contribs: contribs,
        ann_mag_pap_pub: ann_mag_pap_pub,
        ann_mag_evnts: ann_mag_evnts,
        wall_mag_evnts: wall_mag_evnts,
        wall_mag_pap_pub: wall_mag_pap_pub,
        papers_pub: pap_pub,
        tech_contst: tech_contst,
        awrds: awrds,
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
      },
      success: function(response) {
        document.getElementById("popupClose").innerHTML = "&times;";
        document.getElementById("popupHead").innerHTML = "";
        document.getElementById("popupContent").innerHTML = response;
      },
      error: function(response) {
        document.getElementById("popupClose").innerHTML = "&times;";
        document.getElementById("popupHead").innerHTML =
          '<h3 class="text-danger">ERROR</h3>';
        document.getElementById("popupContent").innerHTML =
          "Data not submitted or Sever error occurred!";
      }
    });
  });
});

function warnDo(warn) {
  document.getElementById("popupClose").innerHTML = "&times;";
  document.getElementById("popupHead").innerHTML =
    '<h3 class="text-danger">ERROR</h3>';
  document.getElementById("popupContent").innerHTML =
    "Please fill all fields or delete any unused/blank field!";
  document.getElementById(warn).hidden = false;
}

function errorMade(error, warn) {
  console.log(error);
  document.getElementById("popupClose").innerHTML = "&times;";
  document.getElementById("popupHead").innerHTML =
    '<h3 class="text-danger">UNKNOWN ERROR</h3>';
  document.getElementById("popupContent").innerHTML =
    "Try refreshing the page.";
  document.getElementById(warn).hidden = false;
}

// Workshop and seminars
$(document).ready(function() {
  $("#sub_wrk_shp_form").on("click", function() {
    var warn = false;
    var names = $("input[name^=wrk_shp_name]")
      .map(function(idx, elem) {
        return $(elem).val();
      })
      .get();
    var dates = $("input[name^=wrk_shp_dates]")
      .map(function(idx, elem) {
        return $(elem).val();
      })
      .get();
    var orgs = $("input[name^=wrk_shp_org]")
      .map(function(idx, elem) {
        return $(elem).val();
      })
      .get();

    // deleting the fields that came due to the hidden html
    names.shift();
    dates.shift();
    orgs.shift();

    try {
      if (
        names.length != dates.length ||
        dates.length != orgs.length ||
        orgs.length != names.length
      ) {
        document.getElementById("popupClose").innerHTML = "&times;";
        document.getElementById("popupHead").innerHTML =
          '<h3 class="text-danger">UNKNOWN ERROR</h3>';
        document.getElementById("popupContent").innerHTML =
          "Try refreshing the page.";
        document.getElementById("wrk_shp_warn").hidden = false;
      }
      for (var i = 0; i <= name.length; i++) {
        if (
          (name[i] != " " || name[i] != null) &&
          (dates[i] != " " || dates[i] != null) &&
          (orgs[i] == " " || orgs[i] == null)
        ) {
          names.splice(i, 1);
          dates.splice(i, 1);
          orgs.splice(i, 1);
        } else {
          if (
            (name[i] == " " || name[i] == "") &&
            (dates[i] != " " || dates[i] != "") &&
            (orgs[i] != " " || orgs[i] != "")
          ) {
            warn = true;
            break;
          }
          if (
            (name[i] != " " || name[i] != "") &&
            (dates[i] == " " || dates[i] == "") &&
            (orgs[i] != " " || orgs[i] != "")
          ) {
            warn = true;
            break;
          }
          if (
            (name[i] != " " || name[i] != "") &&
            (dates[i] != " " || dates[i] != "") &&
            (orgs[i] == " " || orgs[i] == "")
          ) {
            warn = true;
            break;
          }
        }
      }
    } catch (e) {
      errorMade(e, "wrk_shp_warn");
    }

    if (warn) {
      warnDo("wrk_shp_warn");
    } else {
      $.ajax({
        type: "POST",
        url: "/ea_form3/",
        data: {
          names: names,
          dates: dates,
          orgs: orgs,
          csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
        },
        success: function(response) {
          document.getElementById("popupClose").innerHTML = "&times;";
          document.getElementById("popupHead").innerHTML = "";
          document.getElementById("popupContent").innerHTML = response;
          document.getElementById("wrk_shp_warn").hidden = true;
          document.getElementById("sub_wrk_shp_form").className =
            "btn btn-success btn-sm disabled";
          document.getElementById("wrk_shp_form_del").hidden = true;
        },
        error: function(response) {
          document.getElementById("popupClose").innerHTML = "&times;";
          document.getElementById("popupHead").innerHTML =
            '<h3 class="text-danger">ERROR</h3>';
          document.getElementById("popupContent").innerHTML =
            "Data not submitted or Sever error occurred!";
          document.getElementById("wrk_shp_warn").hidden = false;
        }
      });
    }
  });
});

// Counseling With Comments
$(document).ready(function() {
  $("#counslng_form").on("click", function() {
    var warn = false;
    var topics = $("input[name^=counslng_form_topics]")
      .map(function(idx, elem) {
        return $(elem).val();
      })
      .get();
    var dates = $("input[name^=counslng_form_dates]")
      .map(function(idx, elem) {
        return $(elem).val();
      })
      .get();

    topics.shift();
    dates.shift();

    try {
      if (topics.length != dates.length) {
        document.getElementById("popupClose").innerHTML = "&times;";
        document.getElementById("popupHead").innerHTML =
          '<h3 class="text-danger">UNKNOWN ERROR</h3>';
        document.getElementById("popupContent").innerHTML =
          "Try refreshing the page.";
        document.getElementById("wrk_shp_warn").hidden = false;
      }
      for (var i = 0; i <= topics.length; i++) {
        if (
          (topics[i] != " " || topics[i] != null) &&
          (dates[i] != " " || dates[i] != null)
        ) {
          names.splice(i, 1);
          dates.splice(i, 1);
          orgs.splice(i, 1);
        } else {
          warn = true;
          break;
        }
      }
    } catch (e) {
      errorMade(e, "counslng_warn");
    }

    if (warn) {
      warnDo("counslng_warn");
    } else {
      $.ajax({
        type: "POST",
        url: "/ea_form4/",
        data: {
          topics: topics,
          dates: dates,
          csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
        },
        success: function(response) {
          document.getElementById("popupClose").innerHTML = "&times;";
          document.getElementById("popupHead").innerHTML = "";
          document.getElementById("popupContent").innerHTML = response;
          document.getElementById("counslng_warn").hidden = true;
          document.getElementById("sub_counslng_form").className =
            "btn btn-success btn-sm disabled";
          document.getElementById("counslng_form_del").hidden = true;
        },
        error: function(response) {
          document.getElementById("popupClose").innerHTML = "&times;";
          document.getElementById("popupHead").innerHTML =
            '<h3 class="text-danger">ERROR</h3>';
          document.getElementById("popupContent").innerHTML =
            "Data not submitted or Sever error occurred!";
          document.getElementById("counslng_warn").hidden = false;
        }
      });
    }
  });
});

function addRow(name) {
  var submit = document.getElementById("sub_" + name);
  var slNo = document.getElementById(name + "_count");
  var original = document.getElementById(name);
  var wrapper = document.getElementById(name + "_body");

  original.hidden = false;
  var copy = original.innerHTML;
  original.hidden = true;
  $(wrapper).append('<tr name="' + name + "_row[]" + '">' + copy + "</tr>");
  slNo.value = Number(slNo.value) + 1;
  submit.hidden = false;
  submit.className = "btn btn-sm btn-success";
  document.getElementById(name + "_del").hidden = false;
}

function deleteRow(name) {
  var chkBox = document.getElementsByName(name + "_chkBox[]");
  var slNo = document.getElementById(name + "_count");
  for (var i = 0; i < chkBox.length; i++) {
    if (chkBox[i].checked) {
      chkBox[i].parentNode.parentNode.remove();
      slNo.value = Number(slNo.value) - 1;
    }
  }
}
