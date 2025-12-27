# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
# INSPIRATION - https://natatsypora.pythonanywhere.com/

from dash import Dash, html, dcc , Input , Output, callback, dash_table
import plotly.express as px
import pandas as pd
import numpy as np

df = pd.read_csv('E://Projects_DA//Sales_Retail_Analysis_SQL//dataset//final_retail_sales.csv')
summary = {
    "total_products": df["product_code"].nunique(),
    "total_category": df["category"].nunique(),
    "total_promos": df["promo_type"].nunique(),
    "total_campaigns": df["campaign_name"].nunique(),
    "total_stores": df["store_id"].nunique(),
    "total_cities": df["city"].nunique(),
    "total_incremental_revenue": str(round(df["incremental_revenue"].sum() / 1_000_000, 2))+ ' million',
    "total_incremental_sold_units": str(df["incremental_sold_units"].sum()) + ' units'
}

optionsCities = pd.Series(df['city'].unique()).apply(lambda x: {'label': x, 'value': x})
optionsCities = pd.concat([optionsCities, pd.Series([{'label':'All Cities','value':'All Cities'}])], ignore_index=True)

# City with number of stores and their revenues 
city_stores = df.groupby(['city']).agg({'store_id':'nunique','incremental_revenue':'sum','incremental_sold_units':'sum', 'revenue_before_promo':'sum','revenue_after_promo':'sum','quantity_sold(before_promo)':'sum','quantity_sold(after_promo)':'sum'}).reset_index().sort_values(by='incremental_revenue', ascending=False)
city_stores['incremental_revenue'] = round(city_stores['incremental_revenue'] / 1000000 , 2) 
city_stores['revenue_after_promo'] = round(city_stores['revenue_after_promo'] / 1000000 , 2) 
city_stores['revenue_before_promo'] = round(city_stores['revenue_before_promo'] / 1000000 , 2) 
city_stores = city_stores.rename(columns = {'incremental_revenue':'Incremental Revenue ( in million )', 'incremental_sold_units':'Incremental Sold Units', 'store_id':'Total Stores', 'city':'City','revenue_after_promo':'revenue after promo (in million)','revenue_before_promo':'revenue before promo (in million)'})

# campaign promotional analysis
# incremental revenue
campaign_df_ir = df.groupby('campaign_name')[['incremental_revenue','revenue_before_promo','revenue_after_promo']].sum().reset_index()
for revenue in ['incremental_revenue','revenue_before_promo','revenue_after_promo']:
    campaign_df_ir[revenue + str(' (in million)')] = round(campaign_df_ir[revenue] / 10_00_000 , 2)

fig_campaign_revenue = px.bar(campaign_df_ir, x='campaign_name', y=['revenue_before_promo (in million)','revenue_after_promo (in million)'], template='seaborn', barmode='group', text_auto=True, title='Total Revenue Generation Before vs. After Promotions')
fig_campaign_revenue.update_layout(plot_bgcolor='white')

fig_campaign_revenue_ir = px.pie(campaign_df_ir, names='campaign_name', values='incremental_revenue (in million)', title = 'Additional Revenue generated rate during campaign promotions',template='seaborn')
fig_campaign_revenue_ir.update_layout(plot_bgcolor='white')

# incremental sold units
campaign_df_isu = df.groupby('campaign_name')[['incremental_sold_units','quantity_sold(before_promo)','quantity_sold(after_promo)']].sum().reset_index()

fig_campaign_units = px.bar(campaign_df_isu, x='campaign_name', y=['quantity_sold(before_promo)','quantity_sold(after_promo)'],
                            barmode='group', text_auto=True, title='Total Units Sold Before vs. After Promotions', template='seaborn')
fig_campaign_units.update_layout(plot_bgcolor='white')

fig_campaign_units_isu = px.pie(campaign_df_isu, names='campaign_name', values='incremental_sold_units', title = 'Additional units sold rate during campaign promotions', template='seaborn')
fig_campaign_units_isu.update_layout(plot_bgcolor='white')

