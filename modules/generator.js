function dareTruthShared(TODStatement, TOD) {
    $("").hide().append(
        "<div id = 'generateMain'><div id = 'generateTOD'>" + TOD + "</div><img src = 'images/generate/" + TOD + " Underline.png' id = 'generateTODUnderline'>Lick the closest wall!</div><br><div id = 'generateAnother'>Generate Another</div><div id = 'generateOr'>or...</div><br><div id = 'generateNew'>New TOD</div>"
    ); //change name of div covering tod //change to read file var
}
    
$(document).ready(function() {
    $("").on("click", function() { //change name of dare clicked
        //$("").slideUp(); //change name of player name & edit animation of name
        var TODStatement = ""
        dareTruthShared(TODStatement, "Dare");
    })
})

$(document).ready(function() {
    $("").on("click", function() { //change name of truth clicked
        //$("").slideUp(); //change name of player name & edit animation of name
        var TODStatement = ""
        dareTruthShared(TODStatement, "Truth");
    })
})