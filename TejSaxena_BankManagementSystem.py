# Project on Bank Management System
#------------------------------------------------------------------------------
#Project Modules
#1.  Customer Management
#1.1 Add Customer
#1.2 Display Customer
#1.3 Search Customer
#1.4 Update Customer
#1.5 Delete Customer
#########################
#2. Account Management
#2.1 Deposit Amout
#2.2 Withdraw Amount
#2.3 Fund Transfer
#2.4 Close an Account
#2.5 Balance Eqnquiry
#2.6 Account Statement
#2.7 All Account Holders List
#########################
#3.  Loan Management
#3.1 Add Loan Account
#3.2 Display Loan Account
#3.3 Search Loan Account
#3.4 Update Loan Account
#3.5 Delete Loan Account
#########################
#----------------------------------------------------------------------------------------------------------

#TejSaxena_XIIA_BankingManagementSystem_17642831

import random
import mysql.connector
from mysql.connector import errorcode
from mysql.connector import(connection)

from datetime import datetime

def displayAll():
    try:     
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='tej0811',database='banking' ,
        auth_plugin='mysql_native_password')
        cursor=mydb.cursor()
        Qry=('select id, accno,name,acctype,openingbalance,createddate,CurrentBalance from tblBankAccount');
        cursor.execute(Qry);
        print("===================Account Holder Details==================================")
        for (id, accno,name,acctype,openingbalance,createddate,CurrentBalance) in cursor:
            print(id," ", accno,name," ",acctype," ",openingbalance," ",createddate," ",CurrentBalance," ")
        print("===================Account Holder Details==================================")
      
        cursor.close()
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        else:
            print(err)
    finally:
        cursor.close()
        mydb.close()   

def displaySp(num): 
    try:    
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='tej0811',database='banking' ,
        auth_plugin='mysql_native_password')
        cursor=mydb.cursor()
        
        Qry=("""select id, accno,name,acctype,openingbalance,createddate,CurrentBalance 
                from tblBankAccount
                where accno= %s""");
        data=(num,)
        cursor.execute(Qry,data)
    
        print("===================Account Statement Details==================================")
        for (id, accno,name,acctype,openingbalance,createddate,CurrentBalance) in cursor:
            print(id," ", accno,name," ",acctype," ",openingbalance," ",createddate," ",CurrentBalance," ")
            #currentbalance=DepositAmount
        print("===================Account Statement Details==================================")
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        else:
            print(err)
    finally:
        cursor.close()
        mydb.close() 
def displayAccountStatement(num): 

    try:    
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='tej0811',database='banking' ,
        auth_plugin='mysql_native_password')
        cursor=mydb.cursor()
        
        Qry=("""select accid,AccNo,name, TransactionType,TransactionAmount,transdate
                from tblBankAccountTransaction BAT, tblBankAccount BA
                where BAT.accid = BA.id and AccNo= %s""");
        data=(num,)
        cursor.execute(Qry,data)
        
        print("===================Account Statement Details==================================")
        for (accid, AccNo,name,TransactionType,TransactionAmount,transdate) in cursor:
            print(accid," ", AccNo," ",name," ",TransactionType," ",TransactionAmount," ",transdate," ")
            #currentbalance=DepositAmount
        print("===================Account Statement Details==================================")
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        else:
            print(err)
    finally:
        cursor.close()
        mydb.close()   

