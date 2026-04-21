
 # <center> RETAIL SALES ANALYTICS </center>
 # <center> Analyse Promotions and Provide Tangible Insights to Sales Director </center>

**Live Dashboard** - https://trushalichawda.pythonanywhere.com/

**SQL Analysis** https://github.com/Trushali29/Retail-Sales-Analysis/blob/main/main.ipynb

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

### 1. Which are the top 10 stores in terms of Incremental Revenue (IR) generated from the promotions?
  
   Mostly stores from Bengaluru, Chennai and Mysuru generated highest revenue in range of 5.0 - 6.50 Million INR after promotions and campaigns. While other cities did generated revenue but their revenue and quantity unity sold even after promotions were less.

### 2. Which are the bottom 10 stores when it comes to Incremental Sold Units (ISU) during the promotional period ?
  
   Stores of cities such as mangalore, visahkapatnam and vijayawada had achieved less revenue of around  4-6 Million INR and sold around 1000 - 3050 units which is lowest as compared to other states. 

### 3. How does the performance of stores vary by city? Are there any common characteristics among the top-performing stores that could be leveraged across other stores ?

  Metropolitan cities like Bengaluru (10 stores, ~5M revenue per store) and Chennai (8 stores, ~5M revenue per store) shows the highest revenue generation.
  Other cities like Mysuru(4 stores, ~4.72 revenue per store) and Madurai(4 stores, ~4.09 revenue per store) has made more impact than cities with store count 5.
  
  However per-store analysis reveals a 2x efficiency gap — Bengaluru generates ₹5.08L per store versus Trivandrum's ₹2.33L, suggesting city size alone doesn't determine performance.

  The core reason would be in the promotion mix. Those cities relied on BOGOF and 500 Cashback. The promotion of 25% OFF performed worst in every city. Even though bengaluru has more loss of -2.74L INR revenue it was able to make more profit with its 10 stores, other cities with more stores has more loss like coimbatore with -1.04L INR and visakhapatanam with -1.29L INR.

**The recommendation would be to invest in promotions of BOGOF and 500 Cashback in cities with least IR.**

### 4. What are the top 2 promotion types that resulted in the highest Incremental Revenue ?
   
   500 Cashback (122.64 million) and Buy One Get One Free (69.32 million) promotion type were highest.

### 5. What are the bottom 2 promotion types in terms of their impact on Incremental Sold Units ?
   
   25% OFF (-5717 Units) and 50% OFF (6931 Units) has shown a worst imapct on Incremental Sold Units. 

### 6. Is there a significant difference in the performance of discount-based promotions versus BOGOF or Cashback promotions ?

  Below stats show that Discount based promotions performs poorly in every city with only a 7.34% of revenue share. 
  
  While Cashback/BOGOF gives a high impact with 92.66% total incremental revenue. This tells us the the next promotion strategy needs Cashback/BOGOF as our top priority. 
  
  In discount based 33% OFF promo shows a neutral performance which also can be used and improve for next festive cycle.     


| promo_category | incremental_revenue | ir_share | isu_share |
|----------------|--------------------:|----------:|----------:|
| Cashback/BOGOF | ₹19.20Cr | 92.66% | 87.43% |
| Discount | ₹1.52Cr | 7.34% | 12.57% |


### 7. Which Promotions strike the best balance between Incremental Sold Units and Maintaining healthy margins ?
   Based on the scatter plot mention below, BOGOF shows high volume, lower revenue per unit, 500 Cashback = high revenue, lower volume, 33% OFF = decent balance but not exceptional and 25% and 50% OFF low promotional contribution. 
   
   This might be since consumer shows interset in getting free things in BOGOF which sells more units but generates less revenue. Also 500 Cashback might work for expensive products sales. 

   The best promotional strategy would be a combination of both 500 Cashback and BOGOF For example, customers spending above a certain threshold could receive BOGOF on essential products while expensive products are paired with 500 Cashback offers. Lastly, 33% OFF can still be improved. 

![alt text](image.png)


### 8. Which Product categories saw the most significant lift in sales from the promotions ?
   
   Grocery & Staples (119K ISU), Combo 1 (40K ISU) and Home Appliances (38K ISU) shows significant lift in sales from promotions.

