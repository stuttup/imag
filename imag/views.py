from django.views import generic


class HomePage(generic.TemplateView):
    template_name = "pages/home.html"


class AboutPage(generic.TemplateView):
    template_name = "pages/about.html"
