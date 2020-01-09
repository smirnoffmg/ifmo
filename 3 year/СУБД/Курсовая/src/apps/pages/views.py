# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import FormView

from apps.core.mixins import DisableAdditionalBlocksMixin
from apps.core.tasks import send_notification
from apps.pages.forms import CallbackForm, FeedbackForm
from apps.pages.models import Feedback


class AboutUsPageView(DisableAdditionalBlocksMixin, TemplateView):
    template_name = 'pages/about_us.html'


class DeliveryPage(DisableAdditionalBlocksMixin, TemplateView):
    template_name = 'pages/delivery.html'


class WarrantyPage(DisableAdditionalBlocksMixin, TemplateView):
    template_name = 'pages/warranty.html'


class CorporatePage(DisableAdditionalBlocksMixin, TemplateView):
    template_name = 'pages/corporate.html'


class ContactsPage(DisableAdditionalBlocksMixin, TemplateView):
    template_name = 'pages/contacts.html'


class FeedbackPageView(DisableAdditionalBlocksMixin, SuccessMessageMixin,
                       CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'pages/feedback.html'
    success_url = reverse_lazy('pages:feedback')
    success_message = u'Спасибо, ваш вопрос отправлен. Наш оператор ' \
                      u'свяжется с вами в течение одного рабочего дня.'


class CreateCallbackView(FormView):
    form_class = CallbackForm

    def get_success_url(self):
        return self.request.META['HTTP_REFERER']

    def form_valid(self, form):
        data = form.cleaned_data
        for email in settings.NOTIFICATION_EMAILS:
            send_notification.delay(
                to=email,
                subject='Новый обратный звонок',
                template_name='emails/new_callback.html',
                context={
                    'name': data.get('name'),
                    'phone': data.get('phone')
                }
            )

        return super(CreateCallbackView, self).form_valid(form)
