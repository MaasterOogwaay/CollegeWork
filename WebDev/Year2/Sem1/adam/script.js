const changeColor = function () {
  const colors = ["Red", "Blue"];

  // Variable to keep track of the
  // current color index
  let currentColorIndex = 0;

  // Function to toggle the background
  // color of the div
  function blinkBackground() {
    document.getElementById("bg").style.backgroundColor = colors[currentColorIndex];
    currentColorIndex = (currentColorIndex + 1) % colors.length;
  }

  setInterval(blinkBackground, 1000);
};

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("btn").addEventListener("click", changeColor);
});
