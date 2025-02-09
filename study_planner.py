import streamlit as st
from dataclasses import dataclass
from typing import List
from enum import Enum

# Define Enums for User Choices
class EducationLevel(Enum):
    HIGH_SCHOOL = "High School"
    UNDERGRADUATE = "Undergraduate"
    GRADUATE = "Graduate"
    SELF_LEARNING = "Self-learning"

class WakeUpTime(Enum):
    EARLY = "5-7 AM"
    NORMAL = "7-9 AM"
    LATE = "9-11 AM"

class ProductivityPeak(Enum):
    MORNING = "Morning (6-11 AM)"
    NOON = "Noon (11 AM - 2 PM)"
    AFTERNOON = "Afternoon (2-6 PM)"
    NIGHT = "Night (6 PM - 2 AM)"

class RoutineType(Enum):
    FIXED = "Fixed Schedule"
    ADAPTIVE = "Adaptive/Flexible Schedule"

class BreakPreference(Enum):
    POMODORO = "Every 25 mins (Pomodoro)"
    HOURLY = "Every 45-60 mins"
    FLEXIBLE = "Whenever needed"

class Goal(Enum):
    IMPROVE_GRADES = "Improve grades"
    SELF_LEARN = "Self learn"
    MASTER_TOPIC = "Master a specific topic"
    EXAM_PREP = "Prepare for exams"

@dataclass
class UserProfile:
    name: str
    education_level: EducationLevel
    wake_up_time: WakeUpTime
    productivity_peak: ProductivityPeak
    routine_type: RoutineType
    break_preference: BreakPreference
    goal: Goal
    specific_topics: List[str]
    has_part_time_job: bool = False
    has_sports: bool = False
    has_gym: bool = False

