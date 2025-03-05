from django.shortcuts import render

def calculator(request):
    result = None
    if request.method == "POST":
        try:
            expression = request.POST.get("expression", "")
            result = eval(expression)  # Evaluating the expression
        except Exception as e:
            result = "Error"
    return render(request, "calculator.html", {"result": result})