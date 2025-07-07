import React, { useEffect, useState } from "react";
import axios from "axios";

axios.defaults.baseURL = "http://127.0.0.1:8000";

export default function SmartTodoApp() {
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState({ title: "", category: "", priority: 3 });
  const [aiSuggestions, setAiSuggestions] = useState([]);

  const fetchTasks = async () => {
    const res = await axios.get("/todos/tasks/?ordering=priority");
    setTasks(res.data);
  };

 const fetchAiSuggestions = async () => {
  try {
    const res = await axios.post("/todos/ai/tasks/suggestions/");
   // console.log("AI Suggestions:", res.data);  // Debug print
    setAiSuggestions(res.data);
  } catch (err) {
    console.error("AI Suggestion Error:", err);  // Show error in console
  }
};



  const addTask = async () => {
    await axios.post("/todos/tasks/", newTask);
    setNewTask({ title: "", category: "", priority: 3 });
    fetchTasks();
  };

  const applySuggestion = (s) => {
  setNewTask({
    title: s.title,
    description: s.description,
    category: s.category,
    priority: s.priority,
  });
};


  useEffect(() => {
    fetchTasks();
  }, []);

  return (
    <div className="p-6 max-w-4xl mx-auto font-sans">
      <h1 className="text-3xl font-bold mb-4">🧠 Smart Todo List</h1>

      <div className="card mb-6 p-4 border rounded shadow">
        <h2 className="text-xl font-semibold mb-2">Quick Add Task</h2>
        <input
          type="text"
          placeholder="Title"
          value={newTask.title}
          onChange={(e) => setNewTask({ ...newTask, title: e.target.value })}
          className="input mb-2 border p-2 rounded w-full"
        />
        <textarea
          placeholder="Description"
          value={newTask.description || ""}
          onChange={(e) => setNewTask({ ...newTask, description: e.target.value })}
          className="textarea mb-2 border p-2 rounded w-full"
        />
        <input
          type="text"
          placeholder="Category"
          value={newTask.category}
          onChange={(e) => setNewTask({ ...newTask, category: e.target.value })}
          className="input mb-2 border p-2 rounded w-full"
        />
        <input
          type="number"
          placeholder="Priority (1-5)"
          value={newTask.priority}
          onChange={(e) => setNewTask({ ...newTask, priority: Number(e.target.value) })}
          className="input mb-2 border p-2 rounded w-full"
        />
        <button onClick={addTask} className="btn bg-blue-600 text-white px-4 py-2 rounded">
          Add Task
        </button>
      </div>

      <div className="grid md:grid-cols-2 gap-4">
        <div>
          <h2 className="text-xl font-bold mb-2">📝 Task List</h2>
          {tasks.map((task) => (
            <div key={task.id} className="mb-2 p-3 border rounded shadow">
              <div className="font-semibold">
                {task.title} <span className="text-sm text-gray-500">(Priority {task.priority})</span>
              </div>
              <div className="text-sm text-gray-700">{task.description}</div>
              <div className="text-xs text-gray-500">Category: {task.category}</div>
            </div>
          ))}
        </div>

        <div>
          <div className="flex justify-between items-center mb-2">
            <h2 className="text-xl font-bold">✨ AI Suggestions</h2>
            <button
              onClick={fetchAiSuggestions}
              className="btn border border-blue-500 text-blue-500 px-3 py-1 rounded hover:bg-blue-50"
            >
              Refresh
            </button>
          </div>
          {aiSuggestions.map((s, idx) => (
            <div
              key={idx}
              className="mb-2 p-3 border rounded shadow cursor-pointer hover:bg-gray-100"
              onClick={() => applySuggestion(s)}
            >
              <div className="font-semibold">{s.title}</div>
              <div className="text-sm">{s.description}</div>
              <div className="text-xs text-gray-500">Suggested Deadline: {s.deadline_suggestion}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
