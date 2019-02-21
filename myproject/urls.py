from django.urls import path, include

urlpatterns = [
    path('tasks/', include('dramatiq_tasks_manager.urls')),
]
