const student = {
  id: 1,
  name: "Billy",
  address: "2 Yellow Road",
  grades: [88, 99, 86],
  addGrade: function (grade) {
    return this.grades.push(grade);
  },
  getAverage: function () {
    let sum = 0;
    for (i = 0; i < this.grades.length; i++) {
      sum += this.grades[i];
    }
    return sum / this.grades.length;
  },
  toString: function () {
    return `ID: ${this.id}\nName: ${this.name}\nGrades: ${this.grades}\nAverage: ${this.getAverage()}`;
  },
};

student.addGrade(77);
console.log(student.toString());
