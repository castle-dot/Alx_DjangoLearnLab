from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

def user_is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@login_required
@user_passes_test(user_is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')
