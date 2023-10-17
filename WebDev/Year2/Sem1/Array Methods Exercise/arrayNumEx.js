const numbers = [456, -20, 33, 476, 999, 62, 7, -100, 10];

/* For all the following exercises:
		- make sure to print out the result to ensure you get the correct answers
		- use the for...of loop for all the for loop examples
*/

/* 1. Use an array method to sort the numbers array */
const sorted = numbers.sort((x, y) => x - y);
console.log("Sorted Array: " + sorted.toString());

/* 2.1 Use an array method to create a new array with each element doubled */
const doubled = numbers.map((val) => val + val);
console.log("Doubled Array: " + doubled.toString());

/* 2.2 Use a for loop to get the same result */
let msgString = "";
for (const element of numbers) {
  msgString += element + element + ", ";
}
console.log("Loop Doubled Array: " + msgString);

/* 3.1 Use an array method to create a new array with
		the negative values removed */
const oddNums = numbers.filter((val) => val % 2 != 0);
console.log("Array of Odd Nums: " + oddNums.toString());

/* 3.2 Use a for loop to get the same result */
let oddString = "";
for (const elems of numbers) {
  if (elems % 2 != 0) {
    oddString += elems + ", ";
  }
}
console.log("Odd Nums (for of loop): " + oddString);

/* 4.1 Use the filter and forEach methods to add all the values greater than 100 */
let sum = 0;
const greaterNums = numbers.filter((val) => val > 100);
// console.log("Greater Nums: " + greaterNums);

greaterNums.forEach((val) => (sum += val));

console.log("Sum of Greater Nums (filter & forEach): " + sum);

/* 4.2 Use filter and reduce to get the same result */
const greaterThan100 = numbers.filter((val) => val > 100);
const greaterThan100Sum = greaterThan100.reduce((total, current) => total + current, 0);
console.log("Sum of Greater Nums (filter & reduce): " + greaterThan100Sum);

/* 4.3 Use a for loop to get the same result */
let sumOfGreaterThan100 = 0;
for (const elems of numbers) {
  if (elems > 100) {
    sumOfGreaterThan100 += elems;
  }
}
console.log("Sum of Greater Nums (for of loop): " + sumOfGreaterThan100);
