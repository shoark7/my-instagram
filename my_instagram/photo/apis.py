from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Photo
from member.models import MyUser
import json


@csrf_exempt
def photo_add(request):
    data = request.POST
    files = request.FILES

    user_id = data['user_id']
    content = data['content']
    image = files['photo']

    author = MyUser.objects.get(id=user_id)
    photo = Photo.objects.create(
        photo=image,
        author=author,
        content=content,
    )
    print(data, files)
    # return HttpResponse(
    #     json.dumps(photo.to_dict()),
    #     content_type='application/json'
    # )
    return HttpResponse(
        json.dumps(photo.to_dict()),
        content_type='application/json'
    )