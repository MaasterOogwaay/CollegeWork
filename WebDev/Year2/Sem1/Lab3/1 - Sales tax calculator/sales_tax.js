"use strict";

const $ = (selector) => document.querySelector(selector);

const handleClick = () => {
  let subTotal = parseFloat($("#subtotal").value);
  let taxRate = parseFloat($("#tax_rate").value);
  console.log(`Subtotal = ${subTotal} | taxrate = ${taxRate}`);

  if (subTotal < 0 || subTotal > 10000) {
    clearBtnHandler();
    alert("Subtotal must be between 0 and 10,000");
    if (taxRate < 0 || taxRate > 12) {
      clearBtnHandler();
      alert("Tax rate must be between 0 and 12");
    }
  } else {
    let salesTax = parseFloat((subTotal * (7.5 / 100)).toFixed(2));
    console.log(salesTax);
    $("#sales_tax").value = `${salesTax}`;

    let total = parseFloat(subTotal + salesTax);
    console.log(total);
    $("#total").value = `${total}`;
    $("#subtotal").focus();
  }
};

const clearBtnHandler = () => {
  $("#subtotal").value = "";
  $("#tax_rate").value = "";
  $("#sales_tax").value = "";
  $("#total").value = "";
  $("#subtotal").focus();
};

window.addEventListener("load", () => {
  $("#subtotal").focus();
  $("#calculate").addEventListener("click", handleClick);
  $("#clear").addEventListener("click", clearBtnHandler);
});