def depositAndWithdraw(num1,num2):
    try:
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='tej0811',database='banking' ,
        auth_plugin='mysql_native_password')
        cursor=mydb.cursor()
        
        Qry=("""select id, accno,name,acctype,openingbalance,createddate,CurrentBalance
                from tblBankAccount
                where accno= %s""");
        data=(num1,)
        cursor.execute(Qry,data)
        currentbalance=0
        RecFound=0
        #records = cursor.fetchall()
        
        for (id, accno,name,acctype,openingbalance,createddate,CurrentBalance) in cursor:
            print("===================Start Account Holder Deatils==================================")
            print(id," ", accno,name," ",acctype," ",openingbalance," ",createddate," ",CurrentBalance," ")
            currentbalance=CurrentBalance
            accid=id
            
            RecFound=1
            print("===================End Account Holder Deatils==================================")
        if(RecFound==0):
            print("No Matching Record")
            input("press any key to continue")
            return
        #print("CurrentBalance ",currentbalance )
        if num2 == 1 :
            amount = int(input("Enter the amount to deposit : "))
            currentbalance += amount
            TransType='D'
        elif num2 == 2 :
            amount = int(input("Enter the amount to withdraw : "))
            TransType='W'
            if amount <= currentbalance :
                currentbalance -=amount
            else :
                print("You cannot withdraw larger amount")
                return
        
        Qry=("""update tblbankaccount set CurrentBalance= %s where accno= %s""");
        data=(currentbalance,num1,)
        cursor.execute(Qry,data)
        Qry=("""insert into tblBankAccountTransaction(accid,TransactionType,TransactionAmount ,transdate ) 
             values(%s,%s,%s,%s)""");
        data=(accid,TransType,amount,formatted_date)
        cursor.execute(Qry,data)
        mydb.commit()
        print("Your account is updated")
        Qry=("""select id, accno,name,acctype,openingbalance,createddate,CurrentBalance 
             from tblBankAccount 
             where accno=%s""");
        data=(num1,)
        cursor.execute(Qry,data)
        print("===================Account Details==================================")
        for (id, accno,name,acctype,openingbalance,createddate,CurrentBalance) in cursor:
            print(id," ", accno,name," ",acctype," ",openingbalance," ",createddate," ",CurrentBalance," ")
        print("===================Account Details==================================")
        cursor.close()
        
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        else:
            print(err)
    finally:
        if mydb.is_connected():
            mydb.close()    

