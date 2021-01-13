class TimeRecoringAutoView(GenericAPIView):

    serializer_class = TimeRcordingAutoSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Time.objects.all()
    @swagger_auto_schema(
        operation_description="date-time format: YYYY-MM-DD hh:mm:ss or iso-8601 (gregorian date)",
        responses={
            201: openapi.Response('Time Created' , TimeRcordingAutoSerializer),
            400: "BAD REQUEST11",
            401: 'Unauthorized'
        },
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

