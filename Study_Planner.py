from dataclasses import dataclass
from typing import List, Dict
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


def generate_study_plan(profile: UserProfile) -> Dict[str, List[Dict[str, str]]]:
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

    if profile.specific_topics:
        if profile.wake_up_time == WakeUpTime.EARLY:
            plan["morning"].append({"time": "5:30 AM - 6:30 AM", "activity": "Gym & Shower"})
            plan["morning"].append({"time": "6:30 AM - 7:00 AM", "activity": "Healthy Breakfast"})
            plan["morning"].append(
                {"time": "7:00 AM - 9:00 AM", "activity": f"Study Session ({profile.specific_topics[0]})"})

        if profile.productivity_peak in [ProductivityPeak.AFTERNOON, ProductivityPeak.NIGHT]:
            plan["evening"].append(
                {"time": "6:00 PM - 8:00 PM", "activity": f"Study Session ({profile.specific_topics[0]})"})
            if len(profile.specific_topics) > 1:
                plan["evening"].append(
                    {"time": "9:00 PM - 12:00 AM", "activity": f"Deep Focus Study ({profile.specific_topics[1]})"})
            plan["evening"].append({"time": "12:00 AM - 1:00 AM", "activity": "Break / Extra Learning"})

    plan["afternoon"].append({"time": "12:00 PM - 2:00 PM", "activity": "Lunch & Relax"})

    return plan


def get_user_input() -> UserProfile:
    name = input("Enter your name: ")

    print("Select your education level:")
    education_level = list(EducationLevel)[
        int(input("1: High School, 2: Undergraduate, 3: Graduate, 4: Self-learning: ").strip()) - 1]

    print("Select your wake-up time:")
    wake_up_time = list(WakeUpTime)[int(input("1: 5-7 AM, 2: 7-9 AM, 3: 9-11 AM: ").strip()) - 1]

    print("Select your productivity peak:")
    productivity_peak = list(ProductivityPeak)[int(input("1: Morning, 2: Noon, 3: Afternoon, 4: Night: ").strip()) - 1]

    print("Select your routine type:")
    routine_type = list(RoutineType)[int(input("1: Fixed, 2: Adaptive/Flexible: ").strip()) - 1]

    print("Select your break preference:")
    break_preference = list(BreakPreference)[int(input("1: Pomodoro, 2: Hourly, 3: Flexible: ").strip()) - 1]

    print("Select your goal:")
    goal = list(Goal)[int(input("1: Improve grades, 2: Self learn, 3: Master a topic, 4: Exam prep: ").strip()) - 1]

    specific_topics = input("Enter specific topics you want to study (comma separated): ").strip().split(', ')
    if not specific_topics or specific_topics == ['']:
        specific_topics = ["General Study"]

    has_part_time_job = input("Do you have a part-time job? (yes/no): ").strip().lower() == "yes"
    has_sports = input("Do you participate in sports? (yes/no): ").strip().lower() == "yes"
    has_gym = input("Do you go to the gym? (yes/no): ").strip().lower() == "yes"

    return UserProfile(name, education_level, wake_up_time, productivity_peak, routine_type, break_preference, goal,
                       specific_topics, has_part_time_job, has_sports, has_gym)


def main():
    user_profile = get_user_input()
    study_plan = generate_study_plan(user_profile)

    print("\n📅 Your Personalized Study Plan:")
    for period, activities in study_plan.items():
        print(f"\n{period.capitalize()}:")
        if activities:
            for activity in activities:
                print(f"  ⏰ {activity['time']} - {activity['activity']}")
        else:
            print("  No activities scheduled.")


if __name__ == "__main__":
    main()