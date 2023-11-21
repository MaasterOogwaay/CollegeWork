let timer = null;

const $ = function (id) {
  return document.getElementById(id);
};

const getData = function () {
  fetch("https://restcountries.com/v3.1/all")
    .then((response) => response.json()) // returns response promise
    .then((json) => {
      // console.log(json);
      getRandomCountry(json);
    }) // returns json promise
    .catch((error) => console.log(error));
};

const searchCountry = function (name) {
  fetch(`https://restcountries.com/v3.1/name/${name}?fullText=true`)
    .then((response) => response.json()) // returns response promise
    .then((json) => {
      // console.log(json);
      buildPage(json);
    }) // returns json promise
    .catch((error) => console.log(error));
};

const getSearchTerm = function () {
  clearInterval(timer);
  let countryName = $("search-bar").value;
  console.log(countryName);
  searchCountry(countryName);
};

const buildPage = function (data) {
  $("card-div2").style.display = "none";
  // console.log(data);
  // console.log(data[0].name.official);
  let flag = data[0].flags.png;
  let countryName = data[0].name.official;
  let population = data[0].population.toLocaleString();
  let region = data[0].region;
  let capital = data[0].capital;
  let area = data[0].area.toLocaleString();

  let isIndependent = "";
  if (data[0].independent == true) {
    isIndependent = "Independent country";
  } else {
    isIndependent = "Not an independent country";
  }

  let result = "";
  result = `
    <div class="w3-card-4">
      <img src="${flag}" alt="Country flag" style="width: 100%;">
      <div class="w3-container">
          <h4>
              <b>${countryName}</b>
          </h4>
          <div>
              <table class="w3-table w3-striped">
                <tr><td>Population</td><td>${population}</td></tr>
                <tr><td>Region</td><td>${region}</td></tr>
                <tr><td>Capital</td><td>${capital}</td></tr>
              </table>
          </div>
          <div class="w3-container w3-center">
            <button onclick="document.getElementById('id01').style.display='block'" class="w3-button w3-black">Open Modal</button>

            <div id="id01" class="w3-modal">
              <div class="w3-modal-content">
                <div class="w3-container">
                  <span onclick="document.getElementById('id01').style.display='none'; getData()" class="w3-button w3-display-topright">&times;</span><br/>
                  <table class="w3-table w3-striped">
                  <tr><td>Official Name</td><td>${countryName}</td></tr>
                  <tr><td>State of Independence</td><td>${isIndependent}</td></tr>
                  <tr><td>Region</td><td>${region}</td></tr>
                  <tr><td>Capital</td><td>${capital}</td></tr>
                  <tr><td>Area</td><td>${area}</td></tr>
                </table>
                </div>
              </div>
            </div>
          </div>
      </div>
    </div>
    `;
  $("card-div1").innerHTML = result;
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

const getRandomCountry = function (data) {
  let result1 = "";
  let result2 = "";
  for (i = 0; i < 3; i++) {
    let randomCountry = Math.floor(Math.random() * data.length);
    //console.log("Random: " + randomCountry);

    let flag = data[randomCountry].flags.png;
    // console.log(flag);
    let countryName = data[randomCountry].name.common;
    let population = data[randomCountry].population.toLocaleString();
    let region = data[randomCountry].region;
    let capital = data[randomCountry].capital;
    let area = data[randomCountry].area.toLocaleString();

    let isIndependent = "";
    if (data[randomCountry].independent == true) {
      isIndependent = "Independent country";
    } else {
      isIndependent = "Not an independent country";
    }

    //console.log(
    //  `Country ${i}: ${flag} | ${countryName} | ${population} | ${region} | ${capital} | ${area} | ${isIndependent}`
    //);

    result1 += `
    <div class="w3-card-2 w3-margin" style="width: 30%; height: 50%;">
    <img src="${flag}" alt="Country flag" style="width: 100%;">
    <div class="w3-container">
        <h4>
            <b>${countryName}</b>
        </h4>
        <div>
            <table class="w3-table w3-striped">
              <tr><td>Population</td><td>${population}</td></tr>
              <tr><td>Region</td><td>${region}</td></tr>
              <tr><td>Capital</td><td>${capital}</td></tr>
            </table>
        </div>
        <div class="w3-container w3-center">
          <button onclick="document.getElementById('id${i}').style.display='block'" class="w3-button w3-black">Open Modal</button>

          <div id="id${i}" class="w3-modal">
            <div class="w3-modal-content">
              <div class="w3-container">
                <span onclick="document.getElementById('id${i}').style.display='none'" class="w3-button w3-display-topright">&times;</span><br/>
                <table class="w3-table w3-striped">
                <tr><td>Official Name</td><td>${countryName}</td></tr>
                <tr><td>State of Independence</td><td>${isIndependent}</td></tr>
                <tr><td>Region</td><td>${region}</td></tr>
                <tr><td>Capital</td><td>${capital}</td></tr>
                <tr><td>Area</td><td>${area}</td></tr>
              </table>
              </div>
            </div>
          </div>
        </div>
    </div>
  </div>
    `;
  }

  for (j = 3; j < 6; j++) {
    let randomCountry = Math.floor(Math.random() * data.length);
    //console.log("Random: " + randomCountry);

    let flag = data[randomCountry].flags.png;
    let countryName = data[randomCountry].name.common;
    let population = data[randomCountry].population.toLocaleString();
    let region = data[randomCountry].region;
    let capital = data[randomCountry].capital;
    let area = data[randomCountry].area.toLocaleString();

    let isIndependent = "";
    if (data[randomCountry].independent == true) {
      isIndependent = "Independent country";
    } else {
      isIndependent = "Not an independent country";
    }

    // console.log(
    //   `Country ${j}: ${flag} | ${countryName} | ${population} | ${region} | ${capital} | ${area} | ${isIndependent}`
    // );

    result2 += `
    <div class="w3-card-2 w3-margin" style="width: 30%; height: 50%;">
      <img src="${flag}" alt="Country flag" style="width: 100%;">
      <div class="w3-container">
          <h4>
              <b>${countryName}</b>
          </h4>
          <div>
              <table class="w3-table w3-striped">
                <tr><td>Population</td><td>${population}</td></tr>
                <tr><td>Region</td><td>${region}</td></tr>
                <tr><td>Capital</td><td>${capital}</td></tr>
              </table>
          </div>
          <div class="w3-container w3-center">
            <button onclick="document.getElementById('id${j}').style.display='block'; clearInterval(timer)" class="w3-button w3-black">Open Modal</button>

            <div id="id${j}" class="w3-modal">
              <div class="w3-modal-content">
                <div class="w3-container">
                  <span onclick="document.getElementById('id${j}').style.display='none'; startTimer()" class="w3-button w3-display-topright">&times;</span><br/>
                  <table class="w3-table w3-striped">
                  <tr><td>Official Name</td><td>${countryName}</td></tr>
                  <tr><td>State of Independence</td><td>${isIndependent}</td></tr>
                  <tr><td>Region</td><td>${region}</td></tr>
                  <tr><td>Capital</td><td>${capital}</td></tr>
                  <tr><td>Area</td><td>${area}</td></tr>
                </table>
                </div>
              </div>
            </div>
          </div>
      </div>
    </div>
    `;
  }

  $("card-div1").innerHTML = result1;
  $("card-div2").innerHTML = result2;
};

const getCountryByRegion = function () {
  // TODO:
  // Make the data load when the dropdown changes
  clearInterval(timer);
  let region = $("region-list").value;
  timer = setInterval(() => {
    fetch(`https://restcountries.com/v3.1/region/${region}`)
      .then((response) => response.json()) // returns response promise
      .then((json) => {
        // console.log(json);
        console.log(region);
        getRandomCountry(json);
      }) // returns json promise
      .catch((error) => console.log(error));
  }, 10000);
};

const startTimer = function () {
  timer = setInterval(() => {
    getData();
  }, 10000);
};

document.addEventListener("DOMContentLoaded", () => {
  // TODO:
  // Stop interval when search-button clicked
  // Restart interval when modal is closed

  $("search-button").addEventListener("click", getSearchTerm);
  getData();
  startTimer();

  $("region-list").addEventListener("change", getCountryByRegion);
});
