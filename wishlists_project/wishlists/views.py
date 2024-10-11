from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import WishlistItem
from .forms import WishlistItemForm
from django.contrib.auth.models import User


@login_required
def wishlist_item_list(request):
    items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'wishlists/wishlist_item_list.html', {'items': items})


@login_required
def wishlist_item_create(request):
    if request.method == 'POST':
        form = WishlistItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('wishlists:wishlist_item_list')
    else:
        form = WishlistItemForm()
    return render(request, 'wishlists/wishlist_item_form.html', {'form': form})


@login_required
def wishlist_item_update(request, pk):
    item = get_object_or_404(WishlistItem, pk=pk, user=request.user)
    if request.method == 'POST':
        form = WishlistItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('wishlists:wishlist_item_list')
    else:
        form = WishlistItemForm(instance=item)
    return render(request, 'wishlists/wishlist_item_form.html', {'form': form})


@login_required
def wishlist_item_delete(request, pk):
    item = get_object_or_404(WishlistItem, pk=pk, user=request.user)
    if request.method == 'POST':
        item.delete()
        return redirect('wishlists:wishlist_item_list')
    return render(request, 'wishlists/wishlist_item_confirm_delete.html', {'item': item})


def wishlist_item_detail(request, username):
    try:
        user = User.objects.get(username=username)
        items = WishlistItem.objects.filter(user=user)
        return render(request, 'wishlists/wishlist_item_detail.html', {'user': user, 'items': items})
    except User.DoesNotExist:
        return render(request, 'wishlists/user_not_found.html', {'username': username})
