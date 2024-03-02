# Calculate return on investment (ROI) based on profit and investment
def calculate_roi(profit, investment):
    return (profit / investment) * 100

# Example usage:
profit = 5000  # Profit generated
investment = 20000  # Total investment
roi = calculate_roi(profit, investment)
print("Return on investment (ROI):", roi, "%")
