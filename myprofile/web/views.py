
from django.conf import settings
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.conf import settings

from myprofile.web.models import(
    Website,
    SkillRate,
    Skill,
    FunProject
)


class WebsiteView(TemplateView):
    template_name = 'index.html'

    @property
    def webcontent_exists(self):
        website = Website.objects.all()
        if website.count() > 0:
            return True
        else:
            return False

    def get_context_data(self, **kwargs):
        context = super(WebsiteView, self).get_context_data(**kwargs)
        if self.webcontent_exists:
            context['website'] = Website.objects.latest('id')
        context['skill_ratings'] = SkillRate.objects.all()
        context['skills'] = Skill.objects.all()
        context['fun_projects'] = FunProject.objects.all()
        context['repo_url'] = settings.REPO_URL
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        name = request.POST.get('name', None)
        from_email = request.POST.get('email', None)
        message = request.POST.get('message', None)
        to_email = settings.WEBEMAIL

        body = '{}\n{}\n{}'.format(from_email, name, message)

        send_mail(
            'New message submitted from your web',
            body,
            from_email,
            [to_email],
            fail_silently=False)

        return super(TemplateView, self).render_to_response(context)


class PythonHubView(TemplateView):
    template_name = 'pythonhub.html'
