from django import template

from django.core.urlresolvers import reverse
from django.template.loader import render_to_string

from django.contrib.contenttypes.models import ContentType
from types import ListType,TupleType

from xformmanager.models import *
import xformmanager.adapter.querytools as qtools
from hq.models import *
import hq.utils as utils
from datetime import timedelta
import graphing.dbhelper as dbhelper
from hq.models import *
register = template.Library()

from graphing.models import RawGraph

import time

xmldate_format= '%Y-%m-%dT%H:%M:%S'
output_format = '%Y-%m-%d %H:%M'



@register.simple_tag
def get_tester_with_counts(user, startdate=None, enddate=None, use_blacklist=True):

    # todo:  query the global meta tables to get all the users
    # and/or query the ExtUser table to get all the registered users.
    totalspan = enddate-startdate
    count_hash_month = {}
    count_hash_total = {}
    extuser = ExtUser.objects.get(id=user.id)
    
    # query the Ext user table to get all the reqisterd user with the same domain
    # with the user.
    #testers = ExtUser.objects.all().filter(domain=extuser.domain)
    defs = FormDefModel.objects.all().filter(domain=extuser.domain)
    ret =""
    #username_to_count_hash = { }
    #if use_blacklist:
        #domain_blacklist = extuser.domain.get_blacklist()
    for fdef in defs:
        try:
            # don't do anything if we can't find a username column
            username_col = fdef.get_username_column()
            if not username_col:
                logging.warning("No username column found in %s, will not display dashboard data." % fdef)
                ret += '<p style="font-weight:bold; color:orange;">Warning: no username column found in %s, no dashboard data will be displayed for this form</p>' % fdef
                continue
            helper = fdef.db_helper
            # let's get the usernames
            usernames_to_filter = helper.get_uniques_for_column(username_col)

            for user in usernames_to_filter:
                count_month = user.objects.filter(date_received <= startdate).count()
                count_hash_month[user] = count_month
                
                count_total = user.objects.all().count()
                count_hash_total[user] = count_total
        except Exception, e:
            # this shouldn't blow up the entire view
            logging.error("problem in dashboard display: %s" % e)
            ret += '<p style="font-weight:bold; color:red;">problem in dashboard display.  Not all data will be visible.  Your error message is: %s</p>' % e
    
    ret += '\n'
    count = 1
    for user in usernames_to_filter:
        ret += '\n<tr class="%s">' % _get_class(count)
        count += 1
        ret += '<td>%s</td>' % (user.last_name)
        ret += '<td>%s</td>' % (user.first_name)
        ret += '<td>%s</td>' % (user.primary_phone)
        ret += '<td>%s</td>' % (count_hash_month[user])
        ret += '<td>%s</td>' % (count_hash_total[user])
        ret += '<td><a href="">Edit</a> |<a href="">Delete</a></td>'
        ret += '</tr>'

    ret += '</table>'
    return ret

def _get_class(count):
    if count % 2 == 0:
        return "even"
    return "odd"
 