def instantFundTransfer(SourceAccountId,DestinationAccountId,toBeTrasferredAmount): 
    try:
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='tej0811',database='banking' ,
        auth_plugin='mysql_native_password')
        cursor=mydb.cursor()
        
        Qry=("""select id, accno,name,acctype,openingbalance,createddate,CurrentBalance 
             from tblBankAccount 
             where accno= %s""");
        data=(SourceAccountId,)
        cursor.execute(Qry,data)
        SourceAccid = ''
        DestinationAccid = ''
        print("===================Source Account Holder Details Before Transfer==================================")
        for (id, accno,name,acctype,openingbalance,createddate,CurrentBalance) in cursor:
            print(id," ", accno,name," ",acctype," ",openingbalance," ",createddate," ",CurrentBalance," ")
            sourcecurrentbalance=CurrentBalance
            SourceAccid=id
    
        Qry=("""select id, accno,name,acctype,openingbalance,createddate,CurrentBalance 
             from tblBankAccount 
             where accno= %s""");
        data=(DestinationAccountId,)
        cursor.execute(Qry,data)
        print("===================Destination Account Holder Details Before Transfer==================================")
        for (id, accno,name,acctype,openingbalance,createddate,CurrentBalance) in cursor:
            print(id," ", accno,name," ",acctype," ",openingbalance," ",createddate," ",CurrentBalance," ")
            destinationcurrentbalance=CurrentBalance
            DestinationAccid=id
        
        if SourceAccid == '' :
            print("Source Account No. doesn't exists")
            return
        if DestinationAccid == '' :
            print("Destination Account No. doesn't exists")
            return
        if toBeTrasferredAmount > sourcecurrentbalance :
            print("You cannot transfer amount larger than current balance in Source Account")
            return
    
        sourcecurrentbalance -= toBeTrasferredAmount
        destinationcurrentbalance += toBeTrasferredAmount
        
        print (destinationcurrentbalance)
        
        Qry=("""update tblbankaccount set CurrentBalance= %s where accno= %s""");
        data=(sourcecurrentbalance,SourceAccountId,)
        cursor.execute(Qry,data)
        Qry=("""insert into tblBankAccountTransaction(accid,TransactionType,TransactionAmount ,transdate ) 
             values(%s,%s,%s,%s)""");
        data=(SourceAccid,'W',toBeTrasferredAmount,formatted_date)
        cursor.execute(Qry,data)
        mydb.commit()
        
        Qry=("""update tblbankaccount set CurrentBalance= %s where accno= %s""");
        data=(destinationcurrentbalance,DestinationAccountId,)
        cursor.execute(Qry,data)
        Qry=("""insert into tblBankAccountTransaction(accid,TransactionType,TransactionAmount ,transdate ) 
             values(%s,%s,%s,%s)""");
        data=(DestinationAccid,'D',toBeTrasferredAmount,formatted_date)
        cursor.execute(Qry,data)
        mydb.commit()
        
        print("Your accounts are updated")
    
        Qry=("""select id, accno,name,acctype,openingbalance,createddate,CurrentBalance 
             from tblBankAccount 
             where accno=%s""");
        data=(SourceAccountId,)
        cursor.execute(Qry,data)
        print("===================Source Account Holder Details After Transfer==================================")
        for (id, accno,name,acctype,openingbalance,createddate,CurrentBalance) in cursor:
            print(id," ", accno,name," ",acctype," ",openingbalance," ",createddate," ",CurrentBalance," ")
    
        Qry=("""select id, accno,name,acctype,openingbalance,createddate,DepositAmount 
             from tblBankAccount 
             where accno=%s""");
        data=(DestinationAccountId,)
        cursor.execute(Qry,data)
        print("===================Destination Account Holder Details After Transfer==================================")
        for (id, accno,name,acctype,openingbalance,createddate,CurrentBalance) in cursor:
            print(id," ", accno,name," ",acctype," ",openingbalance," ",createddate," ",CurrentBalance," ")
    
        cursor.close()
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        else:
            print(err)
    finally:
        if mydb.is_connected():
            mydb.close()    
       
def InsertAccount() : 
    try:
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='tej0811',database='banking' ,
        auth_plugin='mysql_native_password')
        cursor=mydb.cursor()
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        
        name = input("Enter the account holder name : ")
        type = input("Ente the type of account [C/S] : ")
        deposit = int(input("Enter The Initial amount(>=500 for Saving and >=1000 for current:"))
        accNo= random.randint(1000000,9999999)
            
        Qry=("""insert into tblbankaccount(accno,name,acctype,openingbalance,CurrentBalance,createddate ) 
             values(%s,%s,%s,%s,%s,%s)""");
        data=(accNo,name,type,deposit,deposit,formatted_date)
        cursor.execute(Qry,data)
        mydb.commit()
        cursor.close()
        print("\n\n\nAccount Created with Account Number:",accNo)
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        else:
            print(err)
    finally:
        cursor.close()
        mydb.close()    
  
   
def DeleteAccount(num11):
    try:
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='tej0811',database='banking' ,
        auth_plugin='mysql_native_password')
        cursor=mydb.cursor()
        
        Qry=("""select id, accno,name,acctype,openingbalance,createddate,CurrentBalance 
             from tblBankAccount 
             where accno= %s """);
        data=(num11,)
        cursor.execute(Qry,data)
        
           
        print("===================Start Account Holder Deatils==================================")
        for (id, accno,name,acctype,openingbalance,createddate,CurrentBalance) in cursor:
            print(id," ", accno,name," ",acctype," ",openingbalance," ",createddate," ",CurrentBalance," ")
        print("===================End Account Holder Deatils==================================")
        
        Qry=("""delete from tblbankaccount where accno= %s""");
        data=(num11,)
        cursor.execute(Qry,data)
        mydb.commit()
        print("Your account is deleted")
        cursor.close()
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        else:
            print(err)
    finally:
        if mydb.is_connected():
            mydb.close() 
            cursor.close()     
    
