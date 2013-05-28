# Create your views here.
from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response
import json
from django.template import RequestContext
from django.utils.decorators import method_decorator
from userapp.models import *
from django.contrib.auth.models import get_hexdigest
import sys
import random


def enc_password(password):
    algo = 'sha1'
    salt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
    hsh = get_hexdigest(algo, salt, password)
    password = '%s$%s$%s' % (algo, salt, hsh)
    return password


class Index(TemplateView):
    """
    It will return index page
    url : http://accxyx.com/
    """
    #when there is a get request
    def get(self, request):
        return render_to_response('userapp/index.html', locals(), context_instance=RequestContext(request))

    #when there is a post request
    def post(self, request):
        return render_to_response('userapp/index.html', locals(), context_instance=RequestContext(request))


class Signup(TemplateView):
    print "Before post method execution."

    def post(self, request):
        print 'Coming inside post method function'
        if request.is_ajax():
            response = {'result': ''}
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            password = enc_password(password)
            try:
                Player.objects.create(username=username,password=password,email=email)
                response['result'] = 'True'
            except:
                print sys.exc_info()
                response['result'] = 'UserNameAlreadyRegistered'
            json = json.dumps(response)
            return HttpResponse(json, mimetype='application/json')
        else:
            return HttpResponseBadRequest()

    def get(self,request):
        return render_to_response('userapp/index.html')

