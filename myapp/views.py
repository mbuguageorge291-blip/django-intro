from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def products(request):
    age = 45
    weight = 70
    subjects = ["Maths", "English", "Engineering", "Science"]
    isDisabled = False
    data = {'age': age, 'weight': weight, 'subjects': subjects, 'isDisabled': isDisabled}
    return render(request, 'products.html', data)



def about(request):
    return render(request, 'about.html')
