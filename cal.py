# Import the close_calculator function
from function_registry import close_calculator

# Main function
def main():
    try:
        result = close_calculator()
        
        if result:
            print(result)
        else:
            print("close_calculator executed successfully.")
    
    except Exception as e:
        print("Error:", e)

# Entry point
if __name__ == "__main__":
    main()
