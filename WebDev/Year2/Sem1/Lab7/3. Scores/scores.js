const $ = (selector) => document.querySelector(selector);
let scores = [];
let nameScores = [];

const displayScores = () => {

};

const addScore = () => {
    // Your code goes here:



    // get the add form ready for next entry
    $("#first_name").value = "";
    $("#last_name").value = "";
    $("#score").value = "";
    $("#first_name").focus();
};

const clearScores = () => {
    // Your code goes here:



    // remove the score data from the web page
    $("#average_score").value = "";
    $("#scores").value = "";

    $("#first_name").focus();
};

const sortScores = () => {

};

window.addEventListener('load', () => {
    $("#add_button").addEventListener('click', addScore);
    $("#clear_button").addEventListener('click', clearScores);
    $("#sort_button").addEventListener('click', sortScores);
    $("#first_name").focus();
});