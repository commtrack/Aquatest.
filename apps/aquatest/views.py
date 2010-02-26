import logging
import hashlib
import settings
import traceback
import sys
import os
import uuid
import string
from datetime import timedelta
from graphing import dbhelper

from django.http import HttpResponse
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from django.core.exceptions import *
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.db import transaction
from django.db.models.query_utils import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from rapidsms.webui.utils import render_to_response, paginated

from xformmanager.models import *
from hq.models import *
from graphing.models import *
from receiver.models import *

import hq.utils as utils
import hq.reporter as reporter
import hq.reporter.custom as custom
import hq.reporter.metastats as metastats

import hq.reporter.inspector as repinspector
import hq.reporter.metadata as metadata
from hq.decorators import extuser_required

from reporters.utils import *
from reporters.views import message, check_reporter_form, update_reporter
from reporters.models import Reporter, PersistantBackend, PersistantConnection


logger_set = False

@extuser_required()
def testers(request):
    template_name="testers.html"
    context = {}
    startdate, enddate = utils.get_dates(request)
    context['startdate'] = startdate
    context['enddate'] = enddate
    context['view_name'] = 'hq.views.dashboard'
    return render_to_response(request, template_name, context)

@extuser_required()
def testers_delete(request):
    template_name="testers.html"
    return render_to_response(request, template_name, {})

@extuser_required()
def testers_edit(request):
    template_name="testers.html"
    return render_to_response(request, template_name, {})

@extuser_required()
def testers_add(request):
    template_name="testers.html"
    return render_to_response(request, template_name, {})