def generate_study_plan(profile: UserProfile) -> dict:
    plan = {
        "morning": [],
        "afternoon": [],
        "evening": []
    }

    # Early Riser Plan
    if profile.wake_up_time == WakeUpTime.EARLY:
        plan["morning"] = [
            {"time": "5:30 AM - 6:30 AM", "activity": "Gym & Shower"},
            {"time": "6:30 AM - 7:00 AM", "activity": "Healthy Breakfast"},
            {"time": "7:00 AM - 9:00 AM", "activity": f"Study Session 1 ({profile.specific_topics[0]})"},
            {"time": "9:00 AM - 12:00 PM", "activity": "Classes/Tutorials"}
        ]
        plan["afternoon"] = [
            {"time": "12:00 PM - 1:00 PM", "activity": "Lunch & Relax"},
            {"time": "1:00 PM - 3:00 PM", "activity": "Classes/Tutorials"},
            {"time": "3:00 PM - 5:00 PM", "activity": f"Study Session 2 ({profile.specific_topics[1] if len(profile.specific_topics) > 1 else 'Review'})"}
        ]
        plan["evening"] = [
            {"time": "5:00 PM - 6:30 PM", "activity": "Extracurriculars/Sports"},
            {"time": "6:30 PM - 8:00 PM", "activity": "Study Session 3 (Practice & Review)"},
            {"time": "8:00 PM - 9:00 PM", "activity": "Dinner & Relax"},
            {"time": "9:00 PM - 10:00 PM", "activity": "Light Revision"}
        ]

    # Night Owl Plan
    elif profile.productivity_peak == ProductivityPeak.NIGHT:
        plan["morning"] = [
            {"time": "9:30 AM - 10:30 AM", "activity": "Wake up & Breakfast"},
            {"time": "10:30 AM - 12:00 PM", "activity": "Light Study/Classes"}
        ]
        plan["afternoon"] = [
            {"time": "12:00 PM - 3:00 PM", "activity": "Classes/Tutorials"},
            {"time": "3:00 PM - 4:00 PM", "activity": "Break & Relax"},
            {"time": "4:00 PM - 6:00 PM", "activity": f"Study Session 1 ({profile.specific_topics[0]})"}
        ]
        plan["evening"] = [
            {"time": "6:00 PM - 7:00 PM", "activity": "Dinner & Walk"},
            {"time": "7:00 PM - 9:00 PM", "activity": "Study Session 2 (Practice Questions)"},
            {"time": "9:00 PM - 10:00 PM", "activity": "Break/Socializing"},
            {"time": "10:00 PM - 12:00 AM", "activity": f"Deep Focus Study ({profile.specific_topics[1] if len(profile.specific_topics) > 1 else 'Review'})"},
            {"time": "12:00 AM - 1:00 AM", "activity": "Break / Extra Learning"}
        ]

    # Part-Time Job Plan
    elif profile.has_part_time_job:
        plan["morning"] = [
            {"time": "7:30 AM - 8:00 AM", "activity": "Wake up & Quick Breakfast"},
            {"time": "8:00 AM - 12:00 PM", "activity": "Classes/Tutorials"}
        ]
        plan["afternoon"] = [
            {"time": "12:00 PM - 1:00 PM", "activity": "Lunch & Rest"},
            {"time": "1:00 PM - 3:00 PM", "activity": "Classes/Study"},
            {"time": "3:00 PM - 7:00 PM", "activity": "Part-Time Job"}
        ]
        plan["evening"] = [
            {"time": "7:00 PM - 7:30 PM", "activity": "Dinner & Relax"},
            {"time": "8:00 PM - 10:00 PM", "activity": f"Study Session ({profile.specific_topics[0]})"},
            {"time": "10:00 PM - 11:30 PM", "activity": "Revision & Notes"}
        ]

    # Sports/Gym Plan
    elif profile.has_sports or profile.has_gym:
        plan["morning"] = [
            {"time": "6:30 AM - 7:30 AM", "activity": "Gym/Sports"},
            {"time": "7:30 AM - 8:30 AM", "activity": "Breakfast & Light Reading"},
            {"time": "8:30 AM - 9:30 AM", "activity": f"Study Session 1 ({profile.specific_topics[0]})"}
        ]
        plan["afternoon"] = [
            {"time": "9:30 AM - 3:00 PM", "activity": "Classes/Tutorials"},
            {"time": "3:00 PM - 4:00 PM", "activity": "Lunch & Rest"},
            {"time": "4:00 PM - 6:00 PM", "activity": "Sports Training"}
        ]
        plan["evening"] = [
            {"time": "6:00 PM - 6:30 PM", "activity": "Relax"},
            {"time": "6:30 PM - 9:00 PM", "activity": f"Study Session 2 ({profile.specific_topics[1] if len(profile.specific_topics) > 1 else 'Review'})"},
            {"time": "9:00 PM - 9:30 PM", "activity": "Dinner"},
            {"time": "9:30 PM - 11:00 PM", "activity": "Study Session 3"}
        ]

    # Default/Regular Plan
    else:
        plan["morning"] = [
            {"time": "8:00 AM - 9:00 AM", "activity": "Breakfast & Planning"},
            {"time": "9:00 AM - 12:00 PM", "activity": f"Study Session 1 ({profile.specific_topics[0]})"}
        ]
        plan["afternoon"] = [
            {"time": "12:00 PM - 1:00 PM", "activity": "Lunch & Break"},
            {"time": "1:00 PM - 4:00 PM", "activity": "Classes/Tutorials"},
            {"time": "4:00 PM - 6:00 PM", "activity": f"Study Session 2 ({profile.specific_topics[1] if len(profile.specific_topics) > 1 else 'Review'})"}
        ]
        plan["evening"] = [
            {"time": "6:00 PM - 7:00 PM", "activity": "Dinner & Break"},
            {"time": "7:00 PM - 9:00 PM", "activity": "Study Session 3 (Practice Questions)"},
            {"time": "9:00 PM - 10:30 PM", "activity": "Final Review & Planning"}
        ]

    return plan

