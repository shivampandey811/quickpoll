from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Poll, Choice
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import F

def index(request):
    polls = Poll.objects.filter(deadline__gt=timezone.now()) if request.user.is_authenticated else Poll.objects.all()
    return render(request, 'polls/index.html', {'polls': polls})

@login_required
def create_poll(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        choices = request.POST.getlist('choices')
        deadline = request.POST.get('deadline')

        if question and choices and deadline:
            poll = Poll.objects.create(question=question, deadline=deadline, creator=request.user)
            for choice in choices:
                if choice:
                    Choice.objects.create(poll=poll, choice_text=choice)

            return redirect('index')

    return render(request, 'polls/create_poll.html')
from django.utils import timezone
# @login_required
def vote(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    if request.user.is_authenticated:
        if request.user in poll.voters.all():
            return render(request, 'polls/already_voted.html')
        if request.method == 'POST':
            choice_id = request.POST.get('choice')
            if choice_id:
                choice = Choice.objects.get(id=choice_id)
                choice.votes = F('votes') + 1
                choice.save()
                poll.voters.add(request.user)
                return redirect('results', poll_id=poll.id)
    return render(request, 'polls/vote.html', {'poll': poll,'now':timezone.now(), 'user_can_vote': request.user.is_authenticated})

def results(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})
