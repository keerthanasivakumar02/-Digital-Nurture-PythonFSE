const assert = require("assert");
const { add, subtract } = require("./calculator");

describe("Calculator Tests", function () {

    it("should add two numbers", function () {
        assert.strictEqual(add(8, 7), 15);
    });

    it("should subtract two numbers", function () {
        assert.strictEqual(subtract(15, 5), 10);
    });

});