def InsertCustRecord():
    try:
        mydb=connection.MySQLConnection(user='root',passwd='tej0811',
				host='localhost',
				database='banking')
        Cursor = mydb.cursor()
        cust_id=random.randint(1000000,9999999)
        name=input("Enter Name	: ")
        # name=input("Enter Full Name	: ")
        gender=input("Enter Gender : ")
		#dob=date(input("Enter Date of Birth : "))
        mstat=input("Enter Marital Status(U: Unmarried, M: Married, D: Divorcee) : ")
        spouse=input("Enter Spouse Name : ")
        dependents=int(input("Enter No. of dependents :"))
        nationality=input("Enter Nationality :")
        UID =input("Enter Adhaar No:") 
        pan=input("Enter PAN Card No. :")
        qual=input("Enter Qualification :")
        contact=int(input("Enter Contact No. : "))
        email=input("Enter Email Id : ")
        resadd=input("Enter Residential Address : ")
        empname=input("Enter Employer Name : ")
        empadd=input("Enter Employer Address : ")
        des=input("Enter Designation : ")
        exp=int(input("Enter Professional Experience : "))
        grossincome=float(input("Enter Total Gross Income : "))
        netincome=float(input("Enter Total Net Income : "))
        assetdetails=input("Enter Assets Ownership : ")
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
   
        Qry=("""INSERT INTO tblCustomer (CustId,name,gender,createddate,mstat,spouse,dependents,
             nationality,UID,pan,qual,contact,email,resadd,empname,empadd,des,exp,grossincome,netincome,assetdetails) 
            VALUES (%s, %s, %s, %s ,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s, %s)""")
        data=(cust_id,name,gender,formatted_date,mstat,spouse,dependents,
              nationality,UID,pan,qual,contact,email,resadd,empname,empadd,des,exp,grossincome,netincome,assetdetails)
        Cursor.execute(Qry, data)
        mydb.commit()
        Cursor.close()
        mydb.close()
        print("Record Inserted........................")
	
    except mysql.connector.Error as err:
    	if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
    		print("Something is wrong with your username and password")
    	elif err.errno==errorcode.ER_BAD_DB_ERROR:
    		print("Database doesn't exist")
    	else:
    		print(err)
    finally:
        if mydb.is_connected():
            mydb.close() 
            Cursor.close()     

def DisplayCustRecord():
    try:
        mydb=connection.MySQLConnection(user='root',passwd='tej0811',
				host='localhost',
				database='banking')
        Cursor = mydb.cursor()
        query=("""SELECT CustId,name,gender,createddate,mstat,spouse,dependents,
               nationality,UID,pan,qual,contact,email,resadd,empname,empadd,des,
               exp,grossincome,netincome,assetdetails 
               FROM tblcustomer""")
        Cursor.execute(query)
        Rec_count=0
        for (CustId,name,gender,createddate,mstat,spouse,dependents,
             nationality,UID,pan,qual,contact,email,resadd,empname,empadd,
             des,exp,grossincome,netincome,assetdetails) in Cursor:
            Rec_count+=1
            # 	print("====================================================================================")
            print("Customer ID : ", CustId)
            print("Name	: ", name)
            print("Gender : ", gender)
            print("Marital Status : ", mstat)
            print("Spouse Name : ", spouse)
            print("No. of dependents :", dependents)
            print("Nationality :", nationality)
            print("UID :", UID)
            print("PAN :", pan)
            print("Qualification :", qual)
            print("Contact No. : ", contact)
            print("Email Id : ", email)
            print("Residential  Address : ", resadd)
            print("Employer Name : ", empname)
            print("Employer Address : ",	empadd)
            print("Designation : ", des)
            print("Experience : ", exp)
            print("Total Gross Income : ", grossincome)
            print("Total Net Income : ", netincome)
            print("Assets Ownership : ", assetdetails)
            print("====================================================================================")
            input("Press any key to continue")
        print(Rec_count,"Record(s) found")
        Cursor.close()
        mydb.close()
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        else:
            print(err)
    finally:
        if mydb.is_connected():
            mydb.close() 
            Cursor.close()     


