"""
URL configuration for Artificial_Intelligence project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AIapp import views
from django.conf import settings
from django.contrib.staticfiles.urls  import static
from django.contrib.staticfiles.urls  import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("Register/",views.Register,name="Register"),
    path("Login/",views.login,name="Login"),
    path("ForgetPassword/",views.ForgetPassword,name="ForgetPassword"),
    path("Index/",views.index,name="Index"),
    path("Footer/",views.Footer),
    path("ContactUs/",views.contactus,name="ContactUs"),
    path("ChangePassword/",views.ChangePassword,name="ChangePassword"),
    path("HelpAndSupport/",views.HelpAndSupport,name="HelpAndSupport"),
    path("Review/",views.Review,name="Review"),
    path("Base/",views.Base),
    path("FAQ/",views.View_FAQ,name="FAQ"),
    path("EditProfile/",views.EditProfile,name="EditProfile"),
    path("UserProfile/",views.UserProfile,name="UserProfile"),
    path("Sidebar/",views.Sidebar),
    path("Logout/",views.Logout,name="Logout"),
    path("ViewBlogs/",views.ViewBlog,name="Blog"),
    path("Videos/",views.Videos,name="Videos"),
    path("DetailBlogs/<int:id>",views.DetailBlog,name="DetailBlog"),
    path("ViewAITool/",views.ViewAITool,name="ViewAITool"),
    path("DetailAITool/<str:name>",views.DetailAITool,name="DetailAITool"),
    path("DetailAITool2/<int:id>",views.DetailAITool2,name="DetailAITool2"),
    path("Latestnews/",views.Latestnews,name="Latestnews"),
    path("AboutUs/",views.AboutUs,name="AboutUs"),
    path("Initiative/",views.Initiative,name="Initiative"),
    path("DetailInitiative/<int:id>",views.DetailInitiative,name="DetailInitiative"),
    path("MyProfile/",views.MyProfile,name="MyProfile"),
    path("Dashboard/",views.Dashboard,name="Dashboard"),
    path("Analysis1/",views.Analysis1,name="Analysis1"),
    path("Analysis2/",views.Analysis2,name="Analysis2"),
    path("Analysis3/",views.Analysis3,name="Analysis3"),
    path("Analysis4/",views.Analysis4,name="Analysis4"),
    path("DetailBillAnalysis1/",views.DetailBillAnalysis1,name="DetailBillAnalysis1"),
    path("DetailBillAnalysis2/",views.DetailBillAnalysis2,name="DetailBillAnalysis2"),
    path("DetailBillAnalysis3/",views.DetailBillAnalysis3,name="DetailBillAnalysis3"),
    path("DetailBillAnalysis4/",views.DetailBillAnalysis4,name="DetailBillAnalysis4"),
    path("DetailBillAnalysis5/",views.DetailBillAnalysis5,name="DetailBillAnalysis5"),
    path("DetailBillAnalysis6/",views.DetailBillAnalysis6,name="DetailBillAnalysis6"),
    path("DetailBillAnalysis7/",views.DetailBillAnalysis7,name="DetailBillAnalysis7"),
    path("DetailCompanyAnalysis1/",views.DetailCompanyAnalysis1,name="DetailCompanyAnalysis1"),
    path("DetailCompanyAnalysis2/",views.DetailCompanyAnalysis2,name="DetailCompanyAnalysis2"),
    path("DetailCompanyAnalysis3/",views.DetailCompanyAnalysis3,name="DetailCompanyAnalysis3"),
    path("DetailCompanyAnalysis4/",views.DetailCompanyAnalysis4,name="DetailCompanyAnalysis4"),
    path("DetailCompanyAnalysis5/",views.DetailCompanyAnalysis5,name="DetailCompanyAnalysis5"),
    path("DetailCompanyAnalysis6/",views.DetailCompanyAnalysis6,name="DetailCompanyAnalysis6"),
    path("DetailCompanyAnalysis7/",views.DetailCompanyAnalysis7,name="DetailCompanyAnalysis7"),
    path("DetailJobAnalysis1/",views.DetailJobAnalysis1,name="DetailJobAnalysis1"),
    path("DetailJobAnalysis2/",views.DetailJobAnalysis2,name="DetailJobAnalysis2"),
    path("DetailJobAnalysis3/",views.DetailJobAnalysis3,name="DetailJobAnalysis3"),
    path("DetailJobAnalysis4/",views.DetailJobAnalysis4,name="DetailJobAnalysis4"),
    path("DetailJobAnalysis5/",views.DetailJobAnalysis5,name="DetailJobAnalysis5"),
    path("DetailJobAnalysis6/",views.DetailJobAnalysis6,name="DetailJobAnalysis6"),
    path("DetailJobAnalysis7/",views.DetailJobAnalysis7,name="DetailJobAnalysis7"),
    path("DetailExpensesAnalysis1/",views.DetailExpensesAnalysis1,name="DetailExpensesAnalysis1"),
    path("DetailExpensesAnalysis2/",views.DetailExpensesAnalysis2,name="DetailExpensesAnalysis2"),
    path("DetailExpensesAnalysis3/",views.DetailExpensesAnalysis3,name="DetailExpensesAnalysis3"),
    path("DetailExpensesAnalysis4/",views.DetailExpensesAnalysis4,name="DetailExpensesAnalysis4"),
    path("DetailExpensesAnalysis5/",views.DetailExpensesAnalysis5,name="DetailExpensesAnalysis5"),
    path("DetailExpensesAnalysis6/",views.DetailExpensesAnalysis6,name="DetailExpensesAnalysis6"),
    path("DetailExpensesAnalysis7/",views.DetailExpensesAnalysis7,name="DetailExpensesAnalysis7"),
    
]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)