// $document.ready(function(){
//     // var email=document.getElementById("email").value;
//     // var mob1=document.getElementById("mob_no1").value;
//     // var mob2=document.getElementById("mob_no2").value;
//     // console.log(email);
//     // console.log(mob1);
//     // console.log(mob2);
    
// });

function change()
{
    var email=document.getElementById("email").value;
    var mob1=document.getElementById("mob_no1").value;
    var mob2=document.getElementById("mob_no2").value;
    var id=document.getElementById("id").textContent;
    if(mob1 =="" || email =="" )
    {
        alert("Fields cannot be empty!!");
    }
    else if(mob1.length !=10)
    {
        alert("invalid mobile number1")
    }
    else if(mob2.length !=1 && mob2.length !=10)
    {
        alert("invalid mobile number2")
    }
    else
    {
        $.ajax({
            type: "POST",
            url: "change_profile/",
            data: {
              email:email,
              mob1: mob1,
              mob2: mob2,
              id:id,
              csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function (s) {
              if (s == '1') {
                // console.log();
                alert("Update successful!!!");
                location.reload();
              } else {
                console.log(s);
                alert(s);
              }
            }
          });
    }
    
}