from tastypie.resources import ModelResource
from tastypie.contrib.gis.resources import ModelResource
from tastypie import fields
from tastypie import utils
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.validation import Validation, FormValidation
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from django import forms
from django.forms import ModelForm
from datetime import datetime, timedelta
from django.db.models import Q
from tastypie.serializers import Serializer
from django.utils.timezone import is_naive

from qualia.tools.api import *

from documents.models import *


class DocumentList(ModelResource):

    class Meta:
        queryset = Document.objects.all()
        resource_name = 'document'
        allowed_methods = ['get']
        authentication = KeyOnlyAuthentication()
        authorization = DjangoAuthorization()
        always_return_data = True
        detail_uri_name = 'id'

        filtering = {
            'name': ALL,
        }

    def dehydrate_tags(self, bundle):
        return bundle.obj.tags

    def dehydrate_content(self, bundle):
        return bundle.obj.content
