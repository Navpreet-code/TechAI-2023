from django.shortcuts import render,redirect
from AIapp.models import FAQ
from AIapp.models import MyReview
from AIapp.models import Contactus
from AIapp.models import HelpandSupport
from AIapp.models import user_register,Blog,video,category,structure,initiative
from django.conf import settings
from django.core.mail import send_mail
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import country_converter as coco
import statsmodels.api as sm
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
#from statsmodels.tsa.arima.model import ARIMA
#from pmdarima.arima import auto_arima
import warnings
import itertools
import matplotlib
from io import BytesIO
import io
import base64
import requests
import time
from bs4 import BeautifulSoup




# Create your views here.

def Register(request):
	if request.method=="POST":
		Name=request.POST.get('nm')
		em=request.POST.get('em')
		Password=request.POST.get('pw')
		Cpass=request.POST.get('cpw')
		if user_register.objects.filter(Email=em).exists():
			ms="Email Already Exist"
			return render(request,'register.html',{'msg':ms})
		else:
			if Password==Cpass:
				X=user_register()
				X.Name=Name
				X.Email=em
				X.Password=Password
				X.save()
				ms="Registered Successfully"
				return render(request,'register.html',{'msg':ms})
			else:
				ms="Password And Confirm Password Does Not Match"
				return render(request,'register.html',{'msg':ms})
	else:
		return render(request,'register.html')

def login(request):
	if request.method=='POST':
		em=request.POST.get('em')
		pw=request.POST.get('pw')
		expert=user_register.objects.filter(Email=em,Password=pw)
		k=len(expert)
		if k>0:
			request.session['Email']=em
			return redirect('/Dashboard')
		else:
			return render(request,'login.html',{'msg':"Invalid Candidate"})
	else:
		return render(request,'login.html')

def ForgetPassword(request):
	if (request.method=='POST'):
		em=request.POST.get('em')
		user=user_register.objects.filter(Email=em)
		if (len(user)>0):
			pw=user[0].Password
			Subject="Password"
			Message="Welcome!Your Password is " + pw
			email_from=settings.EMAIL_HOST_USER
			recipient_list=[em]
			send_mail(Subject,Message,email_from,recipient_list)
			rest='Your Password is Sent to your respective Email Account.Please Check'
			return render(request,'Forget Password.html',{'rest':rest})
		else:
			res='This Email Id is Not Registered'
			return render(request,'Forget Password.html',{'res':res})
	else:
		return render(request,'Forget Password.html')

def index(request):
	data=Blog.objects.all()
	return render(request,'index.html',{'data':data})
def Footer(request):
	return render(request,'Footer.html')
def ChangePassword(request):
	if not request.session.has_key('Email'):
		return redirect('/Login/')
	if request.method=='POST':
		re=user_register.objects.get(Email=request.session['Email'])
		OldPassword=request.POST.get('opw')
		NewPassword=request.POST.get('npw')
		ConfirmPassword=request.POST.get('cpw')

		if(NewPassword==ConfirmPassword):
			pa=re.Password
			print(pa)

			if(OldPassword==pa):
				re.Password=NewPassword
				re.save()
				rest="Password Changed"
				return render(request,'Change Password.html',{'res':rest})
			else:
				res="Invalid Current Password"
				return render(request,'Change Password.html',{'res':res})
		else:
			res="Confirm Password And New Password Does not Match"
			return render(request,'Change Password.html',{'res':res})
	else:
		return render(request,'Change Password.html')

def Base(request):
	return render(request,'Base.html')
def View_FAQ(request):
	data=FAQ.objects.all()
	return render(request,'View_FAQ.html',{'data':data})
def Review(request):
	if not request.session.has_key('Email'):
		return redirect('/Login/')
	if request.method=="POST":
		X=MyReview()
		X.Title=request.POST.get('ti')
		X.Message=request.POST.get('msg')
		X.save()
		return render(request,'Review.html',{'Success':"Data Successfully Added"})
	else:
		return render(request,'Review.html')

def contactus(request):
	if request.method=="POST":
		X=Contactus()
		X.Name=request.POST.get('nm')
		X.Email=request.POST.get('em')
		X.Subject=request.POST.get('s1')
		X.Message=request.POST.get('msg')
		X.save()
		return render(request,'contact us.html',{'Success':"Data Successfully Added"})
	else:
		return render(request,'contact us.html')

