import datetime


class Product:
    def __init__(self, name="Unknown", price=0, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity
        print(f"Ürün oluşturuldu: {self.name}, Tarih: {datetime.datetime.now()}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not (3 <= len(value) <= 8):
            raise ValueError("Ürün adı 3 ile 8 karakter arasında olmalıdır.")
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Ürün fiyatı 0 veya daha büyük olmalıdır.")
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 1:
            raise ValueError("Ürün miktarı 1 veya daha büyük olmalıdır.")
        self._quantity = value

    def get_total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"Ürün: {self.name}, Fiyat: {self.price}, Adet: {self.quantity}"


class ProductHelper:
    @staticmethod
    def create_item_from_text(file_path):
        products = []
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                name, price, quantity = line.strip().split(',')
                products.append(Product(name, float(price), int(quantity)))
        return products

    @staticmethod
    def get_total_balance(products):
        total = sum(product.get_total_price() for product in products)
        return total * 1.2  # %20 KDV ekleniyor.


# Örnek Kullanım
if __name__ == "__main__":
    # Ürün oluşturma
    product1 = Product("Laptop", 1500, 2)
    product2 = Product("Mouse", 50, 5)
    print(product1)
    print(f"Toplam Fiyat: {product1.get_total_price()}")

    # Dosyadan ürün oluşturma
    file_path = "Products.txt"  # Dosya yolunu buraya ekleyin
    try:
        products = ProductHelper.create_item_from_text(file_path)
        print(f"Ürünler: {[str(product) for product in products]}")
        print(f"Toplam Bakiye (KDV Dahil): {ProductHelper.get_total_balance(products)}")
    except FileNotFoundError:
        print("Belirtilen dosya bulunamadı.")
