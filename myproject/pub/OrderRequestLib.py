from models import Decoration

class OrderRequest:
	decorationId=0
	productId=0
	
	def setDecorationId(self, decorationId):
		print decorationId, "2"
		self.decorationId=decorationId
		self.decoration=Decoration.objects.get(id=decorationId)

	def save(self, response):
		if self.decorationId!=0:
			response.set_cookie("did", self.decorationId)

	def load(self,request):
		if "did" in request.COOKIES:
			self.setDecorationId(int(request.COOKIES["did"]))
		if "did" in request.GET:			
			self.setDecorationId(int(request.GET["did"]))
			print self.decorationId, "3"

	def __init__(self, request):
		self.load(request)