# encoding: utf-8
from django import forms
from django.conf import settings
from .models import Image

BASE = lambda *x: '{0}{1}'.format(settings.STATIC_URL, '/'.join(x))
BOWER = lambda *x: BASE('bower_components', *x)


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', )

    class Media:
        js = (
            BOWER('jquery', 'jquery.min.js'),
            BOWER('jquery-file-upload', 'js', 'vendor', 'jquery.ui.widget.js'),
            BOWER('jquery-file-upload', 'js', 'jquery.iframe-transport.js'),
            BOWER('jquery-file-upload', 'js', 'jquery.fileupload.js'),
        )
