(function() { 

    $("button").click(function() {
        var userInput = this.form.elements["user-input"].value.toUpperCase();
        var operation = this.form.elements["operation"].value;
        var apiEndpoint = "https://beaconinside-crypto.appspot.com/caesar/" + operation
        var params = { "message": userInput }
        $.get(apiEndpoint, params)
            .done(function(cipherText) {
                $(".result").text(cipherText);
            })
            .error(function(err) {
                alert("CORS error! Check console for more details.")
            })
    });
})();
