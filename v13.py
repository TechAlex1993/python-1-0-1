import matplotlib.pyplot as plt

sizes = [25, 20, 45, 10]
labels = ["A", "B", "C", "D"]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
circle = plt.Circle((0, 0), 0.8, color='white')
plt.gca().add_artist(circle)
plt.title("Pie Chart")
plt.show()