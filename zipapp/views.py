from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import zipfile

class PutFileRESTView(APIView):

    def put(self, request, *args, **kwargs):
        zip_file = request.PUT['zip_file']
        zip_ref = zipfile.ZipFile(zip_file, 'r')
        zip_ref.extractall('directory_to_extract_to')
        zip_ref.close()
        response = Response('Extracted and wrote zip file to the specified direc', status=status.HTTP_200_OK)
        return response
