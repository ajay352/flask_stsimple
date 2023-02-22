import stripe
from flask import Flask, redirect,render_template

app = Flask(__name__,static_folder="templates")

stripe.api_key = "sk_test_51MduieSErZbH7P9I7Rkfuk3bPwqvGn6jpB9s1LYKlZq2bDDgvoNsSBjdDNRnVW0QLZIELQVdST3kjfNzUigr3XSn00nRFw0Frp"

YOUR_DOMAIN = "http://localhost:5000"

@app.route('/create-checkout-session',methods=['GET','POST'])
def create_checkout_session():
    checkout_session = stripe.checkout.Session.create(
            line_items = [
                {
                    "price":"price_1MeH4USErZbH7P9INFY4ftAI",
                    "quantity":1
                }
            ],
            mode="subscription",
            success_url=YOUR_DOMAIN + "/success.html",
            cancel_url = YOUR_DOMAIN + "/cancel.html"
        )

    return redirect(checkout_session.url,code=303)

    
    
        
        

    

if __name__ == "__main__":
    app.run(debug=True ,port=8088,use_reloader=False)