from .models import Card
from rest_framework.views import APIView
from .serializers import CardSerializer
from rest_framework.response import Response
from django.shortcuts import  get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib  import  messages


class CardsApiView(APIView):
    def get(self, request):
        cards=Card.objects.all()
        serializer=CardSerializer(cards,many=True)
        return Response(serializer.data)
    
class  OneCardApiView(APIView):
    def post(self,request):
        if "card_number" not in request.data:
            data={

                "status":False,
                "message":"card_number is required"
            }
            return Response(data)
        card_number=request.data['card_number']

        card=get_object_or_404(Card,card_number=card_number)

        serializer=CardSerializer(card)
        return Response(serializer.data)
    




















    

# class LoginView(View):
#     def get(self, request):  

#         form = LoginForm()
#         return render(request,'login.html',context={'form':form})
    
#     def post(self, request):
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username=form.cleaned_data['username']
#             password=form.cleaned_data['password']
         
#             user=authenticate(username=username ,password=password)
#             if user is not None:
#                 login(request,user)
#                 messages.success(request,"siz muvaffaqiyatli kirdingiz")

#             return redirect('landing_page')
#         return render(request,'login.html',context={'form':form})    
# class LogoutView(LoginRequiredMixin,View):
#     def get(self, request):
#         logout(request)
#         messages.success(request,"siz muvaffaqiyatli  logout qildingiz")
#         return redirect('landing_page') 


    

# class RegisterView(View):
#     def get(self, request):  

#         form = RegisterForm()
#         return render(request,'register.html',context={'form':form})
    

#     def post(self, request):
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user=form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             return redirect('landing_page')
#         else:
#             return render(request,'register.html',context={'form':form})