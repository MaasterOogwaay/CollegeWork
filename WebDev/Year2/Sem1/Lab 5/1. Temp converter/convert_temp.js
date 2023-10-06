"use strict";
const $ = (id) => document.getElementById(id);

/*********************
 *  helper functions  *
 **********************/
const calculateCelsius = (temp) => ((temp - 32) * 5) / 9;
const calculateFahrenheit = (temp) => (temp * 9) / 5 + 32;

const toggleDisplay = (label1Text, label2Text) => {
  $("degree_label_1").innerHTML = label1Text;
  $("degree_label_2").innerHTML = label2Text;
  $("degrees_entered").value = "";
  $("degrees_computed").value = "";
};

/****************************
 *  event handler functions  *
 *****************************/
const convertTemp = () => {
  const degreesEntered = $("degrees_entered").value;
  console.log(degreesEntered);
  if (isNaN(degreesEntered)) {
    $("message").innerHTML = "You must enter a valid number of degrees";
    $("degrees_entered").value = "";
    $("degrees_computed").value = "";
    $("degrees_entered").focus();
  } else {
    if ($("to_celsius").checked) {
      const conversion = Math.ceil(calculateCelsius(degreesEntered));
      $("degrees_computed").value = conversion;
      $("message").innerHTML = "";
    } else {
      const conversion = Math.ceil(calculateFahrenheit(degreesEntered));
      $("degrees_computed").value = conversion;
      $("message").innerHTML = "";
    }
  }
};

const toCelsius = () => toggleDisplay("Enter F degrees:", "Degrees Celsius:");
const toFahrenheit = () => toggleDisplay("Enter C degrees:", "Degrees Fahrenheit:");

document.addEventListener("DOMContentLoaded", () => {
  // add event handlers
  $("convert").addEventListener("click", convertTemp);
  $("to_celsius").addEventListener("click", toCelsius);
  $("to_fahrenheit").addEventListener("click", toFahrenheit);

  // move focus
  $("degrees_entered").focus();
});
