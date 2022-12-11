class laptop:

    def __init__(self,name,processor):
        self.name=name
        self.processor=processor

    def printo(self):
        print("My laptop name is:",self.name,"and the processor is:",self.processor)

laptop1=laptop("asus","i7")
laptop2=laptop("dell","i9")

laptop1.printo()
laptop2.printo()