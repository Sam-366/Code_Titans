"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

from google.cloud import generative_ai
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["Create a user friendly car booking system where the booking system verifies the user details using name, surname, ID number in a range of 0-9 accepting 13 digits, phone number in a range of 0-9 that accepts 10 digits and email address. The user must be able to view the car rental available slots from their calendar. The booking system must avoid double booking, the user must pay a deposit fee in ZAR, the booking system must ask for debit card details. The confirmed dates must appear on the booking system calendar and the user's calendar."]
  },
  {
    "role": "model",
    "parts": ["## Car Booking System Design\n\n**Here's a design for a user-friendly car booking system with the features you requested:**\n\n**1. User Verification:**\n\n*   **Registration/Login:** Users will need to register or login to the system. This will involve collecting their:\n    *   **Name and Surname:** Simple text fields.\n    *   **ID Number:** A numeric field with validation to ensure it's 13 digits long and contains only numbers (0-9).\n    *   **Phone Number:** A numeric field with validation to ensure it's 10 digits long and contains only numbers (0-9).\n    *   **Email Address:** A text field with validation to ensure it follows the standard email format. \n\n**2. Availability Calendar:**\n\n*   **Visual Calendar:** The system will display a calendar showing available booking slots for different cars. \n*   **Real-time Updates:** The calendar will be updated in real-time to reflect bookings and cancellations, preventing double bookings.\n*   **Filtering/Sorting:** Users should be able to filter available cars by date, location, car type, and other relevant criteria.\n\n**3. Booking Process:**\n\n*   **Selecting Dates:** Users can select their desired rental start and end dates from the calendar.\n*   **Choosing a Car:** Users can choose from the available cars displayed for their selected dates. Each car listing will include details like the model, features, and rental price.\n*   **Payment:**\n    *   **Deposit:** The system will calculate and display the required deposit amount in ZAR. \n    *   **Debit Card Details:** Users will input their debit card details for the deposit payment. Secure payment gateways should be integrated for this.\n\n**4. Confirmation and Integration:**\n\n*   **Booking Confirmation:** Upon successful payment, the user will receive a booking confirmation with all the details of their rental.\n*   **Calendar Integration:** The confirmed booking dates will be:\n    *   **Marked as unavailable on the system's calendar.**\n    *   **Added to the user's personal calendar (with user permission) using calendar APIs (e.g., Google Calendar API).**\n\n**Additional Features to Consider:**\n\n*   **User Profiles:** Store user information for faster future bookings.\n*   **Car Details Page:** Provide detailed information about each car, including photos, specifications, and reviews.\n*   **Cancellation Policy:** Clearly outline the cancellation policy and associated fees.\n*   **Location Services:** Allow users to search for cars based on their location or preferred pick-up point.\n*   **Notifications:** Send email or SMS notifications to users for booking confirmations, reminders, and updates.\n\n**Technical Considerations:**\n\n*   **Programming Languages:** You can use languages like Python, Java, or JavaScript for the backend and frontend development.\n*   **Frameworks:** Consider using frameworks like Django (Python) or Spring Boot (Java) for faster development.\n*   **Databases:** Choose a suitable database like PostgreSQL or MySQL to store user information, car details, and booking data.\n*   **Cloud Hosting:** Use cloud platforms like AWS or Google Cloud for scalability and reliability.\n\n**By incorporating these features and considerations, you can create a user-friendly and efficient car booking system that meets your requirements.**"]
  },
])

convo.send_message("YOUR_USER_INPUT")
print(convo.last.text)
 
