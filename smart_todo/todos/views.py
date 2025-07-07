from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from .models import Task, ContextEntry
from .serializers import TaskSerializer, ContextEntrySerializer
from .ai_module import analyze_context_and_suggest_tasks
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('priority', 'deadline')
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'category', 'tags']
    ordering_fields = ['priority', 'deadline']

class ContextEntryViewSet(viewsets.ModelViewSet):
    queryset = ContextEntry.objects.all().order_by('-timestamp')
    serializer_class = ContextEntrySerializer

@api_view(['POST'])
def get_ai_task_suggestions(request):
    return Response(analyze_context_and_suggest_tasks())

class AITaskSuggestionsView(APIView):
    def post(self, request):
        # Dummy suggestions for testing
        suggestions = [
            {
                "title": "Prepare for client meeting",
                "description": "Review notes and agenda before call",
                "priority": 2,
                "category": "Work",
                "deadline_suggestion": "2025-07-08"
            },
            {
                "title": "Buy groceries",
                "description": "Milk, Eggs, Bread",
                "priority": 4,
                "category": "Personal",
                "deadline_suggestion": "2025-07-07"
            },
        ]
        return Response(suggestions, status=status.HTTP_200_OK)

