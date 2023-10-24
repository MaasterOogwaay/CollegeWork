const $ = function (selector) {
  return document.querySelector(selector);
};

const getData = function () {
  fetch("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
    .then((response) => response.json()) // returns response promise
    .then((json) => {
      console.log(json);
      buildPage(json);
    }) // returns json promise
    .catch((error) => console.log(error));
};

const buildPage = function (data) {
  // call this function from inside the second .then in the fetch
  //   console.log(data);
  // extract relevant information from the returned json data
  // use innerHTML to write the generated html to the webpage
  let htmlString = "";
  htmlString += `<h2>${data.title}</h2>`;
  htmlString += `<img src="${data.hdurl}">`;
  htmlString += `<p id="date">${data.date}</p>`;
  htmlString += `<p id="explanation">${data.explanation}</p>`;

  $("#data").innerHTML = htmlString;
};

window.addEventListener("load", () => {
  // when the button is clicked, get the data!
  $("#button").addEventListener("click", getData);
});
