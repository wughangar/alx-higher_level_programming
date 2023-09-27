#!/usr/bin/node

const request = require('request');
const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }
  if (response.statusCode !== 200) {
    console.error('Error: Status code:', response.statusCode);
    process.exit(1);
  }
  try {
    const todosData = JSON.parse(body);

    const completedTodos = todosData.filter(todo => todo.completed);

    const userTaskCounts = {};
    completedTodos.forEach(todo => {
      if (userTaskCounts[todo.userId]) {
        userTaskCounts[todo.userId]++;
      } else {
        userTaskCounts[todo.userId] = 1;
      }
    });
    const output = {};
    for (const userId in userTaskCounts) {
      output[userId] = userTaskCounts[userId];
    }
    console.log(output);
  } catch (parseError) {
    console.error('Error parsing API response:', parseError);
    process.exit(1);
  }
});