### 9. Are there specific products that respond exceptionally well or poorly to promotions ?
  
  For festive seasons like diwali and Sankranti, products like Farm Atta Chakki (1.8M INR and 48950 ISU ), Sunflower Oil(8.8M INR  and 43169 ISU ), Home Essential_8 Product Combo (12.2M INR and 40881 ISU ) plays a essential role since these are the things consumers need. These products are always high in demand which generates more revenue. 
  
  In Festive season — people stock up food supplies and decorate homes. Personal care like soap and lotion is not on their priority list during Diwali.

  Other categories like Atliq_Scrub_Sponge_For_Dishwash (-42735 INR and -777 ISU), Atliq_Fusion_Container_Set_of_3 (-305025 INR, -735 ISU) were not in demand for those festives due to which they have negative revenue.

  The best strategy would be to apply more promotion in grocery & staples, combo1 and home appliances category in every stores. Plus if testing a 500 Cashback or BOGOF can also be done on Personal care category. 


| index | product_name                                   | category             | incremental_revenue | incremental_sold_units |
|------:|------------------------------------------------|----------------------|--------------------:|-----------------------:|
| 5     | Atliq_Farm_Chakki_Atta (1KG)                   | Grocery & Staples    | 18248700.0          | 48950                  |
| 13    | Atliq_Suflower_Oil (1L)                        | Grocery & Staples    | 8711196.0           | 43169                  |
| 8     | Atliq_Home_Essential_8_Product_Combo           | Combo1               | 122643000.0         | 40881                  |
| 7     | Atliq_High_Glo_15W_LED_Bulb                    | Home Appliances      | 7589050.0           | 21683                  |
| 14    | Atliq_waterproof_Immersion_Rod                 | Home Appliances      | 17561340.0          | 17217                  |
| 12    | Atliq_Sonamasuri_Rice (10KG)                   | Grocery & Staples    | 13720440.0          | 15954                  |
| 2     | Atliq_Curtains                                 | Home Care            | 3517500.0           | 11725                  |
| 10    | Atliq_Masoor_Dal (1KG)                         | Grocery & Staples    | 1943772.0           | 11301                  |
| 4     | Atliq_Double_Bedsheet_set                      | Home Care            | 12917450.0          | 10855                  |
| 9     | Atliq_Lime_Cool_Bathing_Bar (125GM)            | Personal Care        | 158844.0            | 2562                   |
| 3     | Atliq_Doodh_Kesar_Body_Lotion (200ML)          | Personal Care        | 335350.0            | 1765                   |
| 1     | Atliq_Cream_Beauty_Bathing_Soap (125GM)        | Personal Care        | 89520.0             | 1317                   |
| 0     | Atliq_Body_Milk_Nourishing_Lotion (120ML)      | Personal Care        | 70560.0             | 556                    |
| 6     | Atliq_Fusion_Container_Set_of_3                | Home Care            | -305025.0           | -735                   |
| 11    | Atliq_Scrub_Sponge_For_Dishwash                | Home Care            | -42735.0            | -777                   |

### 10. What is the correlation between product category and promotion type effectiveness ?

BOGOF in combo with Grocery & Staples(275% IR rate), Home Appliances(265% IR rate), Home Care(257.6% IR rate) give a boost store performance. 
Combo1 + 500 Cashback performs better and can be best combinations for future festive too. 33% OFF did a decent work in Grocery & Staples (42.87% IR rate).  

This again proves that consumers looks out for most essential needs like food and essential supplies for them Home care or Personal Care won't be a priority.

33% OFF showed decent performance in Grocery & Staples (42.87% IR) and can be retained. 25% OFF should be eliminated across all categories.

To gain more revenue out of this in next festive season excluding 25% OFF others can be experimented.

**Category vs Promotion Type Effectiveness Table**

| category | promo_type | incremental_revenue | revenue_before_promo | ir_rate_% |
|---|---|---|---|---|
| Grocery & Staples | BOGOF | 27,731,650 | 10,064,950 | 275.53 |
| Home Appliances | BOGOF | 25,150,390 | 9,483,110 | 265.21 |
| Home Care | BOGOF | 16,434,950 | 6,379,170 | 257.63 |
| Combo1 | 500 Cashback | 122,643,000 | 66,897,000 | 183.33 |
| Grocery & Staples | 33% OFF | 15,664,212 | 36,540,540 | 42.87 |
| Personal Care | 50% OFF | 709,624 | 2,162,951 | 32.81 |
| Grocery & Staples | 25% OFF | -771,754 | 6,386,362 | -12.08 |
| Home Care | 25% OFF | -347,760 | 2,477,815 | -14.03 |
| Personal Care | 25% OFF | -55,350 | 309,290 | -17.90 |

