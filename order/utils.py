from cart.models import CartItem

def get_total_amount(request):
    carts=CartItem.objects.filter(user=request.user)
    if carts:
        total_amount=0
        for cart in carts:
            total_amount+=cart.product.price*cart.quantity
            
        return total_amount
    else:
        return 0
        
    