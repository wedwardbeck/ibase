

class CancelMixin(object):
    default_cancel_url = '/'

    def get_context_data(self, arg1=None, **kwargs):
        if arg1 is None:
            context = super(CancelMixin, self).get_context_data(**kwargs)
        else:
            # For WizardViews
            context = super(CancelMixin, self).get_context_data(arg1, **kwargs)

        # First try the referrer URL
        referrer = self.request.META.get('HTTP_REFERER', None)  # Known typo
        if referrer is None:
            context['cancel_url'] = self.default_cancel_url
        else:
            context['cancel_url'] = referrer

        return context
