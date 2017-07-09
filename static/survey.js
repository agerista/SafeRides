function saveSurveytoDB(results) {
    alert(results);
    console.log(results);
}

function submitSurvey(evt) {
    evt.preventDefault();
    
    var formValues = {

        "driver_id": $("#driver_id").val(),
        "rating": $("#rating").val(),
        "punctuality": $("#punctuality").val(),
        "drop_off": $("#drop_off").val(),
        "special_instructions": $("#special_instructions").val(),
        "feel_safe": $("#feel_safe").val(),
        "driving_reckless": $("#driving_reckless").val(),
        "harassment": $("#harassment").val(),
        "comment": $("#comment").val(),
    };

    $.post("/survey",
          formInputs,
          showSearchResults);
}

$("#survey").on("submit", submitSurvey);
