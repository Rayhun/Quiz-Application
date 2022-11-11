from django.db import models
from django.conf import settings


class AbstractModel(models.Model):
    created_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_created',
        null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_updated',
        null=True, blank=True
    )
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    deleted_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_deleted',
        null=True, blank=True
    )
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True, null=True)
    is_delete = models.BooleanField(default=False, null=True)
    order = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        abstract = True


class Section(AbstractModel):
    image = models.ImageField(
        blank=True, null=True, upload_to='sections/%Y/%m/%d'
    )
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=50, blank=True, null=True, unique=True)

    def __str__(self) -> str:
        return self.name


class Question(AbstractModel):
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_question'
    )
    question = models.CharField(max_length=255)
    number = models.DecimalField(default=0.00, decimal_places=2, max_digits=5)
    image = models.ImageField(
        blank=True, null=True, upload_to='questions/%Y/%m/%d'
    )

    def __str__(self) -> str:
        return self.question


class Answer(AbstractModel):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_answer'
    )
    answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.answer
