# StockFlow Backend Case Study

## Candidate
Snehal Thube

## Overview
This repository contains my solution for the Backend Engineering Intern case study at Bynry.

The objective of this case study was to analyze an existing backend implementation, design a scalable database schema, and build an API for a B2B inventory management system.  
While working on this, I focused on writing clean, maintainable code and making practical design decisions similar to real-world scenarios.

---

## Solution Breakdown

### Part 1: Code Review & Debugging
- Identified issues in the given API, including data consistency and missing validations  
- Improved transaction handling to avoid partial database writes  
- Added proper input validation and error handling  

### Part 2: Database Design
- Designed a scalable and normalized schema  
- Supported multiple warehouses per company  
- Handled supplier relationships and product bundles  

### Part 3: Low Stock Alerts API
- Implemented an API to detect low-stock products  
- Considered inventory levels, recent sales activity, and product-specific thresholds  
- Included supplier details to support reordering decisions  

---

## Key Considerations
- Maintaining data consistency across operations  
- Designing for scalability and flexibility  
- Handling real-world edge cases and incomplete requirements  

---

## Tech Stack
- Python (Flask)  
- SQL (for schema design)

---

## Assumptions
- Recent sales activity is considered within the last 30 days  
- A product can be associated with multiple suppliers  
- Low-stock thresholds are defined at the product level  

---

This solution reflects my thought process and approach to solving backend problems with incomplete requirements.  
I prioritized clarity, correctness, and practical design over unnecessary complexity.
