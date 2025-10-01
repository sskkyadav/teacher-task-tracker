from django.shortcuts import render, redirect
from .forms import TeacherLoginForm, WorkEntryForm
from .models import Teacher, WorkEntry

def login_view(request):
    if request.method == "POST":
        form = TeacherLoginForm(request.POST)
        if form.is_valid():
            mobile = form.cleaned_data['mobile']
            password = form.cleaned_data['password']
            try:
                teacher = Teacher.objects.get(mobile=mobile)
                if password == teacher.password:
                    request.session['teacher_mobile'] = mobile
                    request.session['teacher_name'] = teacher.name
                    return redirect('index')
                else:
                    form.add_error(None, "Incorrect password")
            except Teacher.DoesNotExist:
                form.add_error(None, "Teacher not found")
    else:
        form = TeacherLoginForm()
    return render(request, "login.html", {'form': form})

def logout_view(request):
    request.session.flush()
    return redirect('login')

def index(request):
    if 'teacher_mobile' not in request.session:
        return redirect('login')

    teacher_name = request.session['teacher_name']

    if request.method == "POST":
        form = WorkEntryForm(request.POST)
        if form.is_valid():
            work = form.save(commit=False)
            work.teacher_name = teacher_name
            total_fields = 5  # class_section, exam_name, subject_group, subject_name, student_status
            filled = sum([1 for field in [work.class_section, work.exam_name, work.subject_group, work.subject_name, work.student_status] if field])
            work.completion_percent = int((filled / total_fields) * 100)
            work.save()
            return redirect('index')
    else:
        form = WorkEntryForm(initial={'teacher_name': teacher_name})

    entries = WorkEntry.objects.all()
    return render(request, "index.html", {"form": form, "entries": entries})