def SearchCustRecord():
    try:
        mydb=connection.MySQLConnection(user='root',passwd='tej0811',host='localhost',database='banking')
        Cursor = mydb.cursor()
        cust_id=input("Enter Customer ID to be searched from the database : ")
        query=("""SELECT CustId,name,gender,createddate,mstat,spouse,dependents,
               nationality,UID,pan,qual,contact,email,resadd,empname,empadd,des,
               exp,grossincome,netincome,assetdetails 
               FROM tblCustomer 
               WHERE CustId = %s """)
        data=(cust_id,)
        Cursor.execute(query,data)
        Rec_count=0
        for (CustId,name,gender,createddate,mstat,spouse,dependents,nationality,UID,pan,qual,contact,email,resadd,
             empname,empadd,des,exp,grossincome,netincome,assetdetails) in Cursor:
            Rec_count+=1
            print("====================================================================================")
            print("Customer ID : ", cust_id)
            print("Name	: ", name)
            print("Gender : ", gender)
            #print("Date of Birth : ", dob)
            print("Marital Status : ", mstat)
            print("Spouse Name : ", spouse)
            print("No. of dependents :", dependents)
            print("Nationality :", nationality)
            print("UID :", UID)
            print("PAN :", pan)
            print("Qualification :", qual)
            print("Contact No. : ", contact)
            print("Email Id : ", email)
            print("Residential  Address : ", resadd)
            print("Employer Name : ", empname)
            print("Employer Address : ",	empadd)
            print("Designation : ", des)
            print("Experience : ", exp)
            print("Total Gross Income : ", grossincome)
            print("Total Net Income : ", netincome)
            print("Assets Ownership : ", assetdetails)
            print("====================================================================================")
            if Rec_count%2==0:
                input("Press any key to continue")
        print(Rec_count,"Record(s) found")
        Cursor.close()
        mydb.close()

    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        else:
            print(err)
    finally:
        if mydb.is_connected():
            mydb.close() 
            Cursor.close()     


def UpdateCustRecord():
    try:
        mydb=connection.MySQLConnection(user='root',passwd='tej0811',host='localhost',database='banking')
        Cursor = mydb.cursor()
        cust_id=input("Enter Customer ID to be updated in the database : ")
        #Qry=("SELECT * FROM CUSTOMER WHERE cust_id = %s ")
        #		rec_srch=(cust_id)
        print("Enter Customer Record for updation")
        
        name=input("Enter Full Name	: ")
        gender=input("Enter Gender : ")
        mstat=input("Enter Marital Status(Unmarried, Married, Divorcee) : ")
        spouse=input("Enter Spouse Name : ")
        dependents=int(input("Enter No. of dependents :"))
        nationality=input("Enter Nationality :")
        UID=input("Enter Adhaar No :") 
        pan=input("Enter PAN Card No. :")
        qual=input("Enter Qualification :")
        contact=int(input("Enter Contact No. : "))
        email=input("Enter Email Id : ")
        resadd=input("Enter Residential Address : ")
        empname=input("Enter Employer Name : ")
        empadd=input("Enter Employer Address : ")
        des=input("Enter Designation : ")
        exp=int(input("Enter Professional Experience (years) : "))
        grossincome=float(input("Enter Total Gross Income : "))
        netincome=float(input("Enter Total Net Income : "))
        assetdetails=input("Enter Assets Ownership : ")
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        
        Qry=("""UPDATE tblCustomer SET name=%s,gender=%s,mstat=%s,spouse=%s,dependents=%s,
             nationality=%s,UID=%s,pan=%s,qual=%s,contact=%s,email=%s,resadd=%s,empname=%s,
             empadd=%s,des=%s,exp=%s,grossincome=%s,netincome=%s,assetdetails=%s,modifieddate=%s 
             WHERE custid=%s""")
        				
        data=(name,gender,mstat,spouse,dependents,
              nationality,UID,pan,qual,contact,email,resadd,empname,empadd,des,exp,grossincome,
              netincome,assetdetails,formatted_date,cust_id)
        Cursor.execute(Qry, data)
        mydb.commit()
        Cursor.close()
        mydb.close()
        print(Cursor.rowcount, "Record(s) Updated Successfully.......................")
	
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        else:
            print(err)
    finally:
        if mydb.is_connected():
            mydb.close() 
            Cursor.close()     


