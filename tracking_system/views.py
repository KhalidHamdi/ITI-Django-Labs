from django.shortcuts import render, redirect
from openpyxl import load_workbook

EXCEL_FILE = 'tracking_system/data/orders.xlsx'

def read_excel():
    wb = load_workbook(EXCEL_FILE)
    ws = wb.active
    orders = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        order = {
            'orderID': row[0],
            'orderName': row[1],
            'username': row[2],
            'status': row[3],
        }
        orders.append(order)
    return orders

def tracking(request):
    orders = read_excel()

    if request.method == 'POST':
        selected_order_ids = request.POST.getlist('selected_orders')

        selected_orders = [order for order in orders if str(order['orderID']) in selected_order_ids]

        request.session['cart'] = selected_orders

        return redirect('cart')  

    return render(request, 'tracking.html', {'orders': orders})


