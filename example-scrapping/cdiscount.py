from bs4 import BeautifulSoup
import requests

url ="https://www.cdiscount.com/search/10/livres.html?TechnicalForm.SiteMapNodeId=0&TechnicalForm.DepartmentId=10&TechnicalForm.ProductId=&hdnPageType=Search&TechnicalForm.ContentTypeId=16&TechnicalForm.SellerId=&TechnicalForm.PageType=SEARCH_AJAX&TechnicalForm.LazyLoading.ProductSheets=False&TechnicalForm.BrandLicenseId=0&NavigationForm.CurrentSelectedNavigationPath=categorycodepath%2F19&NavigationForm.FirstNavigationLinkCount=2&FacetForm.SelectedFacets.Index=0&FacetForm.SelectedFacets.Index=1&FacetForm.SelectedFacets.Index=2&FacetForm.SelectedFacets.Index=3&FacetForm.SelectedFacets.Index=4&FacetForm.SelectedFacets.Index=5&FacetForm.SelectedFacets.Index=6&FacetForm.SelectedFacets.Index=7&FacetForm.SelectedFacets.Index=8&FacetForm.SelectedFacets.Index=9&FacetForm.SelectedFacets.Index=10&FacetForm.SelectedFacets.Index=11&FacetForm.SelectedFacets.Index=12&FacetForm.SelectedFacets.Index=13&FacetForm.SelectedFacets.Index=14&FacetForm.SelectedFacets.Index=15&SortForm.BrandLicenseSelectedCategoryPath=&SortForm.SelectedSort=PERTINENCE&ProductListTechnicalForm.Keyword=livres&ProductListTechnicalForm.TemplateName=InLine&page="
total_page=20
i=1

all_livres=[]

def getLivres(pageUrl):
    print("Page URL "+ pageSearch)
    response = requests.get(pageUrl)
    print ("Request status "+str(response.ok))
    if response.ok:
        soup = BeautifulSoup(response.content,"html.parser")
        ul=soup.find("ul",{"id":"lpBloc"})
        livres=ul.findAll("li")
        #print(livres)
        for l in livres:
            details=l.find("div",{"class":"prdtBILDetails"})
            price = l.find("span",{"class":"hideFromPro price"})
            if details !=None:
                item={}
                titre=details.find("a")
                div_resume = details.find("div",{"class":"prdtBILDesc jsPrdtBILLink"})
                item["titre"]=titre.text
                item["resume"]=div_resume.text
                if price !=None:
                    item["prix"]=price.text     
                all_livres.append(item)           

while i <total_page:
    pageSearch=url+str(i)
    getLivres(pageSearch)
    i+=1
print(all_livres)