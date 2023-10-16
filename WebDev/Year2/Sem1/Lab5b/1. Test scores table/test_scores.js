const names = ["Ben", "Joel", "Judy", "Anne"];
const scores = [88, 98, 77, 88];

const $ = (selector) => document.getElementById(selector);

const addScore = function () {
  // get user entries
  const name = $("name").value;
  const score = parseInt($("score").value);

  // check entries for validity
  if (name == "" || isNaN(score) || score < 0 || score > 100) {
    alert("You must enter a name and a valid score");
  } else {
    names[names.length] = name;
    scores[scores.length] = score;

    $("name").value = "";
    $("score").value = "";
    $("name").focus();
  }
};

const displayResults = function () {
  const resultsDiv = $("results");

  // Get average
  console.log(scores);
  let res = 0;
  for (let i = 0; i < scores.length; i++) {
    res += scores[i];
    console.log(res + "|" + scores[i]);
  }
  const avgResult = res / scores.length;

  // Get highest score
  let highest = 0;
  for (let i = 0; i < scores.length; i++) {
    if (scores[i] > highest) {
      highest = scores[i];
    }
  }

  resultsDiv.innerHTML =
    "<h2>Results</h2><p>Average Result: " + avgResult + "</p><br><p>Highest result is " + highest + "</p>";
};

const displayScores = function () {
  const table = $("scores_table");
  table.innerHTML = "<tr><th>Names</th><th>Scores</th></tr>";
  //   let tableData = "";
  //   tableData.innerHTML += "<tr><th>Names</th><th>Scores</th></tr>";
  for (i = 0; i < names.length; i++) {
    table.innerHTML += "<tr><td>" + names[i] + "</td><td>" + scores[i] + "</td></tr>";
  }
};

window.addEventListener("load", () => {
  $("add").addEventListener("click", addScore);
  $("display_results").addEventListener("click", displayResults);
  $("display_scores").addEventListener("click", displayScores);
  $("name").focus();
});
