from django.shortcuts import render , redirect
from .models import Expense
from .forms import ExpenseModelForm
# Create your views here.

def index(request):

    expense = Expense.objects.all()  #查詢所有資料
    #變數名稱  #資料表名稱

    form = ExpenseModelForm()

    if request.method == "POST":
        form = ExpenseModelForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect("/expenses")

    context = {
        'expenses': expense,
        'form': form
    }

    return render(request, 'expenses/index.html', context)
    

def update(request, pk):  # pk:參數

    expense = Expense.objects.get(id=pk)

    form = ExpenseModelForm(instance=expense)

    if request.method == 'POST':
        form = ExpenseModelForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
        return redirect('/expenses')

    context = {
        'form': form
    }

    return render(request, 'expenses/update.html', context)


def delete(request, pk):

    expense = Expense.objects.get(id=pk)

    if request.method == "POST":
        expense.delete()
        return redirect('/expenses')

    context = {
        'expense':expense
    }

    return render(request, 'expenses/delete.html', context)

