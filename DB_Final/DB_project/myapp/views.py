from django.shortcuts import render
from django.http import JsonResponse
from myapp import models
import random
from myapp.models import Ticket, Customer, Shows
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
import random
import string
import traceback

def index(request):
    context = {}
    
   # 上映中電影 - 隨機選 5 部上映中電影
    now_showing = models.Movie.objects.filter(status="上映中")
    now_showing_random = random.sample(list(now_showing), min(5, len(now_showing)))
    context["now_showing_random"] = now_showing_random

    # 所有電影 - 隨機選 6 部所有電影
    all_movies = models.Movie.objects.all()
    random_movies = random.sample(list(all_movies), min(6, len(all_movies)))
    context["random_movies"] = random_movies

    # 快速訂票 - 傳遞所有上映中的電影
    context["now_showing_movies"] = now_showing

    return render(request, 'index.html', context)


def search_order(request):
    query = request.GET.get('query', '')
    orders = []
    if query:
        # 將模糊匹配改為完全匹配
        tickets = models.Ticket.objects.filter(phone=query)
        for ticket in tickets:
            show = models.Shows.objects.filter(show_id=ticket.show_id).first()
            customer = models.Customer.objects.filter(phone=ticket.phone).first()
            if show:
                movie = models.Movie.objects.filter(movie_id=show.movie_id.movie_id).first()
                orders.append({
                    "customer_name": customer.name if customer else "未知客戶",
                    "customer_phone": customer.phone if customer else "未知電話",
                    "movie_title": movie.title_ch if movie else "未知電影",
                    "branch": show.branch,
                    "showtime": show.show_time,
                    "verify_code": ticket.verify_code,
                    "selected_seats": [{"row": ticket.seat_row, "col": ticket.seat_col}]
                })
    return render(request, 'search_order.html', {'orders': orders, 'query': query})




def get_branches_by_movie(request, movie_id):
    branches = models.Shows.objects.filter(movie_id=movie_id).values_list('branch', flat=True).distinct()
    return JsonResponse(list(branches), safe=False)

def get_showtimes_by_movie_and_branch(request, movie_id, branch):
    showtimes = models.Shows.objects.filter(
        movie_id=movie_id,
        branch=branch
    ).values('show_id', 'show_time')

    return JsonResponse(list(showtimes), safe=False)

def get_seats_for_show(request, show_id):
    booked_seats = models.Seat.objects.filter(show_id=show_id).values('row', 'col')
    return JsonResponse({'booked_seats': list(booked_seats)})


def generate_verification_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

@csrf_exempt
def submit_ticket(request):
    if request.method == 'POST':
        try:
            # 獲取 POST 資料
            phone = request.POST.get('phone')
            name = request.POST.get('name')
            show_id = request.POST.get('show_id')
            seat_row = request.POST.get('seat_row')
            seat_col = request.POST.get('seat_col')

            # 驗證電話號碼
            if not phone or len(phone) != 9 or not phone.isdigit():
                return JsonResponse({'error': '電話號碼必須為 9 位數字。'}, status=400)

            # 驗證資料
            if not all([phone, name, show_id, seat_row, seat_col]):
                return JsonResponse({'error': '缺少必要的參數'}, status=400)

            # 新增或更新客戶資料
            customer, created = models.Customer.objects.get_or_create(phone=phone)
            customer.name = name
            customer.save()

            # 檢查座位是否已被預訂
            if models.Seat.objects.filter(show_id=show_id, row=seat_row, col=seat_col).exists():
                return JsonResponse({'error': '該座位已被預訂'}, status=400)

            # 儲存座位資料
            models.Seat.objects.create(
                show_id=show_id,
                row=seat_row,
                col=seat_col
            )

            # 後端生成驗證碼
            verify_code = generate_verification_code()

            # 儲存訂單
            models.Ticket.objects.create(
                verify_code=verify_code,
                phone=phone,
                show_id=show_id,
                seat_row=seat_row,
                seat_col=seat_col,
                booking_time=now()
            )

            return JsonResponse({'success': '訂單已成功提交', 'verify_code': verify_code})

        except Exception as e:
            print(traceback.format_exc())  # 輸出詳細堆疊錯誤
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': '僅接受 POST 請求'}, status=405)




@csrf_exempt
def cancel_order(request):
    if request.method == 'POST':
        try:
            phone = request.POST.get('phone')
            verify_code = request.POST.get('verify_code')

            # 驗證資料
            if not all([phone, verify_code]):
                return JsonResponse({'error': '缺少必要的參數'}, status=400)

            # 找到對應的 Ticket
            ticket = models.Ticket.objects.filter(phone=phone, verify_code=verify_code).first()

            if not ticket:
                return JsonResponse({'error': '未找到符合條件的訂單'}, status=404)

            # 刪除對應的座位記錄
            models.Seat.objects.filter(show_id=ticket.show_id, row=ticket.seat_row, col=ticket.seat_col).delete()

            # 刪除 Ticket 資料
            ticket.delete()

            # 如果客戶不再有其他訂單，刪除 Customer 資料
            if not models.Ticket.objects.filter(phone=phone).exists():
                models.Customer.objects.filter(phone=phone).delete()

            return JsonResponse({'success': '訂單已成功取消'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': '僅接受 POST 請求'}, status=405)


def quick_order(request):
    movie_id = request.GET.get('movie_id', None)
    context = {}

    # 傳遞所有上映中的電影
    now_showing = models.Movie.objects.filter(status="上映中")
    context["now_showing_movies"] = now_showing

    # 預選中的電影
    if movie_id:
        selected_movie = models.Movie.objects.filter(movie_id=movie_id).first()
        context["selected_movie"] = selected_movie

    return render(request, 'quick_order.html', context)

def get_showtimes_by_movie_and_branch(request, movie_id, branch):
    showtimes = models.Shows.objects.filter(
        movie_id=movie_id,
        branch=branch
    ).values('show_id', 'show_time')

    formatted_showtimes = [
        {
            'show_id': showtime['show_id'],
            'show_time': showtime['show_time'].strftime("%Y-%m-%d %H:%M") if showtime['show_time'] else ''
        }
        for showtime in showtimes
    ]

    return JsonResponse(formatted_showtimes, safe=False)



def check_phone(request):
    phone = request.GET.get('phone', '')

    if phone and len(phone) == 9 and phone.isdigit():
        customer = Customer.objects.filter(phone=phone).first()
        if customer:
            return JsonResponse({'exists': True, 'name': customer.name}, status=200)
    return JsonResponse({'exists': False, 'name': ''}, status=200)

from django.shortcuts import render
from myapp.models import Movie

def movie_page(request):
    query = request.GET.get('query', '')
    if query:
        # 當有搜尋時，過濾電影
        movies = Movie.objects.filter(title_ch__icontains=query)
        is_search = True
    else:
        # 當沒有搜尋時，顯示所有電影
        movies = Movie.objects.all()
        is_search = False

    return render(request, 'movie_page.html', {'movies': movies, 'is_search': is_search, 'query': query})

