class Region:
    def __init__(self, name, total, male, female, house):
        # self : 자기 자신(객체) # self.필드명(객체변수)
        self.name = name
        self.total = total
        self.male = male
        self.female = female
        self.house = house
        self.malepercent = round((male/total)*100 , 1)
        self.femalepercent = round((female / total) * 100, 1)