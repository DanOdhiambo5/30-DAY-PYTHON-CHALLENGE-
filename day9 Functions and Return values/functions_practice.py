def service_offer(skill, price, delivery):
    return f"Service: {skill} | Price: KES {price} | Delivery: {delivery} days"


print(service_offer("Python Automation", 1500, 3))
print(service_offer("Web Development", 5000, 7))