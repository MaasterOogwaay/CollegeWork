const circle = {
  radius: 5,
  color: "Blue",
  getDiameter: function () {
    return this.radius * 2;
  },
  getArea: function () {
    return Math.PI * (this.radius * this.radius);
  },
  toString: function () {
    console.log(
      `Radius: ${this.radius}\nColor: ${this.color}\nDiameter: ${this.getDiameter()}\nArea: ${this.getArea()}`
    );
  },
};

console.log(circle.toString());