def DeleteCustRecord():
    try:
        mydb=connection.MySQLConnection(user='root',passwd='tej0811',host='localhost',database='banking')
        Cursor = mydb.cursor()
        cust_id=input("Enter Customer ID to be deleted in the database : ")
        Qry=("""DELETE FROM tblCustomer WHERE CustID=%s""")
        del_rec=(cust_id,)
        Cursor.execute(Qry,del_rec)
        mydb.commit()
        Cursor.close()
        mydb.close()
        print(Cursor.rowcount, "Record(s) Deleted Successfully.......................")
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        else:
            print(err)
    else:
        mydb.close()
    
 
def InsertLoanRecord():
    try:
        mydb=mysql.connector.connect(user='root',passwd='tej0811',
                                 host='localhost',
                                 database='banking',auth_plugin='mysql_native_password')
        Cursor=mydb.cursor()
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        #loan_id=int(input("Enter Loan ID : "))
        loan_type=input("Enter Loan Type (H:Home E:Education V:Vehicle P:Personal) : ")
        loan_amount=float(input("Enter Loan Amount : "))
        loan_tenure=int(input("Enter Loan Tenure (Months) : "))
        roi=float(input("Enter Rate of Interest (pa) : "))
        emi=float(input("Enter EMI : "))
        CustId=input("Enter Customer Number : ")
        Qry=("""INSERT INTO tblBankLoan (LoanType ,LoanAmount ,LoanTenure,LoanROI ,LoanEMI,CustId,createddate )  
             VALUES (%s, %s, %s, %s, %s, %s, %s)""")
        data=(loan_type, loan_amount, loan_tenure, roi, emi, CustId,formatted_date)
        Cursor.execute(Qry, data)
        mydb.commit()
        Cursor.close()
        mydb.close()
        print("Record Inserted........................")
	
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        else:
            print(err)
    finally:
        if mydb.is_connected():
            mydb.close() 
            Cursor.close()     

def DisplayLoanRecord():
    try:
        mydb=mysql.connector.connect(user='root',passwd='tej0811',host='localhost',database='banking',
        auth_plugin='mysql_native_password')
        Cursor=mydb.cursor()
        query = ("""SELECT LoanId,LoanType ,LoanAmount ,LoanTenure,LoanROI ,LoanEMI,CustId,createddate 
                 FROM tblBankLoan""")
        Cursor.execute(query)
        print(Cursor.rowcount, "Record(s) Found.......................")
        for (LoanId,LoanType ,LoanAmount ,LoanTenure,LoanROI ,LoanEMI,CustId,createddate) in Cursor:
        # 	print("====================================================================================")
            print("Loan ID: ", LoanId)
            print("Loan Type	: ", LoanType)
            print("Loan Amount : ", LoanAmount)
            print("Loan Tenure (Monhts) : ", LoanTenure)
            print("Rate of Interest (pa) : ", LoanROI)
            print("EMI :", LoanEMI)
            print("Customer ID :", CustId)
            print("====================================================================================")
            input("Press any key to continue")
        Cursor.close()
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        else:
            print(err)
    finally:
        if mydb.is_connected():
            mydb.close() 
 
