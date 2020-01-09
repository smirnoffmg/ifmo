# -*- coding: utf-8 -*-
from braces.views import LoginRequiredMixin
from django.views.generic import ListView


class CRMListMixin(object):
    paginate_by = 20
    search_fields = []
    list_url = None
    create_url = None

    def get_list_url(self):
        return self.list_url

    def get_create_url(self):
        return self.create_url

    def get_search_query(self):
        return self.request.GET.get('query')

    def construct_filter_query(self):
        query = self.get_search_query()
        if query and self.search_fields:
            pass

    def get_context_data(self, **kwargs):
        data = super(CRMListMixin, self).get_context_data(**kwargs)
        data.update({
            'query': self.get_search_query(),
            'list_url': self.get_list_url(),
            'create_url': self.get_create_url(),
        })
        return data


class CRMListView(CRMListMixin, LoginRequiredMixin, ListView):
    pass
