# Base class: Workout
class Workout:
    def __init__(self, name, muscle_group="General"):
        self.name = name
        self.muscle_group = muscle_group
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def display(self):
        status = "✅" if self.completed else "❌"
        print(f"{status} [{self.muscle_group}] {self.name}")

# Derived class: CardioWorkout (Inheritance + Polymorphism)
class CardioWorkout(Workout):
    def __init__(self, name):
        super().__init__(name, muscle_group="Cardio")

    def display(self):  # Polymorphism
        status = "🏃✅" if self.completed else "🏃❌"
        print(f"{status} [CARDIO] {self.name}")

# Workout Manager (Encapsulation + Abstraction)
class GymRoutine:
    def __init__(self):
        self.workouts = []  # encapsulated

    def add_workout(self, workout):
        self.workouts.append(workout)

    def show_workouts(self):
        if not self.workouts:
            print("No workouts added.")
            return
        for idx, workout in enumerate(self.workouts, start=1):
            print(f"{idx}. ", end="")
            workout.display()

    def complete_workout(self, index):
        if 0 <= index < len(self.workouts):
            self.workouts[index].mark_complete()
            print("Workout marked as complete!")
        else:
            print("Invalid workout number.")

    def delete_workout(self, index):
        if 0 <= index < len(self.workouts):
            removed = self.workouts.pop(index)
            print(f"Deleted workout: {removed.name}")
        else:
            print("Invalid workout number.")

# Main program
def main():
    routine = GymRoutine()

    while True:
        print("\n--- Gym Routine Manager ---")
        print("1. Add Workout")
        print("2. Add Cardio Workout")
        print("3. View Workouts")
        print("4. Complete Workout")
        print("5. Delete Workout")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            name = input("Enter workout name: ")
            muscle_group = input("Enter muscle group (e.g., Chest, Legs, Back): ")
            routine.add_workout(Workout(name, muscle_group))

        elif choice == "2":
            name = input("Enter cardio workout name: ")
            routine.add_workout(CardioWorkout(name))

        elif choice == "3":
            routine.show_workouts()

        elif choice == "4":
            idx = int(input("Enter workout number to complete: ")) - 1
            routine.complete_workout(idx)

        elif choice == "5":
            idx = int(input("Enter workout number to delete: ")) - 1
            routine.delete_workout(idx)

        elif choice == "6":
            print("Goodbye! Keep grinding! 💪")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
