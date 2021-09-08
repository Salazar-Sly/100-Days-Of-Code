from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Referral

class IndexView(generic.ListView):
    template_name = 'refer/index.html'
    context_object_name = 'all_referrals'
    
    def get_queryset(self):
        return Referral.objects.all()

class DetailView(generic.DetailView):
    model = Referral
    template_name = 'refer/details.html'


class ReferralCreate(CreateView):
    model = Referral
    fields = ['name', 'physician', 'serviceProvider', 'reason', 'date']