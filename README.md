![Momentum Fitness](/readme-files/readme-documents/momentum-fitness-heade.png)

Momentum fitness is a project made for fitness enthusiasts and gym-freaks alike! Using django as it's framework, users will be able to purchase products from the online shop,
find out where the gyms are located, purchase a membership and access a members only area. The database currently contains products and articles but will collect users information
and also purchase information of the products. This website is a multi-faceted website for all things gym related!

## UX

This website is created for anyone that has ever been or ever wanted to get to the gym! The site users will be individuals that are 
interested in healthy living with a passion for getting out and working for their goals.

- As a user, I can see what the main focus of the website is.

- As a user, I can navigate through the website efficiently without questioning how to return.

- As a user, I will be able to access any social media the website has.

- As a user, I will be able to view the various products the website has in it's online shop.

- As a user, I will be able to add any of these said products into a cart.

- As a user, I will be able to access this cart and see what products I am about to purchase.

- As a user, As a user I will be able to access the checkout, then go onto purchase these products,

- As a user, I will be able to view a a receipt of my purchase/purchases, informing me of the purchases I have made,

- As a user, i will be able to purchase products and membership packages.

- As a user, I will be able to register on the website simplifying purchases and user experience in the future.

- As a user, I will able to see where the gym's are located.

- As a user, I will be able to login, logout and sign up to the website.

- As a registered user, I will be able to access a members only area in my website with articles and advice.

- As a registered user, I will be able to access and edit my profile and see previous purchases in my order history.

- As an administrator, I will be able to access an admin platform on the website.

- As an administrator, I will be able to add, edit or delete any of the products on this website.

