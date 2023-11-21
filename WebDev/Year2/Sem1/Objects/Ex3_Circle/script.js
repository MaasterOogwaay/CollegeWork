// Constructor function
function Circle(radius, color) {
  this.radius = radius;
  this.color = color;
}
// Defining method on Circle prototype
Circle.prototype.getDiameter = function () {
  return this.radius * 2;
};
Circle.prototype.getArea = function () {
  return Math.PI * (this.radius * this.radius);
};
Circle.prototype.toString = function() {
  return `Radius: ${this.radius}\nColor: ${this.color}\nDiameter: ${this.getDiameter()}\nArea: ${this.getArea()}`
}

const c1 = new Circle(10, "Purple");
console.log(c1.toString());
