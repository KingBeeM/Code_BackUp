import matplotlib
import matplotlib.pyplot as plt

# matplotlib version check
print(matplotlib.__version__)

# matplotlib frame
fig, axs = plt.subplots(col=1, row=1, figsize=(10, 6))
plt.show()

# sample data
dates = [
    '2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05',
    '2021-01-06', '2021-01-07', '2021-01-08', '2021-01-09', '2021-01-10'
]
min_temperature = [20.7, 17.9, 18.8, 14.6, 15.8, 15.8, 15.8, 17.4, 21.8, 20.0]
max_temperature = [34.7, 28.9, 31.8, 25.6, 28.8, 21.8, 22.8, 28.4, 30.8, 32.0]

# line grape
fig, axs = plt.subplots(figsize=(10, 6))
axs.plot(dates, min_temperature, label="Min Temp.")
axs.plot(dates, max_temperature, label="Max Temp.")
plt.show()

# [2 x 1] Division
fig, axs = plt.subplots(nrows = 2, ncols = 1, figsize=(10, 6))
axs[0].plot(dates, min_temperature, label="Min Temp.")
axs[1].plot(dates, max_temperature, label="Max Temp.")
plt.show()

# [1 x 2] Division
fig, axs = plt.subplots(nrows = 1, ncols = 2, figsize=(10, 6))
axs[0].plot(dates, min_temperature, label="Min Temp.")
axs[1].plot(dates, max_temperature, label="Max Temp.")
plt.show()

# [2 x 2] Division
fig, axs = plt.subplots(nrows = 2, ncols = 2, figsize=(10, 6))
axs[0, 0].plot(dates, min_temperature, label="Min Temp.")
axs[1, 1].plot(dates, max_temperature, label="Max Temp.")
plt.show()

# [2 x 2] Division sample
fig, axs = plt.subplots(nrows = 2, ncols = 2, figsize=(10, 6))
axs[0, 0].plot(dates, min_temperature, label="Min Temp.")
axs[0, 0].set_title("a [0, 0]")
axs[0, 1].boxplot([min_temperature, max_temperature])
axs[1, 0].plot([1, 2, 3])
axs[1, 1].plot(dates, max_temperature, label="Max Temp.")
plt.show()
