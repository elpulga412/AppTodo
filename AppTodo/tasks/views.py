from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import TaskForm
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
# Create your views here.

def index(request):
	tasks = Task.objects.all()
	context = {'tasks':tasks}
	return render(request, 'tasks/list.html', context)

def updateTask(request, pk):
	task = Task.objects.get(id=pk)
	form = TaskForm(instance=task)
	if request.method == "POST":
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect("/")
	context = {'form':form}
	return render(request, 'tasks/update_task.html', context)

@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all()
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(task, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(data=request.data, instance=tasks)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
	tasks = Task.objects.get(id=pk)
	tasks.delete()
	return Response("Item success fully")

class searchTask(ListAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['title']