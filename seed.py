from app import app, db
from models import User, Recipe

def seed_data():
    db.create_all()

    # Example users
    user1 = User(
        firstName="John",
        lastName="Doe",
        username="johndoe",
        email="johndoe@example.com",
        _password_hash="hashedpassword",
        aboutMe="A passionate cook.",
        image_url="http://example.com/image.jpg",
        bio="Loves to create new recipes."
    )

    user2 = User(
        firstName="Jane",
        lastName="Smith",
        username="janesmith",
        email="janesmith@example.com",
        _password_hash="hashedpassword",
        aboutMe="A food blogger.",
        image_url="http://example.com/image2.jpg",
        bio="Writes about food and recipes."
    )

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    # Example recipes
    recipe1 = Recipe(
        title="Spaghetti Bolognese",
        ingredients="Spaghetti, ground beef, tomato sauce",
        instructions="Cook the spaghetti, prepare the sauce, mix together.",
        author_id=user1.id,
        chefImage="http://example.com/chef1.jpg",
        chefName="John Doe",
        image="http://example.com/spaghetti.jpg",
        url="http://example.com/recipe1",
        moreInfoUrl="http://example.com/info1",
        rating=4.5,
        prepTime="30 minutes",
        servings=4,
        countryOfOrigin="Italy",
        dietType="Non-Vegetarian"
    )

    recipe2 = Recipe(
        title="Vegan Salad",
        ingredients="Lettuce, tomatoes, cucumber, olive oil",
        instructions="Chop the vegetables, mix together, add dressing.",
        author_id=user2.id,
        chefImage="http://example.com/chef2.jpg",
        chefName="Jane Smith",
        image="http://example.com/salad.jpg",
        url="http://example.com/recipe2",
        moreInfoUrl="http://example.com/info2",
        rating=5.0,
        prepTime="15 minutes",
        servings=2,
        countryOfOrigin="USA",
        dietType="Vegan"
    )

    db.session.add(recipe1)
    db.session.add(recipe2)
    db.session.commit()

if __name__ == "__main__":
    seed_data()