# campaign revenue by city
campaign_city_df = df.groupby(['city','campaign_name'])[['incremental_revenue','revenue_before_promo','revenue_after_promo']].sum().reset_index()
for revenue in ['incremental_revenue','revenue_before_promo','revenue_after_promo']:
    campaign_city_df[revenue + str(' (in million)')] = round(campaign_city_df[revenue] / 10_00_000 , 2)

fig_campaign_city = px.scatter(
    campaign_city_df,
    x='city',
    y='incremental_revenue (in million)',
    size='incremental_revenue (in million)',
    color='campaign_name',
    hover_data=['revenue_before_promo (in million)','revenue_after_promo (in million)'],
    title='City Revenue & Incremental Revenue Bubble Chart',
    template='seaborn',
    labels={'incremental_revenue (in million)':'Incremental Revenue (in million)','revenue_before_promo (in million)':'Revenue before promo (in million)','revenue_after_promo (in million)':'Revenue after promo (in million)','campaign_name':'Campaigns'}
)
fig_campaign_city.update_layout(plot_bgcolor='white')


# campaign units sold during promo type
campaign_promo_df = df.groupby(['promo_type','campaign_name'])[['incremental_sold_units','quantity_sold(before_promo)','quantity_sold(after_promo)']].sum().reset_index()

fig_campaign_promo= px.scatter(
    campaign_promo_df,
    x='promo_type',
    y='incremental_sold_units',
    color='campaign_name',
    hover_data=['quantity_sold(before_promo)','quantity_sold(after_promo)'],
    title='Promo type Revenue & Incremental Sold units Bubble Chart',
    opacity=0.8,
    template='seaborn',
    labels={'incremental_sold_units':'Incremental Sold Units','quantity_sold(before_promo)':'Quantity sold (before promo)','quantity_sold(after_promo)':'Quantity sold(after promo)','campaign_name':'Campaigns'}
)
fig_campaign_promo.update_layout(plot_bgcolor='white')
fig_campaign_promo.update_traces(marker_size=10)


# upload the css stylesheet in dash app
external_stylesheets  = ['E://Projects_DA//Sales_Retail_Analysis_SQL//assets//style.css']
app = Dash( external_stylesheets = external_stylesheets)

