from dataclasses import dataclass

@dataclass
class Product:
    name : str
    price : float

@dataclass
class InvoiceDetail:
    product: Product
    quantity: int

    def subtotal(self):
        return self.product.price * self.quantity
    
@dataclass
class Invoice:
    details: list[InvoiceDetail]

    def add_product(self, product):
        self.details.append(product)
    
    def total(self):
        total = 0
        for detail in self.details:
            total += detail.subtotal()
        
        return total

    def show(self):
        for detail in self.details:
            print(f"{detail.product.name} - {detail.product.price} - {detail.quantity} - {detail.subtotal()}")

agua = Product("Agua 1LT", 25.5)
detail_1= InvoiceDetail(agua, 5)

factura = Invoice(details=[detail_1])
factura.show()
