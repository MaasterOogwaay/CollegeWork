const getData = function () {
  fetch("https://jsonplaceholder.typicode.com/users")
    .then((response) => response.json()) // returns response promise
    .then((json) => {
      console.log(json);
      buildPage(json);
    }) // returns json promise
    .catch((error) => console.log(error));
};

const buildPage = function (json) {
  let string = "<h1>Users from JSONPlaceholder</h1>";
  for (i in json) {
    string += `${json[i].name}, ${json[i].address.city}<br>`;
  }
  document.getElementById("text").innerHTML = string;
};

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("button").addEventListener("click", getData);
});
