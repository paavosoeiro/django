from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from polls.models import Poll, Choice

def vote(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render_to_response('polls/poll_detail.html', {'object':p,
			'error_message': 'Voce nao fez uma escolha.',})
	else:
		selected_choice.votes += 1 
		selected_choice.save()
		return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))
