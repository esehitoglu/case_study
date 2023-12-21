// HTTP status code kontrolü
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

// Response içeriğini kontrol etme
pm.test("Response body has the correct structure", function () {
    // JSON formatını kontrol et
    pm.response.to.be.json;

    // Belirtilen yapıya sahip olup olmadığını kontrol et
    pm.test("Response has the correct structure", function () {
        var jsonData = pm.response.json();
        pm.expect(jsonData).to.have.property("data").that.is.an("array");

        jsonData.data.forEach(function (flight) {
            pm.expect(flight).to.have.property("id").that.is.a("number");
            pm.expect(flight).to.have.property("from").that.is.a("string");
            pm.expect(flight).to.have.property("to").that.is.a("string");
            pm.expect(flight).to.have.property("date").that.is.a("string");
        });
    });
});

// Header kontrolü
pm.test("Content-Type is application/json", function () {
    pm.response.to.have.header("Content-Type", "application/json");
});
