#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>

using namespace std;

// Constants for prices and discount
const double COFFEE_PRICE = 15.00;
const double SANDWICH_PRICE = 30.00;
const double SALAD_PRICE = 25.00;
const double JUICE_PRICE = 10.00;
const double MUFFIN_PRICE = 20.00;
const double PIZZA_PRICE = 35.00;
const double SOUP_PRICE = 18.00;
const double BURGER_PRICE = 40.00;
const double DISCOUNT_RATE = 0.10; // 10% discount
const double DISCOUNT_THRESHOLD = 100.00; // Discount applies if bill is over R100

int main() {
    string name, surname;
    int numItems;

    // Step 1: Get user input for name and surname
    cout << "Enter your name: ";
    getline(cin, name);
    cout << "Enter your surname: ";
    getline(cin, surname);

    // Step 2: Ask for the number of items
    cout << "How many items would you like to order (up to 8)? ";
    cin >> numItems;

    // Step 3: Display menu
    cout << "\nCafeteria Menu:" << endl;
    cout << "1. Coffee - R" << COFFEE_PRICE << endl;
    cout << "2. Sandwich - R" << SANDWICH_PRICE << endl;
    cout << "3. Salad - R" << SALAD_PRICE << endl;
    cout << "4. Juice - R" << JUICE_PRICE << endl;
    cout << "5. Muffin - R" << MUFFIN_PRICE << endl;
    cout << "6. Pizza Slice - R" << PIZZA_PRICE << endl;
    cout << "7. Soup - R" << SOUP_PRICE << endl;
    cout << "8. Burger - R" << BURGER_PRICE << endl;

    // Step 4: Order items
    double totalBill = 0.0;
    int itemSelection;

    for (int i = 0; i < numItems; ++i) {
        cout << "Select item " << (i + 1) << " (1-8): ";
        cin >> itemSelection;

        // Validate item selection and update total bill
        switch (itemSelection) {
            case 1: totalBill += COFFEE_PRICE; break;
            case 2: totalBill += SANDWICH_PRICE; break;
            case 3: totalBill += SALAD_PRICE; break;
            case 4: totalBill += JUICE_PRICE; break;
            case 5: totalBill += MUFFIN_PRICE; break;
            case 6: totalBill += PIZZA_PRICE; break;
            case 7: totalBill += SOUP_PRICE; break;
            case 8: totalBill += BURGER_PRICE; break;
            default: cout << "Invalid selection, please choose between 1 and 8." << endl; --i; // Repeat the selection
        }
    }

    // Step 5: Calculate discount if applicable
    double finalBill = totalBill;
    if (totalBill > DISCOUNT_THRESHOLD) {
        finalBill -= (totalBill * DISCOUNT_RATE);
        cout << "\nTotal Bill: R" << totalBill << endl;
        cout << "Discount applied." << endl;
    } else {
        cout << "\nTotal Bill: R" << totalBill << endl;
        cout << "No discount applied." << endl;
    }

    cout << "Final Bill: R" << finalBill << endl;

    // Step 6: Write to file
    ofstream outFile("CafeteriaBill.txt");
    if (outFile) {
        outFile << "Customer Name: " << name << " " << surname << endl;
        outFile << "Total Bill: R" << totalBill << endl;
        outFile << "Final Bill: R" << finalBill << endl;
        outFile.close();
        cout << "\nThe bill has been written to CafeteriaBill.txt." << endl;
    } else {
        cout << "Error opening file." << endl;
    }

    return 0;
}