app.layout = html.Div([
    # meta tag 
    html.Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
    # header tag
html.Header([
        html.H1("Retail Sales Analytics", className='header-title') ,
        html.A("Github Link", href="https://github.com/Trushali29/Retail-Sales-Analysis.git", target="_blank", className='github-link')
    ],className='header'),
        
    # main body section
    html.Div([
        # cards section
        html.Div([
            html.Div([
            html.H2( str(summary['total_products']), className='card-value' ),
            html.Label('Products', className='card-label')
            ], className = 'cards'),
            html.Div([
                html.H2( str(summary['total_category']), className='card-value'),
                html.Label('Categories' , className='card-label')
            ], className = 'cards'),
            html.Div([
                html.H2( str(summary['total_promos']), className='card-value' ),
                html.Label('Promotions', className='card-label')
            ], className = 'cards'),
            html.Div([
                html.H2( str(summary['total_campaigns']), className='card-value'),
                html.Label('Campaigns', className='card-label')
            ], className = 'cards'),
            html.Div([
                html.H2( str(summary['total_stores']),className='card-value' ),
                html.Label('Stores', className='card-label')
            ], className = 'cards'),
            html.Div([
                html.H2( str(summary['total_cities']), className='card-value' ),
                html.Label('Cities', className='card-label')
            ], className = 'cards'),
            html.Div([
                html.H2( str(summary['total_incremental_revenue']), className='card-value' ),
                html.Label('IR', className='card-label')
            ], className='cards'),
            html.Div([
                html.H2( str(summary['total_incremental_sold_units']), className='card-value' ),
                html.Label('ISU', className='card-label')
            ], className='cards')
        ],className='header-cards'),

        # City option Dropdown Filter
        html.Div([
            html.Div([
                dcc.Dropdown(options= optionsCities, value='All Cities',searchable=False, clearable=False, className='options_filters', id='city-option')
            ], className='option-section'), 
            html.Strong('The city option changes will be reflected on all the graphs and tables below. Except campaign graphs section', style={'color':"#F86857"},className='options_filters'), 
        ], className='section'),

        # store performance section
        html.Div([
            # header
            html.H2('Store Performance Analysis',className='section-header'), 
            # figure-section 1
            html.Div([
                dcc.Graph(id='stores_ir', className='figures'),
                dcc.Graph(id='stores_isu', className='figures'),
                dcc.Graph(id='category_ir', className='figures'),
                dcc.Graph(id='category_isu', className='figures')
            ], className='section-figure'),
            html.H2("Detailed IR and ISU information of all cities", style={'textAlign':'center'} ),
            html.Div
            ([
                dash_table.DataTable(
                columns=[ {"name" : x, "id" : x } for x in city_stores.columns ],
                data=city_stores.to_dict('records'),
                # Table Features
                filter_action="native",
                sort_action="native",
                page_size=10,
                # Styling
                style_table={'overflowX': 'auto'},
                style_header={
                    'backgroundColor': '#1f2937',
                    'color': 'white',
                    'fontWeight': 'bold'
                },
                style_cell={
                    'textAlign': 'center',
                    'padding': '8px',
                    'fontFamily': 'Arial'
                })
            ])
        ],className='section'),

        # promotion analysis section
        html.Div([
            html.H2('Promotion Type Analysis',className='section-header'),
            # figure-section 2
            html.Div([
                dcc.Graph(id='top-products-ir'),
                dcc.Graph(id='bottom-products-isu'),
                html.H2("Performance of discount-based promotions verse BOGOF or cashback promotions", style={'textAlign':'center'}),
                dcc.Graph(id='promo-group-ir'),
                dcc.Graph(id='promo-group-isu'),
            ], className='section-figure')
        ],className='section'),

        # product and category section
        html.Div([
            html.H2('Product and Category Analysis',className='section-header'),
            # figure-section 3
            html.Div([ 
                dcc.Graph(id='category-promo-isu'),
                dcc.Graph(id='category-promo-ir'),
            ],className='section-figure'),
            html.H2(id='product-table-title', style={'textAlign':'center'} ),
            html.Div([
                dash_table.DataTable(
                    id='product-table',
                    # 🔹 Table Features
                    filter_action="native",
                    sort_action="native",
                    page_size=10,

                    # 🔹 Styling
                    style_table={'overflowX': 'auto'},
                    style_header={
                        'backgroundColor': '#1f2937',
                        'color': 'white',
                        'fontWeight': 'bold'
                    },
                    style_cell={
                        'textAlign': 'left',
                        'padding': '8px',
                        'fontFamily': 'Arial'
                    }
                )
            ])
        ],className='section'),

    # campaign Analysis
        html.Div([
            html.H2('Campaign Promotional Analysis',className='section-header'),
            html.Div([
                # total revenue for both campaigns and unit solds
                dcc.Graph(figure= fig_campaign_revenue),
                dcc.Graph(figure= fig_campaign_revenue_ir),
                dcc.Graph(figure=fig_campaign_units),
                dcc.Graph(figure=fig_campaign_units_isu),
                # ir for each city compare 

                dcc.Graph(figure=fig_campaign_city),
                # top and bottom promo in each campaign

                dcc.Graph(figure=fig_campaign_promo),
                ], className='section-figure'),

                html.H2( id='category-table-title', style={'textAlign':'center'} ),
                html.Div
                ([
                    dash_table.DataTable(
                        id='category-table',
                        # Table Features
                        filter_action="native",
                        sort_action="native",
                        page_size=10,
                        # Styling
                        style_table={'overflowX': 'auto'},
                        style_header={
                            'backgroundColor': '#1f2937',
                            'color': 'white',
                            'fontWeight': 'bold'
                        },
                        style_cell={
                            'textAlign': 'center',
                            'padding': '8px',
                            'fontFamily': 'Arial'
                        }
                    )
                ])
        ],className='section'),

        # Back to top button
         dcc.Link(
            html.Button(
                "Back to Top", 
                style={
                    'backgroundColor': 'red', 
                    'color': 'white', 
                    'border': 'none',
                    'padding': '10px 20px',
                    'borderRadius': '5px',
                    'cursor': 'pointer'
                }
            ),
            href='#city-option',
            style={
                'position': 'fixed', 
                'bottom': '20px', 
                'right': '20px',
                'zIndex': '1000' # Ensures it stays above other elements
            }
        )
    ], className='main-body'),
    html.Div("Designed using Plotly Dash",className='footer')
], className='main')

