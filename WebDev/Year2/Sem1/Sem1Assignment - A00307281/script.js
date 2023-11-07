const $ = function (id) {
  return document.getElementById(id);
};

const getData = function () {
  fetch("https://restcountries.com/v3.1/all")
    .then((response) => response.json()) // returns response promise
    .then((json) => {
      console.log(json);
      buildPage(json);
      loadContent(json);
    }) // returns json promise
    .catch((error) => console.log(error));
};

const buildPage = function (data) {
  console.log(data[0].name.official);
};

const loadContent = function (data) {
  getData();

  let result = "";
  result = `
        <div class="card">
            <img src="${data[0].flags.png}" alt="Avatar" style="width: 100%;">
            <div class="container">
                <h4><b>John Doe</b></h4>
                <p>Architect & Engineer</p>
            </div>
        </div>
    `;
  $("card-div").innerHTML = result;
};

window.addEventListener("load", () => {
  // when the button is clicked, get the data!
  //   $("search-button").addEventListener("click", getData);
  $("search-button").addEventListener("click", loadContent);
  //   loadContent();
});
