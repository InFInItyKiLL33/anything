var index = 0

$(document).ready(function() {
    $(".checkboxesAdd").click(function() {
        index++;
        $("#newPlayer").append('<br><form class = "checkboxesForm"><input type = "text" class = "mainText" placeholder = "Player Name..." name = a' + index + '0><input type = "text" class = "mainText2Addon" placeholder = "Age" name = a' + index + '1></form>');
    })
})

$(document).ready(function() {
    $("#mainGenerateButton").click(function() {
        var values = {};
        var names = [];
        var age = [];
        var ageGroup = [];
        var restriction = [];

        for (let i = 0; i < index + 1; i++) {
            values[String(i)] = $("input[name = a" + String(i) + "0]").val() + ", " + $("input[name = a" + String(i) + "1]").val();
        }

        for (let i = 0; i < 6; i++) {
            if ($("#age" + String(i + 1)).is(":checked")) {
                ageGroup[i] = 1;
            } else {
                ageGroup[i] = 0;
            }
            if (i < 3) {
                if ($("#r" + String(i + 1)).is(":checked")) {
                    restriction[i] = 1;
                } else {
                    restriction[i] = 0;
                }
            }
        }

        values["filters"] = String(ageGroup) + "," + String(restriction);
        $.post("/generate", values);
    })
})