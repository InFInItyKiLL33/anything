//FAQ.html
$('.QandA').click(function(){
    // DEBUG: console.log("test");
    $(this).find('.Answer').toggle();
});


//generate.html
$('#after').hide();

$('.change_me').click(function() {
  $("#before").fadeOut(function() {
    $("#after").fadeIn();
  });

  //$("#after").css({"display" : "block"});

});

$('#True').click(function() {
  document.getElementById('Question_type').innerHTML = "Truth";
  $("#Question_TD_D").hide();
});

$('#Dare').click(function() {
  document.getElementById('Question_type').innerHTML = "Dare";
  $("#Question_TD_T").hide();
});

$('#Gen_another').click(function() {
  //$("#after").css({"display" : "block"});
  $("#after").fadeOut(function() {
    $("#before").fadeIn();
  });
});

//welcome.HTML


//Aboutus.HTML
$('#Z_pic').mouseenter(function(){
  // DEBUG: console.log("hey");
  $(this).fadeOut(function(){
    $("#Z_story").fadeIn();
  });
});
$('#R_pic').mouseenter(function(){
  // DEBUG: console.log("hey");
  $(this).fadeOut(function(){
    $("#R_story").fadeIn();
  });
});
$('#J_pic').mouseenter(function(){
  // DEBUG: console.log("hey");
  $(this).fadeOut(function(){
    $("#J_story").fadeIn();
  });
});

$('#J_story').mouseleave(function(){
  // DEBUG: console.log("hey");
  $(this).fadeOut(function(){
    $('#J_pic').fadeIn();
  });
});
$('#R_story').mouseleave(function(){
  // DEBUG: console.log("hey");
  $(this).fadeOut(function(){
    $('#R_pic').fadeIn();
  });
});
$('#Z_story').mouseleave(function(){
  // DEBUG: console.log("hey");
  $(this).fadeOut(function(){
    $('#Z_pic').fadeIn();
  });
});

$('#pic_email').mouseenter(function(){
  console.log("hey");
  $(this).fadeOut(function(){
    $("#email_item").fadeIn();
  });
});
$('#pic_follow').mouseenter(function(){
  console.log("hey");
  $(this).fadeOut(function(){
    $("#follow_item").fadeIn();
  });
});

$("#follow_item").mouseleave(function(){
  $(this).fadeOut(function(){
    $("#pic_follow").fadeIn();
  });
});
$("#email_item").mouseleave(function(){
  $(this).fadeOut(function(){
    $("#pic_email").fadeIn();
  });
});

$(document).ready(
  $(".About_us_body2").fadeIn(1250)
)
//test