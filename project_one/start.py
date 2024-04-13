# What is before step one?
# Step 1: Data Loading and Initial Exploration




# Step 2: Data Cleaning
# Check for null values before cleaning
print("\nNull values before cleaning:")


# Handle missing values
# If column is a number, replace with average value of that column
# If column is not a number, drop the data
# You will need to use a for loop




# Confirm that missing values are handled
print("\nData types and missing values after handling missing values:")



# Step 3: Data Filtering and Selection
# Question 1: What is the average price of laptops based on different companies?
print("\nAverage price of laptops based on different companies:")



# Question 2: How does the price distribution vary between laptops with SSD and HDD?
print("\nPrice distribution for laptops with SSD and HDD:")



# Question 3: Which company has the highest average RAM capacity?
df['Ram'] = df['Ram'].str.extract('(\d+)').astype(float)  # Clean RAM column




# Question 4: How does the weight of laptops vary across different screen resolutions?
df['Weight'] = df['Weight'].str.extract('(\d+\.\d+)').astype(float)  # Clean Weight column



# Step 5: Plotting
# Plot questions 1-4 in a 2x2 subplot




# Show plot
