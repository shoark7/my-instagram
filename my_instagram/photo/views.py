from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .models import Photo
# from django.views.generic import ListView
# Create your views here.

# def photo_list(request):
#     photos = Photo.objects.all()
#     context = {
#         'photos': photos,
#     }
#     return render(request, 'photo/photo_list.html', context)


class PhotoList(ListView):
    model = Photo
    paginate_by = 5
    context_object_name = 'photos'
    # queryset = Photo.objects.filter('-created_date')


class PhotoAdd(CreateView):
    model = Photo
    fields = ['photo', 'author', 'content',]
    template_name = 'photo/photo_add.html'
    success_url = '/photo/list'

    # def form_valid(self, form):