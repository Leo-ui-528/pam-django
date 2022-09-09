from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Bb, Owner
from django.views.generic.edit import CreateView
from .forms import BbForm
from django.urls import reverse_lazy


class BbCreateView(CreateView):
    template_name = 'create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['owners'] = Owner.objecs.all()
    return context


def by_owner(request, owner_id):
    bbs = Bb.objects.filter(owner=owner_id)
    owners = Owner.objects.all()
    current_owner = Owner.objects.get(pk=owner_id)
    context = {'bbs': bbs, 'owners': owners, 'current_owner': current_owner}
    return render(request, 'by_owner.html', context)


def index(request):
    bbs = Bb.objects.all()
    owners = Owner.objects.all()
    context = {'bbs': bbs, 'owners': owners}
    return render(request, 'index1.html', context)

    # фильтр по дате:
    # s = 'Список обновлений\r\n\r\n\r\n'
    # for bb in Bb.objects.order_by('-published'):
    #     s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    # return HttpResponse(s, content_type='text/plain; charset=utf-8')