def HelpAndSupport(request):
	if not request.session.has_key('Email'):
		return redirect('/Login/')
	if request.method=="POST":
		X=HelpandSupport()
		X.Title=request.POST.get('ti')
		X.Message=request.POST.get('msg')
		X.save()
		return render(request,'Help And Support.html',{'Success':"Data Successfully Added"})
	else:
		return render(request,'Help And Support.html')

def EditProfile(request):
	if not request.session.has_key('Email'):
		return redirect('/Login/')
	user=user_register.objects.get(Email=request.session['Email'])
	if request.method=='POST':
		user=user_register.objects.get(Email=request.session['Email'])
		user.Name=request.POST.get('nm')
		user.Age=request.POST.get('age')
		user.Gender=request.POST.get('gd')
		user.DOB=request.POST.get('dob')
		user.PhoneNo=request.POST.get('pn')
		user.save()

		# user=user_register.objects.get(Email=request.session['Email'])
		return redirect('/UserProfile',{'user':user})
	else:
		return render(request,'Edit Profile.html',{'user':user})

def UserProfile(request):
	if not request.session.has_key('Email'):
		return redirect('/Login/')	
		user=user_register.objects.get(Email=request.session['Email'])
		return render(request,'User Profile.html',{'user':user})

def Sidebar(request):
	return render(request,'Sidebar.html')

def Logout(request):
	if not request.session.has_key('Email'):
		return redirect('/Login/')
	del request.session['Email']
	return redirect('/Login/')

def ViewBlog(request):
	data=Blog.objects.all()
	return render(request,'View Blog.html',{'data':data})

def Videos(request):
	data=video.objects.all()
	return render(request,'Videos.html',{'data':data})

def DetailBlog(request,id):
	data=Blog.objects.get(id=id)
	return render(request,'Detail Blog.html',{'data':data})

def ViewAITool(request):
	data=category.objects.all()
	return render(request,'View AI_Tool.html',{'data':data})

def DetailAITool(request,name):
	data=structure.objects.filter(category_name=name)
	return render(request,'Detail AI_Tool.html',{'data':data})

def DetailAITool2(request,id):
	data=structure.objects.get(id=id)
	return render(request,'Detail AI_Tool 2.html',{'i':data})

def Latestnews(request):
	import datetime
	from datetime import date
	from newsapi.newsapi_client import NewsApiClient
	newsapi=NewsApiClient(api_key='d1342a766b9a4879b15e918c2a248cf2')
	json_data=newsapi.get_everything(q='Artificial Intelligence',
								     language='en',
								     from_param=str(date.today()-datetime.timedelta(days=29)),
								     to=str(date.today()),
								     page_size=24,
								     page=2,
								     sort_by='relevancy'
)
	k=json_data['articles']
	return render(request,'Latestnews.html',{'k':k})							     
 
def AboutUs(request):
	return render(request,'About Us.html')

def Initiative(request):
	data=initiative.objects.all()
	return render(request,'View Initiative.html',{'data':data})

def DetailInitiative(request,id):
	data=initiative.objects.get(id=id)
	return render(request,'Detail Initiative.html',{'data':data})

def Dashboard(request):
	return render(request,'Dashboard.html')

def Analysis1(request):
	return render(request,'View Analysis 1.html')

def Analysis2(request):
	return render(request,'View Analysis 2.html')

def Analysis3(request):
	return render(request,'View Analysis 3.html')

def Analysis4(request):
	return render(request,'View Analysis 4.html')

def MyProfile(request):
	if not request.session.has_key('Email'):
		return redirect('/Login')
	user=user_register.objects.get(Email=request.session['Email'])
	if request.method=="POST":
		print("yes")
		user.Profile=request.FILES['file1']
		user.save()
		return render(request,'My Profile.html',{'user':user,'msg':'success'})
	else:
		return render(request,'My Profile.html',{'user':user})

def DetailBillAnalysis1(request):
	if request.method=="POST":
		df=pd.read_csv('cumulative-numberof A.I bills-passed.csv')
		Entity=request.POST.get('entity')
		dfa=df[df['Entity']==Entity]
		title='AI Bills Passed In '+Entity
		fig = px.line(dfa, x="Year", y="number_ai_bills_cumulative", title=title)
		graph=fig.to_html()
		return render(request, 'Detail Bill Analysis 1.html',{'graph':graph})
	else:
		return render(request,'Detail Bill Analysis 1.html')

