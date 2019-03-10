from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Candidate, Position, Vote, Partylist
from .forms import (CandidateModelForm, PositionModelForm,
                    RegistrationModelForm, PartylistModelForm)
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout


# Create your views here.
def index(request):
    context = {}
    partylists = Partylist.objects.all()
    context['partylists'] = partylists
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
    context = {}
    positions  = Position.objects.all() 
    context['positions'] = positions
    partylists  = Partylist.objects.all() 
    context['partylists'] = partylists
    if request.method == 'POST':
        form = CandidateModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('votes:candidates_list')
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
        form = CandidateModelForm(request.POST, request.FILES, instance=candidate)
        if form.is_valid():
            form.save()
            return redirect('votes:candidates_list')
        else:
            context['form'] = form
    else:
        form = CandidateModelForm(instance=candidate)
        context['form'] = form
    return render(request, 'update_candidate.html', context)

@login_required
def party_list(request):
    context = {}
    partylists = Partylist.objects.all()
    context['partylists'] = partylists
    return render(request, 'partylist_list.html', context)

@login_required
def det_partylist(request, partylist_id):
    context = {}
    context['partylist'] = Partylist.objects.get(id=partylist_id)
    return render(request, 'detail_partylist.html', context)
    
@login_required
def cre_partylist(request):
    context = {}
    if request.method == 'POST':
        form = PartylistModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('votes:partylist_list')
        else:
            context['form'] = form
    else:
        form = PartylistModelForm()
        context['form'] = form
    return render(request, 'create_partylist.html', context)

@login_required
def upd_partylist(request, partylist_id):
    context = {}
    partylist = Partylist.objects.get(id=partylist_id)
    if request.method == 'POST':
        form = PartylistModelForm(request.POST, instance=partylist)
        if form.is_valid():
            form.save()
            return redirect('votes:partylist_list')
        else:
            context['form'] = form
    else:
        form = PartylistModelForm(instance=partylist)
        context['form'] = form
    return render(request, 'update_partylist.html', context)

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
            return redirect('votes:detail_position')
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
def vote_view(request):
    context = {}
    positions = Position.objects.all()
    partylists = Partylist.objects.all()
    context['positions'] = positions
    context['partylists'] = partylists
    return render(request, 'vote_page.html', context)

@login_required
def vote_candidate(request, position_id):
    context = {}
    context['position'] = Position.objects.get(id=position_id)
    return render(request, 'vote_candidates_pos.html', context)

@login_required
def vote(request, candidate_id):
    candidate = Candidate.objects.get(id=candidate_id)
    vote = Vote(candidate=candidate)
    vote.save()
    return redirect('votes:candidates_list')

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
            return redirect('votes:login')
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
    return redirect('votes:login')