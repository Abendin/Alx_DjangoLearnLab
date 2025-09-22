from django.shortcuts import render
from .models import CustomUser
from .forms import ExampleForm   # ✅ Import ExampleForm as required
from django import forms

# Example search form to validate input
class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)

def user_list(request):
    """
    Securely fetch users with optional search.
    Avoids raw SQL by using Django ORM filtering.
    """
    form = SearchForm(request.GET or None)
    users = CustomUser.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get("query")
        if query:
            users = users.filter(username__icontains=query)

    return render(request, "bookshelf/user_list.html", {"form": form, "users": users})

def example_form_view(request):
    """
    View to handle ExampleForm securely.
    Includes CSRF protection and proper validation.
    """
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Normally you'd process the form data here
            cleaned_data = form.cleaned_data
            return render(request, "bookshelf/form_example.html", {
                "form": form,
                "success": True,
                "data": cleaned_data
            })
    else:
        form = ExampleForm()

    return render(request, "bookshelf/form_example.html", {"form": form})
