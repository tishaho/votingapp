from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Candidate, Position, Vote
from .forms import (CandidateModelForm, PositionModelForm,
                    RegistrationModelForm)
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout


# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

@login_required
def cand_list(request):
    context = {}
    candidates = Candidate.objects.all().order_by('position')
    context['candidates'] = candidates
    return render(request, 'candidates_list.html', context)

@login_required
def det_candidate(request, candidate_id):
    context = {}
    candidate = Candidate.objects.get(id=candidate_id)
    context['candidate'] = candidate
    return render(request, 'detail_candidate.html', context)

@login_required
def cre_candidate(request):
    position  = Position.objects.all() 
    context = {}
    if request.method == 'POST':
        selected_item = get_object_or_404(Position, pk=request.POST.get('position_id'))
        form = CandidateModelForm(request.POST)
        candidate.position = selected_item
        if form.is_valid():
            form.save()
            return redirect('votes:index')
        else:
            context['form'] = form
    else:
        form = CandidateModelForm()
        context['form'] = form
    return render(request, 'create_candidate.html', context)

@login_required
def upd_candidate(request, candidate_id):
    context = {}
    candidate = Candidate.objects.get(id=candidate_id)
    if request.method == 'POST':
        form = CandidateModelForm(request.POST, instance=candidate)
        if form.is_valid():
            form.save()
            return redirect('votes:detail_candidate', form.instance.id)
        else:
            context['form'] = form
    else:
        form = CandidateModelForm(instance=candidate)
        context['form'] = form
    return render(request, 'update_candidate.html', context)

@login_required
def det_position(request):
    context = {}
    positions = Position.objects.all()
    context['positions'] = positions
    return render(request, 'detail_position.html', context)

@login_required
def create_position(request):
    context = {}
    if request.method == 'POST':
        form = PositionModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('votes:index')
        else:
            context['form'] = form
    else:
        form = PositionModelForm()
        context['form'] = form
    return render(request, 'create_position.html', context)

@login_required
def upd_position(request, position_id):
    context = {}
    position = Position.objects.get(id=position_id)
    if request.method == 'POST':
        form = PositionModelForm(request.POST, instance=position)
        if form.is_valid():
            form.save()
            return redirect('votes:detail_position')
        else:
            context['form'] = form
    else:
        form = PositionModelForm(instance=position)
        context['form'] = form
    return render(request, 'update_position.html', context)

@login_required
def vote(request, candidate_id):
    candidate = Candidate.objects.get(id=candidate_id)
    vote = Vote(candidate=candidate)
    vote.save()
    return redirect('votes:index')

def registration(request):
    form = RegistrationModelForm()
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = RegistrationModelForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(request.POST['password'])
            user.save()
            login(request, user)
            return redirect('votes:index')
        else:
            context['form'] = form
    return render(request, 'registration.html', context)

def user_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(user)
            login(request, user)
            return redirect('votes:index')
    return render(request, 'login.html', context)


def user_logout(request):
    context = {}
    logout(request)
    return redirect('votes:index')