@callback(
    Output('stores_ir', 'figure'),
    Output('stores_isu', 'figure'),
    Output('category_ir', 'figure'),
    Output('category_isu', 'figure'),
    Input('city-option', 'value')
)
def store_performance_analysis(city_val):

    if city_val != 'All Cities':
        filtered_df = df[df['city'] == city_val]
    else:
        filtered_df = df 

    # Store IR analysis (convert to millions)
    stores_by_ir = filtered_df.groupby(['store_id', 'city'])['incremental_revenue'].sum().reset_index()
    stores_by_ir['incremental_revenue_million'] = round(stores_by_ir['incremental_revenue'] / 1000000, 2)
    stores_by_ir = stores_by_ir.sort_values(by='incremental_revenue_million', ascending=False)
    
    # Store ISU analysis
    stores_by_isu = filtered_df.groupby(['store_id', 'city'])['incremental_sold_units'].sum().reset_index()
    stores_by_isu = stores_by_isu.sort_values(by='incremental_sold_units')
    
    # Category analysis
    category_by_ir = filtered_df.groupby('category')['incremental_revenue'].sum().reset_index()
    category_by_ir['incremental_revenue_million'] = round(category_by_ir['incremental_revenue'] / 1000000, 2)
    category_by_ir = category_by_ir.sort_values(by='incremental_revenue_million', ascending=False)
    category_by_isu = filtered_df.groupby('category')['incremental_sold_units'].sum().reset_index()
    category_by_isu = category_by_isu.sort_values(by='incremental_sold_units', ascending = False)
    
    # Create figures
    fig_stores_ir = px.bar(stores_by_ir.head(10), x='store_id', y='incremental_revenue_million',
                          title='Highest Stores Performance using Incremental Revenue', hover_data='city',                            text='incremental_revenue_million',template='seaborn' ,
                          labels={'store_id':'Store','incremental_revenue_million':'Incremental Revenue (in millions)'})
    fig_stores_ir.update_layout(plot_bgcolor='white')
    
    fig_stores_isu = px.bar(stores_by_isu.tail(10), x='store_id', y='incremental_sold_units',
                           title='Lowest Stores Performance using Incremental Sold Units', hover_data='city', template='seaborn' ,
                           text='incremental_sold_units',labels={'store_id':'Store','incremental_sold_units':'Incremental Sold Units'})
    fig_stores_isu.update_layout(plot_bgcolor='white')
    
    fig_category_ir = px.bar(category_by_ir, x='category', y='incremental_revenue_million', template='seaborn' , color='category', text='incremental_revenue_million',labels={'category':'Categories','incremental_revenue_million':'Incremental Revenue (in millions)'}, title='Overall Incremental Revenue generated by Category')
    fig_category_ir.update_layout(plot_bgcolor='white', showlegend=False )
    
    fig_category_isu = px.bar(category_by_isu, x='category', y='incremental_sold_units', template='seaborn', color='category', text='incremental_sold_units',labels={'category':'Categories','incremental_sold_units':'Incremental Sold Units'}, title='Overall Incremental Units Sold by Category')
    fig_category_isu.update_layout(plot_bgcolor='white', showlegend=False)
    
    return fig_stores_ir, fig_stores_isu, fig_category_ir, fig_category_isu


