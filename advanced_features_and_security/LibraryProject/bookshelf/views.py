from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Article
from .models import Book
from .forms import ExampleForm
from django.http import HttpResponse

# View to edit an article
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        # Handle the form submission for editing the article
        article.title = request.POST['title']
        article.content = request.POST['content']
        article.save()
    return render(request, 'edit_article.html', {'article': article})

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # Get all books
    return render(request, 'book_list.html', {'books': books})

def form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the valid form data
            example_input = form.cleaned_data['example_input']
            # Use ORM or sanitized methods for database interaction
            # No direct SQL queries should be used here
            return HttpResponse("Form submitted successfully!")
    else:
        form = ExampleForm()

    return render(request, 'form_example.html', {'form': form})