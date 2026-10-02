# GrocBankX

💳 Credit Card Fraud Detection Dataset
This dataset contains numerical features that represent transaction behavior, along with a Class label where:

•0 represents a normal transaction

•1 represents a fraudulent transaction

The dataset is imbalanced, meaning fraudulent transactions are less frequent than normal ones, which makes fraud detection challenging.

From this dataset, I used two features to simulate a real-world grocery payment scenario. I performed preprocessing, handled the imbalance, trained a machine learning model, and saved the trained model using the .pkl extension for reuse in the application.

💡 Real-World Problem Identified
🔐 GrocBankX – Secure Grocery Payment System
Consider a bank like BankX that provides credit cards, and customers use those cards in grocery stores.
Sometimes, when a genuine user makes a purchase with:

In some cases, when a genuine user makes a purchase with:
⬩more number of items
⬩higher amount (for example, vacation or bulk purchases)
the transaction may be falsely identified as fraud and blocked.
Blocking such transactions negatively impacts the user experience.

🎯Solution Implemented
Instead of directly blocking the transaction, I designed a risk-based authentication system:
❯❯Steps
1)The transaction is first checked using a fraud detection model
2)If the transaction looks suspicious, it is not immediately blocked
•The system requests authentication using face verification of the account owner
•To prevent misuse (like showing a photo in front of the camera), eye-blink detection is used
•While blinking, the system automatically captures the image, processes it, and validates the request
3)This approach allows genuine users to complete their transaction securely without unnecessary blocking.


Flow Diagram : 
                GrocBankX Store
                      │
                 Add Products
                      │
                    Cart
                      │
                  Pay Now
                      │
                      ▼
             ┌─────────────────┐
             │ Fraud Detection │
             │  Random Forest  │
             └────────┬────────┘
                      │
              ┌───────┴────────┐
              │                │
           Normal           Suspicious
              │                │
              ▼                ▼
          Payment          Face Verification
          Approved          / Liveness
                               │
                         ┌─────┴─────┐
                         │           │
                      Verified    Failed
                         │           │
                      Approve      Block





