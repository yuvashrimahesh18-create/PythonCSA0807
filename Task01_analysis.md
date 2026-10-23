# Task 1 – Understand the Problem

## 1. Problem Description

The Ksheera Village Milk Co-operative collects milk from farmers. The program records the farmer ID, quantity of milk, fat percentage, SNF percentage and shift. It calculates the milk rate per litre and the payment amount.

## 2. Inputs and Outputs

**Inputs:**
- Farmer ID
- Quantity of milk in litres
- Fat percentage
- SNF percentage
- Morning or evening shift

**Outputs:**
- Rate per litre
- Payment for the milk
- Total payment for ten days

## 3. Named Constants

- Base rate = ₹30.00 per litre
- Standard fat = 3.5%
- Standard SNF = 8.5%
- Fat adjustment = ₹0.40 for every 0.1% change
- SNF adjustment = ₹0.30 for every 0.1% change
- Minimum fat = 2.0%
- Maximum fat = 7.0%

## 4. Validation Rules

1. Farmer ID must not be empty.
2. Milk quantity must be greater than zero.
3. Fat must be between 2.0% and 7.0%.
4. SNF must be within the range approved by the co-operative.
5. Shift must be morning or evening.
6. Invalid inputs must show an error message.
7. Payments must be calculated accurately to two decimal places.

## 5. Assumptions

The standard rate is ₹30.00 per litre at 3.5% fat and 8.5% SNF. Higher fat and SNF readings increase the rate, while lower readings decrease it. The official permitted SNF range must be confirmed.

## 6. Alternative Approach and Complexity

Instead of creating separate variables for every farmer, the program can store each milk entry as a record in a list. A loop can process all records.

For n entries:
- Time complexity: O(n)
- Space complexity: O(n)

This approach is easier to maintain and can handle many farmers.

## Conclusion

Using lists, named constants, input validation and accurate money calculations makes the payment calculator reliable and easier to update.