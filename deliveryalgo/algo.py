import order
import deliveryslot
import slotcollection

if __name__ == "__main__":
    #   new SlotCollection object filled with DeliverySlots
    sc = slotcollection.SlotCollection(12, 2)

    #   simulate a few arbitrary Orders
    ao1 = order.Order("123 Park Ave")
    ao2 = order.Order("15 Park Ave")
    ao3 = order.Order("20 Park Ave")
    ao4 = order.Order("456 Park Ave")
    ao4 = order.Order("456 5th Ave")

    #   add Orders to a DeliverySlot(hour, car)
    sc.addOrderToSlot(1, 1, ao1)
    sc.addOrderToSlot(1, 1, ao2)
    sc.addOrderToSlot(1, 1, ao3)
    sc.addOrderToSlot(1, 1, ao4)
    sc.addOrderToSlot(12, 2, ao4)
   
    #   check that slots have deliveries in them 
    fs = sc.getSlot(1,1)
    fs1 = sc.getSlot(12,2)
    print (len(fs.listOfOrders))
    print (len(fs1.listOfOrders))
    
    #   simulate adding the User's Order
    newUserOrder = order.Order("456 5th Ave")
    print (ao1.getDistance(newUserOrder))