

## User Stories


### User Registration and Authentication

-   As a new user, I want to be able to register an account with my name, email, and password, so I can access the ordering system.

-    As a registered user, I want to be able to log in with my email and password to access my account and place orders.

### Browsing and Selecting Dishes

-    As a user, I want to see a list of dishes with their names and prices when I visit the website's menu page.

-    As a user, I want to be able to filter dishes by categories (e.g., appetizers, main courses) to easily find the type of dishes I want.

-    As a user, I want to click on a dish to view its details, including a description and an option to add it to my order.

### Creating and Managing Orders

-    As a user, I want to be able to select multiple dishes by checking checkboxes next to each dish, so I can add them to my order collectively by     clicking the "Place Order" button.

-    As a user, I want to see a summary of my order, including the selected dishes and the total price, before confirming it.

-    As a user, I want the ability to remove a dish from my order if I change my mind.

-    As a user, I want to be able to update my order and add or remove dishes before confirming it.

### Delivery Information

-    As a user, I want to provide and update my delivery information, including my name, email, street address, city, state, and zip code.

-    As a user, I want to be able to access and update my delivery information from my account profile.

### Confirming Orders

-    As a user, I want to be able to confirm my order by clicking a "Confirm Order" button and receive confirmation of my order placement.

-    As a user, I want to receive an email confirmation with details of my order after confirming it.

### Contacting Support

-    As a user, I want the ability to contact customer support or make inquiries using a contact form.


## Features

1. **User Registration and Authentication:**
   - Users can register for an account and log in securely.
   - Authentication ensures that only logged-in users can access certain features.

2. **Menu Display:**
   - Users can view a menu with various categories of dishes, including starters, main courses, desserts, and drinks.

3. **Dish Details:**
   - Users can click on a dish to view its details, including a description, price, and an image.

4. **Order Management:**
   - Users can select multiple dishes by checking checkboxes next to each dish.
   - The selected dishes are stored temporarily until the user decides to place an order.

5. **Customer Details:**
   - Users can provide and update their delivery information, including name, email, street, city, state, and zipcode.

6. **Real-time Updates:**
   - Changes to the selected dishes are updated in real-time, allowing users to see their order summary.

7. **Order Confirmation:**
   - Users can confirm their order, which includes a summary of selected dishes and delivery information.

8. **Contact Us:**
   - Users can send inquiries or messages to the business through the "Contact Us" feature.

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

## Technologies Used

- Django
- PostgreSQL (for database)
- Cloudinary (for image storage)
- HTML, CSS, JavaScript
- Bootstrap (for styling)
- Heroku (for deployment)

## Setup Instructions

To run the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/<github_repo>.git
   cd <project_name>

Create a virtual environment and activate it:

`python -m venv venv`
`source venv/bin/activate`  # On Windows, use `venv\Scripts\activate`

Install the project dependencies:

`pip install -r requirements.txt`

Create a PostgreSQL database and update the database settings in <project_name>/settings.py.

Apply migrations to create the database tables:

python manage.py makemigrations
python manage.py migrate

Create a superuser account for admin access:

python manage.py createsuperuser

Start the development server:
python manage.py runserver

Access the admin interface at http://127.0.0.1:8000/admin/ to add dishes, meal categories, and other data.

Access the user interface at http://127.0.0.1:8000/ to use the ordering system.


#### Approached with Jquery to handle delete functionality
<!-- <script>
  $(document).ready(function() {
    // Add a click event handler for the "Remove" buttons
    $(".remove-dish").click(function() {
        var dishId = $(this).data("dish-id"); // Get the dish ID from the data attribute
        var removeUrl = `/delete/${dishId}/`; // Construct the URL dynamically

        // Send an AJAX POST request to remove the dish
        $.ajax({
            type: "POST",
            url: removeUrl,
            data: { csrfmiddlewaretoken: csrftoken }, // Include the CSRF token
            dataType: "json",
            success: function(response) {
                if (response.success) {
                    // If the removal was successful, update the order page
                    console.log("Dish removed successfully!");
                    // Reload or update the order page here
                    location.reload(); // You can reload the page for simplicity
                } else {
                    console.log("Dish removal failed.");
                }
            },
            error: function() {
                console.log("Error occurred during dish removal.");
            }
        });
    });
});
</script> -->


#### Approached with Jquery to handle update functionality

<!-- <script>
    // Function to update selected dishes in the session via AJAX
    function updateSelectedDishes(dishId, isChecked) {
        // Send an AJAX request to the server to update selected dishes
        $.ajax({
            type: "POST",
            url: "{% url 'update-selected-dishes' %}",
            data: {
                'dish_id': dishId,
                'is_checked': isChecked
            },
            success: function (data) {
                // You can handle the response if needed
            }
        });
    }

    // Add a click event listener to all checkboxes
    $('input[type="checkbox"]').on('click', function () {
        var dishId = $(this).val();
        var isChecked = $(this).is(':checked');
        updateSelectedDishes(dishId, isChecked);
    });
</script> -->