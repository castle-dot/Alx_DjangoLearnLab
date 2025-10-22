from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

def user_is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

@login_required
@user_passes_test(user_is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')
