class TimeRecoringAutoView(GenericAPIView):

    serializer_class = TimeRcordingAutoSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Time.objects.all()
    @swagger_auto_schema(
        operation_description="date-time format: YYYY-MM-DD hh:mm:ss or iso-8601 (gregorian date)",
        responses={
            201: openapi.Response('Time Created' , TimeRcordingAutoSerializer),
            400: openapi.Response('Bad Request',swagger_schema.get_schema('time-auto')),
            401: 'Unauthorized'
        },
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data,context=request.auth.key)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TimeRecoringStopView(GenericAPIView):

    serializer_class = TimeRecordingStopSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Time.objects.all()
    @swagger_auto_schema(
        operation_description="stop first incomplete time for user of passed token",
        responses={
            200: openapi.Response('Time Stopped' , TimeRecordingStopSerializer),
            401: openapi.Response('UnAuthorize',swagger_schema.get_schema('time-auto-stop')
        },
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data,context=request.auth.key)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

