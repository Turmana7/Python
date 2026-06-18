student_data = {
    "სახელი": "გიორგი",
    "საგნები": {"Python": 95, "კალკულუსი": 80, "ფიზიკა": 90}
}

scores = student_data["საგნები"].values()
average = sum(scores) / len(scores)

print(f"{student_data['სახელი']}-ს საშუალო ქულაა: {average:.2f}")