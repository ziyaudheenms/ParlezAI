from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.models import User
from Interview.models import RecruiterProfile


@api_view(['POST'])
def CreateRecuriter(request):
    username = request.data["username"]
    password = request.data["password"]
    email = request.data["email"]
    company_info = request.data["company_info"]
    company_name = request.data["company_name"]
    profile_pic = request.data["profile_pic"]

    Recruiter = User.objects.create(
        username = username,
        email = email,
        password = password
    )
    RecruiterProfile.objects.create(
        user = Recruiter,
        company_name = company_name,
        company_info = company_info,
        profile_pic = profile_pic
    )

    responce = {
        "status_code" : 5000,
        "message" : "user created successfully"
    }
    return Response(responce)

