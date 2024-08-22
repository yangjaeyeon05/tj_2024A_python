class Region:
    def __init__(self , 동이름 , 총인구수 , 남인구수 , 여인구수 , 세대수):
        self.동이름 = 동이름
        self.총인구수 = 총인구수
        self.남인구수 = 남인구수
        self.여인구수 = 여인구수
        self.세대수 = 세대수
    def 남자비율(self , 남인구수 , 총인구수):
        return round((남인구수 / 총인구수) * 100)
    def 여자비율(self , 여인구수 , 총인구수):
        return round((여인구수 / 총인구수) * 100)

# region = Region("부평1동" ,35141 , 16835 , 18306 , 16861 )
# result = region.남자비율(16835 ,35141)
# print(result)