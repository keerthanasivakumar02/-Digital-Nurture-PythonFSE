const { add, subtract } = require("./calculator");

test("checks addition", () => {
    expect(add(12, 8)).toBe(20);
});

test("checks subtraction", () => {
    expect(subtract(15, 5)).toBe(10);
});