import csv



#INITIALIZING LISTS
sitecode_list=[]
city_list=[]
address_list=[]
isp1vendor_list=[]
isp1ip_list=[]
isp1cid_list=[]
isp2vendor_list=[]
isp2ip_list=[]
isp2cid_list=[]
poc_list=[]


#UPDATE ALL LISTS WITH NEW DATA
def update_lists():
   with open("CircuitList.tsv", "rU") as csvfile:
      reader = csv.reader(csvfile, dialect='excel-tab')
      for row in reader:
         sitecode_list.append(row[0])
         city_list.append(row[1])
         address_list.append(row[2])
         isp1vendor_list.append(row[3])
         isp1ip_list.append(row[4])
         isp1cid_list.append(row[5])
         isp1vendor_list.append(row[6])
         isp2ip_list.append(row[7])
         isp2cid_list.append(row[8])
         poc_list.append(row[9])
update_lists()


#DRAFT EMAIL
def search_sites():
   option = raw_input("\n ENTER SITE CODE \n")
   with open("CircuitList.tsv", "rU") as csvfile:
      reader = csv.reader(csvfile, dialect='excel-tab')
      for row in reader:
         if option == row[0]:
            print "\n DRAFTING EMAIL \n"
            selected_sitecode = row[0]
            selected_city = row[1]
            selected_address = row[2]
            selected_isp1vendor = row[3]
            selected_isp1ip = row[4]
            selected_isp1cid = row[5]
            selected_isp2vendor = row[6]
            selected_isp2ip = row[7]
            selected_isp2cid = row[8]
            selected_poc = row[9]

            ISP1_EMAIL_SUBJECT = "%s Circuit %s with IP %s is DOWN at %s" % (selected_isp1vendor, selected_isp1cid, selected_isp1ip, selected_sitecode)
            ISP2_EMAIL_SUBJECT = "%s Circuit %s with IP %s is DOWN at %s" % (selected_isp2vendor, selected_isp2cid, selected_isp2ip, selected_sitecode)
            ISP1_EMAIL_BODY = "\n#####ENGINEER INSTRUCTIONS START#####\n Please follow the instructions below:\n1 - Create a ticket for this event\n2 - Add your ticket number to subject of email\n3 - Add ticket email to cc list of your email\n4 - Delete this list of instructions & send email\n#####ENGINEER INSTRUCTIONS END#####\n\n\nHello %s,\n \nour circuit %s at our site location: %s is down.\nOur IP address is: %s.\nOur physical address is: %s \nCould you please help investigate the issue?\n\nThanks." % (selected_isp1vendor, selected_isp1cid, selected_sitecode, selected_isp1ip, selected_address)
            ISP2_EMAIL_BODY = "\n#####ENGINEER INSTRUCTIONS START#####\n Please follow the instructions below:\n1 - Create a ticket for this event\n2 - Add your ticket number to subject of email\n3 - Add ticket email to cc list of your email\n4 - Delete this list of instructions & send email\n#####ENGINEER INSTRUCTIONS END#####\n\n\nHello %s,\n \nour circuit %s at our site location: %s is down.\nOur IP address is: %s.\nOur physical address is: %s \nCould you please help investigate the issue?\n\nThanks." % (selected_isp2vendor, selected_isp2cid, selected_sitecode, selected_isp2ip, selected_address)

            print "ISP1 EMAIL SUBJECT: %s" % ISP1_EMAIL_SUBJECT
            print "\nISP1 EMAIL BODY: %s \n\n" % ISP1_EMAIL_BODY
            print "ISP2 EMAIL SUBJECT: %s" % ISP2_EMAIL_SUBJECT
            print "\nISP2 EMAIL BODY: %s \n\n" % ISP2_EMAIL_BODY


#USER SELECTIONS
def select_action():
   all_ip_list = isp1ip_list + isp2ip_list
   all_cid_list = isp1cid_list + isp2cid_list
   all_vendor_list = isp1vendor_list + isp2vendor_list
   print "what would you like to do?"
   option = raw_input("\nEnter the number of the option you want.\n\n1 - Show sitecode list\n2 - Show city list\n3 - Show site addresses\n4 - Show all vendors\n5 - show all ip's\n6 - Show all cid's\n7 - Draft email by entering site code\n10 - Exit program\n> ")
   if option == "1":
      print sitecode_list
   elif option == "2":
      print city_list
   elif option == "3":
      print address_list
   elif option == "4":
      print all_vendor_list
   elif option == "5":
      print all_ip_list
   elif option == "6":
      print all_cid_list
   elif option == "7":
      search_sites()
   elif option == "10":
      print "GOODBYE"
   else:
      print "Invalid selection, exiting program"
select_action()