def SearchLoanRecord():
    try:
        mydb=mysql.connector.connect(user='root',passwd='tej0811',host='localhost',database='banking',
        auth_plugin='mysql_native_password')
        Cursor=mydb.cursor()
        loan_id=input("Enter Loan ID to be searched from the database : ")
        query=("""SELECT LoanId,LoanType ,LoanAmount ,LoanTenure,LoanROI ,LoanEMI,CustId,createddate 
               FROM tblBankLoan 
               WHERE loanid = %s """)
        rec_srch=(loan_id,)
        Cursor.execute(query, rec_srch)
        Rec_count=0
        for (LoanId,LoanType ,LoanAmount ,LoanTenure,LoanROI ,LoanEMI,CustId,createddate) in Cursor:
            Rec_count+=1
        # 	print("====================================================================================")
            print("Loan ID: ", LoanId)
            print("Loan Type	: ", LoanType)
            print("Loan Amount : ", LoanAmount)
            print("Loan Tenure (Monhts) : ", LoanTenure)
            print("Rate of Interest (pa) : ", LoanROI)
            print("EMI :", LoanEMI)
            print("Customer ID :", CustId)
            print("====================================================================================")
            input("Press any key to continue")
        print(Rec_count,"Record(s) found")
        Cursor.close()
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        else:
            print(err)
    finally:
        if mydb.is_connected():
            mydb.close() 

def UpdateLoanRecord():
    try:
        mydb=mysql.connector.connect(user='root',passwd='tej0811',host='localhost',database='banking',
        auth_plugin='mysql_native_password')
        Cursor=mydb.cursor()
        loan_id=input("Enter Loan ID to be updated from the database : ")
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        
        loan_type=input("Enter Loan Type (H:Home E:Education V:Vehicle P:Personal) : ")
        loan_amount=float(input("Enter Loan Amount : "))
        loan_tenure=int(input("Enter Loan Tenure (Months) : "))
        roi=float(input("Enter Rate of Interest (pa) : "))
        emi=float(input("Enter EMI : "))
        Qry=("""UPDATE tblBankLoan SET LoanType=%s,LoanAmount=%s,LoanTenure=%s,LoanROI=%s,LoanEMI=%s, modifieddate=%s 
             WHERE loanid=%s""")
        data=(loan_type, loan_amount, loan_tenure, roi, emi, formatted_date,loan_id)
        Cursor.execute(Qry, data)
        print(Cursor.rowcount, "Record(s) Updated Successfully.......................")
        mydb.commit()
        Cursor.close()
        mydb.close()
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        else:
            print(err)
    finally:
        if mydb.is_connected():
            mydb.close() 
        
def DeleteLoanRecord():
    try:
        mydb=mysql.connector.connect(user='root',passwd='tej0811',host='localhost',database='banking',
        auth_plugin='mysql_native_password')
        Cursor=mydb.cursor()
        loan_id=input("Enter Loan ID to be deleted from the database : ")
        
        Qry=("Delete from tblBankLoan WHERE loanid=%s")
        data=(loan_id,)
        Cursor.execute(Qry, data)
        print(Cursor.rowcount, "Record(s) Deleted Successfully.......................")
        mydb.commit()
        Cursor.close()
        mydb.close()
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        else:
            print(err)
    finally:
        if mydb.is_connected():
            mydb.close() 
        
def MenuCustomer():
    while True:
#        clrscreen()
#        MenuCustomer.clrscreen()
#        clrscreen()
        print("\t\t\t Customer Management\n")
        print("====================================================================================")
        print("1. Add Customer")
        print("2. Display Customer")
        print("3. Search Customer")
        print("4. Update Customer")
        print("5. Delete Customer")
        print("6. Return to Main Menu")
        print("====================================================================================")
    
        choice = int(input("Enter Choice between 1 to 6------------> : "))
        if choice==1:
            InsertCustRecord()
        elif choice==2:
            DisplayCustRecord()
        elif choice==3:
            SearchCustRecord()
        elif choice==4:
        	UpdateCustRecord()
        elif choice==5:
            DeleteCustRecord()
        elif choice==6:
            return
        else:
            print("No such Function....Enter Your Choice again")
        input("Enter any key to continue")
    return

def MenuBankAccount():
    while True:
        print("\t\t\t Bank Account Management\n")
        print("====================================================================================")
        print("\t1. New Account")
        print("\t2. Deposit Amount")
        print("\t3. Withdraw Amount")
        print("\t4. Fund Transfer")
        print("\t5. Close an Account")
        print("\t6. Balance Enquiry")
        print("\t7. Account Statement")
        print("\t8. All Account Holder List")
        print("\t9. Return to Main Menu")
        print("====================================================================================")
    
        ch = input("Enter Choice between 1 to 9------------> : ")
        if ch == '1':
            InsertAccount()
        elif ch =='2':
            num = int(input("\tEnter The Account No. : "))
            depositAndWithdraw(num, 1)
        elif ch == '3':
            num = int(input("\tEnter The Account No. : "))
            depositAndWithdraw(num, 2)
        elif ch == '4':
            num =int(input("\tEnter Source Account No. : "))
            num1 =int(input("\tEnter Destination Account No. : "))
            num2 =int(input("\tEnter Transfer Amount. : "))
            instantFundTransfer(num,num1,num2)
        elif ch == '5':
            num =int(input("\tEnter The Account No. : "))
            DeleteAccount(num)
        elif ch == '6':
            num = int(input("\tEnter The Account No. : "))
            displaySp(num)
        elif ch == '7':
            num =int(input("\tEnter The Account No. : "))
            displayAccountStatement(num)
        elif ch == '8':
            displayAll();
        elif ch == '9':
            print("\tThanks for using Account Management")
            return
        else:
            print("No such Function....Enter Your Choice again")
        input("Enter any key to continue")
    return

def MenuLoan():
    while True:
        print("\t\t\t Loan Management\n")
        print("====================================================================================")
        print("1. Add Loan Account")
        print("2. Display Loan Account")
        print("3. Search Loan Account")
        print("4. Update Loan Account")
        print("5. Delete Loan Account")
        print("6. Return to Main Menu")
        print("====================================================================================")
        choice=int(input("Enter Choice between 1 to 6------------> : "))
        
        if choice==1:
            InsertLoanRecord()
        elif choice==2:
            DisplayLoanRecord()
        elif choice==3:
            SearchLoanRecord()
        elif choice==4:
        	UpdateLoanRecord()
        elif choice==5:
            DeleteLoanRecord()
        elif choice==6:
            return
        else:
            print("No such Function....Enter Your Choice again")
        input("Enter any key to continue")     
    return

def intro():
    
    print("\t\t\t\t**********************")
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t**********************")

    print("\t\t\t\tBrought To You By:")
    print("\t\t\t\tTej Saxena")
    #print("\t\t\t\tTej Saxena and Team")
    #print("\t\t\t\tClass - XII A")

# start of the program
ch=''
intro()
while True:
    #system("cls");
    print("====================================================================================")
    print("\tMAIN MENU")
    print("\t1. Customer Management")
    print("\t2. Account Management")
    print("\t3. Loan Management")
    print("\t4. Exit")
    print("====================================================================================")
    print("\tSelect Your Option (1-4) ")
    ch = input()
    if ch == '1':
        MenuCustomer()
    elif ch =='2':
        MenuBankAccount()
    elif ch == '3':
        MenuLoan()
    elif ch == '4':
        print("\tThanks for using Bank Management System")
        break
    else :
        print("Invalid choice")
    


