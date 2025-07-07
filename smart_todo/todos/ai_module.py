from .models import ContextEntry
from datetime import date, timedelta

def analyze_context_and_suggest_tasks():
    entries = ContextEntry.objects.all().order_by('-timestamp')[:50]
    suggestions = []

    for entry in entries:
        text = entry.content.lower()

        if "meeting" in text:
            suggestions.append({
                "title": "Prepare for meeting",
                "description": f"Auto-generated from: {entry.content}",
                "category": "Work",
                "priority": 1,
                "deadline_suggestion": str(date.today())
            })
        elif "birthday" in text:
            suggestions.append({
                "title": "Buy birthday gift",
                "description": f"Detected from: {entry.content}",
                "category": "Personal",
                "priority": 2,
                "deadline_suggestion": str(date.today() + timedelta(days=1))
            })
        elif "submit" in text or "deadline" in text:
            suggestions.append({
                "title": "Complete submission",
                "description": f"Context: {entry.content}",
                "category": "Urgent",
                "priority": 1,
                "deadline_suggestion": str(date.today())
            })

    return suggestions
