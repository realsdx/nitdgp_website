import threading
from django.db import models
from django.core.mail import send_mail
from base.models import BaseModel
from ckeditor.fields import RichTextField
from department.models import Faculty, Courses
from django.core.mail import EmailMessage


class EmailThread(threading.Thread):

    def __init__(self, subject, html_content, recipient_list, sender):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        self.sender = sender
        threading.Thread.__init__(self)

    def run(self):
        msg = EmailMessage(self.subject, self.html_content, self.sender, self.recipient_list)
        msg.content_subtype = 'html'
        msg.send(fail_silently=False)


class Teachings(BaseModel):

    class Meta:
        verbose_name_plural = 'Teachings'

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    teachings = RichTextField()

    def __str__(self):
        return self.faculty.name

    def _teachings(self):
        return self.teachings

    def save(self):
        # EmailThread('Profile Update for ' + self.faculty.name,
        # 'The following information was added/modified in your profile:<br> <b>Teachings</b> on <b>' +
        # self.updated_at.strftime("%d/%m/%Y %H:%M %p") + '</b><br><br>' + self.teachings, ['devanshgoenka97@gmail.com'],
        # 'NITDGP Admin <webmaster@nitdgp.ac.in>').start()
        super(Teachings, self).save()


class AdministrativeResponsibility(BaseModel):

    class Meta:
        verbose_name_plural = 'Administrative Responsibilities'

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    administrative_responsibilities = RichTextField()

    def __str__(self):
        return self.faculty.name

    def _administrative_responsibilities(self):
        return self.administrative_responsibilities


class AwardsAndRecognition(BaseModel):

    class Meta:
        verbose_name_plural = 'Awards and Recognition'

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    awards_and_recognition = RichTextField()

    def __str__(self):
        return self.faculty.name

    def _awards_and_recognition(self):
        return self.awards_and_recognition


class Education(BaseModel):

    class Meta:
        verbose_name_plural = 'Education'

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    education = RichTextField()

    def __str__(self):
        return self.faculty.name

    def _education(self):
        return self.education


class WorkExperience(BaseModel):

    class Meta:
        verbose_name_plural = 'Work Experience'

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    work_experience = RichTextField()

    def __str__(self):
        return self.faculty.name

    def _work_experience(self):
        return self.work_experience


class Projects(BaseModel):

    class Meta:
        verbose_name_plural = 'Projects'

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    projects = RichTextField()

    def __str__(self):
        return self.faculty.name

    def _projects(self):
        return self.projects


def rename_students(instance, filename):

    return 'faculty/{0}/students/{1}'.format(instance.faculty.name, filename)


class Students(BaseModel):

    class Meta:
        verbose_name_plural = 'Students under Faculty'
        ordering = ['-type']

    TYPES = (('Ongoing', 'Ongoing'), ('Completed', 'Completed'))

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name = models.CharField(max_length=512)
    image = models.ImageField(upload_to=rename_students, blank=True)
    degree = models.CharField(max_length=512, blank=True)
    type = models.CharField(choices=TYPES, max_length=64, default=TYPES[0][0])
    description = models.TextField(blank=True)

    def __str__(self):
        return self.faculty.name

    def _name(self):
        return self.name

    def _degree(self):
        return self.degree


class Misc(BaseModel):

    class Meta:
        verbose_name_plural = 'Miscellanous Details'

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    content = RichTextField()

    def __str__(self):
        return self.faculty.name
