from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django import forms

from .models import Photo, PhotoComment


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
    queryset = Photo.objects.order_by('-created_date')
    # queryset = Photo.objects.filter('-created_date')



@method_decorator(login_required, name='dispatch')
class PhotoAdd(CreateView):
    model = Photo
    fields = ['photo', 'content',]
    template_name = 'photo/photo_add.html'
    # success_url = '/photo/list'
    success_url = reverse_lazy('photo:photo_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




class CommentAddForm(forms.Form):
    reply = forms.CharField(widget=forms.Textarea, required=True)



class PhotoDetail(View):
    def get(self, request, *args, **kwargs):
        view = PhotoDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        pass


# get
class PhotoDisplay(DetailView):
    template_name = 'photo/photo_detail.html'
    model = Photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = PhotoComment.objects.filter(photo=self.object.pk)
        context['form'] = CommentAddForm()
        # context['form'] =
        return context



# post
class CommentCreate(CreateView):
    model = PhotoComment
    fields = ['reply']

    # 'photo', 'author',

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.photo  = self.object

