from django.shortcuts import get_object_or_404, render
from ice_cream.models import IceCream


def ice_cream_detail(request, pk):
    template = 'ice_cream/detail.html'
    ice_cream = get_object_or_404(
        IceCream.objects.filter(
            is_published=True,
            category__is_published=True
        ), id=pk
    )
    context = {'ice_cream': ice_cream}
    return render(request, template, context)


def ice_cream_list(request):
    template = 'ice_cream/list.html'
    ice_cream_catalog = IceCream.objects.select_related(
        'category'
    ).filter(
        is_published=True,
        category__is_published=True
    ).order_by('category')
    context = {'ice_cream_list': ice_cream_catalog}
    return render(request, template, context)
