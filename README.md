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
    "nationalCode": "string",        // Required, national code
    "mobile": "string",              // Required, mobile number
    "phone": "string",               // Required, phone number
    "address": "string",             // Required, address
    "cardNumber": "string",          // Required, card number
    "shabaNumber": "string",         // Required, Shaba number
    "faTerminalName": "string",      // Required, Farsi terminal name
    "enTerminalName": "string"       // Required, English terminal name
  }

