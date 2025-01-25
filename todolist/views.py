from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from todolist.serializers import TasksSerializer
from todolist.models import Tasks
from drf_yasg.utils import swagger_auto_schema

# ver y crear 
@swagger_auto_schema(
    methods=['post'],
    request_body=TasksSerializer,  
    responses={
        201: TasksSerializer,  
        400: "Datos inválidos"  
    }
)
@api_view(['GET', 'POST'])
def task_list_create(request):
    if request.method == 'GET':
        tasks = Tasks.objects.all()
        serializer = TasksSerializer(tasks, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# obtener, actualizar y/o eliminar
@swagger_auto_schema(method='get', responses={200: TasksSerializer, 404: "Task not found"})
@swagger_auto_schema(
    method='put',
    request_body=TasksSerializer,
    responses={200: TasksSerializer, 400: "Datos inválidos", 404: "Task not found"}
)
@swagger_auto_schema(method='delete', responses={204: "Task deleted successfully", 404: "Task not found"})
@api_view(['GET', 'PUT', 'DELETE'])
def task_list_edit(request, pk):
    try:
        task = Tasks.objects.get(pk=pk)
    except Tasks.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TasksSerializer(task)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = TasksSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        task.delete()
        return Response({'message':'Task deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


