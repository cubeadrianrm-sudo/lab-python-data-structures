products = ["t-shirt", "mug", "hat", "book", "keychain"]
customer_orders = set()

p1 = input("Elige el primer producto (t-shirt/mug/hat/book/keychain): ").strip().lower()
p2 = input("Elige el segundo producto (t-shirt/mug/hat/book/keychain): ").strip().lower()
p3 = input("Elige el tercer producto (t-shirt/mug/hat/book/keychain): ").strip().lower()

customer_orders.add(p1)
customer_orders.add(p2)
customer_orders.add(p3)

print(customer_orders)
