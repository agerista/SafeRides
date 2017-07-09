function showSearchResults(results) {
    alert(results);
    console.log(results);
}

function submitSearch(evt) {
    evt.preventDefault();
    
    var formValues = {

        "zipCode": $("#zipCode").val()

    };

    $.post("/search_results",
          formInputs,
          showSearchResults);
}

$("#search-form").on("submit", submitSearch);
