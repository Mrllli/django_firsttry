from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from educoderapp.models import BookInfo,Register
from django.contrib import auth
from django import forms

'''def show_arg(request,id):
    return HttpResponse('show arg %s'%id)'''

'''def show_test(request):
	return render(request,'educoderapp/test_get.html')'''

'''def sub(request):
	a=request.GET.get('your_name')
	return redirect('/')'''

def index_sec(request):
    username = request.session.get("username", None)
    return render(request, 'educoderapp/index_sec.html', context={"username": username})

def logout(request):
    request.session.flush()
    return redirect('/')




def hello(request):
	return HttpResponse("Hello Educoder")


def index(request):

    return render(request, 'educoderapp/index.html')

def register1(request):
    return render(request, 'educoderapp/register.html')

def login1(request):
    return render(request, 'educoderapp/login.html')

# 创建新图书
'''def create2(request):
    book = BookInfo()
    book.btitle = request.POST.get('btitle')  # 获取书名
    book.bpub_date = request.POST.get('bpub_date')  # 获取出版日期
    book.save()
    # 转向到首页
    return HttpResponseRedirect('/')'''


'''def delete(request,ID):
    book=BookInfo.objects.get(id=int(ID))
    book.delete()
    #转向到首页
    return redirect(reverse('educoderapp:index'))'''


class Userform(forms.Form):
	username = forms.CharField(label="用户名")
	password = forms.CharField(label="密码")
	phonenumber = forms.CharField(label = "电话号码")

class Userform_login(forms.Form):
	username = forms.CharField(label="用户名")
	password = forms.CharField(label="密码")

def register(request):
	form_obj = Userform()
	if request.method == "POST":
		form_obj = Userform(request.POST)
		if form_obj.is_valid():
			username = form_obj.cleaned_data['username']
			password = form_obj.cleaned_data['password']
			phonenumber = form_obj.cleaned_data['phonenumber']

			Register.objects.create(username=username,password=password,phonenumber=phonenumber)

			return render_to_response('educoderapp/success.html')


	else:
		return HttpResponse("注册失败")

def login(request):
	if request.method == 'POST':
		userform = Userform_login(request.POST)
		if userform.is_valid():
			username = userform.cleaned_data['username']
			password = userform.cleaned_data['password']

			user = Register.objects.filter(username__exact=username,password__exact=password)

			if user:
				request.session['username'] = username
				username = request.session.get("username", None)
				request.session.set_expiry(0)
				return render(request, 'educoderapp/index_sec.html', context={"username": username})
			else:
				return render_to_response('educoderapp/login.html')

	else:
		userform = Userform()
	return HttpResponse("发生了一些错误")