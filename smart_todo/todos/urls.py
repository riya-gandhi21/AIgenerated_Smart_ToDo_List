from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, ContextEntryViewSet, get_ai_task_suggestions,AITaskSuggestionsView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'context', ContextEntryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('ai/tasks/suggestions/',AITaskSuggestionsView.as_view()),
]
