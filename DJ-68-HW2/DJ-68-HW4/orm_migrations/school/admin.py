from django.contrib import admin

from .models import Student, Teacher, TeacherStudent


class TeachersInline(admin.TabularInline):
    model = TeacherStudent
    verbose_name = 'Прикрепленный учитель'
    verbose_name_plural = 'Прикрепленные учителя'
    extra = 1
    fields = ('teacher', 'teacher_subject')
    readonly_fields = ('teacher_subject',)

    @admin.display(description='Предмет')
    def teacher_subject(self, obj):
        return obj.teacher.subject


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    exclude = ('teachers',)
    list_display = ('name', 'group')
    inlines = [TeachersInline, ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')
