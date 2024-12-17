## API Documentation

### Sign-Up Endpoint

- **URL**: `/v1/sign-up/`
- **Method**: `POST`
- **Description**: This endpoint creates a new user.
- **Request Body**:
  ```json
  {
    "faFirstName": "string",         // Required, Farsi first name
    "faLastName": "string",          // Required, Farsi last name
    "enFirstName": "string",         // Required, English first name
    "enLastName": "string",          // Required, English last name
    "email": "string",               // Required, email address
    "faFatherName": "string",        // Required, Farsi father's name
    "birthDay": "date",              // Required, birth date
    "nationalCode": "string",        // Required, national code max_length = 10
    "mobile": "string",              // Required, mobile number max_length = 10
    "phone": "string",               // Required, phone number max_length = 10
    "address": "string",             // Required, address
    "cardNumber": "string",          // Required, card number max_length = 16
    "shabaNumber": "string",         // Required, Shaba number max_length = 24
    "faTerminalName": "string",      // Required, Farsi terminal name
    "enTerminalName": "string"       // Required, English terminal name
  }
## Upload Picture Endpoint

- **URL**: `/v1/upload/<int:pk>/`
- **Method**: `PUT`
- **Description**: This endpoint uses the user ID to upload their picture.
- **Request Body**:
  ```form-data
  file: <file>