def handle_uploaded_file(f,name):
	destination= open(name,'wb+')
	for chunck in f.chunks():
		destination.write(chunk)
	destination.close()

def DetailBillAnalysis2(request):
	df=pd.read_csv('cumulative-numberof A.I bills-passed.csv')
	fig=px.scatter(df, x="Year", y="number_ai_bills_cumulative",
		size="number_ai_bills_cumulative", color="Entity",
		title="AI Bills Passed In Different Countries In Years",
		hover_name="Entity",log_x=True, size_max=60)
	graph=fig.to_html()
	return render(request,'Detail Bill Analysis 2.html',{'graph':graph})

def DetailBillAnalysis3(request):
	user=user_register.objects.get(Email=request.session['Email'])
	if request.method=="POST":
		df=pd.read_csv('cumulative-numberof A.I bills-passed.csv')
		d1=request.POST.get('entity')
		df1=df[df['Entity']==d1]
		d2=request.POST.get('entity1')
		df2=df[df['Entity']==d2]
		#Create Traces
		title='AI Bills Passed In Two Countries In Different Years. '
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=df1['Year'], y=df1['number_ai_bills_cumulative'],
			mode='lines',
			name=d1))
		fig.add_trace(go.Scatter(x=df2['Year'], y=df2['number_ai_bills_cumulative'],
			mode='lines+markers',
			name=d2))
		graph=fig.to_html()
		return render(request, 'Detail Bill Analysis 3.html',{'graph':graph})
	else:
		return render(request,'Detail Bill Analysis 3.html',{'user':user})

def DetailBillAnalysis4(request):
	if request.method=="POST":
		df=pd.read_csv('cumulative-numberof A.I bills-passed.csv')
		d1=request.POST.get('entity')
		df1=df[df['Entity']==d1]
		d2=request.POST.get('entity1')
		df2=df[df['Entity']==d2]
		d3=request.POST.get('entity2')
		df3=df[df['Entity']==d3]
		#Create Traces
		fig=go.Figure()

		fig.add_trace(go.Scatter(x=df1["Year"], y=df1['number_ai_bills_cumulative'],
			mode='lines+markers',
			name=d1))
		#fig.add_trace(go.Scatter(x=df1["Year"], y=df1['number_ai_bills_cumulative'],mode='lines+markers',name=d1))
		fig.add_trace(go.Scatter(x=df2["Year"], y=df2['number_ai_bills_cumulative'],
			mode='lines+markers',
			name=d2))
		fig.add_trace(go.Scatter(x=df3['Year'], y=df3['number_ai_bills_cumulative'],
			mode='lines+markers',
			name=d3))
		graph=fig.to_html()
		return render(request, 'Detail Bill Analysis 4.html',{'graph':graph})
	else:
		return render(request,'Detail Bill Analysis 4.html')

def DetailBillAnalysis5(request):
	if request.method=="POST":
		df=pd.read_csv('cumulative-numberof A.I bills-passed.csv')
		d1=request.POST.get('entity')
		df1=df[df['Entity']==d1]
		d2=request.POST.get('entity1')
		df2=df[df['Entity']==d2]
		sy=int(request.POST.get('sy'))
		ey=int(request.POST.get('ey'))
		df1=df1[(df1['Year']>=sy) & (df1['Year']<=ey)]
		df2=df2[(df2['Year']>=sy) & (df2['Year']<=ey)]
		#Create Traces
		fig=go.Figure()
		fig.add_trace(go.Scatter(x=df1['Year'], y=df1['number_ai_bills_cumulative'],
			mode='lines',
			name=d1))
		fig.add_trace(go.Scatter(x=df2['Year'], y=df2['number_ai_bills_cumulative'],
			mode='lines+markers',
			name=d2))
		graph=fig.to_html()
		return render(request, 'Detail Bill Analysis 5.html',{'graph':graph})
	else:
		return render(request,'Detail Bill Analysis 5.html')

def DetailBillAnalysis6(request):
	df=pd.read_csv('cumulative-numberof A.I bills-passed.csv')
	cc=coco.CountryConverter()
	df['Entity_codes']=coco.convert(names=df['Code'], to='ISO3')
	print(df['Entity_codes'])
	fig=px.scatter_geo(df, locations="Entity_codes", color="Entity",
						hover_name="Entity",size="number_ai_bills_cumulative",
						animation_frame='Year',
						projection="natural earth")	
	graph=fig.to_html()
	return render(request, 'Detail Bill Analysis 6.html',{'graph':graph})

