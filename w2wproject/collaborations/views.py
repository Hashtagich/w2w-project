from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from brands.models.brand import Brand
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

class LikeListView(ListView):
    model = Like
    template_name = 'like_list.html'
    context_object_name = 'likes'

class MatchListView(ListView):
    model = Match
    template_name = 'match_list.html'
    context_object_name = 'matches'

class ChatDetailView(DetailView):
    model = Chat
    template_name = 'chat_detail.html'
    context_object_name = 'chat'

class MessageListView(ListView):
    model = Message
    template_name = 'message_list.html'
    context_object_name = 'messages'

class MessageDetailView(DetailView):
    model = Message
    template_name = 'message_detail.html'
    context_object_name = 'message'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def brand_add_view(request):
    if request.method == 'POST':
        return render(request, 'brand_add.html')

def brand_list_view(request):
    brands = Brand.objects.all()
    return render(request, 'brand_list.html', {'brands': brands})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('brand-list-with-likes')
    return render(request, 'login.html')

@login_required
def brand_list_with_likes_view(request):
    user = request.user
    user_brand = user.brand
    brands = Brand.objects.all()
    user_likes = Like.objects.filter(from_brand=user_brand)

    return render(request, 'brand_list_with_likes.html', {
        'brands': brands,
        'user_likes': user_likes,
    })

@login_required
def chat_detail_view(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    messages = chat.messages.all()
    return render(request, 'chat_detail.html', {'chat': chat, 'messages': messages})

@login_required
def send_message_view(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Message.objects.create(chat=chat, sender=request.user.brand, text=text)
    return redirect('chat-detail', chat_id=chat.id)
