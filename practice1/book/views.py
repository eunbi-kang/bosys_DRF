from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Book
from .serializers import BookSerializer

# # 기본 뷰
# @api_view(['GET'])
# def book_list(request):
#     return Response(
#         {"message": "Book API is working!"}
#     )

# 기본 뷰
@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        if not books.exists():
            return Response({"message": "책이 없습니다."}, status=status.HTTP_204_NO_CONTENT)
        serializer = BookSerializer(books, many=True)
        return Response({"message": "도서 목록 조회 성공", "books": serializer.data}, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            book = serializer.save()
            return Response({"message": "도서가 추가 되었습니다.", "book": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "도서 추가 실패", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



# 모든 사용자 조회
@api_view(['GET'])
def get_all_books(request):
   book = Book.objects.all()
   serializer = BookSerializer(book, many=True)
   return Response(serializer.data, status=status.HTTP_200_OK)

# 사용자 생성
@api_view(['POST'])
def create_book(request):
   serializer = BookSerializer(data=request.data)
   if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ID로 사용자 조회
@api_view(['GET'])
def get_book_by_id(request, id):
   try:
       book = Book.objects.get(id=id)
       serializer = BookSerializer(book)
       return Response(serializer.data, status=status.HTTP_200_OK)
   except Book.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)

# 사용자 이름으로 조회
@api_view(['GET'])
def get_books_by_name(request, name):
   book = Book.objects.filter(name=name)
   serializer = BookSerializer(book, many=True)
   return Response(serializer.data, status=status.HTTP_200_OK)

# 특정 나이 이상의 사용자 조회
@api_view(['GET'])
def get_books_by_age_gte(request, age):
   book = Book.objects.filter(age__gte=age)
   serializer = BookSerializer(book, many=True)
   return Response(serializer.data, status=status.HTTP_200_OK)

# # 사용자 삭제
@api_view(['DELETE'])
def delete_book_by_id(request, id):
   try:
       book = Book.objects.get(id=id)
       book.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
   except Book.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)

# 도서 삭제 (URL 파라미터 사용)
@api_view(['DELETE', 'POST', 'GET'])  # ✅ DELETE, POST, GET 요청 모두 허용
def delete_book_by_id(request):
    if request.method in ['POST', 'GET']:  # ✅ POST 또는 GET 요청을 DELETE로 변환
        id = request.GET.get('id') or request.POST.get('id')  # URL 또는 Body에서 ID 가져오기
    else:
        id = request.GET.get('id')  # 기존 방식 (DELETE 요청에서 'id' 값 가져오기)

    if not id:
        return Response({"message": "도서 ID를 입력하세요."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        book = Book.objects.get(id=int(id))
        book.delete()
        return Response({"message": "도서가 성공적으로 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)
    except Book.DoesNotExist:
        return Response({"message": "해당 도서가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)
    except ValueError:
        return Response({"message": "유효한 도서 ID를 입력하세요."}, status=status.HTTP_400_BAD_REQUEST)
