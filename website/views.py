from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from .models import Books, Lectures, Subject
from .forms import BookUploadForm, LectureUploadForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Redirect to the home page after login
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
# def login(request):
#     if request.method == "POST":
#         # Get username and password from POST request
#         username = request.POST.get("username") 
#         password = request.POST.get("password") 
        
#         # Authenticate user
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#             # Log the user in
#             login(request, user)
#             # Redirect to the home page after successful login
#             return redirect('home')    
#         else:
#             # Show an error message on failed login
#             return render(request, 'login.html', {'error': 'Invalid username or password'})
    
#     # Handle GET request to show the login page
#     return render(request, 'login.html')
def logout_view(request):
    logout(request)  # This logs out the user
    return redirect('login')  # Redirect to the login page after logout

def home(request):
    if request.method == "POST":
        return render(request, 'home.html', {'message': 'POST Request'})
    return render(request, 'home.html')  # Default response for GET requests
    
# View for displaying all books
    
def books(request):
    booksl = Books.objects.all()
    return render(request, 'books.html', {'books':booksl})
        
def lectures(request):
    subjects = Subject.objects.all()  # All subjects
    lectures_by_subject = {
        subject.id: Lectures.objects.filter(subject=subject) for subject in subjects
    }
    return render(request, 'lectures.html', {
        'subjects': subjects,
        'lectures': lectures_by_subject
    })
    
@staff_member_required
def upload_page(request):
    # Initialize empty forms
    book_form = BookUploadForm()
    lecture_form = LectureUploadForm()

    # Handle POST request for book or lecture form submission
    if request.method == 'POST':
        if 'book_submit' in request.POST:
            book_form = BookUploadForm(request.POST, request.FILES)
            if book_form.is_valid():
                book_form.save()
                messages.success(request, 'Book uploaded successfully.')
                return redirect('upload_page')  # Redirect after success

        elif 'lecture_submit' in request.POST:
            lecture_form = LectureUploadForm(request.POST, request.FILES)
            if lecture_form.is_valid():
                lecture_form.save()
                messages.success(request, 'Lecture uploaded successfully.')
                return redirect('upload_page')  # Redirect after success

    # Render page with both forms
    return render(request, 'upload.html', {
        'book_form': book_form,
        'lecture_form': lecture_form,
    })
    
@staff_member_required
def delete_item(request, item_type, item_id):
    if item_type == 'book':
        item = get_object_or_404(Books, id=item_id)
        redirect_url = 'books'
    elif item_type == 'lecture':
        item = get_object_or_404(Lectures, id=item_id)
        redirect_url = 'lectures'
    else:
        raise ValueError("Invalid item type")
    
    item.delete()
    return redirect(redirect_url)    

@staff_member_required
def edit_item(request, item_type, item_id):
    if item_type == 'book':
        item = get_object_or_404(Books, id=item_id)
        form_class = BookUploadForm
        redirect_url = 'books'
    elif item_type == 'lecture':
        item = get_object_or_404(Lectures, id=item_id)
        form_class = LectureUploadForm
        redirect_url = 'lectures'
    else:
        raise ValueError("Invalid item type")
    
    if request.method == "POST":
        form = form_class(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = form_class(instance=item)
    
    return render(request, 'edit_item.html', {'form': form, 'item': item, 'item_type': item_type})   

@staff_member_required
def upload_book(request):
    if request.method == 'POST':
        form = BookUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book uploaded successfully.')
            return redirect('upload')  # Redirect back to the upload page
    else:
        form = BookUploadForm()
    return render(request, 'upload.html', {'book_form': form, 'lecture_form': LectureUploadForm()})


@staff_member_required
def upload_lecture(request):
    if request.method == 'POST':
        form = LectureUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lecture uploaded successfully.')
            return redirect('upload')  # Redirect back to the upload page
    else:
        form = LectureUploadForm()
    return render(request, 'upload.html', {'lecture_form': form, 'book_form': BookUploadForm()})