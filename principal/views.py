from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
def login_petition(request):
    """
    Handle the login petition.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponseRedirect or HttpResponse: The response object.

    """
    # Create an instance of the AuthenticationForm
    form = AuthenticationForm()

    if request.method == 'POST':
        # Get the form data from the POST request
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate the user
        access = authenticate(username=username, password=password)
        if access is not None:
            if access.is_active:
                # Log in the user
                login(request, access)
                # Redirect to the load_db view
                return HttpResponseRedirect('/load_db')
            else:
                # Redirect to the login page with an error message
                return redirect('/login?message=Tu cuenta no está activa&status=Error')
        else:
            # Redirect to the login page with an error message
            return redirect('/login?message=Usuario o contraseña incorrectos&status=Error')

    # Render the login.html template with the form
    return render(request, 'login.html', {'form': form})


@login_required(login_url='/login')
def load_data(request):
    # TODO: Llama al método populate DB de utils.py y obtén las entidades de la base de datos para luego mostrarlo.
    return render(request, 'load_data.html.html', context={'message': 'Data loaded successfully.'})

def load_recommendations(request):
    # TODO: Llama al método loadRS de utils.py y obtén las entidades de la base de datos para luego mostrarlo.
    return render(request, 'load_recommendations.html', context={'message': 'Recommendations loaded successfully.'})

def home(request):
    return render(request, 'home.html')