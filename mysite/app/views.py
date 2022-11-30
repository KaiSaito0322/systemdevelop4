from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.db.models import Q

from .models import Top, ListOf


class TopView(generic.ListView):
    template_name = 'app/TOP.html'
    context_object_name = 'latest_top_list'

    # タイトルの逆順に並び替えて最新の５つを表示
    # def get_set(self):
    #     return Top.objects.order_by('-id')[:3]

    # 検索機能
    def get_queryset(self):
        q_word = self.request.GET.get('query')

        if q_word:
            object_list = Top.objects.filter(Q(title__icontains=q_word))
        else:
            object_list = Top.objects.all()
        return object_list


class ReplyView(generic.DetailView):
    model = Top
    template_name = 'app/reply.html'


class ListView(generic.DetailView):
    model = Top
    template_name = 'app/List_of.html'


def DetailView(request, top_id, listof_id):
    listof = get_object_or_404(ListOf, pk=listof_id)
    return render(request, 'app/notice.html', {"listof": listof})

