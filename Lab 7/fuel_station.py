
import math


def parse_purchase(text):
    try:
        if not isinstance(text, str) or text.count(":") != 1:
            return None, None

        grade, litres = text.split(":")
        grade = grade.strip()
        litres = float(litres.strip())

        if not grade or not math.isfinite(litres) or litres <= 0:
            return None, None

        return grade.title(), litres

    except (ValueError, TypeError, AttributeError):
        return None, None


def volume_average(volumes_csv):
    try:
        if not isinstance(volumes_csv, str) or not volumes_csv.strip():
            return 0

        values = [int(x.strip()) for x in volumes_csv.split(",")]

        if not values or any(x < 0 for x in values):
            return 0

        return sum(values) // len(values)

    except (ValueError, TypeError, AttributeError):
        return 0


def payable_bill(text):
    try:
        if not isinstance(text, str) or text.count("|") != 1:
            return 0.0

        bill, discount = text.split("|")
        bill = float(bill.strip())
        discount = float(discount.strip())

        if not math.isfinite(bill) or not math.isfinite(discount):
            return 0.0

        if bill < 0 or discount < 0:
            return 0.0

        total = bill * 1.18 - discount
        return max(total, 0.0)

    except (ValueError, TypeError, AttributeError):
        return 0.0


def main():
    print("==== Running parse_purchase ====")
    user_input = input("Enter grade:litres (e.g. diesel:25): ")
    print("Grade and Litres:", parse_purchase(user_input))

    print("\n==== Running volume_average ====")
    user_input = input("Enter pump volumes in litres as CSV (e.g. 10,25,40): ")
    print("Average Volume:", volume_average(user_input))

    print("\n==== Running payable_bill ====")
    user_input = input("Enter bill|discount (e.g. 2500|100): ")
    print("Payable Bill:", payable_bill(user_input))


if __name__ == "__main__":
    main()
