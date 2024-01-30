let timer = null;

const $ = function (id) {
  return document.getElementById(id);
};

const getData = function () {
  fetch("https://restcountries.com/v3.1/all")
    .then((response) => response.json()) // returns response promise
    .then((json) => {
      getRandomCountry(json);
    }) // returns json promise
    .catch((error) => console.log(error));
};

const searchCountry = function (name) {
  fetch(`https://restcountries.com/v3.1/name/${name}?fullText=true`)
    .then((response) => response.json()) // returns response promise
    .then((json) => {
      buildPage(json);
    }) // returns json promise
    .catch((error) => console.log(error));
};

const getSearchTerm = function () {
  clearInterval(timer);
  let countryName = $("searchBar").value;
  console.log(countryName);
  searchCountry(countryName);
};

const buildPage = function (data) {
  $("cardDiv2").style.display = "none";
  let flag = data[0].flags.png;
  let countryName = data[0].name.official;
  let population = data[0].population.toLocaleString();
  let region = data[0].region;
  let capital = data[0].capital;
  let area = data[0].area.toLocaleString();

  let numOfBorders = "";
  if (data[0].borders == undefined) {
    numOfBorders = 0;
  } else {
    numOfBorders = data[0].borders.length;
  }

  let isIndependent = "";
  if (data[0].independent == true) {
    isIndependent = "Independent country";
  } else {
    isIndependent = "Not an independent country";
  }

  let isLandLocked = "";
  if (data[0].landlocked == true) {
    isLandLocked = "Landlocked country";
  } else {
    isLandLocked = "Not a landlocked country";
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
            <button onclick="document.getElementById('id01').style.display='block'" class="w3-button w3-black">Learn More</button>

            <div id="id01" class="w3-modal">
              <div class="w3-modal-content">
                <div class="w3-container">
                  <span onclick="document.getElementById('id01').style.display='none'; getData();" class="w3-button w3-display-topright">&times;</span><br/>
                  <table class="w3-table w3-striped">
                  <tr><td>Official Name</td><td>${countryName}</td></tr>
                  <tr><td>State of Independence</td><td>${isIndependent}</td></tr>
                  <tr><td>Region</td><td>${region}</td></tr>
                  <tr><td>Capital</td><td>${capital}</td></tr>
                  <tr><td>Area</td><td>${area}</td></tr>
                  <tr><td>Landlocked</td><td>${isLandLocked}</td></tr>
                  <tr><td>Number of Borders</td><td>Borders ${numOfBorders} countries</td></tr>
                </table>
                </div>
              </div>
            </div>
          </div>
      </div>
    </div>
    `;
  $("cardDiv1").innerHTML = result;
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
  $("cardDiv1").innerHTML = result;
};

const getRandomCountry = function (data) {
  $("cardDiv2").style.display = "inline-flex";
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
    let numOfBorders = "";
    if (data[randomCountry].borders == undefined) {
      numOfBorders = 0;
    } else {
      numOfBorders = data[randomCountry].borders.length;
    }

    let isIndependent = "";
    if (data[randomCountry].independent == true) {
      isIndependent = "Independent country";
    } else {
      isIndependent = "Not an independent country";
    }

    let isLandLocked = "";
    if (data[randomCountry].landlocked == true) {
      isLandLocked = "Landlocked country";
    } else {
      isLandLocked = "Not a landlocked country";
    }

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
          <button onclick="document.getElementById('id${i}').style.display='block'; clearInterval(timer);" class="w3-button w3-black">Learn More</button>

          <div id="id${i}" class="w3-modal">
            <div class="w3-modal-content">
              <div class="w3-container">
                <span onclick="document.getElementById('id${i}').style.display='none'; startTimer()" class="w3-button w3-display-topright">&times;</span><br/>
                <table class="w3-table w3-striped">
                <tr><td>Official Name</td><td>${countryName}</td></tr>
                <tr><td>State of Independence</td><td>${isIndependent}</td></tr>
                <tr><td>Region</td><td>${region}</td></tr>
                <tr><td>Capital</td><td>${capital}</td></tr>
                <tr><td>Area</td><td>${area}</td></tr>
                <tr><td>Landlocked</td><td>${isLandLocked}</td></tr>
                <tr><td>Number of Borders</td><td>Borders ${numOfBorders} countries</td></tr>
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

    let flag = data[randomCountry].flags.png;
    let countryName = data[randomCountry].name.common;
    let population = data[randomCountry].population.toLocaleString();
    let region = data[randomCountry].region;
    let capital = data[randomCountry].capital;
    let area = data[randomCountry].area.toLocaleString();
    let numOfBorders = "";
    if (data[randomCountry].borders == undefined) {
      numOfBorders = 0;
    } else {
      numOfBorders = data[randomCountry].borders.length;
    }

    let isIndependent = "";
    if (data[randomCountry].independent == true) {
      isIndependent = "Independent country";
    } else {
      isIndependent = "Not an independent country";
    }

    let isLandLocked = "";
    if (data[randomCountry].landlocked == true) {
      isLandLocked = "Landlocked country";
    } else {
      isLandLocked = "Not a landlocked country";
    }

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
            <button onclick="document.getElementById('id${j}').style.display='block'; clearInterval(timer)" class="w3-button w3-black">Learn More</button>

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
                  <tr><td>Landlocked</td><td>${isLandLocked}</td></tr>
                  <tr><td>Number of Borders</td><td>Borders ${numOfBorders} countries</td></tr>
                </table>
                </div>
              </div>
            </div>
          </div>
      </div>
    </div>
    `;
  }

  $("cardDiv1").innerHTML = result1;
  $("cardDiv2").innerHTML = result2;
};

const getCountryByRegion = function () {
  clearInterval(timer);
  let region = $("filterOptions").value;
  if (region == "") {
    getData();
  } else {
    fetch(`https://restcountries.com/v3.1/region/${region}`)
      .then((response) => response.json()) // returns response promise
      .then((json) => {
        getRandomCountry(json);
      }) // returns json promise
      .catch((error) => console.log(error));
    timer = setInterval(() => {
      getCountryByRegion();
    }, 10000);
  }
};

const getFilterOption = function () {
  clearInterval(timer);
  let option = $("filterList").value;
  console.log(option);

  if (option == "") {
    getData();
  } else if (option == "region") {
  } else if (option == "independence") {
  } else if (option == "landlock") {
  } else if (option == "borders") {
  }

  // if (option == "") {
  //   getData();
  // } else {
  //   fetch(`https://restcountries.com/v3.1/region/${region}`)
  //     .then((response) => response.json()) // returns response promise
  //     .then((json) => {
  //       getRandomCountry(json);
  //     }) // returns json promise
  //     .catch((error) => console.log(error));
  //   timer = setInterval(() => {
  //     getCountryByRegion();
  //   }, 10000);
  // }
};

const startTimer = function () {
  timer = setInterval(() => {
    getData();
  }, 10000);
};

document.addEventListener("DOMContentLoaded", () => {
  $("searchButton").addEventListener("click", getSearchTerm);
  getData();
  startTimer();

  $("filterList").addEventListener("change", getFilterOption);
});
