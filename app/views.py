from django.shortcuts import render
from .models import Contact
from .forms import CreateContactForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.


def home(request):
	data = Contact.objects.all()
	form = CreateContactForm()
	if request.method == 'POST':
		form = CreateContactForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'Link edited successfully.')
	else:
		messages.error(request, form.errors)
	context={'form':form,'data':data}
	return render(request, 'phonebook/index.html', context)


def favorite(request):
	data = Contact.objects.filter(favorite=True)
	form = CreateContactForm()
	if request.method == 'POST':
		form = CreateContactForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'Link edited successfully.')
	else:
		messages.error(request, form.errors)
	return render(request,'phonebook/favorite.html', context={'data':data, 'form':form})

def profile(request, pk):  
	edit_form = CreateContactForm()
	data = Contact.objects.get(pk=pk)
	p = Contact.objects.get(pk=pk)
	if request.method == 'POST':
		editform = CreateContactForm(request.POST,request.FILES, instance=p)
		if editform.is_valid():
			editform.save()
			messages.success(request, 'Link edited.')
	
		

	return render(request,'phonebook/profile.html', context={'data':data, 'edit_form': edit_form})

def edit_contacts(request):
    if request.method == 'POST':
        id = request.POST.get('contact_id')
        link = Contact.objects.get(pk=id)
        # print(link.image.url)
        # print(link.url_title)
        link_data = {'id':link.id, 'first_name':link.first_name, 'last_name':link.last_name,
					'country_code':link.country_code, 'phone_number':link.phone_number, 'email_id':link.email_id,
					'favorite':link.favorite, 'category':link.category}
        return JsonResponse(link_data)
    return JsonResponse({'status':0})


def delete_contact(request, pk):
	if request.method == 'POST':
		contact = Contact.objects.get(pk=pk)
		data = Contact.objects.all()
		contact.delete()
		messages.warning(request, "Contact deleted successfully.")
		return render(request, 'phonebook/index.html', {'data': data})
	return render(request, 'phonebook/profile.html')


def SearchResultView(request):
	''' Returns search results from City model that contains query '''
	# if request.method == 'POST':
	query = request.GET.get('q')
	print(query)
	object_list = Contact.objects.filter(
		Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(email_id__icontains=query)
		)
	return render(request, 'app/search_results.html',{'object_list':object_list})