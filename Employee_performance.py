evaluations = [
    {"name": "Ahmed", "score": 80},
    {"name": "Sara", "score": 95},
    {"name": "Ahmed", "score": 90},
    {"name": "Mohamed", "score": 70},
    {"name": "Sara", "score": 88},
    {"name": "Ali", "score": 95},
    {"name": "Ahmed", "score": 85},
    {"name": "Mohamed", "score": 75}
]

stats = {}
for entry in evaluations:
    name = entry["name"]
    score = entry["score"]
    if name not in stats:
        stats[name] = {"total": 0, "count": 0}
    stats[name]["total"] += score
    stats[name]["count"] += 1

averages = []
for name, data in stats.items():
    avg = data["total"] / data["count"]
    averages.append({"name": name, "average": avg})

averages.sort(key=lambda x: x["average"], reverse=True)

top_3 = averages[:3]
for employee in top_3:
    print(f"{employee['name']}: {employee['average']:.2f}")
