# TransactionsRecon
# Task 1

Let's imagine that you got a task from your Manager to reconcile the **31.07.2023 user deposit Bank Statements (SnowPay provider)** to the internal systems of the company (old and new).

- **Balance per bank on the 01.08.2023 00:00:00 (Partner timezone, local)** is **271,628,482 BRL (Brazilian reals)**.

The **bank statements** represent the most correct data, meaning how much money was actually received. You can search paid transactions between two admin panels (old and new). Transactions are not duplicated.

Please find, calculate, and present the following discrepancies:

1. **What status has a transaction in the admin panel?** (Success, Success (activated), Success (updated), etc.)  
   Some transactions might have been wrongly declined. Please add mapping where you find such transactions.

2. **What amount was approved in the admin panel, and how much is the difference with the bank statement?**  
   - **Amount approved in both admin panels:** 130,601,732.25 BRL  
   - **Bank statement amount for matching transactions:** 130,302,555.00 BRL  
   - **Difference:** -299,177.25 BRL

3. **Transactions not found in any admin panel are considered "non-authorized transactions"** for further converting.

4. **Find any other discrepancies**:  
   - I found discrepancies in the transaction number format. (See the attached Excel file with all transaction numbers that were not matching numeric and standard format in both the bank statement and admin panels.)  
   - Also, there is a discrepancy between the **wrongly declined transaction amount** in the admin and declined tables for the following transaction numbers:
     
     ```
     14318611423664
     14318397042738
     14318877490328
     ```

   - Additionally, the following transactions were both **succeeded** and **declined**:
     
     ```
     14319244769635
     14318611423664
     14318397042738
     14318978355714
     14318988601735
     14318877490328
     14318258001444
     ```

   - Two transactions found in the **AdminNew panel** were in non-numeric format, but we can find them in the bank statement as transactions without the "-2" suffix:
     - 14321292282845-2
     - 14321288771122-2  
     These transactions were not considered since they weren't under the SnowPay provider.

5. **Balance Summary for Statuses and Total Amounts across different Admin panels**:

### Success:

Mapped Status: **Success**
	
| Sum of BankAmount | Sum of Amount (Admin New Table) | Sum of Amount (Admin Old Table) | Sum of Amount (Declined Table) | Sum of BankVsAdminTablesDiff |
|-------------------|---------------------------------|---------------------------------|-------------------------------|-----------------------------|
| 130,302,555.00    | 4,950,764.25                    | 125,650,968.00                  | -                             | -299,177.25                 |

---

### Success and Declined:

Mapped Status: **Success and Declined**

| Sum of BankAmount | Sum of Amount (Admin New Table) | Sum of Amount (Admin Old Table) | Sum of Amount (Declined Table) | Sum of BankVsAdminTablesDiff |
|-------------------|---------------------------------|---------------------------------|-------------------------------|-----------------------------|
| 19,786.50         | -                               | 19,786.50                        | 18,450.00                     | 1,336.50                   |

---

### Not active and Declined:

Mapped Status: **Not active and Declined**

| Sum of BankAmount | Sum of Amount (Admin New Table) | Sum of Amount (Admin Old Table) | Sum of BankVsAdminTablesDiff |
|-------------------|---------------------------------|---------------------------------|-----------------------------|
| 8,503.50          | -                               | 8,503.50                         | 0.00                        |

---

### Not active:

Mapped Status: **Not active**

| Sum of BankAmount | Sum of Amount (Admin New Table) | Sum of Amount (Admin Old Table) | Sum of BankVsAdminTablesDiff |
|-------------------|---------------------------------|---------------------------------|-----------------------------|
| 474,702.00        | -                               | 474,702.00                       | 0.00                        |

---

### Non-authorized Transactions:

Just a remark, I filtered the declined table with only SnowPay provider, so this amount of declined transactions corresponds to SnowPay provider declined transactions.

Mapped Status: **Non-authorized transaction**

| Sum of BankAmount | Sum of Amount (Admin New Table) | Sum of Amount (Admin Old Table) | Sum of Amount (Declined Table) | Sum of BankVsAdminTablesDiff |
|-------------------|---------------------------------|---------------------------------|-------------------------------|-----------------------------|
| 140,727,620.10    | -                               | -                               | -                             | 140,727,620.10              |

---

---

# Task 2

The provider sent a weird and unusable Bank Statement, but this is everything you have. You need to separate **Transaction ID numbers**, usually starting with numbers **539**. Please put them in a separate column.

I identified that the unique transaction numbers consist of **12 digits**, so I created a Python function that will search the string, detect occurrences starting with "539%", and return the 12-digit number from the input string, which starts from "539%".

In **Task2Resolved.xlsx**, you will find the extracted transaction numbers.

"""
