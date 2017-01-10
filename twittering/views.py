from django.shortcuts import render

from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import Tweet, Target

from .forms import HandleForm

# Create your views here.


def index(request):
	    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = HandleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            target_handle = form.cleaned_data['target_handle']

            Tweet.objects.get_target_tweets(target_handle, api)
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = HandleForm()

    return render(request, 'twittering/index.html', {'form': form})



def target(request):
	target_user_list = Target.objects.order_by('-target_name')[:5]
	context = {'target_user_list': target_user_list}
	return render(request, 'twittering/target.html', context)


def tweeting(request):
	latest_tweet_list = Tweet.objects.order_by('-tweet_date')[:5]
	context = {'lastest_tweet_list': latest_tweet_list,}
	return render(request, 'twittering/tweeting.html', context)

# def detail(request, tweet_id):
# 	try:
# 		tweet = Tweet.objects.get(pk=tweet_id)
# 	except Tweet.DoesNotExist:
# 		raise Http404("No such tweet!")
# 	else:
# 		return render(request, 'twittering/detail.html', {'tweet': tweet}) 


def detail(request, target_id):
	try:
		target = Target.objects.get(pk=target_id)
	except Target.DoesNotExist:
		raise Http404("No such target!")
	else:
		return render(request, 'twittering/detail.html', {'target': target}) 
