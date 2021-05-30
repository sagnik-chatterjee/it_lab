from django.shortcuts import render

# Create your views here.
from django import forms 


class InputForm(forms.Form):
    text = forms.CharField(max_length=200)

disabled = False 
failed_count =0 


def captcha(request):
    global disabled 
    global failed_count 
    form =InputForm()
    disabled = "First"

    if request.method == "POST":
        if request.POST['text'] !='PQJRYD':
            failed_count+=1
            disabled="Incorrect"
        else:
            failed_count =0 
            disabled = False 
        if failed_count ==3 :
            disabled = True 
            form.fields['text'].widget.attrs['readonly'] = disabled

    context= {
        'form' : form,
        'disabled':disabled,
        'attempts':3-failed_count
    }

    return render(request,'addn1/index.html',context)

