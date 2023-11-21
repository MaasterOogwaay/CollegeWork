const $ = (selector) => document.querySelector(selector);

let names = [];

function Student(fname, lname, score) {
  this.fname = fname;
  this.lname = lname;
  this.score = score;
}

const displayScores = function () {
  //If the array is empty, read the values from localStorage and populate the array
  if (names.length === 0) {
    let storage = localStorage.getItem("names");
    if (storage.length > 0) {
      names = JSON.parse(storage);
    }
  }
  //Work out the average and write to 'Average Score' textbox
  let sum = 0;
  for (let i = 0; i < names.length; i++) {
    sum += names[i].score;
  }
  console.log(sum);
  console.log(names.length);
  let average = sum / names.length;
  console.log(average);
  //Print the names and scores in the textarea
  let content = "";
  for (let i = 0; i < names.length; i++) {
    content += `${names[i].fname} ${names[i].lname} | ${names[i].score}\n`;
  }
  $("#scores").value = content;
  // console.log(content);
  $("#average_score").value = average;
};

const addScore = function () {
  //Read the name and score from the input textboxes and create a student object
  let fname = $("#first_name").value;
  let lname = $("#last_name").value;
  let score = $("#score").value;
  console.log(fname, lname, score);
  const s1 = new Student(fname, lname, score);
  //Add the student object to the array of student objects
  names.push(s1);
  console.log(names);
  //Write the array to localStorage
  localStorage.names = JSON.stringify(names);
  //Clear the input textboxes
  $("#first_name").value = "";
  $("#last_name").value = "";
  $("#score").value = "";
  //Call the displayScores function to display the scores
  displayScores();
};

const clearScores = function () {
  //Delete all the data from the array, localStorage and any textboxes that have data
};

const sortByLastName = function () {
  //sort the array by last name and call displayScores
};

const sortByScore = function () {
  //sort the array by score and call displayScores
};

window.addEventListener("load", () => {
  $("#add_button").addEventListener("click", addScore);
  $("#clear_button").addEventListener("click", clearScores);
  $("#sort_name").addEventListener("click", sortByLastName);
  $("#sort_score").addEventListener("click", sortByScore);
  $("#first_name").focus();
  displayScores();
});