def DetailBillAnalysis7(request):
	if request.method=="POST":
		df=pd.read_csv('cumulative-numberof A.I bills-passed.csv')
		year=int(request.POST.get('year'))
		print("year",year)
		df1=df[df["Year"]==year]
		df1=df1.dropna()
		print("df1",df1)
		df1=df1.sort_values(by='number_ai_bills_cumulative')
		n=int(request.POST.get('entity'))
		dfmax=df1.tail(n)
		print("dfmax",dfmax)
		fig=px.bar(dfmax, y='number_ai_bills_cumulative', x='Entity',
			title='Growth Of Countries In a Specific Year.')
		graph=fig.to_html()
		return render(request, 'Detail Bill Analysis 7.html',{'graph':graph})
	else:
		return render(request,'Detail Bill Analysis 7.html')

def DetailCompanyAnalysis1(request):
	if request.method=="POST":
		df=pd.read_csv('Annual Number of newly funded A.I companies.csv')
		Entity=request.POST.get('entity')
		dfa=df[df['Entity']==Entity]
		title='Annual Number Of Newly Funded AI Companies in ' + Entity
		fig=px.line(dfa, x="Year", y="newly_funded_ai_companies", title=title)
		graph=fig.to_html()
		return render(request,'Detail Company Analysis 1.html',{'graph':graph})
	else:
		return render(request,'Detail Company Analysis 1.html')

def DetailCompanyAnalysis2(request):
	if request.method=="POST":
		df=pd.read_csv('Annual Number of newly funded A.I companies.csv')
		d1=request.POST.get('entity')
		df1=df[df['Entity']==d1]
		d2=request.POST.get('entity1')
		df2=df[df['Entity']==d2]
		#Create Traces
		title='AI Bills Passed In '
		fig=go.Figure()
		fig.add_trace(go.Scatter(x=df1['Year'], y=df1['newly_funded_ai_companies'],
			mode='lines',
			name=d1))
		fig.add_trace(go.Scatter(x=df2['Year'], y=df2['newly_funded_ai_companies'],
			mode='lines+markers',
			name=d2))
		graph=fig.to_html()
		return render(request, 'Detail Company Analysis 2.html',{'graph':graph})
	else:
		return render(request,'Detail Company Analysis 2.html')

def DetailCompanyAnalysis3(request):
	if request.method=="POST":
		df=pd.read_csv('Annual Number of newly funded A.I companies.csv')
		d1=request.POST.get('entity')
		d2=request.POST.get('entity1')
		d3=request.POST.get('entity2')
		df1=df[df['Entity']==d1]
		df2=df[df['Entity']==d2]
		df3=df[df['Entity']==d3]
		#Create Traces
		fig=go.Figure()
		fig.add_trace(go.Scatter(x=df1['Year'], y=df1['newly_funded_ai_companies'],
			mode='lines',
			name=d1))
		fig.add_trace(go.Scatter(x=df2['Year'], y=df2['newly_funded_ai_companies'],
			mode='lines+markers',
			name=d2))
		fig.add_trace(go.Scatter(x=df3['Year'], y=df3['newly_funded_ai_companies'],
			mode='lines+markers',
			name=d3))
		graph=fig.to_html()
		return render(request, 'Detail Company Analysis 3.html',{'graph':graph})
	else:
		return render(request,'Detail Company Analysis 3.html')

def DetailCompanyAnalysis4(request):
	if request.method=="POST":
		df=pd.read_csv('Annual Number of newly funded A.I companies.csv')
		d1=request.POST.get('entity')
		df1=df[df['Entity']==d1]
		sy=int(request.POST.get('sy'))
		ey=int(request.POST.get('ey'))
		df1=df1[(df1['Year']>=sy) & (df1['Year']<=ey)]
		#Create Traces
		fig=go.Figure()
		fig.add_trace(go.Scatter(x=df1['Year'], y=df1['newly_funded_ai_companies'],
			mode='lines', name=d1))
		graph=fig.to_html()
		return render(request,'Detail Company Analysis 4.html',{'graph':graph})
	else:
		return render(request,'Detail Company Analysis 4.html')


