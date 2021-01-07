from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Url
import random,string
# Create your views here.
def getHash():
	return "".join([random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(8)])

def dashboard(request):
	if request.method == "POST":
		URL = request.POST["URL"]
		prefix = "http://marketing.newsbytes/"
		try:
			try:
				url = Url.objects.get(target_url=URL)
				url.count = url.count+1
				url.save()
				return redirect("dashboard")
			except ObjectDoesNotExist:
				alias = prefix+getHash()
				Url.objects.create(user=request.user, target_url=URL, alias=alias, count=1).save()
				return redirect("dashboard")
		except:
			return render(request, "dashboard.html", {"url":URL, "alias":alias})
	return render(request, "dashboard.html")