"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""


data = [
  {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
  {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
  {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def sales_sum(items_sold):
  sales_sum = 0
  for item in items_sold:
    sales_sum += item
  return sales_sum

def sales_avg(items_sold):
  sales_sum = 0
  for item in items_sold:
    sales_sum += item
  return round(sales_sum / len(items_sold), 1)

all_sales_sum = 0
for one_product in data:
  product_sales_sum = sales_sum(one_product['items_sold'])
  print(f'Total sales of {one_product["product"]}: ', product_sales_sum)
  product_sales_avg = sales_avg(one_product['items_sold'])
  print(f'Average sales of {one_product["product"]}: ',product_sales_avg)
  all_sales_sum += product_sales_sum 
  
print(f'Total sales of all products: ', all_sales_sum)
print(f'Average sales of all products: ', all_sales_sum / len(data))
