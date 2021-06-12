# Drims Fse Project
 Dealers Reduction In Marketing System


Abstract

Dealer Reduction in marketing system (DRIMS) is a project concerned with Satisfaction of an end user by supplying timely and accurate information related to goods and services that a legal company or seller provides. This project paper contains detailed information on four major courses namely data gathering, system analysis, system design and implementation.
The data gathering part gives an emphasis on what the current situation is like and lists some background projects to compare whereas the system design part states feasibility usability and related concepts. The system analysis part deals with analyzing the system and implementation to some extent is available.

1.1. Introduction
In this era of information having a timely and accurate information is all what we need to make life easier. As we get access to a quality information our actions become influenced by it. Our system overall is dedicated on providing this information by allowing users to describe themselves as legal providers put detailed information about their products and location on the database. Users then select the product/ products or service/ services they want to have and immediately get access to the providers address. If users want to have a transport access they can select a transport provider which is available on the DRIMS system. Users can also give comments and complement products which in turn increases the reliability of the service provider but mainly helps the end user by giving a more suitable choice. This document is a compilation of all the process and description of ways and methods used to solve the problem. 

1.2.2. Vision of the organization
To provide the most satisfactory, helpful, and lovable software on the market which could compete and exceed all other software related to marketing system in eastern Africa.

1.2.3 Background of the project

Previous projects which are on use are accessed by smart phones, the payment is completed via the systems and users can have transportation services. The systems we saw was concerned with connecting on the basis of selling or buying. There is a lack of user participation because of accessibility and end users satisfaction. Our system is designed to encompass a vast amount of society starting from the farmer to Big companies and enterprises sharing information and earning each-others trust. Providers themselves put a price tag on the product or service they give making it even easier to mace economical decision for the end user. Our system is all about provision of information.

1.2.4 Scope of the study

The scope of this project is clearly stated below because of what the system is expected to perform. The proposed system DRIMS (Dealers Reduction IN Marketing System) focuses on Reducing Dealers Among Producers (companies, farmers,….) And End Users (anyone) Since Now Times Because Of Involvement of many Dealers in Marketing There Is a big Increase In Price of goods because Every Single Dealer Needs Extra Profit From Any Product After Some Time The Price Of That good increases From its Real Price. Our system doesn’t include payment and transaction management it intends to provide timely, accurate, and reliable information. 

# Unit testing

This refers to checking each and every system on its own by running it separately.
A. Black box testing
In this technique, we will test to see if the function of the system is fully operational or error free. This includes testing the interface of the system rather than the logical structure of the system.
B. White box testing
We will use this approach to know the internal working style of the system, test that all internal operations are performed according to specifications and all internal components have been exercised and the logical path of the system are correct.

# Integration testing

Concerned with testing architectural design of the system. Approaches of testing are:
1. Top –Down integration testing 
This will perform starting from the top module up to the last or bottom module individually (tests were run as each individual module is integrated). 
2. Bottom-up integration 
We will begin with the lowest –level modules which are combined to cluster, or build that perform a specific software sub-function (top-level).

# System testing

After completion of the above testing mechanisms we would be confident enough to let our system be tested by a third party and accept comments.

# Acceptance Testing

This testing is done by the customer to ensure that the delivered product meets the requirements and works as the customer expected. It includes:- • 
	Alpha- Conducted by users to ensure they accept the system •
	Beta- Users use real data, not test data

3. Proposed System
3.1. Overview
The proposed system is designed to reduce the number of dealers on the marketing system. Project Management System in to computerized system and also designed to store the transaction information in the database for the purpose of reducing the problem faced by manual system. The application composes different forms to enter different project detail to the database and retrieve required information of the project from the database.
3.2. Functional requirement
Functional requirements are requirements that our system is intended to do. The major functional requirements are listed below.
1. Manage account (create, update, Restrict, delete and view account as producer, consumer Or Normal User)
2. Register products and their status.
3. Register Branch Admins
4. Validate users (Authentication)
5. Restrict or Ban Users.
6. Give and accept Comments.
7. Register producer (add, delete and update) and Authenticate Users (OTP or Email Verification) is the data entered is valid or Not and then Register
8. Register consumer (add, delete and update).
9. Show Current Currency Exchange Rate.
10. Show True Price Of goods.
11. Notify Users (Email, Voice or Message Notification).
12. Register Transportation provider.
13. Connect producers with consumers.

