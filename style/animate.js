//FAQ.html
$('.QandA').click(function(){
    // DEBUG: console.log("test");
    $(this).find('.Answer').toggle();
});


//generate.html
$('.change_me').click(function(){
  $("#after").css({"display" : "block"})
  $("#before").css({"display" : "none"})
});
