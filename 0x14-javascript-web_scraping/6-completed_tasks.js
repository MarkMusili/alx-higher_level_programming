#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
	if (error){
		console.error(error);
	} else {
		const content = JSON.parse(body);

		task_count = {}
		for todo in content:
			if todo['completed']:
				user_id = todo['userID']:
					task_count[user_id] = task_count.get(user_id, 0) + 1;
		console.log(task_count)
	}
});
