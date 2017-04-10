from findspot.models import Space
from findspot.serializers import SpaceSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
import datetime


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
            API: /spot?lat=<latitude>&long=<longitude>&rad=<radius>
            Method: GET
        """

        latitude = request.GET.get('lat')
        longitude = request.GET.get('long')
        radius = request.GET.get('rad')

        # query below says give me all parking spots where lat is greater
        # than equal to lat param, long greater than equal to long param
        # and radius less than equal to the rad param

        queryset = Space.objects.filter(latitude__gte=latitude,
                                               longitude__gte=longitude,
                                               radius__lte=radius,
                                               is_available=True)

        serializer = SpaceSerializer(queryset, many=True)

        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request):
        """
            book a parking slot for time 0 mins to 60 mins
            API: /spot/
            Parameters: {
                            "parking_slot": <spot unique identifier>,
                            "btime": <booking time in mins> 0 - 60 mins
                        }
            Method: PUT
        """

        btime = request.data.get('btime')
        parking_slot = request.data.get('parking_slot')

        try:
            parking_obj = Space.objects.get(id=parking_slot, is_available=True)
        except:
            return Response(dict(success = False,
                                 error="Parking space does not exists"),
                            status=status.HTTP_400_BAD_REQUEST)

        parking_obj.booked_for = btime
        parking_obj.is_available = False
        parking_obj.booked_at = datetime.datetime.now()

        try:
            parking_obj.save()
        except:
            raise

        return Response(dict(success=True), status=status.HTTP_202_ACCEPTED)

    @list_route()
    def view_reserved_parking(self, request):
        """
            show a list of existing parking in the specified radius
            API: /spot/view_reserved_parking?rad=<radius>
            Method: GET
        """

        radius = request.GET.get('rad')

        queryset = Space.objects.filter(radius__lte=radius, is_available=False)

        serializer = SpaceSerializer(queryset, many=True)

        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @detail_route(methods=['PUT'])
    def cancel_reservation(self, request, pk=None):
        try:
            space_object = Space.objects.get(id=pk)
        except:
            return Response(dict(success = False,
                                 error="Parking space does not exists"),
                            status=status.HTTP_400_BAD_REQUEST)

        # can be done using serializers to handle validations
        space_object.booked_for = 0
        space_object.is_available = True

        try:
            space_object.save()
        except:
            raise

        return Response(dict(success=True), status=status.HTTP_202_ACCEPTED)