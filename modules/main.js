var index = 0

$(document).ready(function() {
    $(".checkboxesAdd").click(function() {
        index++;
        $("#newPlayer").append('<br><form class = "checkboxesForm"><input type = "text" class = "mainText" placeholder = "Player Name..." name = a' + index + '0><input type = "text" class = "mainText2Addon" placeholder = "Age" name = a' + index + '1></form>');
    })
})

function onPlayClick() {
    var values = {};
    var names = [];
    var age = [];
    var ageGroup = [];
    var restriction = [];
    var toStop = false

    for (let i = 0; i < index + 1; i++) {
        $("input[name = a" + String(i) + "0]").css("border","1px solid rgb(0, 0, 0, 0.25)");
        $("input[name = a" + String(i) + "1]").css("border","1px solid rgb(0, 0, 0, 0.25)");
        values[String(i)] = $("input[name = a" + String(i) + "0]").val() + ", " + $("input[name = a" + String(i) + "1]").val();
        if ($("input[name = a" + String(i) + "0]").val() == "") {
            $("input[name = a" + String(i) + "0]").css("border","1px solid #a30000");
            toStop = true;
        }
        if ($("input[name = a" + String(i) + "1]").val() == "") {
            $("input[name = a" + String(i) + "1]").css("border","1px solid #a30000");
            toStop = true;
        }
        console.log(parseInt($("input[name = a" + String(i) + "1]").val()))
        if (Number.isNaN(parseInt($("input[name = a" + String(i) + "1]").val()))) {
            $("input[name = a" + String(i) + "1]").css("border","1px solid #a30000");
            toStop = true;
        }
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

    if (toStop == false) {
        values["filters"] = String(ageGroup) + "," + String(restriction);
        post("/generate", values);
    }
}

function post(path, params, method='post') {

    // The rest of this code assumes you are not using a library.
    // It can be made less wordy if you use one.
    const form = document.createElement('form');
    form.method = method;
    form.action = path;
  
    for (const key in params) {
      if (params.hasOwnProperty(key)) {
        const hiddenField = document.createElement('input');
        hiddenField.type = 'hidden';
        hiddenField.name = key;
        hiddenField.value = params[key];
  
        form.appendChild(hiddenField);
      }
    }
  
    document.body.appendChild(form);
    form.submit();
  }