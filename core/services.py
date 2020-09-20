from  time import sleep
from requests_html import HTMLSession
import json


def testm(data):
    price =[]
    productx = []
    productvalue = []
    m = []
    session = HTMLSession()
    r = session.get(data)
    
    # pricex = r.html.xpath('.//span[@data-selenium="uppedDecimalPriceFirst"]')
    # product = r.html.xpath('.//span[@data-selenium="miniProductPageProductName"]')
    # print(pricex)
    # print("---------")
    # print(product)
    # for x in pricex:
    #     print(x.find('span',first=True).text)
    # print(product)
    pricex = r.html.xpath('.//script[@type="application/ld+json"]')
    product = r.html.xpath('.//td[@class="label_3bLwbW8ibvYc5tUwpKVQsL" and @data-selenium="specsItemGroupTableColumnLabel"]')  
    product_value = r.html.xpath('.//td[@class="value_11Av1yGkVYn9TX48mQeu9v" and @data-selenium="specsItemGroupTableColumnValue"]')  

    for pro in product:
        productx.append(pro.find('td',first=True).text)
     
        
    for provalue in product_value:
         productvalue.append(provalue.find('span', first=True).text)
    
    d = dict(zip(productx,productvalue))
    print(d)


def kml(data):
    data_dict = {}
    data_dict['data']= data
    return data_dict

def kcl(data):
    data_dict = {}
    data_dict['data']= data
    return data_dict


    

    # # print(product)
    # print(pricex)
    # for x in pricex:
    #      a = x.find('script', first=True).text
    #      b = json.loads(a)
    #      print(b)
    #      if b.get('offers') != None and b.get('description')!= None :
    #          m.append(dict(b.get('offers')['price'],b.get('description'),b.get('offers')['url']))  
    #          return m
      
        # if c != None :
        #      product.append(str(c))
        # if type(k) != "NoneType":
        # #     price.append(str(k))
        
    
    # print(product)


#     for pricex, productx in   zip(price, product):
#           m.append(dict(pricex, productx))   
#           return m
    
    


# def dict(data,data2,data3):
#        data_dict = {}
#        data_dict['price']= data
#        data_dict['product']= data2
#        data_dict['url']= data3
     
#        return data_dict

# def print_result(task):
#     print(task.result)
#     return task.result

    