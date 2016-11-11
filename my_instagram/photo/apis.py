def photo_add(request):
    data = request.POST
    files = request.FILES

    print(data, files)