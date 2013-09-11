from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.views.generic.simple import direct_to_template
from django.core.mail import send_mail

from models import Decoration, ProductCategory, DecorationCategory, DecorationIngredient
from OrderRequestLib import OrderRequest
from forms import ContactForm


# Create your views here.
from myproject.pub import utils


def base_proc(request):
    
    return {
        #'OccasionList': Occasion.objects.all(),
        'ProductCategoryList': ProductCategory.objects.all(),
        "decorationcats" : DecorationCategory.objects.all().order_by("title_en")
    }

    
def hello(request):
    return HttpResponse("Hello world")


def index(request):
    return render_to_response("index.html", {}, context_instance=RequestContext(request, processors=[base_proc]))


def base(request):
    return render_to_response("base.html", {}, context_instance=RequestContext(request, processors=[base_proc]))


def mail_sent_confirmation(request):
    return render_to_response("mail_sent_confirmation.html", {}, context_instance=RequestContext(request, processors=[base_proc]))


def makeorder(request):
    order=OrderRequest(request)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                cd["decoration_id"] = order.decorationId
                if cd["DecorationIngredient"]:
                    cd["decoration_ingredient_name"] = DecorationIngredient.objects.get(pk=cd["DecorationIngredient"]).title_ru
                utils.send_order_email(cd)
                return HttpResponseRedirect(reverse("mail_sent_confirmation"))
                print "Mail sent"
            except Exception as ex:
                form._errors["__all__"] = form.error_class([str(ex)])
                print "Error in mail sending!!!"

        else:
            print "data is not valid", form.errors
    else:
        form = ContactForm()

    data = {"order": order, "form": form, "decoration_ingredients": DecorationIngredient.objects.all()}

    response=render_to_response("makeorder.html", data, context_instance=RequestContext(request, processors=[base_proc]))
    #order.save(response)
    return response

def genericview(request, page):
    return render_to_response(page, {}, context_instance=RequestContext(request, processors=[base_proc]))

    
def products(request, slug):
    cat = get_object_or_404(ProductCategory, slug=slug)    
    items=cat.product_set.all()
    return productCommon(request, items)
    
def decorations(request):
    items=Decoration.objects.all()
    return decorationCommon(request, items)

def decorationByOccasion(request, slug):
    decoration_category = get_object_or_404(DecorationCategory, slug=slug)
    items=decoration_category.decoration_set.all()
    return decorationCommon(request, items)

def productCommon(request, items):
    rows_list=formatByRowsDecorationList(items)
    paginator = Paginator(rows_list, 4) # Show 25 contacts per page
    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        rows = paginator.page(page)
    except (EmptyPage, InvalidPage):
        rows = paginator.page(paginator.num_pages)
    return render_to_response("products.html", {"rows" : rows}, context_instance=RequestContext(request, processors=[base_proc]))    
    
def decorationCommon(request, items):
    rows_list=formatByRowsDecorationList(items)
    paginator = Paginator(rows_list, 4) # Show 25 contacts per page
    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        rows = paginator.page(page)
    except (EmptyPage, InvalidPage):
        rows = paginator.page(paginator.num_pages)
    return render_to_response("decorations.html", {"rows" : rows}, context_instance=RequestContext(request, processors=[base_proc]))    

def formatByRowsDecorationList(list):
    cnt=0
    rows=[]
    while cnt<len(list):
        row=[]
        for x in range(4):
            if cnt<len(list):
                row.append(list[cnt])
            else:
                row.append(None)
            cnt+=1
        rows.append(row)
    return rows;
