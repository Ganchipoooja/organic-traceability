# Organic Food Traceability System

import datetime

class FoodItem:
    def __init__(self, item_id, name, origin):
        self.item_id = item_id
        self.name = name
        self.origin = origin
        self.history = []  # to store traceability records

    def add_record(self, stage, location, handler):
        record = {
            "stage": stage,
            "location": location,
            "handler": handler,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.history.append(record)

    def trace(self):
        print(f"\nTraceability Report for {self.name} (ID: {self.item_id})")
        print(f"Origin: {self.origin}")
        for record in self.history:
            print(f"- {record['stage']} at {record['location']} by {record['handler']} on {record['timestamp']}")


# Example usage
if __name__ == "__main__":
    # Create a food item
    apple = FoodItem(item_id="A1001", name="Organic Apple", origin="Green Valley Farm")

    # Add traceability records
    apple.add_record(stage="Harvested", location="Green Valley Farm", handler="Farmer Ramesh")
    apple.add_record(stage="Packed", location="Farm Packaging Unit", handler="Worker Anita")
    apple.add_record(stage="Transported", location="Local Distributor", handler="Logistics Co.")
    apple.add_record(stage="Stored", location="Organic Retail Store", handler="Store Manager")
    apple.add_record(stage="Purchased", location="Retail Store", handler="Customer Pooja")

    # Print traceability report
    apple.trace()
