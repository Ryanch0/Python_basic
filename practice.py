
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print(f"{self.name}유닛이 생성 되었습니다.")
#         print(f"체력 {self.hp},공격력 {self.damage}")

# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#     def attack(self,location):
#         print(f"{self.name}:{location} 방향으로 적군을 공격합니다.[공격력{self.damage}]")
    

class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    
    def show_detail(self):
        print(f"{self.location} {self.house_type} {self.deal_type} {self.price} {self.completion_year}")


House("강남","아파트","매매","10억","2010년").show_detail()