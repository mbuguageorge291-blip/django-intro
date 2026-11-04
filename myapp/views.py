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
    scores=[{"name":"Ira Hoffman","English":68,"Math":37,"Science":7,"History":27},{"name":"Cailin Romero","English":56,"Math":53,"Science":38,"History":40},{"name":"Orli Rivas","English":31,"Math":21,"Science":82,"History":81},{"name":"Nolan Davis","English":78,"Math":54,"Science":8,"History":67},{"name":"Garrison Roach","English":54,"Math":32,"Science":53,"History":49},{"name":"Barry Pitts","English":32,"Math":7,"Science":87,"History":5},{"name":"Reagan Roberts","English":36,"Math":74,"Science":32,"History":56},{"name":"Bertha Barry","English":52,"Math":80,"Science":28,"History":67},{"name":"Deirdre Levine","English":55,"Math":59,"Science":76,"History":45},{"name":"Stephanie Briggs","English":70,"Math":66,"Science":53,"History":69}]
    data={'scores': scores}
    return render(request, 'about.html', data)
