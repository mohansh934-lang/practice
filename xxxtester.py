parties = ["BJP", "Congress", "AAP", "TMC", "CPI(M)", "SHIV SENA", "NCP", "BSP", "RJD", "DMK"]

print("Welcome to the Election Committee Portal 2026")

while True:
    party = input("Enter the name of your favorite political party Atleast 2 word: -- ").lower()
    if party == "n":
        print("you vote NOTA ( None of the above )")
        break

    found = False

    for p in parties:
        if p.startswith(party.upper()):
            print("You voted for", p)
            found = True
            break
        
    if found:
        print("Thank you! Your vote has been recorded.")
        break
        
    if not found:
            print("Party not found, please try again or enter 'N' for NOTA") 
