from django.shortcuts import render, redirect

def index(request):
    tasks = request.session.get('tasks', [])
    task_list_html = ''.join(f'<li class="list-group-item d-flex justify-content-between align-items-center">{task}</li>' for task in tasks)
    return render(request, 'index.html', {'task_list_html': task_list_html})

def Add_Task(request):
    tasks = request.session.get('tasks', [])
    data = request.GET.get('text', '').strip()    
    if data:
        tasks.append(data)
    request.session['tasks'] = tasks
    return redirect('/')

def Delete_All_Tasks(request):
    # Clear all tasks from the session
    request.session['tasks'] = []
    return redirect('/')