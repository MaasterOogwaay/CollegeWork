"use strict";
const $ = (selector) => document.querySelector(selector);

document.addEventListener("DOMContentLoaded", () => {
  // add event handlers
  $("#calculate").addEventListener("click", processEntry);
  $("#income").focus();
});

const processEntry = () => {
  let income = parseInt($("#income").value);
  console.log(income);
  if (isNaN(income) || income < 0) {
    alert("You enter enter a number greater than 0");
    $("#income").focus();
  } else {
    calculateTax(income);
    $("#income").focus();
  }
};

const calculateTax = (income) => {
  if (income < 9225) {
    $("#tax").value = 0;
  }
  if (income >= 9225 && income < 37450) {
    $("#tax").value = 922.5;
  }
  if (income >= 37450 && income < 90750) {
    $("#tax").value = 5156.25;
  }
  if (income >= 90750 && income < 189300) {
    $("#tax").value = 18481.25;
  }
  if (income >= 189300 && income < 411500) {
    $("#tax").value = 46075.25;
  }
  if (income >= 411500 && income < 413200) {
    $("#tax").value = 119401.25;
  }
  if (income >= 413200) {
    $("#tax").value = 119996.25;
  }
};
