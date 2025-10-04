from django.shortcuts import render
def rectarea(request):
    context = {}
    context['area'] = ""
    context['l'] = ""
    context['b'] = ""
    if request.method == 'POST':
        print("POST method is used")
        l = request.POST.get('length', '0')
        b = request.POST.get('breadth', '0')
        print('request', request)
        print("Length=", l)
        print("Breadth=", b)
        area = int(l) * int(b)
        context['area'] = area
        context['l'] = l
        context['b'] = b
        print('Area', area)
    return render(request, 'mathapp/math.html', context)