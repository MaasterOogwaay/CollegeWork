// Constructor function
class Circle {
  constructor(radius, color) {
    this.radius = radius;
    this.color = color;
  }
  // Defining method on Circle prototype
  getDiameter() {
    return this.radius * 2;
  }
  getArea() {
    return Math.PI * (this.radius * this.radius);
  }
  toString() {
    return `Radius: ${this.radius}\nColor: ${this.color}\nDiameter: ${this.getDiameter()}\nArea: ${this.getArea()}`;
  }
}

const c1 = new Circle(10, "Purple");
console.log(c1.toString());
