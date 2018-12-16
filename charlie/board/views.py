from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse




#from django.template import loader

#def detail(request):
#    template = loader.get_template(template_name='index.html')
#    context = {
#        'title': 'Untitled',
#        'content': None,
#    }
#    return HttpResponse(template.render(context, request))


from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist
from .models import Post

class DetailView(TemplateView):
    template_name = "content.html"

    def get_context_data(self, **kwargs):
        #return {'title': 'Untitled', 'content': None }

        try:
            #p = Post.objects.get(pk=self.request.GET.get('id'))
            p = Post.objects.get(pk=kwargs.get('id', None))
            return{ 'title': p.title, 'content': p.content }
        except ObjectDoesNotExist:
            return{ 'title': '없는 게시물 입니다.', 'content': None }

from django.shortcuts import redirect

class PostCreateView(TemplateView):
    template_name = "create.html"

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        author = request.POST.get('author')
        content = request.POST.get('content')

        if title and author and content:
            p = Post.objects.create(
                title=title,
                author=author,
                content=content
            )
            return redirect(f"/detail/{p.pk}")
        else:
            return HttpResponse("<h1>Please fill in all fields.</h1>\n"+
            '<a href="./"Return</a>')

class IndexView(TemplateView):
    template_name = "index.html"

    def index(request):
        return HttpResponse("<h1>Hello World!</h1>")
