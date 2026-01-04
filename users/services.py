import stripe
import os
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_product_stripe():
    """Создание продукта."""
    try:
        return stripe.Product.create(name="New_Product")
    except stripe.error.StripeError as e:
        print(f"Ошибка при создании продукта: {e}")
        return None


def create_stripe_price_amount(product_id: str, amount: float) -> dict:
    """Создание цены."""
    try:
        return stripe.Price.create(
            currency="usd",
            unit_amount=int(
                amount * 100
            ),  # Конвертируем в минимальное деление валюты (центы)
            product=product_id,  # Используем ID существующего продукта
        )
    except stripe.error.StripeError as e:
        print(f"Ошибка при создании цены: {e}")
        return None


def create_stripe_session(price: dict) -> tuple:
    """Создание сессии."""
    try:
        session = stripe.checkout.Session.create(
            success_url=os.getenv("SUCCESS_URL_SESSION"),  # URL успеха после оплаты
            line_items=[{"price": price.get("id"), "quantity": 1}],
            mode="payment",
        )
        return session.get("id"), session.get("url")
    except stripe.error.StripeError as e:
        print(f"Ошибка при создании сессии: {e}")
        return None, None
