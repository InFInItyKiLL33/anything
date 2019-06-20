//FAQ.html
$('.QandA').click(function(){
    // DEBUG: console.log("test");
    $(this).find('.Answer').toggle();
});


//generate.html
$('after').hide();

$('.change_me').click(function(){
  $("#before").stop().fadeOut();

  //$("#after").css({"display" : "block"});
  $("#after").stop().fadeIn();
});

$('#True').click(function() {
  document.getElementById('Question_type').innerHTML = "Truth";
});

$('#Dare').click(function() {
  document.getElementById('Question_type').innerHTML = "Dare";
});

$('#Gen_another').click(function() {
  $("#before").stop().fadeIn();

  //$("#after").css({"display" : "block"});
  $("#after").stop().fadeOut();

});
