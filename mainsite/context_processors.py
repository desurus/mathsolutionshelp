from django.conf import settings  # import the settings file


def get_email_address(request):
    return {'CONTACTS_EMAIL_ADDRESS': settings.EMAIL_ADDRESS}
