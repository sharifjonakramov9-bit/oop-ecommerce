# 🛒 OOP eCommerce Project

Bu loyiha — **Python OOP (Object-Oriented Programming)** konseptlarini amaliy o‘rganish uchun yaratilgan kichik **eCommerce (online shop)** modeli.
Loyiha orqali siz **class**, **object**, **inheritance**, **composition**, **encapsulation** kabi OOP tushunchalarini real hayotdagi “do‘kon” misolida o‘rganasiz.

---

## 🎯 Maqsad

* OOP’ni amaliy yo‘l bilan tushunish
* Real hayotdagi tizimni Python orqali modellashtirish
* Class’lar o‘rtasidagi **munosabatlar**ni (relationship) ko‘rsatish:

  * “Shop”da ko‘p “Product” bo‘ladi
  * “Customer” “Order” yaratadi
  * “Order” ichida ko‘p “OrderItem” bo‘ladi

---

## 🧱 Model (Class) tuzilmasi

### 1. `Product`

* Mahsulot haqidagi ma’lumotni ifodalaydi.
* **Fields:**

  * `name` — mahsulot nomi
  * `price` — narxi
  * `stock` — ombordagi miqdor
* **Methods:**

  * `reduce_stock(quantity)` — mahsulot sotilganda miqdorni kamaytiradi

---

### 2. `Customer`

* Xaridor haqidagi ma’lumotni saqlaydi.
* **Fields:**

  * `name` — xaridor ismi
  * `balance` — mablag‘i
* **Methods:**

  * `add_balance(amount)` — balansga pul qo‘shish
  * `deduct_balance(amount)` — xarid paytida balansdan pul yechish

---

### 3. `OrderItem`

* Buyurtmadagi bitta mahsulotni bildiradi.
* **Fields:**

  * `product` — `Product` obyekti
  * `quantity` — nechta olinayotganini bildiradi
* **Methods:**

  * `get_total()` — jami summa (`product.price * quantity`)

---

### 4. `Order`

* Xaridor tomonidan yaratilgan buyurtma.
* **Fields:**

  * `customer` — `Customer` obyekti
  * `items` — `OrderItem` obyektlar ro‘yxati
* **Methods:**

  * `add_item(product, quantity)` — buyurtmaga mahsulot qo‘shish
  * `calculate_total()` — buyurtma umumiy summasini hisoblash
  * `complete_order()` — buyurtmani yakunlash (balans va omborni yangilaydi)

---

### 5. `Shop`

* Umumiy do‘konni bildiradi.
* **Fields:**

  * `name` — do‘kon nomi
  * `products` — mavjud mahsulotlar ro‘yxati
  * `customers` — ro‘yxatdan o‘tgan xaridorlar
* **Methods:**

  * `add_product(product)` — do‘konga mahsulot qo‘shish
  * `add_customer(customer)` — yangi xaridor qo‘shish
  * `show_products()` — mavjud mahsulotlarni chiqarish

---

## ⚙️ Misol ishlatish

```python
from models import Product, Customer, Order, Shop

# Do‘kon yaratish
shop = Shop("TechStore")

# Mahsulotlar
laptop = Product("Laptop", 1200, 5)
mouse = Product("Mouse", 25, 30)
shop.add_product(laptop)
shop.add_product(mouse)

# Xaridor
user = Customer("Ali", 2000)
shop.add_customer(user)

# Buyurtma yaratish
order = Order(user)
order.add_item(laptop, 1)
order.add_item(mouse, 2)

# Umumiy summa
print("Total:", order.calculate_total())

# Buyurtmani yakunlash
order.complete_order()
```

---

## 🧠 OOP tushunchalari

| OOP Konsepti      | Qayerda ishlatilgan                 | Tavsif                                        |
| ----------------- | ----------------------------------- | --------------------------------------------- |
| **Class**         | `Product`, `Customer`, `Order`, ... | Har bir model uchun alohida class             |
| **Object**        | `laptop = Product(...)`             | Har bir mahsulot yoki xaridor obyekt sifatida |
| **Composition**   | `Order` ichida `OrderItem`          | Katta obyektlar kichik obyektlardan tuzilgan  |

---

## 🧩 Kengaytirish g‘oyalari

* 🏷️ Mahsulotga **kategoriya** qo‘shish
* 💳 Balansga **to‘lov tizimi** qo‘shish
* 📦 **Foydalanuvchi interfeysi** (CLI yoki GUI) yaratish
* 🧾 Buyurtmalar tarixini saqlash

---

## 📚 Talabalar uchun topshiriqlar

1. `Product` classiga `__str__` method qo‘shing — mahsulotni chiroyli ko‘rsatish uchun.
2. `Order` classida chegirma funksiyasi yarating.
3. `Shop` classida mahsulotlarni **narx bo‘yicha saralash** methodini yozing.
4. Balans yetarli bo‘lmasa, `complete_order()` xatolik chiqarsin.