def DetailCompanyAnalysis5(request):
	if request.method=="POST":
		df=pd.read_csv('Annual Number of newly funded A.I companies.csv')
		d1=request.POST.get('entity')
		d2=request.POST.get('entity1')
		df1=df[df['Entity']==d1]
		df2=df[df['Entity']==d2]
		sy=int(request.POST.get('sy'))
		ey=int(request.POST.get('ey'))
		df1=df1[(df1['Year']>=sy) & (df1['Year']<=ey)]
		df2=df2[(df2['Year']>=sy) & (df2['Year']<=ey)]
		#Create Traces
		fig=go.Figure()
		fig.add_trace(go.Scatter(x=df1['Year'], y=df1['newly_funded_ai_companies'],
			mode='lines',
			name=d1))
		fig.add_trace(go.Scatter(x=df2['Year'], y=df2['newly_funded_ai_companies'],
			mode='lines+markers',
			name=d2))
		fig.add_trace(go.Scatter(x=df2['Year'], y=df2['newly_funded_ai_companies'],
			mode='lines+markers',
			name=d2))
		graph=fig.to_html()
		return render(request, 'Detail Company Analysis 5.html',{'graph':graph})
	else:
		return render(request,'Detail Company Analysis 5.html')

def DetailCompanyAnalysis6(request):
	df=pd.read_csv('Annual Number of newly funded A.I companies.csv')
	cc=coco.CountryConverter()
	df['Entity_codes']=coco.convert(names=df['Code'], to='ISO3')
	print(df['Entity_codes'])
	fig=px.scatter_geo(df, locations="Entity_codes", color="Entity",
		hover_name="Entity", size="newly_funded_ai_companies", animation_frame='Year',
		projection="natural earth")
	graph=fig.to_html()
	return render(request, 'Detail Company Analysis 6.html',{'graph':graph})

def DetailCompanyAnalysis7(request):
	if request.method=="POST":
		df=pd.read_csv('Annual Number of newly funded A.I companies.csv')
		year=int(request.POST.get('year'))
		print("year",year)
		df1=df[df["Year"]==year]
		df1=df1.dropna()
		print("df1",df1)
		df1=df1.sort_values(by='newly_funded_ai_companies')
		n=int(request.POST.get('entity'))
		dfmax=df1.tail(n)
		print("dfmax",dfmax)
		fig=px.bar(dfmax, y='newly_funded_ai_companies', x='Entity',
			title='Growth of Countries.')
		graph=fig.to_html()
		return render(request, 'Detail Company Analysis 7.html',{'graph':graph} )
	else:
		return render(request, 'Detail Company Analysis 7.html')

def DetailJobAnalysis1(request):
	df=pd.read_csv('share A.I job-postings (1).csv')
	title='AI Job Postings In All Countries'
	fig=px.area(df, x="Year", y="ai_job_postings",color="Entity",
		line_group="Entity",title=title)
	graph=fig.to_html()
	return render(request,'Detail Job Analysis 1.html',{'graph':graph})

def DetailJobAnalysis2(request):
	if request.method=="POST":
		df=pd.read_csv('share A.I job-postings (1).csv')
		Entity=request.POST.get('entity')
		dfa=df[df['Entity']==Entity]
		title='AI Job Posting in '+ Entity
		fig=px.area(dfa,x="Year", y="ai_job_postings", color="Entity",
			line_group="Entity",title=title)
		graph=fig.to_html()
		return render(request,'Detail Job Analysis 2.html',{'graph':graph})
	else:
		return render(request,'Detail Job Analysis 2.html')

def DetailJobAnalysis3(request):
	if request.method=="POST":
		df=pd.read_csv('share A.I job-postings (1).csv')
		c1= request.POST.get('entity')
		c2=request.POST.get('entity1')
		df1=df[df['Entity']==c1]
		df2=df[df['Entity']==c2]
		dfc=df[(df['Entity']==c1) | (df['Entity']==c2)]
		title='AI Job Postings In Two Countries.'
		fig=px.area(dfc, x="Year", y="ai_job_postings", color="Entity",
			line_group="Entity",title=title )
		graph=fig.to_html()
		return render(request,'Detail Job Analysis 3.html',{'graph':graph})
	else:
		return render(request,'Detail Job Analysis 3.html')

