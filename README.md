
# 🧠 Smart Todo List with AI Suggestions

Smart Todo List is a full-stack web application built with **Django REST Framework** and **React**. It allows users to:
- Add, view, and organize tasks
- Prioritize them based on importance
- Get AI-powered task suggestions

---

## 🔧 Technologies Used

- **Frontend:** React, Axios, Tailwind CSS (optional for styling)
- **Backend:** Django, Django REST Framework
- **Database:** SQLite (default), supports PostgreSQL
- **AI Suggestion Engine:** Placeholder for LLM-based integration (expandable)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/smart-todo-list.git
cd smart-todo-list
```

---

### 2. Backend Setup (Django)

#### 🧱 Create Virtual Environment

```bash
python -m venv env
source env/bin/activate     # On Windows: env\Scripts\activate
```

#### 📦 Install Requirements

```bash
pip install -r requirements.txt
```

#### 🔧 Database Configuration

By default, SQLite is used. If switching to PostgreSQL, update `smart_todo/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'smart_todo',
        'USER': 'your_pg_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

#### 📥 Apply Migrations

```bash
python manage.py migrate
```

#### ▶️ Run Backend Server

```bash
python manage.py runserver
```

---

### 3. Frontend Setup (React)

```bash
cd frontend
npm install
npm start
```

> Make sure the backend is running at `http://localhost:8000`

---

## ✨ Features

### ✅ Task Management
- Add task with title, description, category, and priority (1-5)
- View all tasks with sorting by priority
- Categorized display

### 🤖 AI Task Suggestions
- Get task suggestions by clicking **Refresh**
- Suggestions are shown below task list
- Click a suggestion to autofill task form

---

## 🖼️ UI Screenshots

### 🔽 Add Task Panel

![Add Task UI](SmartToDoList_Project\Scrrenshot_UI\Task-UI.png)

### 📋 Task List + AI Suggestions

![Task List](SmartToDoList_Project\Scrrenshot_UI\AI-Generate.png)

---

## 🧠 How AI Suggestions Work

- Currently mocked/stubbed in backend
- Endpoint: `POST /todos/ai/tasks/suggestions/`
- Can integrate with LLM (e.g., OpenAI, LangChain) to generate smart suggestions

---

## 🛠️ Future Enhancements

- User login & auth
- Task deadlines and reminders
- Calendar integration
- Speech-to-text task entry
- Drag & drop for task reordering

---

