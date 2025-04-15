from django.shortcuts import render
from django.views.generic import TemplateView

from birthday.models import Birthday


class Homepage(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в словарь ключ total_count;
        # значение ключа — число объектов модели Birthday.
        context["total_count"] = Birthday.objects.count()
        return context
    


# def homepage(request):
#     return render(request, 'pages/index.html')
