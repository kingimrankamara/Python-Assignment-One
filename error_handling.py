def load_data(filename):
    try:
        data = pd.read_csv(filename)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{filename}' is empty.")
    except Exception as e:
        print(f"Error: {e}")

# Load dataset with error handling
df = load_data('iris.csv')  # replace with actual file path
