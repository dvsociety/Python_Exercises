"""
Ejercicio 8.7.4. Sistema de facturación simplificado
Se cuenta con una lista ordenada de productos, en la que uno consiste en una tupla de 
(identificador, descripción, precio), y una lista de los productos a facturar, 
en la que cada uno consiste en una tupla de (identificador, cantidad).
Se desea generar una factura que incluya la cantidad, la descripción, el precio unitario y 
el precio total de cada producto comprado, y al final imprima el total general.
Escribir una función que reciba ambas listas e imprima por pantalla la factura solicitada.
"""

def simple_billing(ordered_products: list, invoice_products: list):
    final_invoice = []
    general_price = 0

    for product in range(len(ordered_products)):
        if ordered_products[product][0] == invoice_products[product][0]:
            total_price = ordered_products[product][2] * invoice_products[product][1]
            final_invoice.append((ordered_products[product][0],ordered_products[product][1],ordered_products[product][2], total_price))

    for i in final_invoice:
        general_price += i[3]

    return final_invoice, general_price

ordered_products = [(4004,"Pasta dental",350),(2494,"Cepillo de dientes",600)]
invoice_products = [(4004,50),(2494,30)]
print(simple_billing(ordered_products,invoice_products))
