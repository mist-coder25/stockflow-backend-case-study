# StockFlow Backend Case Study

## Candidate
Snehal Thube

## Overview
This repository contains my solution for the Backend Engineering Intern case study at Bynry.

The objective of this case study was to analyze an existing backend implementation, design a scalable database schema, and implement an API for a B2B inventory management system.  
While working on this, I focused on writing clean, maintainable code and making practical design decisions aligned with real-world backend systems.

---

## Solution Breakdown

### Part 1: Code Review & Debugging
- Identified key issues in the given API, including data consistency problems and missing validations  
- Improved transaction handling to prevent partial database writes  
- Added proper input validation and error handling to make the API more robust  

### Part 2: Database Design
- Designed a scalable and normalized schema  
- Supported multiple warehouses per company and product  
- Modeled supplier relationships and product bundles effectively  

### Part 3: Low Stock Alerts API
- Implemented an API to identify low-stock products  
- Considered inventory levels, recent sales activity, and product-specific thresholds  
- Included supplier details to support efficient reordering  

---

## Key Considerations
- Maintaining data consistency across operations  
- Designing for scalability and flexibility  
- Handling real-world edge cases and incomplete requirements  

---

## Tech Stack
- Python (Flask)  
- SQL (Schema Design)

---

## Assumptions
- Recent sales activity is considered within the last 30 days  
- A product can be associated with multiple suppliers  
- Low-stock thresholds are defined at the product level  

---

## Case Study Document
You can view my complete case study response here:  
https://docs.google.com/document/d/1RIcmcVT4HutD0dAn6sWz__Sde5dGZqDOl0-5CNGi_uE/edit?usp=sharing

---

## 🌱 Conclusion
This solution reflects my approach to solving backend problems in scenarios with incomplete requirements.  
I prioritized clarity, correctness, and practical design while keeping scalability and maintainability in mind.
