#mangesh.ghaisas@merucapitals.com
from collections import defaultdict

class new_order:
    def __init__(self, order_id, side, price, quantity):
        self.order_id = order_id
        self.side = side
        self.price = price
        self.quantity = quantity

    def update(self, new_price=None, new_quantity=None):
        if new_price is not None:
            self.price = new_price
        if new_quantity is not None:
            self.quantity = new_quantity

class change_order:
    def __init__(self, order_id, new_price=None, new_quantity=None):
        self.order_id = order_id
        self.new_price = new_price
        self.new_quantity = new_quantity

class cancel_order:
    def __init__(self, order_id):
        self.order_id = order_id



class OrderBook:
    def __init__(self):
        self.buy_orders =defaultdict(int)
        self.sell_orders = defaultdict(int)

    def OnNewOrder(self, order):
        if order.side == 'B':
            # Check if the order_id exists in buy_orders
            if order.order_id in self.buy_orders:
                # Update quantity of existing buy order
                self.buy_orders[order.order_id].quantity += order.quantity
            else:
                # Create a new order object and store it
                self.buy_orders[order.order_id] = order
        elif order.side == 'S':
            # Check if the order_id exists in sell_orders
            if order.order_id in self.sell_orders:
                # Update quantity of existing sell order
                self.sell_orders[order.order_id].quantity += order.quantity
            else:
                # Create a new order object and store it
                self.sell_orders[order.order_id] = order      




    def OnChangeOrder(self, order):
        if order.order_id in self.buy_orders:
            old_order = self.buy_orders[order.order_id]
            old_order.update(new_price=order.new_price, new_quantity=order.new_quantity)

        elif order.order_id in self.sell_orders:
            old_order = self.sell_orders[order.order_id]
            old_order.update(new_price=order.new_price, new_quantity=order.new_quantity)




    def OnCancelOrder(self, order):
        if order.order_id in self.buy_orders:
            del self.buy_orders[order.order_id]
            

        elif order.order_id in self.sell_orders:
            del self.sell_orders[order.order_id]
           

    
    
    def Print(self):
        print("Buys")
        sorted_buy_orders = sorted(self.buy_orders.values(), key=lambda x: x.price, reverse=True)
        for order in sorted_buy_orders:
            print(f"Order ID: {order.order_id}, Side: {order.side}, Price: {order.price}, Quantity: {order.quantity}")

        print("\nSells")
        sorted_sell_orders = sorted(self.sell_orders.values(), key=lambda x: x.price)
        for order in sorted_sell_orders:
            print(f"Order ID: {order.order_id}, Side: {order.side}, Price: {order.price}, Quantity: {order.quantity}")



order_book = OrderBook()





#Testing

# Adding new orders

order_book.OnNewOrder(new_order(order_id=2, side='B', price=100, quantity=3000))
order_book.OnNewOrder(new_order(order_id=3, side='S', price=102, quantity=7000))
order_book.OnNewOrder(new_order(order_id=4, side='S', price=101, quantity=4000))
order_book.OnNewOrder(new_order(order_id=1, side='B', price=100, quantity=2000)) 

# Printing the order book
order_book.Print()

# Changing an order
order_book.OnChangeOrder(change_order(order_id=1, new_price=99, new_quantity=2000))


# Printing the updated order book
order_book.Print()


# Changing an order
order_book.OnChangeOrder(change_order(order_id=1, new_quantity=1000))




# Printing the updated order book
order_book.Print()


#Cancelling an order
order_book.OnCancelOrder(cancel_order(order_id=2))

# Printing the updated order book
order_book.Print()