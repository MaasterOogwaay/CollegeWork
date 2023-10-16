const toDoArray = [];

const $ = (id) => document.getElementById(id);

const addToList = function () {
  const task = $("add_to_list_input").value;
  console.log(task);
  toDoArray[toDoArray.length] = task;

  const list = $("list");
  let index = 1;
  let createLi = (list.innerHTML = "");
  for (i = 0; i < toDoArray.length; i++) {
    createLi += '<li id="' + index + '">' + index + ". " + toDoArray[i] + "</li>";
    index++;
  }
  list.innerHTML = createLi;
  $("add_to_list_input").value = "";

  // <input type="checkbox" id="vehicle1" name="vehicle1" value="Bike">
};

const removeFromList = function () {
  const index = $("remove_from_list_input").value;
  let getLiByID = $(`${index}`);
  //   getLiByID.remove();
  console.log(getLiByID);

  if (getLiByID == null) {
    $("error_message").innerHTML = "Index does not exist!";
  } else {
    getLiByID.remove();
    $("remove_from_list_input").value = "";
  }
};

window.addEventListener("load", () => {
  $("add_to_list_btn").addEventListener("click", addToList);
  $("remove_from_list_btn").addEventListener("click", removeFromList);
  $("add_to_list_input").focus();

  $("add_to_list_input").addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
      console.log("Enter key pressed!");
      addToList();
    }
  });

  $("remove_from_list_input").addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
      console.log("Enter key pressed!");
      removeFromList();
    }
  });
});
