from django.contrib.contenttypes.models import ContentType
from django.template.response import TemplateResponse
from django.db.models import ObjectDoesNotExist
from django.http import Http404

from rcomments.models import RComment

def comment_list(request, ct_id, object_pk):
    try:
        ct = ContentType.objects.get_for_id(int(ct_id))
        obj = ct.get_object_for_this_type(pk=object_pk)
    except (ContentType.DoesNotExist, ObjectDoesNotExist):
        raise Http404()

    clist = RComment.objects.for_model(obj)
    return TemplateResponse(request, 'comment_list.html', {'comment_list': clist})