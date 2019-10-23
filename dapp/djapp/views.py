from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .forms import kakikomiForm
from .models import kakikomiModel
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.

def kakikomi(request):
    if request.method == 'GET': #確認画面から戻った時
        f = kakikomiForm(request.session.get('form_data'))
    else:  #基本的にはPOST、送信ボタンを押した時
        f = kakikomiForm(request.POST)
        if f.is_valid:  #ヴァリデーションチェック
            request.session['form_data'] = request.POST
            # POSTで受けたデータをセッションに書き込む
            return redirect('djapp:user_data_confirm')
    return render(request, 'djapp/index.html', {'form1': f})


def user_data_confirm(request):
    session_form_data = request.session.get('form_data')
    # セッションデータを代入
    if session_form_data is None:
        return redirect('djapp:kakikomi')
    
    context = {
        'form': kakikomiForm(session_form_data)
        # フォーム形式で出力するため
    }
    return render(request, 'djapp/user_data_confirm.html', context)

# def user_data_create(request):
#     session_form_data = request.session.pop('form_data', None)
#     # セッションを空にして取り出す

#     if session_form_data is None:
#         return redirect('djapp:user_data_input')

#     form = kakikomiForm(session_form_data)
    
#     form.save()
#     return redirect('djapp:user_list')
class user_data_create(generic.CreateView):
    model = kakikomiModel

    form_class = kakikomiForm
#     success_url = reverse_lazy('user_list')
    # context = {
    #     'form': form
    # }
    # return render(request, 'djapp/user_data_input.html', context)

# class UserList(generic.ListView):
#     model = kakikomiModel
#     template_name = "user_list.html"
