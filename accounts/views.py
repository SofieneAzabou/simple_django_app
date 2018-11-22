from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse_lazy
from django.views import generic
from accounts.forms import CustomUserCreationForm


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def ChangeEmail(request):
    template = loader.get_template('change.html')
    context = {}
    user_id = request.user.id
    if request.method == 'POST':
        new_email = request.POST.get('new_mail')
        curr_user = User.objects.get(id=user_id)
        curr_user.email = new_email
        print(curr_user.email)
        curr_user.save()
        return HttpResponseRedirect('/')
    return HttpResponse(template.render(context, request))
