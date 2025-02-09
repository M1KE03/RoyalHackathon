import streamlit as st
import random

def get_snack_suggestions(preferences):
    """Get snack suggestions based on user preferences"""
    snacks_db = {
        'sweet': {
            'general': [
                'Fresh fruit (apples, bananas, grapes)',
                'Dried fruit mix',
                'Dark chocolate squares',
                'Yogurt with honey',
                'Trail mix with dried fruits',
                'Fruit smoothie'
            ],
            'vegan': [
                'Dates with almond butter',
                'Vegan dark chocolate',
                'Mixed dried fruits',
                'Banana chips',
                'Coconut date balls',
                'Berry smoothie with plant milk'
            ],
            'gluten_free': [
                'Rice cakes with honey',
                'Gluten-free granola with fruit',
                'Dark chocolate covered nuts',
                'Fruit leather',
                'Yogurt parfait with berries',
                'Chocolate covered rice cakes'
            ]
        },
        'salty': {
            'general': [
                'Mixed nuts',
                'Popcorn',
                'Whole grain crackers',
                'Rice crackers',
                'Roasted chickpeas',
                'Pretzel sticks'
            ],
            'vegan': [
                'Roasted seaweed snacks',
                'Seasoned nuts',
                'Vegan crackers',
                'Roasted chickpeas',
                'Salted edamame',
                'Air-popped popcorn'
            ],
            'gluten_free': [
                'Rice crackers',
                'Mixed nuts',
                'Roasted chickpeas',
                'Gluten-free pretzels',
                'Popcorn',
                'Corn chips'
            ]
        },
        'protein_rich': {
            'general': [
                'Hard-boiled eggs',
                'Greek yogurt',
                'Cheese cubes',
                'Turkey roll-ups',
                'Tuna on crackers',
                'Protein bars'
            ],
            'vegan': [
                'Hummus with vegetables',
                'Edamame',
                'Roasted chickpeas',
                'Nut butter with apple slices',
                'Vegan protein bars',
                'Trail mix with nuts'
            ],
            'gluten_free': [
                'Hard-boiled eggs',
                'Cheese cubes',
                'Mixed nuts',
                'Greek yogurt',
                'Gluten-free protein bars',
                'Turkey roll-ups'
            ]
        },
        'light_and_fresh': {
            'general': [
                'Cucumber slices',
                'Cherry tomatoes',
                'Carrot sticks',
                'Celery with peanut butter',
                'Bell pepper strips',
                'Fresh fruit slices'
            ],
            'vegan': [
                'Vegetable sticks',
                'Fresh fruit slices',
                'Cherry tomatoes',
                'Cucumber rounds',
                'Celery with almond butter',
                'Bell pepper strips'
            ],
            'gluten_free': [
                'Fresh vegetable sticks',
                'Fruit slices',
                'Cherry tomatoes',
                'Cucumber rounds',
                'Celery with peanut butter',
                'Bell pepper strips'
            ]
        }
    }
    
    suggestions = []
    diet_type = 'general'
    if preferences['dietary_restrictions'] == 'Vegan':
        diet_type = 'vegan'
    elif preferences['dietary_restrictions'] == 'Gluten-free':
        diet_type = 'gluten_free'
        
    for craving in preferences['cravings']:
        if craving in snacks_db:
            available_snacks = snacks_db[craving][diet_type]
            suggestions.extend(random.sample(available_snacks, min(2, len(available_snacks))))
    
    return list(set(suggestions))  # Remove duplicates

def show_snack_tab():
    st.subheader("🍎 Study Snack Suggestions")
    
    st.write("""
    Need a study snack? Let's find something healthy and satisfying!
    Choose your preferences below, and we'll suggest some brain-boosting snacks.
    """)
    
    # Get user preferences
    dietary_restrictions = st.selectbox(
        "Do you have any dietary restrictions?",
        ["None", "Vegan", "Gluten-free"]
    )
    
    cravings = st.multiselect(
        "What kind of snack are you craving?",
        ["sweet", "salty", "protein_rich", "light_and_fresh"],
        default=["light_and_fresh"]
    )
    
    if st.button("Get Snack Suggestions"):
        if not cravings:
            st.warning("Please select at least one type of snack you're craving!")
            return
            
        preferences = {
            'dietary_restrictions': dietary_restrictions,
            'cravings': cravings
        }
        
        suggestions = get_snack_suggestions(preferences)
        
        if suggestions:
            st.write("### 🍽️ Here are your personalized snack suggestions:")
            
            for i, snack in enumerate(suggestions, 1):
                st.markdown(f"""
                <div style="
                    background-color: #f0f2f6;
                    padding: 10px;
                    border-radius: 5px;
                    margin: 5px 0;
                    color: #0F1116;  # Dark text color
                    font-weight: 500;  # Medium weight for better readability
                    border-left: 4px solid #1e88e5;  # Added a blue accent
                ">
                    {i}. {snack}
                </div>
                """, unsafe_allow_html=True)
                
            st.write("""
            ### 📝 Tips for Study Snacking:
            - Keep portions moderate
            - Choose easy-to-eat snacks that won't distract from studying
            - Stay hydrated! Keep water nearby
            - Avoid messy foods that might damage study materials
            - Choose snacks that provide sustained energy
            """)
        else:
            st.error("No snacks found matching your preferences. Try different options!")