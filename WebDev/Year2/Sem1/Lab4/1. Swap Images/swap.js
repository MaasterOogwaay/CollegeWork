const $ = function (id) {
  return document.getElementById(id);
};

const btnClick = () => {
  const h1 = $("header");
  const img = $("image");
  //   console.log(img);
  if (h1.innerHTML == "Picture 1") {
    h1.innerHTML = "Picture 2";
    img.getAttribute("src");
    img.setAttribute("src", "imgs/image2.png");
  } else {
    h1.innerHTML = "Picture 1";
    img.getAttribute("src");
    img.setAttribute("src", "imgs/image1.png");
  }
};

document.addEventListener("DOMContentLoaded", () => {
  $("swapImageBtn").addEventListener("click", btnClick);
});
