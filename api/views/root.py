from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def api_root(request, format=None):
    """
    Root of the application's API.
    """
    return Response({
        'actions': reverse('actions', request=request, format=format),
        'assets': reverse('assets', request=request, format=format),
        'cvi': reverse('cvi', request=request, format=format),
        'devices': reverse('devices', request=request, format=format),
        'functions': reverse('functions', request=request, format=format),
        'groups': reverse('groups', request=request, format=format),
        'impacts': reverse('impacts', request=request, format=format),
        'missions': reverse('missions', request=request, format=format),
        'network': reverse('network', request=request, format=format),
        'risk-appetite': reverse('risk-appetite', request=request, format=format),
        'threats': reverse('threats', request=request, format=format),
        'vulnerabilities': reverse('vulnerabilities', request=request, format=format)
    })
