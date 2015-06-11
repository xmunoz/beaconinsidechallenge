(function() { 

    $("button").click(function() {
        var userInput = this.form.elements["user-input"].value.toUpperCase();
        var endpointOperation = this.form.elements["operation"].value;
        var params = { "message": userInput }
        $.get(endpointOperation, params)
            .done(function(cipherText) {
                $(".result").text(cipherText);
            })
            .error(function(err) {
                alert("CORS error! Check console for more details.")
            })
    });
})();
