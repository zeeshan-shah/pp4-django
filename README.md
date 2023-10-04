# TastyBites: Your Culinary Adventure

Welcome to TastyBites, where food meets technology in the most delightful way! 🍔📱

![Am I Responsive](https://res.cloudinary.com/db2fhoogx/image/upload/v1234567/am-i-responsive_xahqyr.jpg)

Are you ready to embark on a culinary journey that combines mouthwatering dishes with a seamless digital experience? Look no further! Our app offers an innovative way to explore our menu, place orders, and enjoy a hassle-free dining experience, whether you're in the restaurant or ordering from the comfort of your home.

With a user-friendly interface, real-time updates, and a rich selection of dishes, your culinary desires are just a click away. Whether you're a hungry customer looking to satisfy your cravings or an admin ready to manage your restaurant's offerings, TastyBites has you covered.

Explore the world of TastyBites, where delicious food and cutting-edge technology converge to bring you a dining experience like no other.

The live link for TastyBites can be found [HERE](https://pp4-django-43b291f3bcf7.herokuapp.com/).

Let's dive in and discover the features, functionalities, and the mouthwatering menu that awaits you!

## User Stories

### User Registration and Authentication

- As a new user, I want to be able to register an account with my name, email, and password, so I can access the ordering system.

- As a registered user, I want to be able to log in with my email and password to access my account and place orders.

### Browsing and Selecting Dishes

- As a user, I want to see a list of dishes with their names and prices when I visit the website's menu page.

- As a user, I want to be able to filter dishes by categories (e.g., appetizers, main courses) to easily find the type of dishes I want.

- As a user, I want to click on a dish to view its details, including a description and an option to add it to my order.

### Creating and Managing Orders

- As a user, I want to be able to select multiple dishes by checking checkboxes next to each dish, so I can add them to my order collectively by clicking the "Place Order" button.

- As a user, I want to see a summary of my order, including the selected dishes and the total price, before confirming it.

- As a user, I want the ability to remove a dish from my order if I change my mind.

- As a user, I want to be able to update my order and add or remove dishes before confirming it.

### Delivery Information

- As a user, I want to provide and update my delivery information, including my name, email, street address, city, state, and zip code.

- As a user, I want to be able to access and update my delivery information from my account profile.

### Confirming Orders

- As a user, I want to be able to confirm my order by clicking a "Confirm Order" button and receive confirmation of my order placement.

- As a user, I want to receive an email confirmation with details of my order after confirming it.

### Contacting Support

- As a user, I want the ability to contact customer support or make inquiries using a contact form.

## Admin User Stories

### Admin Dashboard

- As an admin, I want access to a dedicated admin dashboard where I can manage the restaurant's menu and orders.

- As an admin, I want to log in using my unique admin credentials to access the admin dashboard.

### Managing Menu

- As an admin, I want to be able to add new dishes to the menu by providing details such as dish name, description, price, and image.

- As an admin, I want to edit existing dish information, including name, description, price, and image, to keep the menu up-to-date.

- As an admin, I want the ability to delete dishes from the menu that are no longer offered.

### Managing Orders

- As an admin, I want to view and manage incoming orders in real-time, including order details, customer information, and order status.

- *Future Implementation:* As an admin, I want to update the order status to indicate whether an order is pending, preparing, out for delivery, or completed.

- *Future Implementation:* As an admin, I want to send order confirmation emails to customers after an order is confirmed.

- *Future Implementation:* As an admin, I want to generate order reports for a specified time period, including order volume and revenue.

## Design

### Menu Page:

![Menu Wireframe](https://res.cloudinary.com/db2fhoogx/image/upload/v1234567/wireframe1_pmm7zt.jpg)

### Cart Page:

![Cart Wireframe](https://res.cloudinary.com/db2fhoogx/image/upload/v1234567/wireframe2_c9smdh.jpg)

### Database Schema:

![Database Schema](https://res.cloudinary.com/db2fhoogx/image/upload/v1234567/database-scheme_zaoyxv.jpg)

### Typography

- **Font Selection:** TastyBites employs a combination of fonts to create a visually appealing and engaging experience. Headings (h1 to h6) use the elegant 'Crimson Text' font with a weight of 600 and an italic style, while paragraphs (p) and other text elements feature the cursive 'Courgette' font with a weight of 400.

- **Font Sizes:** The project carefully selects font sizes to establish a clear visual hierarchy. Larger fonts, such as those used for headings, capture attention and guide users, while smaller fonts, ideal for body text, enhance readability.

### Imagery

- **Background Image:** TastyBites features a captivating background image that sets the mood for the website. The background is a high-quality photograph of delicious cuisine, making users eager to explore the menu.

- **Overlay:** An overlay with a semi-transparent background (rgba(0, 0, 0, 0.5)) adds sophistication to the design, making the foreground content stand out while maintaining readability.

- **Content Styling:** The content within the overlay is centered both horizontally and vertically (positioned using `transform`) to ensure a visually pleasing layout. The text is presented in white to contrast with the overlay and background image.

- **Font Styles:** Typography choices, such as font size and style, complement the overall aesthetics. The 'title' uses a font size of 3rem to create prominence, while the 'description' employs a font size of 1.5rem for clarity.

- **Navbar Styles:** The navigation bar (navbar) features a dark background color (#0B0B0B) with contrasting white text (#EEEBD0). The 'navbar-brand' font utilizes the cursive 'Dancing Script' font with a weight of 700 for a touch of elegance.

- **Custom Button Styles:** Buttons on the site are designed with a bold background color (#CC2936) and white text (#FFFFCC). On hover, the background color changes to a lighter shade while maintaining contrast.

- **Card Styles:** Dish cards within the menu section are thoughtfully designed with attention to detail. The images within the cards have a max height to ensure consistency and aesthetic appeal. The card content is aligned to the left to create a clean, organized look.

- **Footer Styles:** The footer section adopts a dark background color (#0B0B0B) with white text (#EEEBD0) for a cohesive design. Social icons are displayed with a subtle hover effect, adding interactivity and accessibility.

- **Media Queries:** To ensure a responsive design, media queries are used to adjust styles based on screen size. This guarantees that the typography and imagery remain visually pleasing across various devices.

The combination of carefully selected typography and captivating imagery in TastyBites contributes to an inviting and immersive user experience, enticing visitors to explore the world of culinary delights.


## Features

1. **User Registration and Authentication:**
   - Users can register for an account and log in securely.
   - Authentication ensures that only logged-in users can access certain features.

![User Login](https://res.cloudinary.com/db2fhoogx/image/upload/v1234567/user-login_q4wn7w.jpg)

2. **Menu Display:**
   - Users can view a menu with various categories of dishes, including starters, main courses, desserts, and drinks.

![Menu Display](https://res.cloudinary.com/db2fhoogx/image/upload/v1234567/menu_zeblqw.jpg)

3. **Dish Details:**
   - Users can click on a dish to view its details, including a description, price, and an image.

![Dish Detail](https://res.cloudinary.com/db2fhoogx/image/upload/v1234567/dish-detail_m17kwd.jpg)

4. **Order Management:**
   - Users can select multiple dishes by checking checkboxes next to each dish.
   - The selected dishes are stored temporarily until the user decides to place an order.

![Order Management](https://res.cloudinary.com/db2fhoogx/image/upload/v1234567/select-dishes_grybll.jpg)

5. **Customer Details:**
   - Users can provide and update their delivery information, including name, email, street, city, state, and zipcode.

![Customer Details](https://res.cloudinary.com/db2fhoogx/image/upload/v1234567/delivery-detail_nxyf1z.jpg)

![Update Customer Details](https://res.cloudinary.com/db2fhoogx/image/upload/v1234567/customer-update_ohfdq5.jpg)


6. **Real-time Updates:**
   - Changes to the selected dishes are updated in real-time, allowing users to see their order summary.

![Update Order](https://res.cloudinary.com/db2fhoogx/image/upload/v1234567/order-detail_mtqqch.jpg)

7. **Order Confirmation:**
   - Users can confirm their order, which includes a summary of selected dishes and delivery information.

![Order Confirmation](https://res.cloudinary.com/db2fhoogx/image/upload/v1234567/order-confirmation_zk4gsg.jpg)

8. **Contact Us:**
   - Users can send inquiries or messages to the business through the "Contact Us" feature.

![Contact Us Form](https://res.cloudinary.com/db2fhoogx/image/upload/v1234567/contact-us1_zbq7ko.jpg)

![Contact Us Confirmation](https://res.cloudinary.com/db2fhoogx/image/upload/v1234567/contact-us2_z55w3m.jpg)

9. **Data Persistence:**
   - User data, including customer details and orders, is stored securely in a database.

10. **Dynamic Categorization:**
    - Dishes are categorized dynamically, making it easy for users to find their preferred type of dish.

11. **Deployment on Heroku:**
    - The project is deployed on Heroku, allowing users to access the live website via a provided link.

12. **Agile Development:**
    - Agile development practices were followed during the project, promoting collaboration and flexibility.

13. **GitHub Kanban Board:**
    - A GitHub Kanban board was used for project management, making it easier to track and manage tasks.

These features make your app a user-friendly platform for browsing, selecting, and confirming food orders. Users can conveniently manage their orders and delivery details, ensuring a smooth and enjoyable experience.

## Live Demo

You can access a live demo of the application [TastyBites](https://pp4-django-43b291f3bcf7.herokuapp.com/).

## CRUD Operations in My Project

In my project, I utilize CRUD operations, which stand for Create, Read, Update, and Delete. These operations are fundamental for managing data within the application. Below, I'll explain each operation as it relates to my project.

### Create (C)

### Creating a New Dish

As an admin, I have the capability to add new dishes to my restaurant's menu.
The process involves navigating to the admin dashboard, where I can access the dish creation form.
I input essential details such as the dish name, description, price, and image.
Upon submission, a new dish entry is created in the database, and it becomes visible on the menu.

### Adding a Customer Profile

Customers can create their profiles, providing necessary information like their name, email, and address for delivery.
This information is stored in the database, allowing customers to have personalized experiences.

### Read (R)

### Viewing the Menu

Users, both admin and customers, can access the menu page, which presents a comprehensive list of available dishes.
They can see crucial information, including dish names, descriptions, prices, and images.
This operation allows users to retrieve information about available menu items without modifying the data.

### Checking Order Details

Customers can review the details of their orders on the order summary page.
They have visibility into the names and prices of the dishes they've selected, as well as the total order price.
This transparency assists customers in reviewing their selections before finalizing their orders.

### Viewing the Customer Profile

Registered users can view their entered data on their customer profile page.
This includes details like their name, email, and address, which they provided during registration.
Users can access this information as needed.

### Update (U)

### Modifying Dish Information

As an admin, I can make adjustments to dish details if they change or require corrections.
Accessing the edit form for a specific dish allows me to update any of its attributes.
After making changes, I can save the updates, ensuring that my menu remains current and accurate.

### Editing User Profile

Registered users have the privilege of updating their profile information.
They can modify fields such as their name, email, and address by accessing the profile edit page.
Once changes are made, users can save the updated data, keeping their account information current.

### Delete (D)

### Removing Dishes

Admins possess the authority to remove dishes from the menu when necessary.
By selecting the delete option for a dish, confirming the action, and confirming, admins can remove dishes from the database.
This operation is beneficial for eliminating dishes that are no longer offered on the menu.

### Canceling Orders

Customers have the flexibility to remove selected dishes from their cart or cancel entire orders.
This allows users to empty their cart if they change their minds or encounter issues before confirming their orders.

These CRUD operations serve as the foundation for managing data and user interactions within my project, ensuring efficient data management and a seamless user experience.

## Testing

| Issue | Description | Resolution |
|-------|-------------|------------|
| 1     | Changes in Dish Model | The addition of the `slug` field to the Dish model caused issues for dishes created before this change. To resolve this, the database was wiped entirely, and migrations were recreated. This ensured that all dishes had a valid `slug` field. |
| 2     | Template Loading | Templates placed in subfolders were not loading properly. The issue was resolved by updating the `TEMPLATES` setting in `settings.py` to include the correct template path, including subfolders (e.g., `'TEMPLATES_DIR'` and `BASE_DIR / 'templates' / 'customer'`). |
| 3     | Footer Position | The footer was not fixed to the bottom of the page as intended. This issue was addressed by wrapping the footer content in an additional `<div>` container and applying CSS styles to achieve the desired fixed position. |
| 4     | Carousel Behavior | Initially, jQuery was included for carousel functionality in the menu page. However, a bug was discovered where the carousel for one category of dishes affected others when clicking the next or previous button. This unintended behavior made it challenging to navigate the menu efficiently. To resolve this issue, an alternative and simplified solution was found on the internet, improving the independence of carousel behavior for different dish categories. |
| 5     | Contact Us Form | The contact form was displaying all alert messages instead of specifically showing the successful message confirmation. To resolve this, conditional statements were added to display the appropriate message based on form submission. |
| 6     | Checkbox Behavior | Checkboxes in the menu were resetting to their default unchecked state when users returned to the menu from the cart to update their order selection. To address this, code was added to the menu page to track previously checked checkboxes, ensuring users could see their selections while updating their orders. |
| 7     | JavaScript Loading | An error was observed in the development tool console tab. Upon troubleshooting, it was identified that the error was due to the unnecessary loading of JavaScript code using `{% load static %}` in all HTML templates, even when JavaScript was only required for the `menu.html` template for carousel functionality. To address this, a `{% block extra_scripts %}` was introduced to include JavaScript code only in templates where it is needed, eliminating the error. |

### Validator Testing

#### W3C Validator

##### Home Page

![Validate Home Page](https://res.cloudinary.com/db2fhoogx/image/upload/v1234567/html-checker1_kwaovq.jpg)

##### Menu Page

![Validate Menu Page](https://res.cloudinary.com/db2fhoogx/image/upload/v1234567/html-checker2_pm0vjr.jpg)

##### Cart Page

![Validate Cart Page](https://res.cloudinary.com/db2fhoogx/image/upload/v1234567/html-checker3_gtt3bv.jpg)

##### Contact Us Page

![Validate Contact Us Page](https://res.cloudinary.com/db2fhoogx/image/upload/v1234567/html-checker4_ckylqy.jpg)


#### Jigsaw Validator

CSS files pass through the Jigsaw validator with no issues found.

![Validate CSS](https://res.cloudinary.com/db2fhoogx/image/upload/v1234567/css-checker_kdyfac.jpg)


## Technologies Used

- Python
- Django
- ElephantSQL (for database)
- Cloudinary (for image storage)
- HTML, CSS, JavaScript
- Bootstrap (for styling)
- Heroku (for deployment)

## Setup Instructions

1. Install Django and gunicorn:

    ```bash
    pip3 install 'django<4' gunicorn
    ```

2. Install supporting libraries:

    ```bash
    pip3 install dj_database_url==0.5.0 psycopg2
    ```

3. Install Cloudinary Libraries:

    ```bash
    pip3 install dj3-cloudinary-storage
    pip3 install urllib3==1.26.15
    ```

4. Create a requirements file:

    ```bash
    pip3 freeze --local > requirements.txt
    ```

5. Create your project (replace `PROJ_NAME` with your project name):

    ```bash
    django-admin startproject PROJ_NAME .
    ```

    (Don’t forget the period `.` at the end.)

6. Create an app (replace `APP_NAME` with your app name):

    ```bash
    python3 manage.py startapp APP_NAME
    ```

7. Add your app to the installed apps in `settings.py`:

    ```python
    INSTALLED_APPS = [
        …
        'APP_NAME',
    ]
    ```

    Save the file.

8. Migrate the changes:

    ```bash
    python3 manage.py migrate
    ```

9. Run the server to test:

    ```bash
    python3 manage.py runserver
    ```

## Step 2: Deploying an App to Heroku

Follow these 5 stages to deploy your app to Heroku:

1. Create a new external database:

   - Log in to your ElephantSQL account.
   - If you don't have an ElephantSQL.com account yet, create one.
   - Click “Create New Instance”.
   - Set up your plan and give it a name.
   - Select the Tiny Turtle (Free) plan.
   - Select a data center near you.
   - Click “Review” and then “Create instance”.
   - Copy your ElephantSQL database URL using the Copy icon (it will start with postgres://).

2. Create a new Heroku app:

   - Name it (e.g., `APP_NAME`).
   - Set the location to Europe.

3. Attach the database:

   - Open the settings tab.
   - Click "Reveal Config Vars".
   - Add a Config Var called `DATABASE_URL` with the value being the ElephantSQL database URL you copied.

4. Prepare your environment and `settings.py` file:

   - Create a new `env.py` file on the top-level directory (e.g., `env.py`).
   - Import the `os` library and set environment variables.
   - Add your secret key to `os.environ["SECRET_KEY"]`.

     ```python
     os.environ["DATABASE_URL"] = "Paste in ElephantSQL database URL"
     os.environ["SECRET_KEY"] = "Make up your own randomSecretKey"
     ```

   - Reference `env.py` in your project settings.
   - Replace the old `DATABASES` section with the new one that links to `DATABASE_URL` on Heroku.

5. Update static and media file settings:

   - Configure Django to use Cloudinary for media and static files.
   - Add your Cloudinary URL and other required settings to `env.py`.
   - Set up the Cloudinary libraries in the `INSTALLED_APPS` list.

6. Add your Heroku hostname to `ALLOWED_HOSTS` in the `settings.py` file.

7. Add, commit, and push your changes to your Git repository.

8. Deploy your content manually through Heroku, for example, using GitHub as the deployment method.

That's it! Your Django project should now be set up and deployed on Heroku.
