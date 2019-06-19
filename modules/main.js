$(document).ready(function() {
    $(".checkboxesAdd").click(function() {
        $("#newPlayer").append('<br><form class = "checkboxesForm"><input type = "text" class = "mainText" placeholder = "Player Name..." name = ""><input type = "text" class = "mainText2Addon" placeholder = "Age" name = ""></form>')
    })
})