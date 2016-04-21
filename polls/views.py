# Create your views here.
from polls.models import Poll, Choice
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from polls.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext


'''
def index(request): # Httpresponse return
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    t = loader.get_template('polls/index.html')
    c = Context({
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(t.render(c))
'''


def home(request):
    return render_to_response('polls/home.html')


def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('polls/index.html',{'latest_poll_list': latest_poll_list})


def detail(request, poll_id):
    '''
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    '''
    p = get_object_or_404(Poll, pk=poll_id) #use this line to replace above 4 lines
    return render_to_response('polls/detail.html', {'poll': p})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)



def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)



@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", form
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            user.first_name=form.cleaned_data['first_name'],
            user.last_name=form.cleaned_data['last_name']
            user.save()
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })

    return render_to_response(
    'registration/register.html',
    variables,
    )

def register_success(request):
    return render_to_response(
    'registration/success.html',
    )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def welcome(request):
    return render_to_response(
    'polls/welcome.html',
    { 'user': request.user }
    )
