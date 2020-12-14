class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()

나 = 자식()

# 자식 클래스를 생성했고, 자식 클래스는 '자식생성' 이후 부모 클래스를 생성하므로
# 생성 순서는 '자식생성' \n '부모생성' 일 것 이다.