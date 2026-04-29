from flask import Flask, render_template

app = Flask(__name__, template_folder="templates1")

recipes = {
    "Kinder Soft Cookies": {
        "title": "Kinder Soft Cookies 🍪",
        "ingredients": ["120g butter (room temperature)", "80g brown sugar", "80g white sugar", "1 tsp vanilla extract", "1 egg", "300g all-purpose flour", "1tsp baking powder", "1/2 tsp baking soda", "15 kinder chocolate pieces"],
        "steps": ["Preheat the oven to 180°C (350°F).", "In a bowl, mix the butter with the brown and white sugar until creamy.", "Add the egg and vanilla extract, and mix well.", "In another bowl, combine the flour, baking powder, and baking soda.", "Gradually add the dry ingredients to the wet mixture and mix until a dough forms.", "Fold in the kinder chocolate pieces.", "Shape the dough into small balls and place them on a baking tray.", "Bake for 15-20 minutes, depending on how soft you want them.", "Serve"]
    },
    "Tiramisu Balls": {
        "title": "Tiramisu Balls 🍽️",
        "ingredients": ["200g crushed ladyfingers (savoiardi biscuits)", "200g mascarpone cheese", "2tbsp powdered sugar", "2 vanilla sachets", "1tsp liquid vanilla extract", "1 shot of espresso coffee", "Cocoa powder (for coating)"],
        "steps": ["Crush the ladyfingers into fine crumbs", "In a bowl, mix the mascarpone, powdered sugar, vanillin, and vanilla extract until smooth.", "Add the espresso and mix well", "Combine the cream with the crushed ladyfingers and mix until a soft dough forms.", "Shape the mixture into small balls.", "Roll each ball in cocoa powder to coat.", "Refrigerate for at least 1 hour before serving.", "Enjoy"]
    }
}

@app.route("/")
def home():
    return render_template("index.html", recipes=recipes)

@app.route("/recipe/<name>")
def recipe(name):
    return render_template("recipe.html", recipe=recipes[name])

app.run(debug=True)