@callback(
    Output('top-products-ir','figure'),
    Output('bottom-products-isu','figure'),
    Output('promo-group-ir', 'figure'),
    Output('promo-group-isu','figure'),
    Input('city-option', 'value')
)
def promotion_type_analysis(city_val):
    
    # top promotions based on IR
    promo_name = {'25% OFF':'discount_based','50% OFF':'discount_based','33% OFF':'discount_based','500 Cashback':'cashback_promo','BOGOF':'buy_one_get_one_free'}

    if city_val != 'All Cities':
        filtered_df = df[df['city'] == city_val]
    else:
        filtered_df = df

    promotions_df = filtered_df.groupby('promo_type')[['incremental_revenue','revenue_before_promo','revenue_after_promo','incremental_sold_units','quantity_sold(before_promo)','quantity_sold(after_promo)']].sum().reset_index()
    promotions_df['promo_group'] = promotions_df['promo_type'].map(promo_name)
    # convert all revenue value into millions
    for col in ['incremental_revenue','revenue_before_promo','revenue_after_promo']:
        promotions_df[col] = round(promotions_df[col]/1000000,2)

    # top 2 promotions
    top_promo_ir = promotions_df.sort_values(by='incremental_revenue',ascending=False)

    # bottom 2 promotions
    bottom_promo_isu = promotions_df.sort_values(by='incremental_sold_units')

    # promotion group 
    promo_group = promotions_df.groupby('promo_group')[['incremental_revenue','revenue_before_promo','revenue_after_promo','incremental_sold_units','quantity_sold(before_promo)','quantity_sold(after_promo)']].sum().reset_index()

    # promotions figure
    fig_promo_ir = px.bar(top_promo_ir, y='incremental_revenue',x='promo_type',color='incremental_revenue',text_auto = True,
                          template='seaborn', hover_data=['revenue_before_promo','revenue_after_promo'], 
                          labels={'promo_type':'Promotions','incremental_revenue':'Incremental Revenue (in millions)','revenue_before_promo':'revenue before promo','revenue_after_promo':'revenue after promo'},
                          title='Overall Incremental Revenue based Promotions'                  
    )
    fig_promo_ir.update_layout(plot_bgcolor='white').update_traces(textposition='auto').update_coloraxes(showscale=False)


    fig_promo_isu = px.bar(bottom_promo_isu, y='incremental_sold_units', x='promo_type', color='incremental_sold_units', text_auto = True, 
                           template='seaborn', hover_data=['quantity_sold(before_promo)','quantity_sold(after_promo)'],
                           labels={'promo_type':'Promotions','incremental_sold_units':'Incremental Sold Units','quantity_sold(before_promo)':'quantity sold(before promo)','quantity_sold(after_promo)':'quantity sold(after promo)'},
                           title='Overall Incremental Sold Units based Promotions')
    fig_promo_isu.update_layout(plot_bgcolor='white').update_traces(textposition='auto').update_coloraxes(showscale=False)

    fig_promo_group_ir = px.pie(promo_group, names = 'promo_group', values ='incremental_revenue', template='seaborn', title='Incremental Revenue based distribution')

    fig_promo_group_isu = px.pie(promo_group, names='promo_group', values='incremental_sold_units',template='seaborn', title='Incremental Sold Units based distribution')

    return fig_promo_ir, fig_promo_isu, fig_promo_group_ir, fig_promo_group_isu


@callback(
    Output('category-promo-isu','figure'),
    Output('category-promo-ir','figure'),
    Output('product-table','columns'),
    Output('product-table','data'),
    Output('product-table','style_data_conditional'),
    Output('product-table-title','children'),
    Input('city-option','value')
)

