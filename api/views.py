from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task


@api_view(['GET'])
def apiOverview(request):
    """
    API endpoint that shows every endpoint url available
    """
    api_urls = {
        'List': '/task-list/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
        'Detail': '/task-detail/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    """
    API endpoint for all tasks on database
    """
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request,pk):
    """
    API endpoint for detailed view on a specific task
    """
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    """
    API endpoint for task creation
    """
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.erros, status=400)


@api_view(['POST'])
def taskUpdate(request,pk):
    """
    API endpoint for task update
    """
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def taskDelete(request,pk):
    """
    API endpoint for task delete
    """
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Item Removed')
