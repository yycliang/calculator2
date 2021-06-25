from .models import Calculation
from django.shortcuts import render, redirect
from .form import CalculationForm
Meta = CalculationForm.Meta


def calculate(request):
    if request.method == 'POST':
        form = CalculationForm(request.POST)
        operator = request.POST.get('operator')
        num_one = request.POST.get('num_one')
        num_two = request.POST.get('num_two')
        calc_date = request.POST.get('calc_date')
        if form.is_valid():
            if(operator == '+'):
                result = int(num_one) + int(num_two)
            elif(operator == '-'):
                result = int(num_one) - int(num_two)
            elif(operator == '*'):
                result = int(num_one) * int(num_two)
            else:
                result = int(num_one) / int(num_two)
            calculation = form.save(commit=False)
            calculation.result = result
            calculation.save()
            return redirect('results/')
    else:
        form = CalculationForm()
    return render(request, 'home.html', {'form': form})


def results(request):
    past = Calculation.objects.all()
    return render(request, 'results.html', {'past': past})
