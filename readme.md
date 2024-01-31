
---

# Django Todo App

This is a simple Django-based Todo app that provides RESTful API endpoints for managing tasks. It supports creating, listing, getting, updating, and deleting tasks, as well as bulk creation.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/django-todo-app.git
   cd django-todo-app
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Apply migrations to create the database:

   ```bash
   python manage.py migrate
   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```

The app should now be accessible at [http://localhost:8000](http://localhost:8000).

## API Endpoints

### Create a new task

```bash
POST /v1/tasks
```

**Input**

```json
{ "title": "Test Task 1", "is_completed": false }
```

**Output**

```json
{ "id": 1 }
```

### List all tasks

```bash
GET /v1/tasks
```

**Output**

```json
{
   "tasks": [
      { "id": 1, "title": "Test Task 1", "is_completed": false },
      { "id": 2, "title": "Test Task 2", "is_completed": true }
   ]
}
```

### Get a specific task

```bash
GET /v1/tasks/{id}
```

**Output**

```json
{ "id": 1, "title": "Test Task 1", "is_completed": false }
```

### Update a specific task

```bash
PUT /v1/tasks/{id}
```

**Input**

```json
{ "title": "Updated Task", "is_completed": true }
```

### Delete a specific task

```bash
DELETE /v1/tasks/{id}
```

### Bulk add tasks

Note: The bulk add tasks has got a bug and not working as of now

```bash
POST /v1/tasks/bulk
```

**Input**

```json
{
   "tasks": [
      { "title": "Test Task 1", "is_completed": true },
      { "title": "Test Task 2", "is_completed": false },
      { "title": "Test Task 3", "is_completed": true }
   ]
}
```

## Testing

<!-- To run tests, use the following command in a new terminal while the django development server is still running:

```bash
python manage.py test
``` 
or 
-->
simply navigate to the root directory and run:
```
pytest
```
Note : The pytest file was written according to flask based so liitle structural changes were made in the test file to test the same endpoints with the same tests.