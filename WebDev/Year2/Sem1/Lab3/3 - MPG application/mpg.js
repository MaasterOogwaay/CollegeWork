"use strict";

const $ = (selector) => document.querySelector(selector);

const processEntries = () => {
  const miles = parseFloat($("#miles").value);
  const gallons = parseFloat($("#gallons").value);

  if (isNaN(miles) || miles <= 0) {
    alert("Enter a valid number of miles");
  } else if (isNaN(gallons) || gallons <= 0) {
    alert("Enter a valid number of miles gallons of gas used");
  } else {
    $("#mpg").value = (miles / gallons).toFixed(2);
  }
};

const clearEntries = () => {
  $("#miles").value = "";
  $("#gallons").value = "";
  $("#mpg").value = "";
};

document.addEventListener("DOMContentLoaded", () => {
  $("#calculate").addEventListener("click", processEntries);
  $("#miles").focus();
});

// document.addEventListener("dblclick", () => {
//   clearEntries();
// });

$("#mpg").ondblclick = () => {
  clearEntries();
};

$("#gallons").addEventListener("focusout", () => {
  processEntries();
});
