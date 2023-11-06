from django.shortcuts import render
from .forms import MyForm
from .cleaner import excess_remover
import pandas as pd
import pickle
pickled_Model = pickle.load(open('Model_Lr_Tweets2023.pkl', 'rb'))

# Create your views here.
def face(request):
    if request.method == 'POST':
        form_instance = MyForm(request.POST)
        if form_instance.is_valid():
            text = form_instance.cleaned_data.get('text')
            data = {'text': text}
            twisted = pd.Series(excess_remover(data.get('text')))
            prediction = pickled_Model.predict(twisted)
            response = 'a disaster tweet.' if prediction else 'not a disaster tweet.'
            output = f"This is {response}"
            return render(request, 'frontapp/main.html', {'that_form': MyForm(), 'data': data, 'prediction':output})
        else:
            return render(request, 'frontapp/main.html', {'that_form': MyForm()})
        
    else:
        return render(request, 'frontapp/main.html', {'that_form': MyForm()})

    
def contact(request):
    return render(request, 'frontapp/contact.html', {})