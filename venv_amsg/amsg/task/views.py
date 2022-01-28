from email import message
from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from accounts.models import *
from task.models import *
from .forms import *
from django.http import HttpResponse

import random,string


# Create your views here.
class ToppageView(generic.TemplateView):
    template_name = "toppage.html"


class UserListView(generic.ListView):
    model = CustomUser
    template_name = "user_list.html"

    def get_queryset(self):
        return CustomUser.objects.all()


# ユーザー登録view
class UserCreateView(generic.CreateView):
    model = CustomUser
    template_name = "user_create.html"
    form_class = UserCreateForm
    success_url = reverse_lazy('task:user_list')

    def form_valid(self,form):
        obj = form.save(commit=False)
        # 作成時に紐づける
        obj.user_school = self.request.user.user_school
        
        # ランダム文字列生成
        randlst = [random.choice(string.ascii_letters + string.digits) for i in range(10)]
        random_string =  ''.join(randlst)
        print("************************")
        print(random_string)
        print("************************")
        obj.set_password(random_string)
        
        obj.save()
        messages.success(self.request,'ユーザーを作成しました。')
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,'失敗しました。')
        return super().form_invalid(form)


class UserInfoView(generic.DetailView):
    model = CustomUser
    template_name = 'user_info.html'


class UserEditView(generic.UpdateView):
    model = CustomUser
    template_name = 'user_edit.html'
    form_class = UserEditForm

    def get_success_url(self):
        return reverse_lazy('task:user_info',kwargs={'pk':self.kwargs['pk']})

    def form_valid(self,form):
        messages.success(self.request,'ユーザーの名前を変更しました')
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,'編集に失敗しました')
        return super().form_invalid(form)


class ClassListView(generic.ListView):
    model = Class
    template_name = 'class_list.html'

    def get_queryset(self):
        return Class.objects.all()


class ClassCreateView(generic.CreateView):
    model = Class
    template_name = "class_create.html"
    form_class = ClassCreateForm
    success_url = reverse_lazy('task:class_list')

    def form_valid(self,form):
        obj = form.save(commit=False)
        # 作成時に紐づける
        obj.class_school = self.request.user.user_school

        obj.save()
        messages.success(self.request,'クラスを作成しました。')
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,'失敗しました。')
        return super().form_invalid(form)


# studentの一覧が表示されてません
# get_context_data使えばできると思う
class ClassInfoView(generic.DetailView):
    model = Class
    template_name = "class_info.html"


class ClassEditView(generic.UpdateView):
    model = Class
    template_name = 'class_edit.html'
    form_class = ClassCreateForm

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['stu_list'] = CustomUser.objects.filter(
            user_school=self.request.user.user_school,
            user_auth='3'
            )
        return context

    def post(self,request,*args,**kwargs):
        pk_list = request.POST.getlist('add') # postで送られてきた生徒データがlist状でpk_listに格納される
        # classinfoで使ったpkのクラスのインスタンスが欲しい -> get
        # self.kwargs['pk'] = 2
        class_data = Class.objects.get(id=self.kwargs['pk']) #現在編集してるClassインスタンスのidを取得

        # 送られてきたstudentのidを一つずつ取り出し、それを使ってStudentインスタンス取得
        # studentインスタンスのuser_class情報に現在編集してるクラスのインスタンスを指定する
        # studentインスタンスを保存
        for stu_pk in pk_list:
            student = CustomUser.objects.get(id=stu_pk)
            student.user_class = class_data
            student.save()
        
        return HttpResponse('')

    def get_success_url(self):
        return reverse_lazy('task:class_info',kwargs={'pk':self.kwargs['pk']})


class TaskListView(generic.ListView):
    model = Task
    template_name = "task_list.html"

    def get_queryset(self):
        tasks = Task.objects.filter(task_school=self.request.user.user_school)
        return tasks


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "task_create.html"
    form_class = TaskCreateForm
    success_url = reverse_lazy('task:task_list')

    def form_valid(self,form):
        obj = form.save(commit=False)
        # 作成時に紐づける
        obj.task_school = self.request.user.user_school
        obj.save()
        messages.success(self.request,'ユーザーを作成しました。')
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,'失敗しました。')
        return super().form_invalid(form)


class TaskInfoView(generic.DetailView):
    model = Task
    template_name = 'task_info.html'


class TaskEditView(generic.UpdateView):
    model = Task
    template_name = 'task_edit.html'
    form_class = TaskCreateForm

    def get_success_url(self):
        return reverse_lazy('task:task_info',kwargs={'pk':self.kwargs['pk']})


class QuestionListView(generic.ListView):
    model = Question
    template_name = "question_list.html"

    def get_queryset(self):
        questions = Question.objects.filter(q_school=self.request.user.user_school)
        return questions


class QuestionCreateView(generic.CreateView):
    model = Question
    template_name = "question_create.html"
    form_class = QuestionCreateForm
    success_url = reverse_lazy('task:question_list')

    def form_valid(self,form):
        obj = form.save(commit=False)
        # 作成時に紐づける
        obj.q_school = self.request.user.user_school
        obj.save()
        messages.success(self.request,'を作成しました。')
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,'失敗しました。')
        return super().form_invalid(form)


class QuestionInfoView(generic.DetailView):
    model = Question
    template_name = 'question_info.html'


class QuestionEditView(generic.UpdateView):
    model = Question
    template_name = 'question_edit.html'
    form_class = QuestionCreateForm

    def get_success_url(self):
        return reverse_lazy('task:question_info',kwargs={'pk':self.kwargs['pk']})


class TaskSetView(generic.UpdateView):
    model = Task
    template_name = 'task_set.html'
    form_class = TaskSetForm

    # task_set.htmlで配布先クラスを表示できるように get_context_data 使う
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['class_list'] = Class.objects.filter(
            class_school=self.request.user.user_school
            )
        return context

    # 選択されたクラスに配布する    
    def post(self,request,*args,**kwargs):
        pk_list = request.POST.getlist('distribute') # postで送られてきたclass_idをlist状でpk_listに格納
        task_data = Task.objects.get(id=self.kwargs['pk']) #現在編集してるTaskインスタンスのidを取得

        # Distribution.objects.create(task_obj,class_obj)
        # 配布する課題とクラスを Distributionクラスと紐づける
        for class_pk in pk_list:
            class_data = Class.objects.get(id=class_pk)
            # create()だけでDistributionオブジェクトを作成して保存できる
            distribution = Distribution.objects.create(distribute_task=task_data, distribute_class=class_data)
            print("********************")
            print(distribution.distribute_task)
            print(distribution.distribute_class)
            print("********************")
            # 課題クラスのstatusを公開にする
            task_data.task_status = '1'
            task_data.save()
        
        return HttpResponse('')


class PossibleTaskListView(generic.ListView):
    model = Task
    template_name = 'possible_task_list.html'

    # 自分のクラスが Distributionクラスで紐づけられている Taskを見たい
    # 自分のクラス情報 -> class_data = user.user_class
    # Distributionクラスで紐づいてるTaskのクエリ情報
    #   -> task_query = Distribution.objects.filter(distribute_class=class_data)