def product_category_analysis(city_val):
    if city_val != 'All Cities':
        filtered_df = df[df['city'] == city_val]
    else:
        filtered_df = df
     
    ## PRODUCT AND CATEGORY ANALYSIS
    product_by_isu = filtered_df.groupby(['product_name','category','promo_type'])[['incremental_sold_units','incremental_revenue']].sum().reset_index().sort_values(by='incremental_sold_units', ascending=False)
    product_by_isu['incremental_revenue'] = round(product_by_isu['incremental_revenue'] / 1000000 , 2) 
    product_by_isu  = product_by_isu.rename(columns={'product_name':'Product name','category':'Cateogry', 'promo_type':'Promo Type','incremental_revenue':'Incremental Revenue (in million)', 'incremental_sold_units':'Incremental Sold Units'})

    category_by_isu = filtered_df.groupby('category')['incremental_sold_units'].sum().reset_index().sort_values(by = 'incremental_sold_units', ascending=False)
    
    category_by_ir = filtered_df.groupby('category')['incremental_revenue'].sum().reset_index().sort_values(by = 'incremental_revenue', ascending=False)
    category_by_ir['incremental_revenue'] = round(category_by_ir['incremental_revenue'] / 1000000,2)

    fig_category_by_isu = px.bar(category_by_isu, x='category', y='incremental_sold_units', color='category' , title='Category Sales by ISU', text='incremental_sold_units', labels={'incremental_sold_units':'Incremental Sold Units'}, template='seaborn')
    fig_category_by_isu.update_layout(plot_bgcolor='white').update_traces(textposition='auto').update_coloraxes(showscale=False)

    fig_category_by_ir = px.bar(category_by_ir, x='category', y='incremental_revenue', color='category', title='Category Sales by IR', text='incremental_revenue', labels={'incremental_revenue':'Incremental Revenue (in millions)'}, template='seaborn')
    fig_category_by_ir.update_layout(plot_bgcolor='white').update_traces(textposition='auto').update_coloraxes(showscale=False)


    product_table_column = [{ "name" : x, "id" : x } for x in product_by_isu.columns ]
    product_table_data = product_by_isu.to_dict('records')
    product_table_style_data_conditional = [
                        {
                            'if': {
                                'filter_query': '{Incremental Sold Units} < 0',
                                'column_id': 'Incremental Sold Units'
                            },
                            'color': 'red'
                        },
                        {
                            'if': {
                                'filter_query': '{Incremental Sold Units} >= 0',
                                'column_id': 'Incremental Sold Units'
                            },
                            'color': 'green'
                        },
                        {
                            'if': {
                                'filter_query': '{Incremental Revenue (in million)} < 0',
                                'column_id': 'Incremental Revenue (in million)'
                            },
                            'color': 'red'
                        },
                        {
                            'if': {
                                'filter_query': '{Incremental Revenue (in million)} >= 0',
                                'column_id': 'Incremental Revenue (in million)'
                            },
                            'color': 'green'
                        }
                    ]
    

    return fig_category_by_isu, fig_category_by_ir, product_table_column,product_table_data,product_table_style_data_conditional, f'Detail of Products Incremental Revenues and units sold - {city_val}'

@callback(
        Output('category-table-title','children'),
        Output('category-table','columns'),
        Output('category-table','data'),
        Input('city-option','value')
)
def category_city(city_val):
    if city_val != 'All Cities':
        filtered_df  = df[df['city'] == city_val]
    else:
        filtered_df = df
    
    # campaign category
    campaign_category_df =  filtered_df.groupby(['category','campaign_name'])[['incremental_revenue','revenue_before_promo','revenue_after_promo']].sum().reset_index()
    for revenue in ['incremental_revenue','revenue_before_promo','revenue_after_promo']:
        campaign_category_df[revenue + str(' (in million)')] = round(campaign_category_df[revenue] / 10_00_000 , 2)
    
    display_category_df = campaign_category_df[['category','campaign_name','incremental_revenue (in million)','revenue_before_promo (in million)','revenue_after_promo (in million)']]

    return f'Campaign Revenue of each Categories - {city_val}', [ {"name" : x, "id" : x } for x in display_category_df.columns ], display_category_df.to_dict('records')


if __name__ == "__main__":
    app.run(debug=False)