def DetailJobAnalysis4(request):
	if request.method=="POST":
		df=pd.read_csv('share A.I job-postings (1).csv')
		c1= request.POST.get('entity')
		c2=request.POST.get('entity1')
		c3=request.POST.get('entity2')
		df1=df[df['Entity']==c1]
		df2=df[df['Entity']==c2]
		df3=df[df['Entity']==c3]
		title='AI Job Postings In Three Countries.'
		dfc=df[(df['Entity']==c1) | (df['Entity']==c2) | (df['Entity']==c3)]
		fig=px.area(dfc, x="Year", y="ai_job_postings", color="Entity",
			line_group="Entity",title=title )
		graph=fig.to_html()
		return render(request,'Detail Job Analysis 4.html',{'graph':graph})
	else:
		return render(request,'Detail Job Analysis 4.html')

def DetailJobAnalysis5(request):
	if request.method=="POST":
		df=pd.read_csv('share A.I job-postings (1).csv')
		c1=request.POST.get('entity')
		dff=df[df['Entity']==c1]
		sy=int(request.POST.get('sy'))
		ey=int(request.POST.get('ey'))
		dfc=dff[(dff['Year']>=sy) & (dff['Year']<=ey)]
		fig=px.area(dfc, x="Year", y="ai_job_postings", color="Entity",
			line_group="Entity")
		graph=fig.to_html()
		return render(request,'Detail Job Analysis 5.html',{'graph':graph})
	else:
		return render(request,'Detail Job Analysis 5.html')

def DetailJobAnalysis6(request):
	if request.method=="POST":
		df=pd.read_csv('share A.I job-postings (1).csv')
		c1=request.POST.get('entity1')
		c2=request.POST.get('entity2')
		df1=df[df['Entity']==c1]
		df2=df[df['Entity']==c2]
		sy=int(request.POST.get('sy'))
		ey=int(request.POST.get('ey'))
		df1=df1[(df1['Year']>=sy) & (df1['Year']<=ey)]
		df2=df2[(df2['Year']>=sy) & (df2['Year']<=ey)]
		#Create Traces
		fig=go.Figure()
		fig.add_trace(go.Scatter(x=df1['Year'], y=df1['ai_job_postings'],
			mode='lines',
			name=c1))
		fig.add_trace(go.Scatter(x=df2['Year'], y=df2['ai_job_postings'],
			mode='lines+markers',
			name=c2))
		graph=fig.to_html()
		return render(request,'Detail Job Analysis 6.html',{'graph':graph})
	else:
		return render(request,'Detail Job Analysis 6.html')

def DetailJobAnalysis7(request):
	df=pd.read_csv('share A.I job-postings (1).csv')
	cc=coco.CountryConverter()
	df['Entity_codes']=coco.convert(names=df['Code'], to='ISO3')
	print(df['Entity_codes'])
	fig=px.scatter_geo(df, locations="Entity_codes", color="Entity",
		hover_name="Entity",size="ai_job_postings",animation_frame='Year',
		projection="natural earth")
	graph=fig.to_html()
	return render(request, 'Detail Job Analysis 7.html',{'graph':graph})

def DetailExpensesAnalysis1(request):
	if request.method=="POST":
		df=pd.read_csv('World developement index.csv')
		cc=coco.CountryConverter()
		df['Entity_codes']=coco.convert(names=df['Country Code'], to='ISO3')
		print(df['Entity_codes'])
		year=request.POST.get('n')
		title='World development index in '
		df1=df.loc[:,['Country Name','Entity_codes',year]]
		fig=px.scatter_geo(df, locations="Entity_codes", color="Country Name",
			hover_name="Country Name", title=title,size=year,
			projection="natural earth")
		graph=fig.to_html()
		return render(request,'Detail Expenses Analysis 1.html',{'graph':graph})
	else:
		return render(request,'Detail Expenses Analysis 1.html')

def DetailExpensesAnalysis2(request):
	if request.method=="POST":
		df=pd.read_csv('World developement index.csv')
		year=request.POST.get('year')
		df1=df.loc[:,['Country Name',year]]
		df1=df1.dropna()
		df1=df1.sort_values(by=year)
		n=int(request.POST.get('country'))
		dfmin=df1.head(n)
		title='World Development Index of all Countries'
		fig=px.bar(dfmin,y=year,x='Country Name',title=title)
		graph=fig.to_html()
		return render(request,'Detail Expenses Analysis 2.html',{'graph':graph})
	else:
		return render(request,'Detail Expenses Analysis 2.html')

