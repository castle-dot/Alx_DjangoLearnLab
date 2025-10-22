from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

def user_is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@login_required
@user_passes_test(user_is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
