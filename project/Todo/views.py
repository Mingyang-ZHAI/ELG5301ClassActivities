from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import TodoM


def list_todo(request, *args, **kwargs):
    if request.method == "GET":
        todos = TodoM.objects.all()
        data = [
            {
                "id": todo.id,
                "todo": todo.task,
                "done": todo.done
            } for todo in todos
        ]
        return JsonResponse({
            "data": data
        })
    return JsonResponse(data={
        "message": "Method not allowed"
    }, status=405)


def create_todo(request, *args, **kwargs):
    if request.POST:
        todo = TodoM.objects.create(task=request.POST.get("task"))
        return JsonResponse(data={
            "todo": todo.task
        }, status=201)
    return JsonResponse(data={
        "message": "Method not allowed"
    }, status=405)


def retrieve_todo(request, id, *args, **kwargs):
    if request.method == "GET":
        todo = get_object_or_404(TodoM, id=id)
        return JsonResponse(data={
            "todo": todo.task,
            "done": todo.done
        })
    return JsonResponse(data={
        "message": "Method not allowed"
    }, status=405)


def update_todo(request, id, *args, **kwargs):
    if request.POST:
        todo = get_object_or_404(TodoM, id=id)
        todo.task = request.POST.get("task") or todo.task
        done = request.POST.get("done")
        todo.done = bool(done) or todo.done
        todo.save()
        return JsonResponse(data={
            "todo": todo.task,
            "done": todo.done
        })
    return JsonResponse(data={
        "message": "Method not allowed"
    }, status=405)


def delete_todo(request, id, *args, **kwargs):
    if request.method == "DELETE":
        todo = get_object_or_404(TodoM, id=id)
        todo.delete()
        return JsonResponse({}, status=204)
    return JsonResponse(data={
        "message": "Method not allowed"
    }, status=405)
