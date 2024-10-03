let current_year = 2024;
let century = 100;

const readline = require('readline').createInterface({
	input: process.stdin,
	output: process.stdout
});

readline.question('Input your name: ', name => {
	readline.question('Input your age: ', age => {
			console.log(`${name}, in the ${current_year - age + century} you will be 100 years old!!! `);
			readline.close();
	});
});