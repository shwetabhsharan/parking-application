from findspot.models import Space
from findspot.serializers import SpaceSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class SpaceViewSet(ModelViewSet):
    """
        Parking space view set
    """

    serializer_class = SpaceSerializer
    queryset = Space.objects.all()
    authentication_classes = [TokenAuthentication]

    def list(self, request, *args, **kwargs):
        """
            list all the available parking spaces available
        """

        latitude = request.GET.get('lat')
        longitude = request.GET.get('long')
        radius = request.GET.get('rad')

        queryset = Space.objects.filter(latitude=latitude,
                                               longitude=longitude,
                                               radius=radius,
                                               is_available=True)
        serializer = SpaceSerializer(queryset, many=True)
        
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request):
        """
            book a parking slot
        """
        btime = request.data.get('btime')
        parking_slot = request.data.get('parking_slot')
        try:
            parking_obj = Space.objects.get(id=parking_slot, is_available=True)
        except:
            return Response(dict(success = False, error="Parking space does not exists"), status=status.HTTP_400_BAD_REQUEST)

        parking_obj.booked_for = btime
        try:
            parking_obj.save()
        except Exception, e:
            raise

        return Response(dict(success = True), status=status.HTTP_202_ACCEPTED)
