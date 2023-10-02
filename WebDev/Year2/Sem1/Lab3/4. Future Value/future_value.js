"use strict";

const $ = function (selector) {
  return document.querySelector(selector);
};

const processEntries = () => {
  const investment = $("#investment").value;
  const annualRate = $("#annual_rate").value;
  const years = $("#years").value;

  if (investment < 0 || investment > 100000) {
    $("investment_error").textContent = "Must be > 0 or < 100,000";
  } else if (annualRate < 0 || annualRate > 12) {
    $("rate_error").innerHTML = "Must be > 0 or <= 12";
  } else if (years < 0 || years > 50) {
    $("years_error").innerHTML = "Must be > 0 or <= 50";
  } else {
    const result = calculateFV(investment, annualRate, years);
    $("#future_value").value = result;
  }
};

const calculateFV = (investment, annualRate, years) => {
  const total = (investment * (annualRate / 100) * years).toFixed(2);
  console.log(`${investment} | ${annualRate} | ${years}`);
  console.log(total);
  return total;
};

document.addEventListener("DOMContentLoaded", () => {
  $("#calculate").addEventListener("click", processEntries);
  $("#investment").focus();
});
