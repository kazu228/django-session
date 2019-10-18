from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .forms import kakikomiForm
# Create your views here.

def kakikomi(request):
    if request.method == 'GET': #確認画面から戻った時
        f = kakikomiForm(request.session.get('form_data'))
    else:  #基本的にはPOST、送信ボタンを押した時
        f = kakikomiForm(request.POST)
        if f.is_valid:  #ヴァリデーションチェック
            request.session['form_data'] = request.POST
            return redirect('djapp:user_data_confirm')
    return render(request, 'djapp/index.html', {'form1': f})


def user_data_confirm(request):
    session_form_data = request.session.get('form_data')
    if session_form_data is None:
        return redirect('djapp:kakikomi')
    
    context = {
        'form': kakikomiForm(session_form_data)
    }
    return render(request, 'djapp/user_data_confirm.html', context)
