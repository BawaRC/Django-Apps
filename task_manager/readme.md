# Task Manager App

## What is this?
A simple Task Manager app built with Django. You can create, update, and delete tasks. Tasks are linked to categories, and you can filter them by due date, category, or name. The backend uses Django REST Framework and `django-filter` for filtering. The frontend uses HTML and Bootstrap.

## Features
- CRUD operations on tasks (Create, Read, Update, Delete)
- Tasks belong to categories.
- Filter tasks by:
  - **Category**
  - **Due Date**
  - **Name**
- Built with **Django REST Framework** and **django-filter** for easy filtering.

## Models
- **Task**:
  - `name`: Name or description of the task
  - `due_date`: The date the task is due
  - `category_id`: Foreign key linking the task to a category
- **Category**:
  - `name`: Name of the category (e.g., "Work", "Personal")

## API Endpoints
- `GET /tasks/`: List all tasks (can filter by category, due date, and name)
- `POST /tasks/`: Create a new task
- `GET /tasks/{id}/`: Get a specific task
- `PUT /tasks/{id}/`: Update a task
- `DELETE /tasks/{id}/`: Delete a task

- `GET /categories/`: List all categories
- `POST /categories/`: Create a category
- `GET /categories/{id}/`: Get a specific category
- `PUT /categories/{id}/`: Update a category
- `DELETE /categories/{id}/`: Delete a category

## Filtering
You can filter tasks by passing query parameters in the URL:
- **By category**: `/tasks/?category=Work`
- **By due date**: `/tasks/?due_date=2024-11-20`
- **By task name**: `/tasks/?name=Meeting`
- Combine filters: `/tasks/?category=Work&due_date=2024-11-20&name=Meeting`

## Acknowledgements
- **Django**
- **Django REST Framework**
- **django-filter**
- **Bootstrap**
