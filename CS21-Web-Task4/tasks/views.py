from .models import *
from .forms import *
from django.shortcuts import render ,redirect
from django.http import HttpResponse

# Create your views here.


# def index(request):
#     return render(request,'tasks/list.html ')

def index(request):
	tasks = Task.objects.all()

	form = TaskForm()

	if request.method =='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')


	context = {'tasks':tasks, 'form':form}
	return render(request, 'tasks/list.html', context)

def updateTask(request, pk):
	taskk = Task.objects.get(id=pk)

	form = TaskForm(instance=taskk)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=taskk)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}

	return render(request, 'tasks/update.html', context)

def deleteTask(request, pk):
	item = Task.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	context = {'item':item}
	return render(request, 'tasks/delete.html', context)
