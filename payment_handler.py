import stripe
import logging
from typing import Dict, Optional
import streamlit as st

class PaymentHandler:
    def __init__(self):
        self.setup_logging()
        self.setup_stripe()
        
    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
    def setup_stripe(self):
        """Initialize Stripe with API keys"""
        try:
            # Get API keys from Streamlit secrets
            stripe.api_key = st.secrets["STRIPE_SECRET_KEY"]
            self.publishable_key = st.secrets["STRIPE_PUBLISHABLE_KEY"]
            self.logger.info("Stripe initialized successfully")
        except Exception as e:
            self.logger.error(f"Error initializing Stripe: {str(e)}")
            raise

    async def create_product(self, name: str, description: str, price: float) -> Dict:
        """Create a Stripe product with price"""
        try:
            # Create product
            product = stripe.Product.create(
                name=name,
                description=description
            )
            
            # Create price for the product
            price_obj = stripe.Price.create(
                product=product.id,
                unit_amount=int(price * 100),  # Convert to cents
                currency="usd",
                recurring={"interval": "month"}  # For subscription products
            )
            
            return {
                "product_id": product.id,
                "price_id": price_obj.id,
                "name": name,
                "price": price
            }
            
        except Exception as e:
            self.logger.error(f"Error creating product: {str(e)}")
            return None
