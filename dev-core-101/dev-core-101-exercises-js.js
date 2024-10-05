//even or odd
let num = parseInt(prompt("Input number: "));

if (num % 2 == 0)
	console.log("The number is even");
else
	console.log("The number is odd");

//multiplication table
let number = parseInt(prompt("Input number: "));

for (let i = 1; i <= 10; i++ ) {
	console.log(`${number} * ${i} = ${number * i} `);
}

//from m/s to km/h
let velocity = parseInt(prompt("Input velocity in m/s: "))
console.log(`${velocity} m/s = ${velocity * 3.6} km/h`);
