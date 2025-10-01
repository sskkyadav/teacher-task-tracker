from django import forms
from .models import WorkEntry

class TeacherLoginForm(forms.Form):
    mobile = forms.CharField(label="Mobile Number", max_length=15, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))

class WorkEntryForm(forms.ModelForm):
    class Meta:
        model = WorkEntry
        fields = ['class_section','exam_name','subject_group','subject_name','student_status','teacher_name']
        widgets = {
            'class_section': forms.TextInput(attrs={'class':'form-control'}),
            'exam_name': forms.TextInput(attrs={'class':'form-control'}),
            'subject_group': forms.TextInput(attrs={'class':'form-control'}),
            'subject_name': forms.TextInput(attrs={'class':'form-control'}),
            'student_status': forms.TextInput(attrs={'class':'form-control'}),
            'teacher_name': forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
        }
