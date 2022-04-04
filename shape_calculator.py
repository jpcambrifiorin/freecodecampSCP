class Rectangle:
  def __init__(self,width,height):
    self.width=width
    self.height=height

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  def get_area(self):
    return self.width*self.height

  def get_perimeter(self):
    return self.width*2 + self.height*2

  def get_picture(self):
    if self.width >= 50 or self.height >=50:
      return "Too big for picture."
    
    retValue=""
    for i in range(self.height):
      retValue=retValue+"*"*self.width+"\n"    
    return retValue
  
  def get_diagonal(self):
    return ((self.width**2 + self.height**2) ** 0.5)

  def get_amount_inside(self,rect):
    if rect.width<=self.width and rect.height<=self.height:
      return int((self.width/rect.width)*(self.height/rect.height))
    return 0


  def set_width(self,width):
    self.width=width

  def set_height(self,height):
    self.height=height



class Square(Rectangle):
  
  def __init__(self,side):
    self.side=side
    Rectangle.__init__(self,side,side)

  def __str__(self):
    return f"Square(side={self.side})"

  def set_width(self,side):
    self.side=side
    super().set_width(side)
    super().set_height(side)

  def set_height(self,side):
    self.side=side
    super().set_width(side)
    super().set_height(side)
