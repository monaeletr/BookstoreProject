import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()


url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)

def get_books():
    response = supabase.table("books").select("*").limit(5).execute()
    return response.data


def add_book(isbn, title, author, year_of_publication, publisher, image_url_s, image_url_m, image_url_l):
    response = supabase.table("books").insert({
        "isbn": isbn,
        "title": title,
        "author": author,
        "year_of_publication": year_of_publication,
        "publisher": publisher,
        "image_url_s": image_url_s,
        "image_url_m": image_url_m,
        "image_url_l": image_url_l
    }).execute()
    
    return response.data

def increase_stock(isbn, new_purchase_amt):
    result = supabase.table("inventory").select("quantity_in_stock").eq("isbn", isbn).single().execute()
    current_stock = result.data["quantity_in_stock"]

    new_stock = current_stock + new_purchase_amt

    response = (
        supabase.table("inventory")
        .update({"quantity_in_stock": new_stock})
        .eq("isbn", isbn)
        .execute()
    )
    
    return response.data

def buy_book(isbn, amt_sold):
    result = supabase.table("inventory").select("quantity_in_stock").eq("isbn", isbn).single().execute()
    if not result.data:
        return {"error": f"Book with ISBN {isbn} not found in inventory."}


    current_stock = result.data["quantity_in_stock"]

    if current_stock >= amt_sold:
        new_stock = current_stock - amt_sold

        response = (
            supabase.table("inventory")
            .update({"quantity_in_stock": new_stock})
            .eq("isbn", isbn)
            .execute()
        )
        return response.data
    
    else:
        return {"error": f"Not enough stock. Current: {current_stock}, Requested: {amt_sold}"}
    
    
def check_inventory(isbn):
    result = supabase.table("inventory").select("quantity_in_stock").eq("isbn", isbn).single().execute()
    current_stock = result.data["quantity_in_stock"]
    return {f"Current stock of isbn {isbn} is {current_stock}"}


# updated = increase_stock("0001047973", 10)
# print(updated) 

# print(buy_book("0001360469", 3))   
# print(buy_book("0001372564", 100)) 

print(check_inventory("0001360469"))

