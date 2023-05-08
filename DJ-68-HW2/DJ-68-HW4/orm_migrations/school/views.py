from django.views.generic import ListView

from .models import Student


class StudentList(ListView):
    template_name = 'school/students_list.html'
    context_object_name = 'students'

    def get_queryset(self):
        return Student.objects.all().prefetch_related('teachers')