def DetailExpensesAnalysis3(request):
	if request.method=="POST":
		df=pd.read_csv('World developement index.csv')
		year=request.POST.get('year')
		df1=df.loc[:,['Country Name',year]]
		df1=df1.dropna()
		df1=df1.sort_values(by=year)
		n=int(request.POST.get('country'))
		dfmax=df1.tail(n)
		title='World Development Index of all Countries'
		fig=px.bar(dfmax,y=year,x='Country Name',title=title)
		graph=fig.to_html()
		return render(request,'Detail Expenses Analysis 3.html',{'graph':graph})
	else:
		return render(request,'Detail Expenses Analysis 3.html')

def DetailExpensesAnalysis4(request):
	if request.method=="POST":
		df=pd.read_csv('World developement index.csv')
		df=df.transpose()
		df.columns=df.iloc[0,:]
		df=df.iloc[4:,:]
		c=dict.fromkeys(df.columns,float)
		df=df.astype(c)
		df=df.reset_index()
		df.rename(columns={'index':'Year'},inplace=True)
		c={'Year':int}
		df=df.astype(c)
		c1=request.POST.get('country')
		df1=df.loc[:,['Year',c1]]
		df1=df1.dropna()
		title='World Development Index of ' + c1
		fig=px.scatter(df1,x="Year", y=c1,
			size=c1, color="Year", title=title,
			log_x=True, size_max=60)
		graph=fig.to_html()
		return render(request,'Detail Expenses Analysis 4.html',{'graph':graph})
	else:
		return render(request,'Detail Expenses Analysis 4.html')

def DetailExpensesAnalysis5(request):
	if request.method=="POST":
		df=pd.read_csv('World developement index.csv')
		year=request.POST.get('year')
		dfy=df.loc[:,['Country Name',year]]
		dfy=dfy.dropna()
		dfy=dfy.sort_values(by=year)
		dfy=dfy.tail()
		title='World Development Index in ' + year 
		fig=px.scatter(dfy, x=year, y=year,color="Country Name",
			hover_name="Country Name", log_x=True, size_max=60)
		graph=fig.to_html()
		return render(request,'Detail Expenses Analysis 5.html',{'graph':graph})
	else:
		return render(request,'Detail Expenses Analysis 5.html')

def DetailExpensesAnalysis6(request):
	if request.method=="POST":
		df=pd.read_csv('World developement index.csv')
		year=request.POST.get('year')
		dfy=df.loc[:,['Country Name',year]]
		dfy=dfy.dropna()
		dfy=dfy.sort_values(by=year)
		dfy=dfy.head()
		title='World Development Index in ' + year 
		fig=px.scatter(dfy, x=year, y=year, size=year, title=title, color="Country Name",
			hover_name="Country Name", log_x=True, size_max=60)
		graph=fig.to_html()
		return render(request,'Detail Expenses Analysis 6.html',{'graph':graph})
	else:
		return render(request,'Detail Expenses Analysis 6.html')

def DetailExpensesAnalysis7(request):
	if request.method=="POST":
		df=pd.read_csv('World developement index.csv')
		df=df.transpose()
		df.columns=df.iloc[0,:]
		df=df.iloc[4:,:]
		c=dict.fromkeys(df.columns,float)
		df=df.astype(c)
		df=df.reset_index()
		df.rename(columns={'index':'Year'},inplace=True)
		c={'Year':int}
		df=df.astype(c)
		c1=request.POST.get('entity1')
		c2=request.POST.get('entity2')
		c3=request.POST.get('entity3')
		df1=df.loc[:,['Year',c1]]
		df2=df.loc[:,['Year',c2]]
		df3=df.loc[:,['Year',c3]]
		sy=int(request.POST.get('year1'))
		ey=int(request.POST.get('year2'))
		df1=df1[(df1['Year']>=sy) & (df1['Year']<=ey)]
		df2=df2[(df2['Year']>=sy) & (df2['Year']<=ey)]
		df3=df3[(df3['Year']>=sy) & (df3['Year']<=ey)]
		#Create Traces
		fig=go.Figure()
		fig.add_trace(go.Scatter(x=df1['Year'], y=df1[c1],mode='lines',name=c1))
		fig.add_trace(go.Scatter(x=df2['Year'], y=df2[c2],mode='lines+markers',name=c2))
		fig.add_trace(go.Scatter(x=df3['Year'], y=df3[c3],mode='lines+markers',name=c3))
		graph=fig.to_html()
		return render(request,'Detail Expenses Analysis 7.html',{'graph':graph})
	else:
		return render(request,'Detail Expenses Analysis 7.html')


