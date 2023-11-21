class Student {
  constructor(id, name, address, grades) {
    this.id = id;
    this.name = name;
    this.address = address;
    this.grades = grades;
  }
  addGrade(grade) {
    return this.grades.push(grade);
  }
  getAverage() {
    let sum = 0;
    for (let i = 0; i < this.grades.length; i++) {
      sum += this.grades[i];
    }
    return sum / this.grades.length;
  }
  toString() {
    return `ID: ${this.id}\nName: ${this.name}\nGrades: ${this.grades}\nAverage: ${this.getAverage()}`;
  }
}

const s1 = new Student(1, "Billy", "3 Yellow Road", [99, 88, 77, 66]);
s1.addGrade(55);
console.log(s1.toString());

class Postgrad extends Student {
  constructor(id, name, address, grades, allowance) {
    super(id, name, address, grades);
    this.allowance = allowance;
  }
  toString() {
    //Overrides the toString from the Person class
    return `ID: ${this.id}\nName: ${this.name}\nGrades: ${this.grades}\nAverage: ${this.getAverage()}\nAllowance: ${
      this.allowance
    }`;
  }
}

const p1 = new Postgrad(88, "Steve Jobs", "3 Yellow Road", [78, 88, 92, 55], 18000);
p1.addGrade(90);
console.log(p1.toString());
