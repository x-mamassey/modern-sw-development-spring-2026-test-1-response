# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.
# Comment to prove I edited 😁

p_hp = 50
b_hp = 50
MAX_HP = 50

def attack():
    global b_hp
    b_hp -= 10
    
    if b_hp < 0:
        b_hp = 0
    print("You deal 10 damage!")

def heal():
    global p_hp
    
    if p_hp <= 0:
        print("Omae Wa Mou Shindeiru.")
    else:
        p_hp = min(p_hp + 20, 50)
    print(f"Healed! HP is now {p_hp}")

# --- Simple Game Loop ---
while p_hp > 0 and b_hp > 0:
    print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
    choice = input("Action [a]ttack, [h]eal, [c]heat: ").lower()

    if choice == 'a':
        attack()
    elif choice == 'h':
        heal()

    else:
        print("Invalid choice! Please choose 'a' or 'h'.")

    if b_hp <= 0:
        print("Victory!")
        break

    if b_hp > 0:
        p_hp -= 10

print("Game Over!")
