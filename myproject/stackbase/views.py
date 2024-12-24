from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from .models import Question, Comment
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .forms import CommentForm
from django.urls import reverse, reverse_lazy
class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    ordering =  ['-date_created']
    
class QuestionDetailView(DetailView):
    model = Question
        
class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question   
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class QuestionUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Question   
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def test_func(self):
        questions = self.get_object()
        if self.request.user == questions.user:
           return True
        return False        
    
class QuestionDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Question
    context_object_name = 'questions'
    success_url = "stackbase:question_list"   
    def test_func(self):
        questions = self.get_object()
        if self.request.user == questions.user:
           return True
        return False     

class CommentDetailView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'stackbase/question_detail.html'
    
    def form_valid(self, form):
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('stackbase:question_detail')


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'stackbase/question_answer.html'
        
    def form_valid(self, form):
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('stackbase:question_lists')


