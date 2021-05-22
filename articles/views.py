from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Article, Comment


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ('title', 'body',)

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = {'title', 'body'}

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'article_comment.html'
    fields = {'article', 'comment', 'author'}



