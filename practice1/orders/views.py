from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Orders
from .serializers import OrdersSerializer


# # 기본 뷰
# @api_view(['GET'])
# def order_list(request):
#     return Response({"message": "Orders API is working!"})
@api_view(['GET'])
def order_list(request, id=None):
    if request.method == 'GET':
        orders = Orders.objects.all()
        if not orders.exists():
            return Response({"message": "주문내역이 없습니다."}, status=status.HTTP_204_NO_CONTENT)
        serializer = OrdersSerializer(orders, many=True)
        return Response({"message": "주문 목록 조회 성공", "orders": serializer.data}, status=status.HTTP_200_OK)


# 모든 주문 조회
@api_view(['GET'])
def get_all_orders(request):
    orders = Orders.objects.all()
    serializer = OrdersSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 주문 생성
@api_view(['POST'])
def create_order(request):
    serializer = OrdersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ID로 사용자 조회
@api_view(['GET'])
def get_order_by_id(request, id):
    try:
        orders = Orders.objects.get(id=id)
        serializer = OrdersSerializer(orders)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Orders.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


# 사용자 이름으로 조회
@api_view(['GET'])
def get_order_by_name(request, name):
    orders = Orders.objects.filter(name=name)
    serializer = OrdersSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 특정 나이 이상의 사용자 조회
@api_view(['GET'])
def get_order_by_age_gte(request, age):
    orders = Orders.objects.filter(age__gte=age)
    serializer = OrdersSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



# 주문 삭제 (URL 파라미터 사용)
@api_view(['DELETE', 'POST', 'GET'])  # ✅ GET 요청도 허용
def delete_order_by_id(request):
    if request.method in ['POST', 'GET']:  # ✅ POST 또는 GET 요청을 DELETE로 변환
        id = request.GET.get('id') or request.POST.get('id')  # URL 또는 Body에서 ID 가져오기
    else:
        id = request.GET.get('id')  # 기존 방식 (DELETE 요청에서 'id' 값 가져오기)

    if not id:
        return Response({"message": "주문 ID를 입력하세요."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        order = Orders.objects.get(id=int(id))
        order.delete()
        return Response({"message": "주문이 성공적으로 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)
    except Orders.DoesNotExist:
        return Response({"message": "해당 주문이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)
    except ValueError:
        return Response({"message": "유효한 주문 ID를 입력하세요."}, status=status.HTTP_400_BAD_REQUEST)
