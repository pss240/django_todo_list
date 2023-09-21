from django.shortcuts import render
from posting.models import Task

from posting.serializer import TaskSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def getTaskList(request):
    TaskSetQuery = Task.objects.all()
    serializer = TaskSerializer(TaskSetQuery,many=True)
    print(serializer.data)
    return Response(serializer.data,status = 200)


@api_view(['POST'])
def addTask(request):
    if request.method =='POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        else:
            print(serializer.errors)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def updateTask(request,pk,work):
    targetTask = Task.objects.get(id=pk)
    targetTask.work = work
    targetTask.isComplete=False
    targetTask.save()
    serialized_Task = TaskSerializer(targetTask)
    return Response(serialized_Task.data,status=200)

@api_view(['GET'])
def deleteTask(request,pk):
    Task.objects.get(id=pk).delete()
    return Response(status=200)