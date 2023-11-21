const $ = function (id) {
  return document.getElementById(id);
};

const getData = function (lat, long) {
  fetch(
    `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${long}&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_hours,precipitation_probability_max,wind_speed_10m_max`
  )
    .then((response) => response.json()) // returns response promise
    .then((json) => {
      console.log(json);
      fillTable(json);
    }) // returns json promise
    .catch((error) => console.log(error));
};

const getSearchTerm = function () {
  let countryName = $("search-bar").value;
  console.log(countryName);
  getCountry(countryName);
};

// https://restcountries.com/v3.1/name/Ireland?fullText=true

const getCountry = function (countryName) {
  fetch(`https://restcountries.com/v3.1/name/${countryName}?fullText=true`)
    .then((response) => response.json()) // returns response promise
    .then((json) => {
      console.log(json);
      console.log(json[0].latlng);
      let lat = json[0].latlng[0];
      let long = json[0].latlng[1];
      console.log(lat, long);
      getData(lat, long);
    }) // returns json promise
    .catch((error) => console.log(error));
};

const fillTable = function (data) {
  let tableContent =
    "<tr><th>Time</th><th>Code</th><th>Min Temp</th><th>Max Temp</th><th>Wind Speed</th><th>Precipitation Probability</th><th>Precipitation Hours</th></tr>";

  for (let i = 0; i < data.daily.time.length; i++) {
    let time = data.daily.time[i];

    let code = data.daily.weather_code[i];

    let temp_min = data.daily.temperature_2m_min[i];
    let tempMinUnit = data.daily_units.temperature_2m_min;

    let temp_max = data.daily.temperature_2m_max[i];
    let tempMaxUnit = data.daily_units.temperature_2m_max;

    let windSpeed = data.daily.wind_speed_10m_max[i];
    let windSpeedUnit = data.daily_units.wind_speed_10m_max;

    let precipitationProbability = data.daily.precipitation_probability_max[i];
    let precipitationProbabilityUnit = data.daily_units.precipitation_probability_max;

    let precipitationHours = data.daily.precipitation_hours[i];
    let precipitationHoursUnit = data.daily_units.precipitation_hours;
    tableContent += `<tr><td>${time}</td><td>${code}</td><td>${temp_min}${tempMinUnit}</td><td>${temp_max}${tempMaxUnit}</td>`;
    tableContent += `<td>${windSpeed}${windSpeedUnit}</td><td>${precipitationProbability}${precipitationProbabilityUnit}</td><td>${precipitationHours}${precipitationHoursUnit}</td></tr>`;
  }
  $("table1").innerHTML = tableContent;
};

document.addEventListener("DOMContentLoaded", () => {
  navigator.geolocation.getCurrentPosition((position) => {
    let lat = position.coords.latitude.toFixed(2);
    let long = position.coords.longitude.toFixed(2);

    // latText.innerText = lat.toFixed(2);
    // longText.innerText = long.toFixed(2);
    console.log(`Lat: ${lat} | Long: ${long}`);

    getData(lat, long);
  });

  $("search-button").addEventListener("click", getSearchTerm);
});
