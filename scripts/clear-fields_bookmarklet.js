javascript:(function(){
    var formElements = document.querySelectorAll("input, textarea, select, [type='hidden']");
    for (var i = 0; i < formElements.length; i++) {
        if (formElements[i].type === "checkbox") {
            formElements[i].checked = false;
        } else {
            formElements[i].value = "";
        }
    }
})();
