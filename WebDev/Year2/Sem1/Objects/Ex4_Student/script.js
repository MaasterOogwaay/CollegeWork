function Student(id, name, address, grades) {
  this.id = id;
  this.name = name;
  this.address = address;
  this.grades = grades;
}

Student.prototype.addGrade = function (grade) {
  return this.grades.push(grade);
};
Student.prototype.getAverage = function () {
  let sum = 0;
  for (i = 0; i < this.grades.length; i++) {
    sum += this.grades[i];
  }
  return sum / this.grades.length;
};
Student.prototype.toString = function () {
  return `ID: ${this.id}\nName: ${this.name}\nGrades: ${this.grades}\nAverage: ${this.getAverage()}`;
};

// student.addGrade(77);
// console.log(student.toString());
const s1 = new Student(1, "Billy", "3 Yellow Road", [99, 88, 77, 66]);
s1.addGrade(55);
console.log(s1.toString());
