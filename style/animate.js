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
});

$('#Dare').click(function() {
  document.getElementById('Question_type').innerHTML = "Dare";
});

$('#Gen_another').click(function() {
  //$("#after").css({"display" : "block"});
  $("#after").fadeOut(function() {
    $("#before").fadeIn();
  });
});

//Aboutus.HTML
$('#Z_pic').click(function(){
  console.log("hey");
  $(this).fadeOut(function(){
    $("#Z_story").fadeIn();
  });
});
$('#R_pic').click(function(){
  // DEBUG: console.log("hey");
  $(this).fadeOut(function(){
    $("#R_story").fadeIn();
  });
});
$('#J_pic').click(function(){
  // DEBUG: console.log("hey");
  $(this).fadeOut(function(){
    $("#J_story").fadeIn();
  });
});

$('#J_story').click(function(){
  // DEBUG: console.log("hey");
  $(this).fadeOut(function(){
    $('#J_pic').fadeIn();
  });
});
$('#R_story').click(function(){
  // DEBUG: console.log("hey");
  $(this).fadeOut(function(){
    $('#R_pic').fadeIn();
  });
});
$('#Z_story').click(function(){
  // DEBUG: console.log("hey");
  $(this).fadeOut(function(){
    $('#Z_pic').fadeIn();
  });
});

$('#pic_email').click(function(){
  console.log("hey");
  $(this).fadeOut(function(){
    $("#email_item").fadeIn();
  });
});
$('#pic_follow').click(function(){
  console.log("hey");
  $(this).fadeOut(function(){
    $("#follow_item").fadeIn();
  });
});

$("#follow_item").click(function(){
  $(this).fadeOut(function(){
    $("#pic_follow").fadeIn();
  });
});
$("#email_item").click(function(){
  $(this).fadeOut(function(){
    $("#pic_email").fadeIn();
  });
});
