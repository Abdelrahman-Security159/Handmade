from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_auth
from django.contrib.auth.hashers import make_password
from django.contrib import messages  # For displaying error/success messages
from django.shortcuts import render, get_object_or_404, redirect

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Shop, Product

from . import models

# Home Page View
def index(request):
    return render(request, 'index.html')

# Login View
def login(request):
    if request.method == "POST":
        # Retrieve form data
        username = request.POST.get('username')  # Use POST.get() to safely retrieve data
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Log in the user
            login_auth(request, user)

            # Redirect based on user role
            if user.role == 'owner':
                return redirect('owner:owner_dashboard')  # Redirect to owner dashboard
            elif user.role == 'user':
                return redirect('user:user_dashboard')  # Redirect to user dashboard
            else:
                return redirect('login')  # Default redirect
        else:
            # Display error message for invalid credentials
            messages.error(request, "Invalid username or password.")
            return render(request, 'auth/login.html')

    # Render login page for GET requests
    return render(request, 'auth/login.html')

# Register View
def register(request):
    if request.method == "POST":
        # Retrieve form data
        first_name = request.POST.get('first-name')
        middle_name = request.POST.get('middle-name', '') 
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        phone = request.POST.get('phone')
        role = request.POST.get('role') 

        # Validate password confirmation
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'auth/register.html')

        # Check if the email is already registered
        if models.User.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered.")
            return render(request, 'auth/register.html')

        try:
            user = models.User(
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
                email=email,
                password=make_password(password),  
                phone=phone,
                role=role,
            )
            user.save()

            # Display success message
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login') 
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return render(request, 'auth/register.html')

    # Render registration page for GET requests
    return render(request, 'auth/register.html')

@login_required
def owner_dashboard(request):
    # Ensure only owners can access this view
    if request.user.role != 'owner':
        return redirect('login')  # Redirect unauthorized users to login
    # services = Product.objects.filter(owner_id=request.user)

    # Fetch all shops owned by the logged-in user
    shops = Shop.objects.filter(owner=request.user)
    services = Product.objects.filter(owner=request.user)
    # return HttpResponse(shops)
    return render(request, 'owner/dashboard.html', {'shops': shops, 'services':services})

@login_required
def manage_services(request):
    # Ensure only owners can access this view
    if request.user.role != 'owner':
        return redirect('login')  # Redirect unauthorized users to login

    # Fetch all services/Product associated with shops owned by the logged-in user
    services = Product.objects.filter(owner_id=request.user)

    return render(request, 'owner/manage-services.html', {'services': services})

@login_required
def user_dashboard(request):
    # Ensure only users can access this view
    if request.user.role != 'user':
        return redirect('login')  # Redirect unauthorized users to login

    # Fetch all shops
    shops = Shop.objects.all()

    # Fetch all Product/services
    services = Product.objects.all()

    return render(request, 'user/dashboard.html', {'shops': shops, 'services': services})

@login_required
def view_shop(request, shop_id):
    # Fetch the shop details
    shop_instance = get_object_or_404(Shop, id=shop_id)

    # Fetch all services/Product associated with the shop
    services = Product.objects.filter(Shop=shop_instance)

    return render(request, 'user/view_shop.html', {'shop': shop_instance, 'services': services})
@login_required

@login_required
def purchase_service(request, service_id):
    # Ensure only users can access this view
    if request.user.role != 'user':
        return redirect('login')  # Redirect unauthorized users to login

    if request.method == 'POST':
        # Fetch the service
        product = Product.objects.get(pk=service_id)
        # return HttpResponse(product.owner)
        
        Shop.objects.create(
        
            name=product.name,
            owner=models.User.objects.get(pk=product.owner.id),
            buyer=request.user,
            product=product
        )
        
        # Create an order (assuming you have an Order model)
        # Example:
        # Order.objects.create(user=request.user, service=service, status='Pending')

        return redirect('site:user_dashboard')  # Redirect to user dashboard after purchase
        
@login_required
def create_service(request):
    # Ensure only owners can access this view
    if request.user.role != 'owner':
        return redirect('login')  # Redirect unauthorized users to login

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        # shop_id = request.POST.get('shop')  # Assuming shop ID is passed via form

        # Validate shop ownership
        # try:
        #     shop_instance = shop.objects.get(id=shop_id, owner=request.user)
        # except shop.DoesNotExist:
        #     return redirect('site:manage_services')  # Redirect if shop doesn't exist or isn't owned by the user

        # Create a new service
        Product.objects.create(
            name=name,
            description=description,
            price=price,
            owner=request.user,
            # shop=shop_instance
        )
        return redirect('site:manage_services')  # Redirect to manage services after creation

    # Fetch all shops owned by the logged-in user
    # shops = shop.objects.filter(owner=request.user)
    return render(request, 'owner/create_service.html')

@login_required
def delete_service(request, service_id):
    # Ensure only owners can access this view
    if request.user.role != 'owner':
        return redirect('login')  # Redirect unauthorized users to login
    # Fetch the service
    service = get_object_or_404(Product, id=service_id)
    
    # Ensure the service belongs to one of the owner's shops
    if service.owner != request.user:
        return redirect('site:manage_services')  # Redirect if the service doesn't belong to the owner

    service.delete()
    return redirect('site:manage_services')  # Redirect to manage services after deletion