# -*- coding: utf-8 -*-

import json

from django.shortcuts import render
from django.http import HttpResponse

from spildb.core.models import Spil


def home(request):
    spil_models = Spil.objects.all()
    spil = [s.to_dict() for s in spil_models]

    return HttpResponse(json.dumps(spil), content_type='application/json')

