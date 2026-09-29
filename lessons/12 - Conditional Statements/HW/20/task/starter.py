rain_probability = float(input("Enter rain probability (%): "))
print()
if rain_probability <= 30:
    print("Low probability.")
if 30 <= rain_probability and rain_probability <= 60:
    print("Average probability.")
if 60 <= rain_probability and rain_probability <= 80:
    print("High probability.")
if 80 <= rain_probability and rain_probability <= 100:
    print("Very high probability.")
