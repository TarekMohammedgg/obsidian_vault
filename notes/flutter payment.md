---
tags:
  - flutter
  - paymen
  - stripe
---
# Flutter Payment Integration Notes

## 1. Core Concepts of Payment Gateways (PG)

**Definition**: A Payment Gateway (PG) acts as a mediator (Process) between the User/Buyer and the Merchant.

**Stakeholders**: The process involves the User, the Merchant, the Card Bank, and the Node Bank.

**Purpose**: Its primary goal is to protect the rights of the user, the merchant, and the bank.

**Verification**: The system must check if the user has a sufficient amount (balance) for the transaction.

## 2. Integration Flows

There are two main ways to integrate a service like Stripe into a mobile application:

- **SDK Flow**: Used when a ready-made Software Development Kit (SDK) is provided by the service.
- **API Flow**: Used when a mobile SDK is not provided or when a direct API process is preferred.

## 3. Stripe Payment Flow (Stripe Gateway)

The process for handling a transaction (e.g., $10) involves several technical steps:

- **Payment Intent**: A "Payment Intent" must be created to initiate the process.
- **Authentication Keys**:
    - **Publishable Key**: Used as a token for identification.
    - **Secret Key**: Used to confirm that the specific user is authorized to make the payment.
- **Client Secret**: The server returns a client_secret to the application to be used in the payment process.
- **Transaction Handling**: The payment is processed, and the app must handle cases where the payment might succeed or fail.

## 4. Payment Gateway (PG) vs. In-App Purchase (IAP)

The choice between PG and IAP depends on the nature of the product.

|Feature|Payment Gateway (PG)|In-App Purchase (IAP)|
|---|---|---|
|Product Type|Physical products|Digital products|
|Examples|Physical goods|Subscriptions or digital items|
|Date Noted|15/10/25|15/10/25|

## 5. Multiple Payment Gateways

Applications may integrate multiple PGs like Stripe, PayPal, or Pymos.

**Location**: PG selection often depends on the user's location, such as specific options for Egypt.

**Payment Method**:

- **Card-based**: Uses user card data directly.
- **Hosted Gateway**: (e.g., PayPal) The app does not need to handle card data as it uses a hosted solution.

