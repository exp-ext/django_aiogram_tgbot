from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

User = get_user_model()


def page_not_found(request: HttpRequest, exception) -> HttpResponse:
    return render(request, 'core/404.html', {'path': request.path}, status=404)


def server_error(request: HttpRequest) -> HttpResponse:
    return render(request, 'core/500.html', status=500)


def permission_denied(request: HttpRequest, exception) -> HttpResponse:
    return render(request, 'core/403.html', status=403)


def csrf_failure(request: HttpRequest, reason='') -> HttpResponse:
    return render(request, 'core/403csrf.html')


def paginator_handler(request: HttpRequest,
                      query: QuerySet,
                      issuance: int = 12) -> Paginator:
    """
    Использует класс Django Paginator для создания объекта paginator,
    принимает:
    - request (:obj:`HttpRequest`) - запрос
    - query (:obj:`QuerySet`) - объект QuerySet
    - issuance (:obj:`int`) - необязательный аргумент, количество элементов
    в выдаче на странице. По умолчанию 12.

    Возвращает постраничный QuerySet, используя метод get_page объекта
    paginator.
    """
    paginator = Paginator(query, issuance)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)
