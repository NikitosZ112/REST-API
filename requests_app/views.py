from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated 
from .models import Request, RequestMessage 
from .serializers import RequestSerializer, RequestMessageSerializer 
 
class RequestViewSet(viewsets.ModelViewSet): 
    serializer_class = RequestSerializer 
    queryset = Request.objects.all() 
    permission_classes = [IsAuthenticated] 
 
    def get_queryset(self): 
        return Request.objects.filter(user=self.request.user) 
 
class RequestMessageViewSet(viewsets.ModelViewSet): 
    serializer_class = RequestMessageSerializer 
    queryset = RequestMessage.objects.all() 
    permission_classes = [IsAuthenticated] 
 
    def get_queryset(self): 
        request_id = self.kwargs['request_id'] 
        return RequestMessage.objects.filter(request_id=request_id) 