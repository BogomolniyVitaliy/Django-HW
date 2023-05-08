from django.db import models


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name='Имя')
    subject = models.CharField(max_length=10, verbose_name='Предмет')

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name='Имя')
    group = models.CharField(max_length=10, verbose_name='Класс')
    teachers = models.ManyToManyField(Teacher, through='TeacherStudent', related_name='students', blank=True)

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'
        ordering = ('name',)

    def __str__(self):
        return self.name


class TeacherStudent(models.Model):
    id = models.AutoField(primary_key=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Учитель')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Студент')

    def __str__(self):
        return f"{self.teacher.name} - {self.teacher.subject}"
