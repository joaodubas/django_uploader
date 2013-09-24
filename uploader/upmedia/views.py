# encoding: utf-8
import json
import mimetypes
import re
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import ImageForm
from .models import Image


def order_name(name):
    name = re.sub(r'^.*/', '', name)
    if len(name) <= 20:
        return name
    return name[:10] + "..." + name[-7:]


def serialize(instance, file_attr='file'):
    obj = getattr(instance, file_attr)
    return {
        'url': obj.url,
        'name': order_name(obj.name),
        'type': mimetypes.guess_type(obj.path)[0] or 'image/png',
        'thumbnailUrl': obj.url,
        'size': obj.size,
        'deleteUrl': reverse('media:image_delete', args=[instance.pk]),
        'deleteType': 'DELETE',
    }


class UploaderResponseMixin(object):
    def form_valid(self, form):
        self.object = form.save()
        content = json.dumps({
            'files': (serialize(self.object, 'image'),)
        })
        return HttpResponse(
            content=content,
            mimetype='application/json'
        )


class ImageCreateView(UploaderResponseMixin, CreateView):
    model = Image
    form_class = ImageForm


class ImageUpdateView(UploaderResponseMixin, UpdateView):
    model = Image
    form_class = ImageForm


class ImageDeleteView(DeleteView):
    model = Image
