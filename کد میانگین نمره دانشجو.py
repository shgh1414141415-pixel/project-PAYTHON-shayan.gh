codes = []
averages = []

# ===== حلقه‌ی اصلی: گرفتن کد دانشجو =====
while True:
    code = input("Student code (empty = exit): ")
    if code == "":
        break

    # ===== گذربان کد دانشجویی =====
    if code.isdigit() == False:
        print("!! Invalid: code must be numbers only. Try again.")
    else:
        total = 0
        count = 0

        # ===== گرفتن نمره‌ها =====
        while True:
            g = input("Grade 0-20 (empty = next student): ")
            if g == "":
                break

            # ===== گذربان نمره (بدون try/except) =====
            if g.replace(".", "", 1).isdigit():
                grade = float(g)
                if grade < 0 or grade > 20:
                    print("!! Invalid: grade must be between 0 and 20. Skipped.")
                else:
                    total = total + grade
                    count = count + 1
            else:
                print("!! Invalid: grade must be a number. Skipped.")

        # ===== گذربان حداقل یک نمره =====
        if count == 0:
            print("!! No valid grade entered. Student skipped.")
        else:
            codes.append(code)
            averages.append(total / count)

# ===== چاپ نتایج با while ساده =====
print("\n--- RESULTS ---")
i = 0
while i < len(codes):
    print("Code:", codes[i], "| Average:", round(averages[i], 2))
    i = i + 1