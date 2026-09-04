const tasks = [];
let taskIdCounter = 0;

const form = document.getElementById('taskForm');
const taskInput = document.getElementById('taskInput');
const listTasksContainer = document.querySelector('.listTasks');

form.addEventListener('submit', (event) => {
	event.preventDefault();
	addTask();
});

function addTask() {
	const taskText = taskInput.value.trim();

	if (taskText === '') {
		alert('Please enter a valid task.');
		taskInput.focus();
		return;
	}

	const currentId = taskIdCounter++;
	const newTask = {
		task_id: currentId,
		text: taskText,
		done: false,
	};

	tasks.push(newTask);

	const taskDiv = document.createElement('div');
	taskDiv.classList.add('task-item');
	taskDiv.dataset.taskId = currentId;

	const deleteBtn = document.createElement('button');
	deleteBtn.classList.add('delete-btn');
	deleteBtn.type = 'button';
	deleteBtn.setAttribute('aria-label', `Delete task: ${taskText}`);
	deleteBtn.innerHTML = '<i class="fa-solid fa-xmark" aria-hidden="true"></i>';
	deleteBtn.addEventListener('click', () => deleteTask(currentId, taskDiv));

	const checkbox = document.createElement('input');
	checkbox.type = 'checkbox';
	checkbox.id = `task-${currentId}`;
	checkbox.setAttribute('aria-label', `Mark task complete: ${taskText}`);

	const taskSpan = document.createElement('span');
	taskSpan.textContent = taskText;

	checkbox.addEventListener('change', () => doneTask(currentId, taskSpan, checkbox));

	taskDiv.append(deleteBtn, checkbox, taskSpan);
	listTasksContainer.appendChild(taskDiv);

	taskInput.value = '';
	taskInput.focus();
}

function doneTask(id, textElement, checkboxElement) {
	const foundTask = tasks.find((task) => task.task_id === id);

	if (foundTask) {
		foundTask.done = checkboxElement.checked;
		textElement.parentElement.classList.toggle('completed', foundTask.done);
	}
}

function deleteTask(id, taskElement) {
	const taskIndex = tasks.findIndex((task) => task.task_id === id);

	if (taskIndex !== -1) {
		tasks.splice(taskIndex, 1);
	}

	taskElement.remove();
}
