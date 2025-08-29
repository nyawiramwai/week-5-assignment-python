class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery
    
    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}... 📞")
    
    def charge(self, percent):
        self.battery += percent
        if self.battery > 100:
            self.battery = 100
        print(f"{self.brand} {self.model} charged to {self.battery}% 🔋")
class SmartphonePro(Smartphone):
    def __init__(self, brand, model, storage, battery, camera_quality):
        # Reuse parent attributes with super()
        super().__init__(brand, model, storage, battery)
        self.camera_quality = camera_quality
    def call(self, number):
        print(f"{self.brand} {self.model} (Pro) is video calling {number} in HD 🎥")
    
    def take_photo(self):
        print(f"📸 Taking a photo with {self.camera_quality}MP camera!")
