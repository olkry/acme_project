# from django.shortcuts import render, get_object_or_404, redirect
# from django.core.paginator import Paginator
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView)
from django.urls import reverse_lazy

from .forms import BirthdayForm
from .utils import calculate_birthday_countdown
from .models import Birthday


class BirthdayMixin:
    model = Birthday


'''
def birthday(request, pk=None):
    # if request.GET:
    #     form = BirthdayForm(request.GET)
    #     if form.is_valid():
    #         pass
    # else:
    #     form = BirthdayForm()
    # Если в запросе указан pk (если получен запрос на редактирование объекта):
    if pk is not None:
        # Получаем объект модели или выбрасываем 404 ошибку.
        instance = get_object_or_404(Birthday, pk=pk)
    # Если в запросе не указан pk (если получен запрос к странице создания):
    else:
        # Связывать форму с объектом не нужно, установим значение None.
        instance = None
    # Передаём в форму либо данные из запроса, либо None.
    # В случае редактирования прикрепляем объект модели.
    form = BirthdayForm(
        request.POST or None,
        # Файлы, переданные в запросе, указываются отдельно.
        files=request.FILES or None,
        instance=instance,
    )
    context = {'form': form}
    if form.is_valid():
        form.save()
        birthday_countdown = calculate_birthday_countdown(
            form.cleaned_data['birthday']
        )
        context.update({'birthday_countdown': birthday_countdown})

    return render(request, 'birthday/birthday.html', context)
'''


class BirthdayCreateView(BirthdayMixin, CreateView):
    # model = Birthday
    # # Этот класс сам может создать форму на основе модели!
    # # Нет необходимости отдельно создавать форму через ModelForm.
    # # Указываем поля, которые должны быть в форме:
    # # fields = '__all__'
    # # Указываем имя формы если она созана с виджетами и клинами:
    # form_class = BirthdayForm
    # template_name = 'birthday/birthday.html'
    # # Указываем namespace:name страницы,куда будет перенаправлен пользователь
    # # после создания объекта:
    # success_url = reverse_lazy('birthday:list')
    form_class = BirthdayForm


class BirthdayUpdateView(BirthdayMixin, UpdateView):
    # model = Birthday
    # form_class = BirthdayForm
    # template_name = 'birthday/birthday.html'
    # success_url = reverse_lazy('birthday:list')
    form_class = BirthdayForm


'''
def birthday_list(request):
    birthdays = Birthday.objects.order_by('id')
    paginator = Paginator(birthdays, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'birthday/birthday_list.html', context)
'''


class BirthdayListView(ListView, BirthdayMixin):
    # model = Birthday
    ordering = 'id'
    paginate_by = 3


'''
def delete_birthday(request, pk):
    instance = get_object_or_404(Birthday, pk=pk)
    # В форму передаём только объект модели;
    # передавать в форму параметры запроса не нужно.
    form = BirthdayForm(instance=instance)
    context = {'form': form}
    # Если был получен POST-запрос...
    if request.method == 'POST':
        # ...удаляем объект:
        instance.delete()
        # ...и переадресовываем пользователя на страницу со списком записей.
        return redirect('birthday:list')
    return render(request, 'birthday/birthday.html', context)
'''


class BirthdayDeleteView(BirthdayMixin, DeleteView):
    # model = Birthday
    success_url = reverse_lazy('birthday:list')


class BirthdayDetailView(DetailView):
    model = Birthday

    def get_context_data(self, **kwargs):
        # Получаем словарь контекста:
        context = super().get_context_data(**kwargs)
        # Добавляем в словарь новый ключ:
        context['birthday_countdown'] = calculate_birthday_countdown(
            # Дату рождения берём из объекта в словаре context:
            self.object.birthday
        )
        return context

