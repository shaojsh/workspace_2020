import logging

# import simplejson
import os

from django.http import JsonResponse, HttpRequest, HttpResponseRedirect, StreamingHttpResponse
from django.shortcuts import render, HttpResponse

from application import music

from .models import BlogPost


# Create your views here.

# def reg(request: HttpRequest):
#     try:
#         # payload = json.loads(request.body.decode())
#         payload = simplejson.loads(request.body)
#         email = payload['email']
#         # 数据库中查看Email有没有
#         qs = User.objects.filter(email=email)
#         print(qs.query, '---------------')
#         if qs:  # email已经存在了
#             return HttpResponseBadRequest()
#         name = payload['name']
#         password = payload['password']
#         print(email, name, password)
#         logging.info(email)
#         user = User()
#         user.email = email
#         user.password = password
#         user.name = name
#
#         try:
#             user.save()
#             return JsonResponse({'user_id': user.id})
#         except Exception as e:
#             raise
#     except Exception as e:
#         logging.info(e)
#     return HttpResponseBadRequest()


def index(request: HttpRequest):
    return render(request, 'index.html')


def aboutme(request: HttpRequest):
    return render(request, 'about.html')


def searchBlogPost(request):
    if request.method == "GET":
        keyworld = request.GET.get("keyword")
        blogNetList = BlogPost.objects.filter(des__contains=keyworld)
        return render(request, "blog-post.html", {"blogNetList": blogNetList})


def blogPostKogou(request: HttpRequest):
    return render(request, 'blogDel-kugou.html')


def ajax_song(request):
    if request.is_ajax():
        song = request.GET.get("song")
        music.get_song(song)

        return JsonResponse({'content': "这是ajax请求"})
    else:
        return JsonResponse({'content': "这是假的ajax请求"})


def blogPost(request: HttpRequest):
    blogNetList = BlogPost.objects.all()  # 将数据全部展示至html中
    return render(request, "blog-post.html", {"blogNetList": blogNetList})


def delete_class(request: HttpRequest):
    if request.method == "GET":  # 请求方法为POST时，进行处理
        delId = request.GET.getlist('id')
        delId = delId.__getitem__(0)
        BlogPost.objects.filter(id=delId).delete()
        blogNetList = BlogPost.objects.all()  # 将数据全部展示至html中
        return render(request, "blog-post.html", {"blogNetList": blogNetList})


def uploadFiles(request: HttpRequest):
    if request.method == "POST":  # 请求方法为POST时，进行处理
        myFile = request.FILES.get("myfile", None)  # 获取上传的文件，如果没有文件，则默认为None
        des = request.POST.get('des')
        if not myFile:
            blogNet = request.POST.get('blogNet')
            if not blogNet:
                return HttpResponse("no files or no blogNet for upload!")
            else:
                BlogPost.objects.create(  # 执行插入语句.网址
                    type=0,
                    blogNet=blogNet,
                    des=des
                )
            blogNetList = BlogPost.objects.all()  # 将数据全部展示至html中
            return render(request, "blog-post.html", {"blogNetList": blogNetList})

        # 执行插入语句文件
        BlogPost.objects.create(  # 执行插入语句
            type=1,
            blogNet=myFile.name,
            des=des
        )

        blogNetList = BlogPost.objects.all()  # 将数据全部展示至html中,逆序排列
        destination = open(os.path.join("E:\\upload", myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        return render(request, "blog-post.html", {"blogNetList": blogNetList})


def downloadFiles(request: HttpRequest):
    if request.method == "GET":  # 请求方法为POST时，进行处理
        typeFile = request.GET.getlist('type')
        cv = 'MyCV.doc'
        if not typeFile:
            file = open('E:\\upload\\' + cv, 'rb')
            response = StreamingHttpResponse(file)
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename =' + cv
            return response
        data = request.GET.getlist('data')
        if typeFile[0] == '1':
            file = open('E:\\upload\\' + data[0], 'rb')
            response = StreamingHttpResponse(file)
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename =' + data[0]
            return response
        else:
            return HttpResponseRedirect(data[0])
