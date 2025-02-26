---
title: "E-commerce dashboard"
slug: e-commerce-dashboard
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1740472860231/451c8b1d-b4ea-49ff-bf4a-f79388ed8b5e.avif

---

## Introduction

Running an online store means constantly asking yourself:

* Are we growing faster in certain regions?
    
* Which products actually make us money?
    
* Do we sell more on weekends than weekdays?
    
* Who's our ideal customer?
    

I decided to build a dashboard that turns our complex transaction records into simple visuals that answer these questions. My goal was straightforward: create a single hub where the team can monitor sales performance, identify emerging trends, get insights on customer behavior, and determine which products are driving our business forward.

## The Data

I used the Brazilian E-commerce dataset from Kaggle, which contains real sales from 2016-2018, including:

* What people bought and which categories
    
* When orders were placed
    
* Who bought what and where they live
    
* How many items sold and at what price
    

\[Link: [https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)\]

## Planning the Dashboard

Before jumping into code, I thought about who would use this thing and what they'd need:

**Who's it for?** Sales and marketing folks who need quick answers without digging through spreadsheets

**What should it show?**

* Key numbers at a glance (so managers can check if we're on target)
    
* Sales over time (to spot seasonal patterns and plan promotions)
    
* Customer breakdowns (to figure out who to target)
    
* Product insights (to know what to stock up on)
    
* Regional sales map (to see where we're killing it and where we're not)
    
* Filters to drill down into specific timeframes or categories
    

## Picking the Tools

After checking out different options, I settled on:

* Python (because it's what I know best)
    
* Pandas and NumPy (for data wrangling)
    
* Streamlit (for building the interface)
    
* Plotly (for making interactive charts)
    
* Git (to track changes)
    

I went with Streamlit because it's straightforward, works well with data libraries, and lets me test ideas quickly.

## Cleaning Up the Data

First things first—I had to sort through the mess of raw data:

\[Screenshot of data cleaning process\]

I focused on:

**Getting rid of the junk**: Removed duplicates and error entries that would mess up our numbers.

\[Screenshot of duplicate removal code\]

**Fixing data types**: Made sure dates were actually dates and numbers were actually numbers.

\[Screenshot of data type conversion\]

**Creating helpful columns**: Added stuff like month, year, and day of week to make analysis easier.

**Pre-calculating totals**: Grouped data at different levels to make the dashboard run faster.

\[Screenshot of data aggregation\]

## Calculating the Important Numbers

With clean data, I pulled out the metrics that matter:

\[Screenshot of metrics calculation\]

I also prepared data for trend analysis:

\[Screenshot of trend data preparation\]

## Building the Basic Dashboard

Next, I started putting together the interface:

\[Screenshot of dashboard code\]

\[Screenshot of dashboard interface\]

## Creating Sales Charts

I built interactive charts to show sales patterns:

\[Screenshot of visualization code\]

\[Screenshot of sales trend charts\]

## Challenges I Hit

This wasn't all smooth sailing:

* **Messy source data**: Some transactions were missing customer info, and dates were all over the place
    
* **No product categories**: Had to make my own classification system based on product codes and descriptions
    
* **Performance issues**: Had to optimize things when the dataset got large
    

## What's Next

In the next part of this project, I'm planning to add:

**Deeper customer analysis**:

* RFM segmentation (how recently and frequently people buy, and how much they spend)
    
* Tracking how well we keep customers over time
    

**Product insights**:

* Identifying bestsellers and duds
    
* Finding which products are often bought together
    

**Geographic visualization**:

* Sales maps by region
    
* How distance affects order size
    

**Sales forecasting**:

* Predicting future sales
    
* Spotting unusual patterns
    

## Wrapping Up

The dashboard's still a work in progress, but it's already giving our team useful insights about sales patterns we couldn't easily spot before. I'm pretty happy with how the interactive filters turned out - they've saved us hours of manual data slicing.

Next time, I'll walk through the customer segmentation features I'm building and show some surprising patterns we discovered in our product category performance.

The code's up on my GitHub if you want to take a peek under the hood. Always open to suggestions, so hit me up in the comments if you have thoughts!