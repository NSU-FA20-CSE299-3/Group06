<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">&nbsp;</p>
<p align="center"><strong><img src="https://media.dhakatribune.com/uploads/2016/11/nsulogo.jpg" alt="" width="307" height="172" /></strong></p>
<p align="center"><strong>North South University</strong></p>
<p align="center">Department of Electrical &amp; Computer Engineering</p>
<p align="center"><strong>Project Report</strong></p>
<p align="center"><strong>Group No</strong>: 06</p>
<p align="center"><strong>Fall 2020</strong></p>
<p align="center"><strong>Project Name</strong>: STUDENT MANAGEMENT PORTAL</p>
<p align="center"><strong>Course No</strong>: CSE 299 <strong>Sec</strong><strong>:</strong> 03</p>
<p align="center"><strong>Faculty</strong>: Shaikh Shawon Arefin Shimon (Sas3)</p>
<p align="center"><strong><u>Member</u></strong><u>:</u></p>
<p align="center"><strong>Name</strong><strong>:</strong> Fatin Fuad Karim</p>
<p align="center"><strong>ID</strong><strong>:&nbsp; </strong>1621197642</p>
<p align="center"><strong>Email</strong><strong>:</strong> <a href="mailto:">fatin.fuad@northsouth.edu</a></p>

<p align="center"><strong>Git Repository</strong><strong>: </strong><a href="https://github.com/NSU-FA20-CSE299-3/Group06">https://github.com/NSU-FA20-CSE299-3/Group06/</a></p>
<p align="center"><strong>Date Prepared</strong><strong>: </strong>21/01/2021</p>
<p><strong>&nbsp;</strong></p>
<p><strong>&nbsp;</strong></p>
<h2> Project Name:  STUDENT MANAGEMENT PORTAL </h2><br>
<h3 id="table-of-contents">Table of contents</h3>

<ol>
  <a href="">Introduction<br></a>
  <a href="">Software Specification<br></a>
  <a href="">Technology<br></a>
  <a href="">BusinessPlan/Monetization</a><br>
  <a href="">Conclusion</a><br><hr>

</ol>
<br>


<h2 id="#introduction">1. Introduction</h2>
<h3>1.1 Project Idea:</h3>
<p>We learn more about an academic institute by keeping track of their students. Due to Covid-19 pandemic our education system totally shifted online. Unfortunately, Most of the Schools in our country does not have a system to keep in touch with their students.
As a result, The teachers and students are almost disconnected from each other, On the other hand it seems due to Covid-19 educational institute will not open soon.
So there is no communication between the teachers and students, To create communication between them we have come up with School Management Portal.
Our mission is to connect all existing Students of a institution no matter where they are in this world with internet connection. Each students can find the latest educational update inside the website.
Student Management Portal is a web application built with the latest technologies, It will builds the connection between the teachers and students.
</p>

<h2 id="features">2. Software Specification</h2>
This project has the following features -
<h3>2.1 User Registration:</h3>
  To access any platform user's must have to registered by the authority, After completing the registration user will be given a username and password by which user can enter the portal.And it must contain 150 characters or fewer characters. Letters, digits and @/./+/-/_ are permitted only.
   <br>
   <br>
 <p align="center">
   <img width="700" height="420" src="Mockup/signup.png"><br>
   Figure 1.0
 </p>
 <h3>2.2 Login to a specific platform :</h3>
  The main feature of ‘STUDENT MANAGEMENT PORTAL’ is that users will be able to view different platforms on one window after logging in once. This section is know as the profile. The users information is shown on the left as seen in figure 2.0.<br>
  <br>


  <p align="center">
  <img width="700" height="400" src="Mockup/login.png"><br>
  Figure 2.0
</p>
<br>
<br>
  <p>Currently the following functions are available -
  <p>
    * Users/Teachers can access class routine, syllabus, exam routine section.<br>
    * Users/Teachers can add or delete their class routine, syllabus, exam routine. <br>
    * Users/Teachers will also be able to see posts of the specific class routine, syllabus, exam routine.</p> <br><br><br>

  <p align="center">
  <img width="700" height="420" src="images/insidesite.png"><br>
  Figure 3.0
</p>  
<h3>2.3 Admin Panel:</h3>
There's also a Admin panel from which the admin can delete unwanted users. Assign new admins with filtered permission and monitor activities.
<p align="center">
<img width="700" height="420" src="Mockup/admin.png"><br>
Figure 4.0
</p>

 <h2 id="#technology">3. Technology</h2>
 <h3>3.1 Proposed Technology Stack: </h3>
 <p>For UI design we decided to use Bootstrap. Bootstrap is a free and open-source CSS framework directed at responsive front-end web development. It contains CSS and JavaScript-based design templates for typography, forms, buttons, navigation and other interface components. Bootstrap will be used over the usual HTML and CSS. <br> <br>
 And for the backend We will use Python’s web framework - Django as the website’s backend. Django hides website's source code. The framework has protection against XSS and CSRF attacks, SQL injections, clickjacking, etc. Django notifies of a number of common security mistakes better than PHP.<br> <br>
On the other hand we will be using SQLite which is versatile and portable.</p>

<br>

 <h3>3.2 Implemented Technology Stack: </h3>
 <p>We used Python’s web framework - Django as the website’s backend as we mentioned eariler in our proposal, On the other hand we used HTML,CSS and Bootstrap for our frontend design. 
<br>
For database we used SQLite</p>

<h5>3.2.1 Design Pattern: </h5>
 <p>By default the Django framework follows the model-view-template pattern which a close immitation of the Model-view-controller. We decided to stay with this MVT pattern</p>



<h2 id="businessplan">4. BusinessPlan/Monetization</h2>
<p>
As the web application is targeting the authority and students of the Schools, we will try to get fund from the school.
Companies can also place ads on the Portal for jobs charging 100 BDT per day. We will provide an advertisement package for such companies.
</p>

<h2>5. Conclusion</h2>
<p id="#conclusion">
In summary Student Mangement Portal is a web-based software that tries to connect teachers and student together. In this project we achieved most of the functionalities proposed. Except to create the student portal and online admission system. We also didn't able to connect the sign in page with the database who are already registered by the admin and couldn't able to implement the ad sense.. During the development process we faced issues trying to create the model for academic section,connect all the pages with the base file, though later we solved it. In future, we plan to implement these missing functionalities,come up with better solution for the implementation and make the platform even better.</p>
