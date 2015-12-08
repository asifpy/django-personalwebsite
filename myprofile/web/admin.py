from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin

from myprofile.web.models import(
    Website,
    SkillRate,
    Skill,
    FunProject
)


admin.site.register(Website, MarkdownModelAdmin)
admin.site.register(Skill)
admin.site.register(SkillRate)
admin.site.register(FunProject)
