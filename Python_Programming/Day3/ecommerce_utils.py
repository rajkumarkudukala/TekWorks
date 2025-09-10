#ecommerce_utils.py
def apply_discount(total, discount):
    return total-(total*discount/100)

def add_gst(total, gst):
    return total+(total*gst/100)

def generate_invoice(cart):
    subtotal = 0
    for i in cart:
        subtotal+=cart[i]
    discount = apply_discount(subtotal, 10)
    gst = add_gst(discount, 18)
    print("------INVOICE-------------------------")
    for i in cart:
        print(i,cart[i],sep="   :  ")
    print("---------------------------------------")
    print("subtotal: ",subtotal)
    print(f"After 10% discount:",discount)
    print(f"After 18% GST:",gst)
    print("---------------------------------------")
    print("Thank you for shopping with us!")
