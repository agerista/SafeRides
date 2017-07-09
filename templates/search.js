function showSearchResults(results) {
    alert(results);
    console.log(results);
}

function submitSearch(evt) {
    evt.preventDefault();
    
    var formValues = {

        "driver": $("#driver").val()

    };

    $.post("/",
          formInputs,
          showSearchResults);
}

$("#search-form").on("submit", submitSearch);
