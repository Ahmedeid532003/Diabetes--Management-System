from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse 
from .models import client , DiabetesPatient


from clients.backends import CustomBackend  # Import your custom backend  




def home_page(request):
    return render(request, 'clients/index.html')


def info(request):
    return render(request, 'clients/info.html')

def DAT(request):
    return render(request, 'clients/D+T.html')
def ex(request):
    return render(request, 'clients/ex.html')
def inn(request):
    return render(request, 'clients/in.html')
def inside(request):
    return render(request, 'clients/inside.html')
def second_page(request):
    return render(request, 'clients/second_page.html')
def SECOND__PAGE(request):
    return render(request, 'clients/SECOND__PAGE.html')
def EnterDataYourself(request):
    return render(request, 'clients/EnterDataYourself.html')
def Survey(request):
    return render(request, 'clients/Survey.html')


def Data(request):
    if request.method == 'POST':
        # Extract data from the form
        full_name = request.POST.get('fullName')
        Dtype = request.POST.get('Type')
        age = request.POST.get('age')
        hba1c = request.POST.get('HbA1c')
        weight = request.POST.get('Weight')
        height = request.POST.get('Height')
        blood_pressure = request.POST.get('Pressure')
        cholesterol = request.POST.get('Cholesterol')
        gender = request.POST.get('gender')
        pregnant = request.POST.get('pregnant') == 'Yes'

        # Save data to the database
        DiabetesPatient.objects.create(
            full_name=full_name,
            Dtype=Dtype,
            age=age,
            hba1c=hba1c,
            weight=weight,
            height=height,
            blood_pressure=blood_pressure,
            cholesterol=cholesterol,
            gender=gender,
            pregnant=pregnant
        )
        return redirect('Survey')
    
    return render(request, 'clients/EnterDataYourself.html')




def login_page(request):
    return render(request, 'registration/login.html')




def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print("1  ",username,"2  ",password)
        user = CustomBackend().authenticate(request, username=username, password=password)
        print("123  ")
        print("user 12312331===== ",user)
        if user is not None:
            print(user)
            return redirect(reverse('home_page'))  # Replace with the URL for the success page
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
    return render(request, 'registration/login.html')

def register_user(request):
    if request.method == 'POST':
        # Extract form data from POST request
        UserName = request.POST.get('username')
        Name = request.POST.get('name')
        Password = request.POST.get('password')
        Email = request.POST.get('email')
        BirthDate=request.POST.get('birthdate')

        # Save the data to the database using the User model
        User = client(UserName=UserName, Name=Name, Password=Password, Email=Email,BirthDate=BirthDate)
        User.save()

        # Redirect to a success page or any other page after successful registration
        return redirect(reverse('login_page'))

    # If the request method is GET, render the registration form
    return render(request, 'clients/register.html')






