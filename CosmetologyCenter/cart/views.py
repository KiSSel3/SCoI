from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartIssueAddForm
from services.models import Issue
# Create your views here.
@require_POST
def cart_add(request, issue_id):
    if not request.user.is_authenticated:
        raise PermissionDenied("No acceess")

    cart = Cart(request)
    issue = get_object_or_404(Issue, id=issue_id)
    form = CartIssueAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(issue=issue,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_details')

def cart_remove(request, issue_id):
    if not request.user.is_authenticated:
        raise PermissionDenied("No acceess")

    cart = Cart(request)
    book = get_object_or_404(Issue, id=issue_id)
    cart.remove(book)
    return redirect('cart:cart_details')
def cart_detail(request):
    if not request.user.is_authenticated:
        raise PermissionDenied("No acceess")
    cart = Cart(request)
    return render(request, 'cart/details.html', {'cart': cart})
