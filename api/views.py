import base64
import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status

# Helper function to get highest lowercase alphabet
def get_highest_lowercase_alphabet(data):
    lowercase_alphabets = [char for char in data if char.islower()]
    if lowercase_alphabets:
        return max(lowercase_alphabets)
    return None

@api_view(['POST', 'GET'])
def bfhl_api(request):
    if request.method == 'POST':
        # Process the POST request
        try:
            data = request.data['data']
            file_b64 = request.data.get('file_b64', '')

            # Separate numbers and alphabets
            numbers = [item for item in data if item.isdigit()]
            alphabets = [item for item in data if item.isalpha()]

            # Find the highest lowercase alphabet
            highest_lowercase_alphabet = get_highest_lowercase_alphabet(alphabets)

            # Handle file validity
            file_valid = False
            file_mime_type = None
            file_size_kb = None
            if file_b64:
                try:
                    file_data = base64.b64decode(file_b64)
                    file_size_kb = len(file_data) / 1024
                    file_valid = True  # Assume file is valid if it can be decoded
                    file_mime_type = 'unknown'  # Modify to determine MIME type
                except Exception:
                    file_valid = False

            # Create response
            response = {
                "is_success": True,
                "user_id": "john_doe_17091999",  # Example user_id, modify as needed
                "email": "john@xyz.com",  # Example email
                "roll_number": "ABCD123",  # Example roll number
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else [],
                "file_valid": file_valid,
                "file_mime_type": file_mime_type,
                "file_size_kb": file_size_kb
            }
            return JsonResponse(response, status=status.HTTP_200_OK)

        except KeyError:
            return JsonResponse({"error": "Invalid request data"}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        # Handle the GET request
        response = {
            "operation_code": 1
        }
        return JsonResponse(response, status=status.HTTP_200_OK)
