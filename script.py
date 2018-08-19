from bs4 import BeautifulSoup
import requests
import csv

missing_value_representation="missing"
delimeter=";"

csv.register_dialect('myDialect',
delimiter = delimeter,
quoting=csv.QUOTE_NONE,
skipinitialspace=True)

def ret_text(soup,tag,key,value):
    if (soup.find(tag, {key: value}) == None):
        return missing_value_representation
    elif soup.find(tag, {key: value}).text.strip() =="":
        return missing_value_representation
    else:
        return soup.find(tag, {key: value}).text.strip()

with  open('cms_scrape.csv','w') as f_out:
    row=['City/Landmark', 'P.O.Box_number', 'Telephone_number', 'Mobile_numbers', 'Fax_number']
    writer=csv.writer(f_out,dialect='myDialect')
    writer.writerow(row)
    # csv_writer = csv.writerow()

    for i in range(0, 342):
        source = requests.get('https://www.yellowpages.ae/c/advs/abu-dhabi/garage-services-{}-1.html'.format(i)).text
        soup = BeautifulSoup(source, 'lxml')

        for j in range(0,10):

            company_name_id="ContentPlaceHolder1_grdListing_hlcampanyname_{}".format(j)
            landmark_id="ContentPlaceHolder1_grdListing_lblLandmark_{}".format(j)
            po_box_number="ContentPlaceHolder1_grdListing_lblPoBox1_Number_{}".format(j)
            telephone_number1="ContentPlaceHolder1_grdListing_lblTel1_CntryCode_{}".format(j)
            telephone_number2="ContentPlaceHolder1_grdListing_lblTel2_AreaCode_{}".format(j)
            telephone_number3="ContentPlaceHolder1_grdListing_lblTel3_ListingTel_{}".format(j)
            mobile_number="ContentPlaceHolder1_grdListing_dlothercontact_{}_lblcontactinfo_0".format(j)
            fax_1="ContentPlaceHolder1_grdListing_lblFax1_CntryCode_{}".format(j)
            fax_2="ContentPlaceHolder1_grdListing_lblFax2_AreaCode_{}".format(j)
            fax_3="ContentPlaceHolder1_grdListing_lblFax3_FaxNumber_{}".format(j)

            Company_Name=ret_text(soup,'a','id',company_name_id)
            Land_Martk=ret_text(soup,'span','id',landmark_id)
            PO_Number=ret_text(soup,'span','id',po_box_number)

            TN1=ret_text(soup,'span','id',telephone_number1)
            TN2=ret_text(soup,'span','id',telephone_number2)
            TN3=ret_text(soup,'span','id',telephone_number3)

            if ((TN1 == missing_value_representation )| (TN2 == missing_value_representation) | (TN3 == missing_value_representation )):
                Telephone_Number=missing_value_representation
            else:
                Telephone_Number=TN1+" "+TN2+" "+TN3

            Mobile_Number=ret_text(soup,'span','id',mobile_number)

            F1=ret_text(soup,'span','id',fax_1)
            F2=ret_text(soup,'span','id',fax_2)
            F3=ret_text(soup,'span','id',fax_3)

            if ((F1 == missing_value_representation )| (F2 == missing_value_representation) | (F3 == missing_value_representation )| ((F1 == "+8" ) & (F2 == "00") & (F3 == "0" ))):
                Fax=missing_value_representation
            else:
                Fax=F1+" "+F2+" "+F3

            row=[Land_Martk,PO_Number,Telephone_Number,Mobile_Number,Fax]
            writer.writerow(row)



        



