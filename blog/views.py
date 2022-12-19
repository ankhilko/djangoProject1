from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_GET
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from .models import Post, Contact
from .forms import ContactForm
# Create your views here.



class BaseMixin:
    context = {
        'twitter': 'https://twitter.com',
        'facebook': 'https://facebook.com',
        'github': 'https://github.com',
    }

    # def get_mixin(self):
    #     return {}

class PostListView(BaseMixin, ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()    # перегружаем родительский метод, дополняем его (полиморфизм)
        context['heading'] = 'MIXIN HEADING'
        context['subheading'] = 'mixin subheading'
        context.update(self.context)
        # context.update(self.get_mixin)
        return context


class PostDetailView(BaseMixin, DetailView):
    template_name = 'blog/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'
    model = Post
    # slug_field = 'slug'      # если у нас несколько слагов или другое название

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()    # перегружаем родительский метод, дополняем его (полиморфизм)
        context.update(self.context)
        return context



class AboutTemplateView(BaseMixin, TemplateView):
    template_name = 'blog/about.html'
    context_object_name = 'about'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()    # перегружаем родительский метод, дополняем его (полиморфизм)
        context.update(self.context)
        context['heading'] = 'ABOUT'
        context['coordinate'] = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2350.682974602827!2d27.547051915390377!3d53.90183854065862!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x46dbcfe95955c31b%3A0xb360ae59fb52db5d!2sFaberlik%20Nemiga%205!5e0!3m2!1sen!2sby!4v1671128792219!5m2!1sen!2sby'
        context['text'] = '''
        ABOUT ABOUT ABOUT ABOUT ABOUT ABOUT
        ABOUT ABOUT ABOUT ABOUT ABOUT ABOUT
        ABOUT ABOUT ABOUT ABOUT ABOUT ABOUT
        ABOUT ABOUT ABOUT ABOUT ABOUT ABOUT
        '''
        return context


class ContactCreateView(BaseMixin, CreateView):
    template_name = 'blog/contact.html'
    context_object_name = 'contact'
    model = Contact

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()    # перегружаем родительский метод, дополняем его (полиморфизм)
        context.update(self.context)
        return context






@require_GET
def blog_list(request: HttpRequest):            #функция представления - обрабатывает все запросы
    posts_list = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts_list})   # не дано передвать папку тэплейт - он автоматом там ищет
    # передаем параметры в документ {'posts': posts_list}, 'a': 'a')   # не дано передвать папку тэплейт - он автоматом там ищет


def post_detail(request: HttpRequest, post_slug: str):
    post = get_object_or_404(Post, slug=post_slug)
    # post = Post.objects.get(slug=post_slug)
    return render(request, 'blog/post.html', {'post': post})




def contact(request: HttpRequest):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'blog/contact.html', {'contact_form': ContactForm})


def about(request: HttpRequest):
    return render(request, 'blog/about.html')


def error404(request, exception):                       # settings -> debug -> False
    return render(request, 'blog/error_404.html')