3.3. Non-functional requirement
Non-functional requirements are requirement, which has no essential for the system, but it can support and give more quality for the system. 
A. Users interface requirement 
o	User interface should be menu driven and attractive.
o	 The interface should be user friendly. 
o	The system should support error-handling mechanism that display graphic approach and the system guide the user what will be the next action.
B. Authentication Requirement.
o	The system support user name and password to authentic.
o	The system has different privilege to protect intruding.
C. Robustness (Error handling requirement): 
o	The system have error handling mechanisms that is, as errors occur it will not stop functioning rather provide error manages and back to the previous page to give chance to reenter data and process the task by beyond the error.
D. Well documented:
o	the document of this project is processed in well manner
E. Resources: 
o	The system is compatible with specified hardware and software environment 
F. Usability
The system is user friendly. The new system provides web application user interfaces that are compatible with any browsers. 
o	The system shall provide the easy access 
o	 The system is easy to deal with. 
o	The system should is easy to understand. 
o	Unauthorized person should not use the system; rather just view the main page.
o	No one can change the password without login to the system
G. Hardware consideration: 
The following sub-sections discuss the various aspect of hardware requirement. 
o	Processing power: 64 bit operating system and Intel(R) core (TM)i3-237M CPU @1.50GZ.
o	Memory and secondary storage: more than 4GB, 500GB hard disk and swap space (if the RAM is insufficient).
o	Peripherals: includes CD ROM device, network device, etc.
H. Software consideration:
o	Platform: our system supports any operating system and all browsers. I. Performance requirement the system performs its task within a user acceptable time and space. This includes the following:- 
o	Response time: - depending on the strength of available network the system should be response in short period of time.
o	Storage space:-to do work efficiently the processor to be more than 2GB RAM, 
I. Reliability: 
o	The system should be reliable. Appropriate error messages will be provided to users whenever incorrect information is inserted and handle the occurrence of that error.

3.4. System model
System model is an abstraction of a system that focuses on interesting aspects and ignores irrelevant details. The DRIMS system basically contains three types of system models namely:
 	1. Functional model (scenario, use case model) 
2. Object model (class diagram) 
3. Dynamic model (sequence, activity and state chart diagrams).
3.4.1. Scenario
Scenario is real-life example of how the system can be used. It should include scenario name, flow of event, what can go wrong and how this is handled. Based on this the following scenarios for our project are listed below.
1. Registering users (buyer, seller or transport provider)
Initial assumption:
Let assume that our customers use android phone and there is access for using the system.
Normal condition: 
First search the system’s web-page with its link then the web-page displayed with different kinds of button. From this button he selects registration button. The system suggests different kind of registration buttons means buyers registration, sellers registration and transportation registration. Then, the system displays registration forms. Then, he/she will fill the form. The system checks the forms for validation and generate password for them that used for login use case.
What can go wrong?
If the forms not filled appropriately the system display the error encountered when filling forms and request them to reenter. Then they can correct the errors.

2. See products and get access to it
Initial assumption:
A consumer initially has a buyer account and wants to consume/buy a product
Normal: 
The user must load the web page then he must login by using his buyer user name and password. After logged in to his account the system will display every available product on his page. If the buyer wants to see the details of the product before selecting it, he can click the “Detail” button and can have full information of the product. After checking the products and decide what to buy he can click on the “Select” button. If the consumer want to know the price he can he just ne ed to click the “Calculate” button on the product icon after inserting the amount he wants the system will calculate the total amount of money needed to buy that product. If the buyer can afford the price mentioned he just has to click the “agree” button. And the system will automatically send notification to the producer of the product by different means (messaging, email). And if the system will display the address of the seller to the buyer. The system will offer the user if he needs transportation access, if the user needs the access he can see available transportation systems and allow the user to select. After the user selects the system will display the information he needs to contact with the transportation provider.
3. Posting/ updating/ deleting products
Initial assumption:
The producer is already registered and wants to post product/s or update the available one.
Normal: 
The producer will load the page and login to his seller account. If his username and password are valid the system will allow him to load his account. 
If he wants to add new product/s he have to click on “post product” button and browse the product photo/video and detail information from his working device or drag and drop it there.