My wireframes were made using [Balsamic](https://balsamiq.com/). You can view them [here](/readme-files/wireframes/momentum-wires.pdf)

## Schema

My Database is divided into five sections. 

- The first and most simple is categories. This is just the 5 categories that the products are divided into.

![Schema Categories](/readme-files/readme-documents/categories-schema.png)

- The second manages the different products on the website.

![Schema Products](/readme-files/readme-documents/products-schema.png)

- The third database contains articles and training advice that is featured on the members only page.

![Schema Articles](/readme-files/readme-documents/articles-schema.png)

- The fourth contains all the orders that have been made via the website.

![Schema Orders](/readme-files/readme-documents/orders-schema.png)

- Finally, the fifth contains all the users that have registered on the website.

![Schema Users](/readme-files/readme-documents/users-schema.png)

### Features left to implement

- In the future I would like to implement subscription payments. Due to time constrains this was not at all possible.

- I will ensure that registration is for subscribed members and I will also implement some form of discounts on the products for these users.

- I would also like to enlarge the size of the members area to have more workout plans, diet plans etc. I could also implement a schedule to book 
into classes and book times with personal trainers.

- I will also update the maps to have tags to describe the exact locations of the gyms.

## technologies used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)

    - HTML5 is a markup language used for structuring and presenting content on the World Wide Web.

- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

    - Cascading Style Sheets (CSS) is a style sheet language used for describing the presentation of a document written in a markup language like HTML.

- [Javascript](https://en.wikipedia.org/wiki/JavaScript)

    - JavaScript (JS) is a lightweight, interpreted, or just-in-time compiled programming language with first-class functions.

- [J. Query (3.4.1)](https://jquery.com/download/)

    - jQuery is a JavaScript library designed to simplify HTML DOM tree traversal and manipulation, as well as event handling, CSS animation, and Ajax.

- [Google Fonts](https://fonts.google.com/)

    - Google Fonts (previously called Google Web Fonts) is a library of 991 free licensed font families, an interactive web directory for browsing the library,
      and APIs for conveniently using the fonts via CSS[1] and Android.

- [Bootstrap (4.4.1)](https://getbootstrap.com/)

    - An open source toolkit for developing with HTML, CSS, and JS.

- [Font Awesome (V5.6.3)](https://fontawesome.com/)

    - A toolkit for icons.

- [Python](https://www.python.org/)

    - Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, 
      Python's design philosophy emphasizes code readability with its notable use of significant whitespace.

- [Django](https://www.djangoproject.com/)

    Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design

- [SQLite](https://www.sqlite.org/index.html)

    - SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.

- [AWS](https://en.wikipedia.org/wiki/Amazon_Web_Services)

    Amazon Web Services (AWS) is a subsidiary of Amazon providing on-demand cloud computing platforms and APIs to individuals, companies, and governments, on a metered pay-as-you-go basis.

## Testing

- Having written my HTML I have validated it on [The W3C Markup validation service](https://validator.w3.org/).

- I have validated my css on [Jigsaw](https://jigsaw.w3.org/css-validator/).

- My Python has been tested using [Pep8online](http://pep8online.com/).

I acknowledge a few lines of my pep8 may not be correct, again I was running on a very tight deadline and while formatting it, it broke some of the code so I had to keep some of it in it's 
original form.

This website was tested across multiple browsers (Chrome, Safari, Firefox and Microsoft edge.) It is also responsive,
having tested it on chrome developer tools across ipad, various iphones, samsungs etc. I have also tested it on iphone x, iphone 7, macbook and desktop.

I chose to remove the hero image from mobile devices and implicate a simple grey background for the reason that, when I was viewing my project on an actual iphone, rather than developer tools
I noticed that the contrasts and colours were too intense for the display. 

### User stories Testing

- As a user, I can see what the main focus of the website is.

![Momentum Fitness](/readme-files/readme-documents/momentum-fitness-heade.png)

- As a user, I can navigate through the website efficiently without questioning how to return.

![navbar](/readme-files/readme-documents/navbar.png)

    - I have been through the website ensuring that the links work.

- As a user, I will be able to access any social media the website has.

![Socials](/readme-files/readme-documents/socials.png)

    - I have clicked on each social media link, checking if they go to the correct site in a new window.

- As a user, I will be able to view the various products the website has in it's online shop.

![Products](/readme-files/readme-documents/products.png)

- As a user, I will be able to add any of these said products into a cart.

- As a user, I will be able to access this cart and see what products I am about to purchase.

![Shopping Cart](/readme-files/readme-documents/shopping-cart.png)

    - I have been through the products, added the to the cart and checked the quantity, etc is correct.

- As a user, As a user I will be able to access the checkout, then go onto purchase these products,

![Checkout](/readme-files/readme-documents/checkout.png)

    - I have been to the checkout, ensuring that my items are there and I can purchase then.

- As a user, I will be able to view a a receipt of my purchase/purchases, informing me of the purchases I have made,

![Checkout Success](/readme-files/readme-documents/checkout-success.png)

    - I have been through the checkout and tested the confirmation

- As a user, i will be able to purchase products and membership packages.

![Members](/readme-files/readme-documents/membership.png)

    - I have visitied the 'join us page' and insured that you can purchase memberships.

- As a user, I will be able to register on the website simplifying purchases and user experience in the future.

![Signup](/readme-files/readme-documents/signup.png)

     I have been to the signup page and attempted registering with success.

- As a user, I will able to see where the gym's are located.

![Map](/readme-files/readme-documents/map.png)

- As a user, I will be able to login, logout and sign up to the website.

![Logout](/readme-files/readme-documents/logout.png)

     I have tested both logging in and out.

- As a registered user, I will be able to access a members only area in my website with articles and advice.

![Members Tips](/readme-files/readme-documents/members-tips.png)

- As a registered user, I will be able to access and edit my profile and see previous purchases in my order history.

![Profile](/readme-files/readme-documents/profile.png)

    - I have been to the profile page and accessed my information.

- As an administrator, I will be able to access an admin platform on the website.

![Admin](/readme-files/readme-documents/admin.png)

    - I have accessed the administration panel and checked everything is up to scratch.

- As an administrator, I will be able to add, edit or delete any of the products on this website.

    - This is done through the administration panel. This has been tested continuously through the project.

### Problems Encountered

During this project I encountered various small problems, some I fixed and some were just not manageable in the short timeframe. I acknowledge there 
are many improvements that can be made for this site but I will continue to advance my knowledge in specific technologies and build my portfolio now that
the course this project was used for is complete. 

    - One problem I have is that when editing the quantity in product details or in the cart the quantity chosen only adds onto the existing quantity.
    This is because I haven't used javascript in this aspect of my work. This is mainly because of the timeframe I had for completing this project.

    - I also have a health form that I was planning to link in when a user bought a membership, questioning reasons for signing up for a membership. Again, due to 
    time constraints, I did not find the time to complete this.

    - I had difficulties using python to hide my maps api key. Because of this the maps api key is not currently hidden. Although within the google dashboard settings,
    it is set so that only this website can use this key.

## Deployment

This site is hosted on Heroku deployed directly from the master branch. To deploy the website you must first create a Heroku account.

- Next you will create an app on Heroku

![Create Heroku App](/readme-files/readme-documents/heroku-create-app.png)

-After this you will want to add your configuration variables. You can do this inside settings of your Heroku app. You want to add IP address, Port, and your 
environment variables of the application. In this case my variable examples are stored in my env_sample.py file. You will have to create your own based on the examples of what
you need. I would highly recommend you store your environment variables in their own file which is ignored when being push to a server.

![Configuration variables](/readme-files/readme-documents/environment-variables.png)

- You will need to ensure you have a Procfile. You do this by entering the following into the bash terminal.

![Procfile](/readme-files/readme-documents/procfile.png)

- You will also need a requirements.txt file.

![Requirements.txt](/readme-files/readme-documents/requirements.png)

- git add . and git commit with a meaningful commit

![Git Commit](/readme-files/readme-documents/git-commit.png)

- Once these requirements are done you can login to your Heroku in the bash terminal.

![Heroku Login](/readme-files/readme-documents/heroku-login.png)

- Next push the application to heroku using.

![Heroku push](/readme-files/readme-documents/git-push.png)

- Finally command Heroku to start running the application 

![Heroku Run](/readme-files/readme-documents/heroku-run.png)

- Now, inside Your Heroku dashboard in the top right of the window you can now open the the application.

![Open App](/readme-files/readme-documents/open-app.png)

-You will also have to set up your own Amazon Web Services account to upload your static and media files into.

**To run locally you can clone this repository directly into the editor of your choice by firstly,**

- copying the link from clone or download on my [GitHub page](https://github.com/TheoNorris/momentum-fitness).

![git copy](/readme-files/readme-documents/git-clone-example.png)

- then, pasting git clone https://github.com/TheoNorris/the-odd-dog-blog.git into your terminal.

![git clone](/readme-files/readme-documents/git-clone.png)

- To cut ties with this GitHub repository, type `git remote rm origin` into the terminal.

![git remove](/readme-files/readme-documents/git-remove.png)

- Upon using this project you will need to use your own environment variables. You can see an example
of the variables I have used in my env_sample.py file. Before you host this project, ensure that you 
have ignored this file before pushing your project to the server.

![env vars](/readme-files/readme-documents/env.png)

## Credits

### content and media

The checkout app and profile app were taken frok my Boutique Ado app I created following the Code Institute videos. being said, slightly altered. Other parts have similarly been created following tutorials.
The articles I have used on this website are copyright free and have been taken from [News USA](https://www.copyrightfreecontent.com/?s=dog+couch).
The photos were taken from [Pexels](https://www.pexels.com/) and a whole variation of photographers. https://www.pexels.com/video/a-woman-lifting-a-cast-iron-kettle-weights-while-in-a-push-up-exercise-position-3209068/
https://www.instagram.com/ajaybhargavguduru/, https://www.instagram.com/andreapiacquadio_/, https://www.instagram.com/kaboompics/, https://www.instagram.com/thisisengineering/
https://www.pexels.com/@ella-olsson-572949?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels
, https://www.pexels.com/@gustavo-fring?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels, https://www.instagram.com/pikx.niagara/, https://www.instagram.com/willpicturethis/

### Acknowledgements

A thank you to [Cormac](https://github.com/armedcor) for his continual help through the project.
