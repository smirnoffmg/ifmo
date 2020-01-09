# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from urlparse import urljoin

from django.conf import settings
from django.db import models
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from apps.core import GenericModel, PathAndRename

files_dir = PathAndRename('bouquets/')


@python_2_unicode_compatible
class CRMFile(GenericModel):
    file = models.FileField(verbose_name=_('file'), upload_to=files_dir)

    class Meta:
        verbose_name = _('file')
        verbose_name_plural = _('files')

    def __str__(self):
        return self.filename()

    def filename(self):
        return os.path.basename(self.file.name)

    def get_full_url(self):
        return urljoin(settings.DOMAIN_NAME, self.file.url)