If he wants to update currently available product/s he can go to the right bottom of the product icon and click on “edit” and then he can edit the photo/video or the detail information.
If he wants to delete a product from his page because of different reasons he just have to click on “delete” button which is appearing on the left bottom of the product icon.
After these actions of the seller the system will notify the updated information to price checker and quality checker and if they give confirmation to the products the system automatically will update the buyer’s and visitor’s(main page of the web) page.
What can go wrong?
If the price/quality checker does not confirm the products the system will give notification to the seller that the product is not a right product/the price is not fair. If the seller gives correction to the product he posted he can go on but if he do the same thing again and again he will get warning or he may be banned at all.
4.Adding/ updating/ deleting transportation system
Initial assumption:
The transport provider may be a single person or a company in which many cars and people are included. For now we use the general term ‘transport provider’ to include both of them. The transport provider is registered on the system and already has an account.
Normal: 
The transport provider logs on to the system. 
If he wants to update the information of available transport system it can update the information of all of the working cars instantaneously. 
If he wants to add newly available transport system it can add a new information by clicking the “add” button.
If it wants to remove the transport system he can delete the information.
What could go wrong?
5. Accessing the system by using any mobile phone
Initial assumption:
The user has an account and a smart phone and he has an access to the net.
Normal the user opens browser and logs in to the system then selects whatever product he is needing.
What can go wrong? 
Someone wants To buy A product From producer But He doesn’t Know How To use or Read so He can use Our Mobile Calling System message or Voice Call instructions and he after All his Requirements are Chosen Then He Selects And Confirms His Choice Then ,He Will Get Phone Number or Email  Address Of Seller And Transport Access.
6. Registering branch admin
Initial assumption: 
The admin will choose whom to employee.
Normal:
If the admin wants to select a branch admin from the recent users (buyer, seller, and transport provider) he can go to their profiles and give permission in order to make them a branch admin with restrictions.
If the admin wants to employ new branch admin by making a registration form for the appliers he must first release the form to be filled then after applicants have registered and filled the form properly until the due date, he will select one/some of them. Then the system will automatically send a notification which includes key features to access the system (by SMS/email) to the applicants.

7. Commenting and complaining

Initial assumption:
The producer, consumer and transportation provider registered and already validated and logged in with proper user name and password. The visitor is visiting the web. And they get the services of DRIMS or just visiting the site.
Normal:
If buyer, seller, transporter or visitor wants to give comment, click the comment button, then texting box will display on page. The commenting user will write the comment and post it by clicking comment button. If they have complain they can complain by clicking on the complain button and write it down then click complain button. And the complaint is visible only for the admins. Then the admins must notified as soon as complaints post complains. And admins give response by clicking on response button on the system then response box will be displayed. Admins add response and click on send response button. That will send back to customer.
What can go wrong?
The customer’s commenting or complaining box is empty. The system must reply with empty comment or complain.
3.4.2. Use case model
Actors
Actors of our projects are:
	Buyers
	Sellers
	Transportation
	Administrator
	Branch administrator
	Phone and computer 
	Visitor
	True price suppliers
	Printers
Primary actors
Primary actors of our project are:
	Buyers
	Sellers
	Transporters
	Visitors
	Administrator
Secondary actors
Secondary actors of our projects are:
	Administrator
	Branch Administrator
	Printers
	Phone
	Price checker
	Quality checker
Use Case identification:
Our system includes the following use cases:-
	login
	register product
	register buyers
	register sellers
	register transport
	display error
	authenticate password
	accepting notification
	register branch admin
	select items
	display item info
	display registered successfully
	verify register
	update products
	update transportations
	commenting 
 View detail: used to view all information included under the system, such as:
	view product
	view price
	view comment
	view transportation
Update details: used to update the required information in the system such as:
	update products
	update transportations
	update price 
 Delete details: Used to delete all irrelevant information in the system, such as
	delete products
Actors’ identifications:


•	Register branch admin
•	Login to the system
•	View information
•	Manage account
•	Accepting comment
•	Log out
•	Give comment
•	Verify register
•	Change password
•	Delete customers 

                                                                                                    
•	Registration
•	Login 
•	Viewing information
•	Accepting notification
•	Logout
•	Update products 
•	Selects transporters
