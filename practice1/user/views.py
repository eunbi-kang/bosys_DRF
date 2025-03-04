from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer

# # 기본 뷰
# @api_view(['GET'])
# def user_list(request):
#     return Response(
#         {"message": "User API is working!"}
#     )

# 기본 뷰
@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        if not users.exists():
            return Response({"message": "사용자가 없습니다."}, status=status.HTTP_204_NO_CONTENT)
        serializer = UserSerializer(users, many=True)
        return Response({"message": "사용자 목록 조회 성공", "users": serializer.data}, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "사용자가 생성되었습니다.", "user": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "사용자 생성 실패", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



# 모든 사용자 조회
@api_view(['GET'])
def get_all_users(request):
   user = User.objects.all()
   serializer = UserSerializer(user, many=True)
   return Response(serializer.data, status=status.HTTP_200_OK)

# 사용자 생성
@api_view(['POST'])
def create_user(request):
   serializer = UserSerializer(data=request.data)
   if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ID로 사용자 조회
@api_view(['GET'])
def get_user_by_id(request, id):
   try:
       user = User.objects.get(id=id)
       serializer = UserSerializer(user)
       return Response(serializer.data, status=status.HTTP_200_OK)
   except User.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)

# 사용자 이름으로 조회
@api_view(['GET'])
def get_users_by_name(request, name):
   user = User.objects.filter(name=name)
   serializer = UserSerializer(user, many=True)
   return Response(serializer.data, status=status.HTTP_200_OK)

# 특정 나이 이상의 사용자 조회
@api_view(['GET'])
def get_users_by_age_gte(request, age):
   user = User.objects.filter(age__gte=age)
   serializer = UserSerializer(user, many=True)
   return Response(serializer.data, status=status.HTTP_200_OK)

# 사용자 삭제
@api_view(['DELETE'])
def delete_user_by_id(request, id):
   try:
       user = User.objects.get(id=id)
       user.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
   except User.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)

