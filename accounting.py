customer_file = open("customer-orders.txt")
melon_cost = 1.00

def process_customer(text, melon_cost):
    list_of_lists = []
    for line in text:
        line = line.rstrip()
        tokens = line.split("|")
        list_of_lists.append(tokens)
    print list_of_lists

    for customer in list_of_lists:
        melon_qty = float(customer[2])
        if melon_qty*melon_cost != float(customer[3]):
            print customer[1], "paid {:.2f}, expected {:.2f}".format(
        float(customer[3]), (melon_qty*melon_cost))

process_customer(customer_file, melon_cost)

#def process_orders(text):
  #  customers = {}

    




customer1_name = "Joe"
customer1_melons = 5
customer1_paid = 5.00

customer2_name = "Frank"
customer2_melons = 6
customer2_paid = 6.00

customer3_name = "Sally"
customer3_melons = 3
customer3_paid = 3.00

customer4_name = "Shawna"
customer4_melons = 9
customer4_paid = 9.50

customer5_name = "David"
customer5_melons = 4
customer5_paid = 4.00

customer6_name = "Ash"
customer6_melons = 3
customer6_paid = 2.00

customer1_expected = customer1_melons * melon_cost
if customer1_expected != customer1_paid:
    print customer1_name, "paid {:.2f}, expected {:.2f}".format(
        customer1_paid, customer1_expected)

customer2_expected = customer2_melons * melon_cost
if customer2_expected != customer2_paid:
    print customer2_name, "paid {:.2f}, expected {:.2f}".format(
        customer2_paid, customer2_expected)

customer3_expected = customer3_melons * melon_cost
if customer3_expected != customer3_paid:
    print customer3_name, "paid {:.2f}, expected {:.2f}".format(
        customer3_paid, customer3_expected)

customer4_expected = customer4_melons * melon_cost
if customer4_expected != customer4_paid:
    print customer4_name, "paid {:.2f}, expected {:.2f}".format(
        customer4_paid, customer4_expected)

customer5_expected = customer5_melons * melon_cost
if customer5_expected != customer5_paid:
    print customer5_name, "paid {:.2f}, expected {:.2f}".format(
        customer5_paid, customer5_expected)

customer6_expected = customer6_melons * melon_cost
if customer6_expected != customer6_paid:
    print customer6_name, "paid {:.2f}, expected {:.2f}".format(
        customer6_paid, customer6_expected)
