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