**Key Findings**

- **BOGOF** works best across Grocery, Home Appliances and Home Care — all above 257% IR rate
- **500 Cashback** is the only effective promo for Combo1 — 183% IR rate
- **25% OFF** is harmful across ALL categories it was applied to — negative IR rate in every case
- **Personal Care** responds poorly to every promo type — highest was only 32.81% with 50% OFF

## AD-HOC Queries

### 1. Provide a list of products with a base price greater than 500 and that are featured in promo type of 'BOGOF'. This information will help us in identifying a high-value products that are currently been heavily discounted, which can be useful for evaluating our pricing and promotions strategies.

| product_name                       | base_price |
|------------------------------------|------------|
| Atliq_Double_Bedsheet_set          | 1190       |
| Atliq_waterproof_Immersion_Rod     | 1020       |


### 2. Generate a report that provides an overview of the number of stores in each city. The results will be sorted in descending order of store counts, allowing us to identify the cities with the highest store presence. The report includes two essential fields: city and store count, which will assist in optimizing our retail operations.

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


### 3. Generate a report that displays each campaign along with the total revenue generated before and after the campaign ?
The report includes three key fields: campaign_name, total_revenue(before_promotion), total_revenue(after_promotion).
This report should help in evaluating the financial impact of our promotional campaigns. (Display the values in millions).

| campaign_name | revenue_before (in Millions) | revenue_after (in Millions) |
|---------------|------------------------------|-----------------------------|
| Sankranti     | 58.13                        | 140.40                      |
| Diwali        | 82.57                        | 207.46                      |


### 4. Produce a report that calculates the Incremental Sold Units (ISU%) for each category during the Diwali Campaign. Additionally, provide rankings for the categories based on their ISU%. 

The report will include three key fields: category, isu%, and rank order. This information will assist in assessing the category_wise success and impact of the diwali campaign on the incremental sales.

| rank_value | category              | isu_percent |
|------------|-----------------------|-------------|
| 1          | Home Appliances       | 244.23      |
| 2          | Combo1                | 202.36      |
| 3          | Home Care             | 79.63       |
| 4          | Personal Care         | 31.06       |
| 5          | Grocery & Staples     | 18.05       |


### 5. Create a report featuring the Top 5 products, ranked by incremental revenue percentage (IR%), across all campaigns.

The report will provide essential information including product_name, category, and ir%. This analysis helps identify the most successful products in terms of incremental revenue across our campaigns, assisting in product optimization.

| product_name                              | category           | ir_percent | rank_value |
|-------------------------------------------|--------------------|------------|------------|
| Atliq_waterproof_Immersion_Rod            | Home Appliances    | 266.19     | 1          |
| Atliq_High_Glo_15W_LED_Bulb               | Home Appliances    | 262.98     | 2          |
| Atliq_Double_Bedsheet_set                 | Home Care          | 258.27     | 3          |
| Atliq_Curtains                            | Home Care          | 255.34     | 4          |
| Atliq_Home_Essential_8_Product_Combo      | Combo1             | 183.33     | 5          |


### Promo Effectiveness on Campaigns

| campaign_name | promo_type | incremental_revenue |
|---|---|---|
| Diwali | 500 Cashback | 101.93 |
| Sankranti | BOGOF | 53.48 |
| Sankranti | 500 Cashback | 20.71 |
| Diwali | BOGOF | 15.84 |
| Sankranti | 33% OFF | 8.06 |
| Diwali | 33% OFF | 7.60 |
| Diwali | 50% OFF | 0.51 |
| Sankranti | 50% OFF | 0.20 |
| Sankranti | 25% OFF | -0.17 |
| Diwali | 25% OFF | -1.00 |

## Key Findings

1. Diwali made 124.88 million more profits in top cities as compared to Sankranti (82.28 millions).

2. 500 Cashback has made 101.93 million in Diwali and also have made 20.71 millions in Sankranti.

3. 500 Cashback and BOGOF promotions dominates whereas 25% OFF show worst performance in both festives. 

4. Combo 1 and 500 Cashback shows best combination with 183% of IR. While Grocery & Staples, Home Appliances and Home Care has made most profits in BOGOF promo.
