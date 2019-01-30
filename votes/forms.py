from django.forms import ModelForm
from .models import Candidate

class CandidateModel(ModelForm):
	class Meta:
		model = Candidate
		exclude = ['id']


class New_Candidate(ModelForm):
	class Meta:
		model = Candidate
		exclude = ['id']