def show_planner_tab():
    
    st.subheader("📅 Personalized Study Planner")
    try:
        st.markdown("""
            <style>
                .center-image {
                    display: flex;
                    justify-content: center;
                    margin-right: 15px;  /* Add margin to move image right */
                }
            </style>
        """, unsafe_allow_html=True)
        
        # Center the image using columns with more precise control
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.markdown('<div class="center-image">', unsafe_allow_html=True)
            st.image("assets/clawendar.png", width=200)
            st.markdown('</div>', unsafe_allow_html=True)
    
    except Exception as e:
        st.error(f"Could not load image. Please ensure 'clawendar.png' is in the assets folder.")
    

    
    st.write("""
    Let's create a personalized study schedule that fits your lifestyle and preferences!
    Fill in the details below to get your customized study plan.
    """)
    
    # Get user input
    name = st.text_input("What's your name?", key="planner_name")
    
    col1, col2 = st.columns(2)
    
    with col1:
        education_level = st.selectbox(
            "Education Level",
            options=[level.value for level in EducationLevel],
            key="education_level"
        )
        
        wake_up_time = st.selectbox(
            "Preferred Wake-up Time",
            options=[time.value for time in WakeUpTime],
            key="wake_up_time"
        )
        
        productivity_peak = st.selectbox(
            "When are you most productive?",
            options=[peak.value for peak in ProductivityPeak],
            key="productivity_peak"
        )
        
        routine_type = st.selectbox(
            "Preferred Routine Type",
            options=[routine.value for routine in RoutineType],
            key="routine_type"
        )
    
    with col2:
        break_preference = st.selectbox(
            "Break Preference",
            options=[pref.value for pref in BreakPreference],
            key="break_preference"
        )
        
        goal = st.selectbox(
            "Primary Goal",
            options=[g.value for g in Goal],
            key="goal"
        )
        
        specific_topics = st.text_input(
            "Specific Topics (comma-separated)",
            key="specific_topics"
        ).split(',')
        specific_topics = [topic.strip() for topic in specific_topics if topic.strip()]
        
        st.write("Additional Information:")
        has_part_time_job = st.checkbox("I have a part-time job")
        has_sports = st.checkbox("I participate in sports")
        has_gym = st.checkbox("I go to the gym")
    
    if st.button("Generate Study Plan"):
        if not name or not specific_topics:
            st.warning("Please fill in all required fields!")
            return
            
        # Create user profile
        profile = UserProfile(
            name=name,
            education_level=EducationLevel(education_level),
            wake_up_time=WakeUpTime(wake_up_time),
            productivity_peak=ProductivityPeak(productivity_peak),
            routine_type=RoutineType(routine_type),
            break_preference=BreakPreference(break_preference),
            goal=Goal(goal),
            specific_topics=specific_topics,
            has_part_time_job=has_part_time_job,
            has_sports=has_sports,
            has_gym=has_gym
        )
        
        # Generate and display plan
        plan = generate_study_plan(profile)
        
        st.write(f"### 📚 Study Plan for {name}")
        
        for period, activities in plan.items():
            st.write(f"#### {period.capitalize()}")
            
            for activity in activities:
                st.markdown(f"""
                <div style="
                    background-color: #f0f2f6;
                    padding: 10px;
                    border-radius: 5px;
                    margin: 5px 0;
                    color: #0F1116;
                    font-weight: 500;
                    border-left: 4px solid #1e88e5;
                ">
                    <strong>⏰ {activity['time']}</strong><br>
                    {activity['activity']}
                </div>
                """, unsafe_allow_html=True)
        
        st.success("Plan generated successfully! Adjust times as needed to fit your schedule.")
        
        st.info("""
        💡 **Tips for Success:**
        - Stick to your schedule for at least 21 days to form a habit
        - Be flexible when needed, but try to maintain consistency
        - Review and adjust your plan weekly
        - Use the Pomodoro timer to stay focused during study sessions
        - Take proper breaks to maintain productivity
        """)