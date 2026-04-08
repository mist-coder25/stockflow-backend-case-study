from decimal import Decimal
from flask import request, jsonify
@app.route('/api/products', methods=['POST'])
def create_product():
data = request.json
try:
# Validate required fields
required_fields = ['name', 'sku', 'price']
for field in required_fields:
if field not in data:
return {"error": f"{field} is required"}, 400
# Validate price
try:
price = Decimal(str(data['price']))
except:
return {"error": "Invalid price format"}, 400
# Check SKU uniqueness
existing_product = Product.query.filter_by(sku=data['sku']).first()
if existing_product:
return {"error": "SKU already exists"}, 400
# Create product (NO warehouse_id here)
product = Product(
name=data['name'],
sku=data['sku'],
price=price
)
db.session.add(product)
db.session.flush() # get product.id without commit
# Optional inventory creation
if 'warehouse_id' in data:
inventory = Inventory(
product_id=product.id,
warehouse_id=data['warehouse_id'],
quantity=data.get('initial_quantity', 0)
)
db.session.add(inventory)
# Single transaction commit
db.session.commit()
return {
"message": "Product created successfully",
"product_id": product.id
}, 201
except Exception as e:
db.session.rollback()
return {"error": str(e)}, 500
