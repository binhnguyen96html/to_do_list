from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse

from todos_2.models import Todo

# Create your views here.
def list_todo_items(request):
  # return HttpResponse('from list_todo_items')
  context = {'todo_list': Todo.objects.all()}
  return render(request, 'todos_2/todo_list.html', context)

def inster_todo_items(request:HttpRequest):
  todo = Todo(content = request.POST['content'])
  todo.save()
  return redirect('/todos/list')

def delete_todo_item(request, todo_id):
  todo_to_delete = Todo.objects.get(id=todo_id)
  todo_to_delete.delete()
  return redirect('/todos/list')
