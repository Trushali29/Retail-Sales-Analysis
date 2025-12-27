
 # <center>RETAIL SALES ANALYTICS </center>

 <center><h4>Analyse Promotions and Provide Tangible Insights to Sales Director</h4></center>

**Domain**: FMCG

**Function**: Sales / Promotions

AtliQ Mart is a retail giant with over 50 supermarkets in the southern region of India. All their 50 stores ran a massive promotion during the Diwali 2023 and Sankranti 2024 festive periods on their AtliQ-branded products.

Now, the Sales Director wants to understand:

Which promotions performed well ?

Which promotions did not perform well ?

This analysis will help them make informed decisions for the next promotional cycle.
 
 ## 🛍️ Incremental Revenue
    Incremental revenue is the additional income a business generates from a specific activity, such as a new product launch or marketing campaign. It is calculated by subtracting the baseline revenue (without the new activity) from the total revenue with the activity. This metric helps businesses measure the financial impact of a change, allowing them to assess its effectiveness and return on investment (ROI). 


## 🛍️ Incremental Sold Units (ISU)
    Incremental Units — represent the additional units sold as a direct result of a specific marketing effort or promotion, above what would have been sold under normal conditions. 
    ISU is a key performance indicator (KPI) used to measure the effectiveness and return on investment (ROI) of marketing campaigns, discounts, or promotional activities.
   
   
   Incremental Units (ISU) = Actual Promo Units - Baseline Units
   
   Where,

   **Actual Promo Units** → Total units sold during the promotional period  
   **Baseline Units** → Expected units that would have been sold during the same period *without* any promotions or campaigns

## Store Performance Analysis

**1. Which are the top 10 stores in terms of Incremental Revenue (IR) generated from the promotions?**
  
   Mostly stores from Bengaluru, Chennai and Mysuru generated highest revenue in range of 5.0 - 6.50 Million INR after promotions and campaigns. While other cities did generated revenue but there revenue and quantity unity sold even after promotions were less.

**2. Which are the bottom 10 stores when it comes to Incremental Sold Units (ISU) during the promotional period ?**
  
   Stores of cities such as mangalore, visahkapatnam and vijayawada had achieved less revenue of around  4-6 Million INR and sold around 1000 - 3050 units which is lowest as compared to other states. 

**3. How does the performance of stores vary by city? Are there any common characteristics among the top-performing stores that could be leveraged across other stores ?**
   
   Factors like there are 7 to 10 stores in cities like Hyderabad, Bengaluru, Chennai which made more revenue than other cities.

**4. What are the top 2 promotion types that resulted in the highest Incremental Revenue ?**
   
   500 Cashback (122.64 million) and Buy One Get One Free (69.32 million) promotion type were highest.

**5. What are the bottom 2 promotion types in terms of their impact on Incremental Sold Units ?**
   
   25% OFF (-5717 Units) and 50% OFF (6931 Units) has shown a worst imapct on Incremental Sold Units. 

**6. Is there a significant difference in the performance of discount-based promotions verse BOGOF or Cashback promotions ?**
   
   Cashback and BOGOF has generated more revenue after promotion and sold more products then discount based promotions.
   Discount based promotions achieved only 7.34 % of Incremental Revenue and 12.6 % of Incremental Sold Units. 

**7. Which Promotions strike the best balance between Incremental Sold Units and Maintaining healthy margins ?**
   
   Offers such as 33% OFF, 500 Cashback seems to have a better promotions balance

**8. Which Product categories saw the most significant lift in sales from the promotions ?**
   
   Grocery & Staples (119K ISU), Combo 1 (40K ISU) and Home Appliances (38K ISU) shows significant lift in sales from promotions.

**9. Are there specific products that respond exceptionally well or poorly to promotions ?**

**10. What is the correlation between product category and promotion type effectiveness ?**


## AD-HOC Queries
**1.Provide a list of products with a base price greater than 500 and that are featured in promo type of 'BOGOF'. This information will help us in identifying a high-value products that are currently been heavily discounted, which can be usefull for evaluting our pricing and promotions strategies.**

| product_name                       | base_price |
|------------------------------------|------------|
| Atliq_Double_Bedsheet_set          | 1190       |
| Atliq_waterproof_Immersion_Rod     | 1020       |


**2. Generate a report that provides an overview of the number of stores in each city. The results will be sorted in descending order of store counts, allowing us to identify the cities with the highest store presence. The report includes two essential fields: city and store count, which will assist in optimizing our retail operations.**

| city            | store_count |
|-----------------|-------------|
| Bengaluru       | 10          |
| Chennai         | 8           |
| Hyderabad       | 7           |
| Coimbatore      | 5           |
| Visakhapatnam   | 5           |
| Madurai         | 4           |
| Mysuru          | 4           |
| Mangalore       | 3           |
| Trivandrum      | 2           |
| Vijayawada      | 2           |


**3. Generate a report that displays each campaign along with the total revenue generated before and after the campaign ?**

The report includes three key fields: campaign_name, total_revenue(before_promotion), total_revenue(after_promotion).
This report should help in evaluating the financial impact of our promotional campaigns. (Display the values in millions).

| campaign_name | revenue_before (in Millions) | revenue_after (in Millions) |
|---------------|------------------------------|-----------------------------|
| Sankranti     | 58.13                        | 140.40                      |
| Diwali        | 82.57                        | 207.46                      |


4. **Produce a report that calculates the Incremental Sold Units (ISU%) for each category during the Diwali Campaign. Additionally, provide rankings for the categories based on their ISU%.** 

The report will include three key fields: category, isu%, and rank order. This information will assist in assessing the category_wise success and imapct of the diwali campaign on the incremental sales.

| rank_value | category              | isu_percent |
|------------|-----------------------|-------------|
| 1          | Home Appliances       | 244.23      |
| 2          | Combo1                | 202.36      |
| 3          | Home Care             | 79.63       |
| 4          | Personal Care         | 31.06       |
| 5          | Grocery & Staples     | 18.05       |


**5. Create a report featuring the Top 5 products, ranked by incremental revenue percentage (IR%), across all campaigns.**
The report will provide essential information including product_name, category, and ir%. This analysis helps identify the most successful products in terms of incremental revenue across our campaigns, assisting in product optimization.

| product_name                              | category           | ir_percent | rank_value |
|-------------------------------------------|--------------------|------------|------------|
| Atliq_waterproof_Immersion_Rod            | Home Appliances    | 266.19     | 1          |
| Atliq_High_Glo_15W_LED_Bulb               | Home Appliances    | 262.98     | 2          |
| Atliq_Double_Bedsheet_set                 | Home Care          | 258.27     | 3          |
| Atliq_Curtains                            | Home Care          | 255.34     | 4          |
| Atliq_Home_Essential_8_Product_Combo      | Combo1             | 183.33     | 5          |
