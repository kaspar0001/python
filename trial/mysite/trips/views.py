#from django.shortcuts import render

# Create your views here.

#############################################################

# trips/views.py

#from django.http import HttpResponse

#def hello_world(request):
#    return HttpResponse("Hello World!")

#############################################################

# trips/views.py

#from datetime import datetime
#from django.http import HttpResponse


#def hello_world(request):
#    output = """
#        <!DOCTYPE html>
#        <html>
#            <head>
#            </head>
#            <body>
#                Hello World! <em style="color:LightSeaGreen;">{current_time}</em>
#            </body>
#        </html>
#    """.format(current_time=datetime.now())
#
#    return HttpResponse(output)

#############################################################

# trips/views.py

from datetime import datetime
from django.shortcuts import render


def hello_world(request):
    return render(request, 'hello_world.html', {
        'current_time': datetime.now(),
    })

from .models import Post


def home(request):
    post_list = Post.objects.all()
    return render(request, 'home.html', {
        'post_list': post_list,
    })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})
