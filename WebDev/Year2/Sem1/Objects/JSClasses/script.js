class Person {
  constructor(fname, lname, dept) {
    this.fname = fname;
    this.lname = lname;
    this.dept = dept;
  }
  getName() {
    return `Full Name: ${this.fname} ${this.lname}`;
  }
  toString() {
    return `Full Name: ${this.fname} ${this.lname}, Dept: ${this.dept}`;
  }
}
const p1 = new Person("Billy", "Gates", "Engineering");
console.log(p1.toString());
console.log(p1.getName());

class Student extends Person {
  constructor(fname, lname, dept, course) {
    super(fname, lname, dept);
    this.course = course;
  }
  toString() {
    //Overrides the toString from the Person class
    return `Name: ${this.fname} ${this.lname}, Dept: ${this.dept}, Course
  : ${this.course}`;
  }
}
const s1 = new Student("Johnny", "Bloggs", "Science", "Biology");
console.log(s1.toString());
console.log(s1.getName()); //uses the getName() from the Person class
