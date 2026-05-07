from django.urls import path


from family import views

urlpatterns = [
    path('addmember/',views.add_member,name='addmember'),
    path('familydata/',views.family_data,name='familydata'),
    path('update_member/<int:id>',views.update_data,name='update_member'),
    path('delete_member/<int:id>',views.delete_data,name='delete_member'),
    path('addexpenses/',views.add_expenses,name='addexpenses'),
    path('viewexpenses/',views.view_expenses,name='viewexpenses'),
    path('monthly/',views.monthly,name='monthly'),
    path('yearly/',views.yearly,name='yearly'),
    path('total/',views.total,name='total'),
    path('updateexpense/<int:id>', views.update_expense, name='updateexpense'),
    path('deleteexpense/<int:id>', views.delete_expense, name='deleteexpense'),
]