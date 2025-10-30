def generate_code(function_name: str) -> str:
    return f'''from function_registry import {function_name}

def main():
    try:
        result = {function_name}()
        if result:
            print(result)
        else:
            print("{function_name} executed successfully.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
'''
