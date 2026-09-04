let numSquares = 6;
let colors = [];
let pickedColor;

const squares = document.querySelectorAll('.square');
const colorDisplay = document.getElementById('colorDisplay');
const messageDisplay = document.getElementById('message');
const resetButton = document.getElementById('reset');
const modeButtons = document.querySelectorAll('.modeBtn');

init();

function init() {
	setupModeButtons();
	setupSquares();
	reset();
}

function setupModeButtons() {
	modeButtons.forEach((button) => {
		button.addEventListener('click', () => {
			modeButtons.forEach((modeButton) => modeButton.classList.remove('selected'));
			button.classList.add('selected');
			numSquares = button.dataset.mode === '3' ? 3 : 6;
			reset();
		});
	});
}

function setupSquares() {
	squares.forEach((square) => {
		square.addEventListener('click', () => {
			const clickedColor = square.style.backgroundColor;

			if (clickedColor === pickedColor) {
				messageDisplay.textContent = 'Correct!';
				resetButton.textContent = 'Play Again?';
				changeColors(pickedColor);
			} else {
				square.style.backgroundColor = '#232323';
				messageDisplay.textContent = 'Try Again';
			}
		});
	});
}

function reset() {
	colors = generateRandomColors(numSquares);
	pickedColor = pickColor();
	colorDisplay.textContent = pickedColor.toUpperCase();
	messageDisplay.textContent = '';
	resetButton.textContent = 'New Colors';

	squares.forEach((square, index) => {
		if (colors[index]) {
			square.style.display = 'block';
			square.style.backgroundColor = colors[index];
			square.setAttribute('aria-label', `Color swatch ${index + 1}`);
		} else {
			square.style.display = 'none';
		}
	});
}

resetButton.addEventListener('click', reset);

function changeColors(color) {
	squares.forEach((square, index) => {
		if (colors[index]) {
			square.style.backgroundColor = color;
		}
	});
}

function pickColor() {
	return colors[Math.floor(Math.random() * colors.length)];
}

function generateRandomColors(number) {
	return Array.from({ length: number }, randomColor);
}

function randomColor() {
	const red = Math.floor(Math.random() * 256);
	const green = Math.floor(Math.random() * 256);
	const blue = Math.floor(Math.random() * 256);
	return `rgb(${red}, ${green}, ${blue})`;
}
