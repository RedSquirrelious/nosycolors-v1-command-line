from django.shortcuts import render

from django.http import HttpResponse, Http404

from .models import Tweet, Target

# Create your views here.




def index(request):
	target_user_list = Target.objects.order_by('-target_name')[:5]
	context = {'target_user_list': target_user_list}
	return render(request, 'showoff/index.html', context)


def tweeting(request):
	latest_tweet_list = Tweet.objects.order_by('-tweet_date')[:5]
	context = {'lastest_tweet_list': latest_tweet_list,}
	return render(request, 'showoff/tweeting.html', context)

# def detail(request, tweet_id):
# 	try:
# 		tweet = Tweet.objects.get(pk=tweet_id)
# 	except Tweet.DoesNotExist:
# 		raise Http404("No such tweet!")
# 	else:
# 		return render(request, 'showoff/detail.html', {'tweet': tweet}) 


def detail(request, target_id):
	try:
		target = Target.objects.get(pk=target_id)
	except Target.DoesNotExist:
		raise Http404("No such target!")
	else:
		return render(request, 'showoff/detail.html', {'target': target}) 
