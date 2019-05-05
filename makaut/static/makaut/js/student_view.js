$(document).ready(function() {
    var student_id = document.getElementById("student_id").innerHTML;
    var new_entry = document.getElementById("new_entry").value;

    if (new_entry == 1) {
        window.location.reload(false);
    }

    $('#edit').on('click', function() {
        var elements = document.getElementsByClassName("sems");
        if ($('#edit').text() === "Save") {
            total = new Array();
            var array_s1 = $('.s1').map(function() {
                if (($(this).val()) == '') {
                    return (0);
                } else {
                    return $(this).val();
                }
            }).get();
            var array_s2 = $('.s2').map(function() {
                if (($(this).val()) == '') {
                    return (0);
                } else {
                    return $(this).val();
                }
            }).get();
            var array_s3 = $('.s3').map(function() {
                if (($(this).val()) == '') {
                    return (0);
                } else {
                    return $(this).val();
                }
            }).get();
            var array_s4 = $('.s4').map(function() {
                if (($(this).val()) == '') {
                    return (0);
                } else {
                    return $(this).val();
                }
            }).get();
            var array_s5 = $('.s5').map(function() {
                if (($(this).val()) == '') {
                    return (0);
                } else {
                    return $(this).val();
                }
            }).get();
            var array_s6 = $('.s6').map(function() {
                if (($(this).val()) == '') {
                    return (0);
                } else {
                    return $(this).val();
                }
            }).get();

            var array_s7 = $('.s7').map(function() {
                if (($(this).val()) == '') {
                    return (0);
                } else {
                    return $(this).val();
                }
            }).get();

            var array_s8 = $('.s8').map(function() {
                if (($(this).val()) == '') {
                    return (0);
                } else {
                    return $(this).val();
                }
            }).get();

            //TOTAL POINTS validation
            //total[0]= array_s1[0]+array_s2[0]+array_s3[0]+array_s4[0]+array_s5[0]+array_s6[0]+array_s7[0]+array_s8[0]+array_s1[1]+array_s2[1]+array_s3[1]+array_s4[1]+array_s5[1]+array_s6[1]+array_s7[1]+array_s8[1];
            total[0] = parseInt(array_s1[0]) + parseInt(array_s2[0]) + parseInt(array_s3[0]) + parseInt(array_s4[0]) + parseInt(array_s5[0]) + parseInt(array_s6[0]) + parseInt(array_s7[0]) + parseInt(array_s8[0]) + parseInt(array_s1[1]) + parseInt(array_s2[1]) + parseInt(array_s3[1]) + parseInt(array_s4[1]) + parseInt(array_s5[1]) + parseInt(array_s6[1]) + parseInt(array_s7[1]) + parseInt(array_s8[1]);
            total[1] = parseInt(array_s1[2]) + parseInt(array_s2[2]) + parseInt(array_s3[2]) + parseInt(array_s4[2]) + parseInt(array_s5[2]) + parseInt(array_s6[2]) + parseInt(array_s7[2]) + parseInt(array_s8[2]) + parseInt(array_s1[3]) + parseInt(array_s2[3]) + parseInt(array_s3[3]) + parseInt(array_s4[3]) + parseInt(array_s5[4]) + parseInt(array_s6[5]) + parseInt(array_s7[6]) + parseInt(array_s8[7]);
            total[2] = parseInt(array_s1[4]) + parseInt(array_s2[4]) + parseInt(array_s3[4]) + parseInt(array_s4[4]) + parseInt(array_s5[4]) + parseInt(array_s6[4]) + parseInt(array_s7[4]) + parseInt(array_s8[4]);
            total[3] = parseInt(array_s1[5]) + parseInt(array_s2[5]) + parseInt(array_s3[5]) + parseInt(array_s4[5]) + parseInt(array_s5[5]) + parseInt(array_s6[5]) + parseInt(array_s7[5]) + parseInt(array_s8[5]);
            total[4] = parseInt(array_s1[6]) + parseInt(array_s2[6]) + parseInt(array_s3[6]) + parseInt(array_s4[6]) + parseInt(array_s5[6]) + parseInt(array_s6[6]) + parseInt(array_s7[6]) + parseInt(array_s8[6]);
            total[5] = parseInt(array_s1[7]) + parseInt(array_s2[7]) + parseInt(array_s3[7]) + parseInt(array_s4[7]) + parseInt(array_s5[7]) + parseInt(array_s6[7]) + parseInt(array_s7[7]) + parseInt(array_s8[7]);
            total[6] = parseInt(array_s1[8]) + parseInt(array_s2[8]) + parseInt(array_s3[8]) + parseInt(array_s4[8]) + parseInt(array_s5[8]) + parseInt(array_s6[8]) + parseInt(array_s7[8]) + parseInt(array_s8[8]) + parseInt(array_s1[9]) + parseInt(array_s2[9]) + parseInt(array_s3[9]) + parseInt(array_s4[9]) + parseInt(array_s5[9]) + parseInt(array_s6[9]) + parseInt(array_s7[9]) + parseInt(array_s8[9]);
            total[7] = parseInt(array_s1[10]) + parseInt(array_s2[10]) + parseInt(array_s3[10]) + parseInt(array_s4[10]) + parseInt(array_s5[10]) + parseInt(array_s6[10]) + parseInt(array_s7[10]) + parseInt(array_s8[10]);
            total[8] = parseInt(array_s1[11]) + parseInt(array_s2[11]) + parseInt(array_s3[11]) + parseInt(array_s4[11]) + parseInt(array_s5[11]) + parseInt(array_s6[11]) + parseInt(array_s7[11]) + parseInt(array_s8[11]);
            total[9] = parseInt(array_s1[12]) + parseInt(array_s2[12]) + parseInt(array_s3[12]) + parseInt(array_s4[12]) + parseInt(array_s5[12]) + parseInt(array_s6[12]) + parseInt(array_s7[12]) + parseInt(array_s8[12]);
            total[10] = parseInt(array_s1[13]) + parseInt(array_s2[13]) + parseInt(array_s3[13]) + parseInt(array_s4[13]) + parseInt(array_s5[13]) + parseInt(array_s6[13]) + parseInt(array_s7[13]) + parseInt(array_s8[13]) + parseInt(array_s1[14]) + parseInt(array_s2[14]) + parseInt(array_s3[14]) + parseInt(array_s4[14]) + parseInt(array_s5[14]) + parseInt(array_s6[14]) + parseInt(array_s7[14]) + parseInt(array_s8[14]);
            total[11] = parseInt(array_s1[15]) + parseInt(array_s2[15]) + parseInt(array_s3[15]) + parseInt(array_s4[15]) + parseInt(array_s5[15]) + parseInt(array_s6[15]) + parseInt(array_s7[15]) + parseInt(array_s8[15]) + parseInt(array_s1[16]) + parseInt(array_s2[16]) + parseInt(array_s3[16]) + parseInt(array_s4[16]) + parseInt(array_s5[16]) + parseInt(array_s6[16]) + parseInt(array_s7[16]) + parseInt(array_s8[16]) + parseInt(array_s1[17]) + parseInt(array_s2[17]) + parseInt(array_s3[17]) + parseInt(array_s4[17]) + parseInt(array_s5[17]) + parseInt(array_s6[17]) + parseInt(array_s7[17]) + parseInt(array_s8[17]) + parseInt(array_s1[18]) + parseInt(array_s2[18]) + parseInt(array_s3[18]) + parseInt(array_s4[18]) + parseInt(array_s5[18]) + parseInt(array_s6[18]) + parseInt(array_s7[18]) + parseInt(array_s8[18]) + parseInt(array_s1[19]) + parseInt(array_s2[19]) + parseInt(array_s3[19]) + parseInt(array_s4[19]) + parseInt(array_s5[19]) + parseInt(array_s6[19]) + parseInt(array_s7[19]) + parseInt(array_s8[19]);
            total[12] = parseInt(array_s1[20]) + parseInt(array_s2[20]) + parseInt(array_s3[20]) + parseInt(array_s4[20]) + parseInt(array_s5[20]) + parseInt(array_s6[20]) + parseInt(array_s7[20]) + parseInt(array_s8[20]);
            total[13] = parseInt(array_s1[21]) + parseInt(array_s2[21]) + parseInt(array_s3[21]) + parseInt(array_s4[21]) + parseInt(array_s5[21]) + parseInt(array_s6[21]) + parseInt(array_s7[21]) + parseInt(array_s8[21]);
            total[14] = parseInt(array_s1[22]) + parseInt(array_s2[22]) + parseInt(array_s3[22]) + parseInt(array_s4[22]) + parseInt(array_s5[22]) + parseInt(array_s6[22]) + parseInt(array_s7[22]) + parseInt(array_s8[22]);
            total[15] = parseInt(array_s1[23]) + parseInt(array_s2[23]) + parseInt(array_s3[23]) + parseInt(array_s4[23]) + parseInt(array_s5[23]) + parseInt(array_s6[23]) + parseInt(array_s7[23]) + parseInt(array_s8[23]);
            total[16] = parseInt(array_s1[24]) + parseInt(array_s2[24]) + parseInt(array_s3[24]) + parseInt(array_s4[24]) + parseInt(array_s5[24]) + parseInt(array_s6[24]) + parseInt(array_s7[24]) + parseInt(array_s8[24]);
            total[17] = parseInt(array_s1[25]) + parseInt(array_s2[25]) + parseInt(array_s3[25]) + parseInt(array_s4[25]) + parseInt(array_s5[25]) + parseInt(array_s6[25]) + parseInt(array_s7[25]) + parseInt(array_s8[25]);
            total[18] = parseInt(array_s1[26]) + parseInt(array_s2[26]) + parseInt(array_s3[26]) + parseInt(array_s4[26]) + parseInt(array_s5[26]) + parseInt(array_s6[26]) + parseInt(array_s7[26]) + parseInt(array_s8[26]);
            total[19] = parseInt(array_s1[27]) + parseInt(array_s2[27]) + parseInt(array_s3[27]) + parseInt(array_s4[27]) + parseInt(array_s5[27]) + parseInt(array_s6[27]) + parseInt(array_s7[27]) + parseInt(array_s8[27]);
            total[20] = parseInt(array_s1[28]) + parseInt(array_s2[28]) + parseInt(array_s3[28]) + parseInt(array_s4[28]) + parseInt(array_s5[28]) + parseInt(array_s6[28]) + parseInt(array_s7[28]) + parseInt(array_s8[28]);
            total[21] = parseInt(array_s1[29]) + parseInt(array_s2[29]) + parseInt(array_s3[29]) + parseInt(array_s4[29]) + parseInt(array_s5[29]) + parseInt(array_s6[29]) + parseInt(array_s7[29]) + parseInt(array_s8[29]);
            var all_total = 0;
            var i;
            for (i = 0; i <= 21; i++) {
                all_total = all_total + total[i];
            }
            total[22] = all_total;

            //console.log(total[0]);
            document.getElementById('swayam').innerHTML = total[0];
            document.getElementById('moocs').style.display = "none";

            document.getElementById('td').innerHTML = total[1];
            document.getElementById('tf').style.display = "none";

            document.getElementById('rrt').innerHTML = total[2];
            document.getElementById('rr').style.display = "none";

            document.getElementById('ttp').innerHTML = total[3];
            document.getElementById('tp').style.display = "none";

            document.getElementById('tpc').innerHTML = total[4];
            document.getElementById('pc').style.display = "none";

            document.getElementById('pd').innerHTML = total[5];
            document.getElementById('tpd').style.display = "none";

            document.getElementById('pl').innerHTML = total[6];
            document.getElementById('tpl').style.display = "none";

            document.getElementById('nb').innerHTML = total[7];
            document.getElementById('tnb').style.display = "none";

            document.getElementById('rp').innerHTML = total[8];
            document.getElementById('trp').style.display = "none";

            document.getElementById('ip').innerHTML = total[9];
            document.getElementById('tip').style.display = "none";

            document.getElementById('bd').innerHTML = total[10];
            document.getElementById('tbd').style.display = "none";

            document.getElementById('ps').innerHTML = total[11];
            document.getElementById('tps').style.display = "none";

            document.getElementById('cp').innerHTML = total[12];
            document.getElementById('tcp').style.display = "none";

            document.getElementById('mp').innerHTML = total[13];
            document.getElementById('tmp').style.display = "none";

            document.getElementById('sp').innerHTML = total[14];
            document.getElementById('tsp').style.display = "none";

            document.getElementById('rr').innerHTML = total[15];
            document.getElementById('trr').style.display = "none";

            document.getElementById('pc').innerHTML = total[16];
            document.getElementById('tpc').style.display = "none";

            document.getElementById('yc').innerHTML = total[17];
            document.getElementById('tyc').style.display = "none";

            document.getElementById('se').innerHTML = total[18];
            document.getElementById('tse').style.display = "none";

            document.getElementById('ac').innerHTML = total[19];
            document.getElementById('tac').style.display = "none";

            document.getElementById('ta').innerHTML = total[20];
            document.getElementById('tta').style.display = "none";

            document.getElementById('ca').innerHTML = total[21];
            document.getElementById('tca').style.display = "none";

            //for total
            document.getElementById('all_total').innerHTML = all_total;
            document.getElementById('tall_total').style.display = "none";
            $.ajax({
                type: "POST",
                url: "update/",
                data: {
                    'student_id': student_id,
                    'sem1': JSON.stringify(array_s1),
                    'sem2': JSON.stringify(array_s2),
                    'sem3': JSON.stringify(array_s3),
                    'sem4': JSON.stringify(array_s4),
                    'sem5': JSON.stringify(array_s5),
                    'sem6': JSON.stringify(array_s6),
                    'sem7': JSON.stringify(array_s7),
                    'sem8': JSON.stringify(array_s8),
                    'total': JSON.stringify(total),
                    'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
                },
                success: function() {
                    alert("Change is successfully saved!!");
                }
            });

            for (var i = 0; i < elements.length; i++) {
                //console.log(i);
                elements[i].disabled = true;
            }
            $('#edit').text("Edit");
        } else {
            for (var i = 0; i < elements.length; i++) {
                //elements[i].style.backgroundColor="red";
                elements[i].disabled = false;
            }
            $('#edit').text("Save");
        }
    });
});