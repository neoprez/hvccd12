"""
This package holds the main pages that are mostly not dynamic.
"""
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """
    The home view
    """
    template_name = 'home.html'

