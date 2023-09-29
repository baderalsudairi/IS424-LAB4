from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


tax_rate = 0.15

def default_view(request):
    return render(request, 'tax_calculator/default.html')

def calculate_tax(request, number):
    try:
        
        number = float(number)
        total_price = number + (number * tax_rate)
        return HttpResponse(f'Total Price after {tax_rate * 100}% tax: ${total_price:.2f}')
    except ValueError:
        return HttpResponse('Invalid input. Please provide a valid number.')

def tax_rate_view(request):
    return render(request, 'tax_calculator/tax_rate.html')
