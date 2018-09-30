from django.views import generic

class Error404(generic.TemplateView):
    template_name = '404.html'

class Error400(generic.TemplateView):
    template_name = '400.html'

class Error500(generic.TemplateView):
    template_name = '500.html'