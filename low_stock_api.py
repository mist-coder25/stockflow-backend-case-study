@app.route('/api/companies/<int:company_id>/alerts/low-stock', methods=['GET'])
def get_low_stock_alerts(company_id):
try:
alerts = []
warehouses = Warehouse.query.filter_by(company_id=company_id).all()
warehouse_ids = [w.id for w in warehouses]
results = db.session.query(
Product, Inventory, Warehouse, Supplier
).join(Inventory)\
.join(Warehouse)\
.join(Product_Suppliers)\
.join(Supplier)\
.filter(Inventory.warehouse_id.in_(warehouse_ids))\
.all()
for product, inventory, warehouse, supplier in results:
recent_sales = get_recent_sales(product.id)
if not recent_sales:
continue
threshold = get_threshold(product)
if inventory.quantity < threshold:
alerts.append({
"product_id": product.id,
"product_name": product.name,
"sku": product.sku,
"warehouse_id": warehouse.id,
"warehouse_name": warehouse.name,
"current_stock": inventory.quantity,
"threshold": threshold,
"days_until_stockout": estimate_stockout_days(product.id),
"supplier": {
"id": supplier.id,
"name": supplier.name,
"contact_email": supplier.contact_email
}
})
return {
"alerts": alerts,
"total_alerts": len(alerts)
}
except Exception as e:
return {"error": str(e)}, 500
