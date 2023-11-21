"use strict";

const $ = (selector) => document.querySelector(selector);

document.addEventListener("DOMContentLoaded", () => {
  // preload images
  const imageLinks = $("#image_list").querySelectorAll("a");
  for (let link of imageLinks) {
    const image = new Image();
    image.src = link.href;

    // attach mouseover and mouseout events for each image

    $("#image1").onmouseover = function () {
      $("#image1").src = imageLinks[0].href;
    };
    $("#image1").onmouseout = function () {
      $("#image1").src = imageLinks[2].href;
    };

    $("#image2").onmouseover = function () {
      $("#image2").src = imageLinks[1].href;
    };
    $("#image2").onmouseout = function () {
      $("#image2").src = imageLinks[3].href;
    };
  }
});
