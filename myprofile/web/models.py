from django.db import models
from django.core.exceptions import ValidationError

from django_markdown.models import MarkdownField


class BaseSkill(models.Model):
    class Meta:
        abstract = True

    def clean(self):
        """
        Throw ValidationError if you try to save more than skill limit count
        """
        model = self.__class__
        if (model.objects.count() == self.skill_limit and
                self.id != model.objects.get().id):
            raise ValidationError(
                "Can only create {} instances of {}." .format(
                    self.skill_limit, model.__name__))


class Website(models.Model):
    title = models.CharField(
        max_length=100,
        help_text="Website title"
        )
    about = MarkdownField()
    profile_img = models.ImageField(
        upload_to='uploads/img',
        help_text='profile picture')


class SkillRate(BaseSkill):
    skill_name = models.CharField(
        max_length=100,
        help_text='Your skill, eg. Python')
    rate = models.IntegerField(help_text="Skill level in %")

    skill_limit = 5


class Skill(BaseSkill):
    name = models.CharField(max_length=100)
    description = MarkdownField()

    skill_limit = 5


class FunProject(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100)
    description = MarkdownField()
    repo_url = models.URLField()


