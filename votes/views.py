from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Candidate
from .models import Position
from .models import Vote
from .forms import CandidateModel
from .forms import New_Candidate

# Create your views here.
def index(request):
	context = {}
	candidates = Candidate.objects.all()
	context['candidates'] = candidates
	return render(request, 'index.html', context)


def candidate_detail(request, candidate_id):
	context = {}
	context['candidate'] = Candidate.objects.get(id=candidate_id)

	return render(request, 'candidate_detail.html', context)


def candidate_create(request):
	context = {}
	form = New_Candidate()

	if request.method == 'POST':
		form = CandidateModel(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Post added')

	return render(request, "candidate_create.html", {'form': form})


def candidate_update(request, candidate_id):
	context = {}
	candidates = Candidate.objects.get(id=candidate_id)

	if request.method == 'POST':
		form = CandidateModel(request.POST, instance=candidates)
		if form.is_valid():
			form.save()
			return HttpResponse('Post updated')

		else:
			context['form'] = form
			return render(request, 'candidate_update.html', context)
		
	else:
		context['form'] = CandidateModel(instance=candidates)
		return render(request, 'candidate_update.html', context)
