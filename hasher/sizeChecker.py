from django.db.models import FileField
from django.forms import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class ContentTypeRestrictedFileField(FileField):
    def __init__(self, *args, **kwargs):
        self.max_upload_size = kwargs.pop('max_upload_size', None)
        if not self.max_upload_size:
            self.max_upload_size = settings.MAX_UPLOAD_SIZE

        super(ContentTypeRestrictedFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(ContentTypeRestrictedFileField, self).clean(*args, **kwargs)
        file = data.file
        try:
            if file._size > self.max_upload_size:
                raise forms.ValidationError(_('Please keep filesize under'
                                              ' %s. Current filesize %s')
                                            % (filesizeformat(self.max_upload_size), filesizeformat(file._size)))
        except AttributeError:
            pass

        return data
