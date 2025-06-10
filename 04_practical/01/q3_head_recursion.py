# q3_head_recursion.py

def countdown_head(n):
    if n < 0:
        return
    countdown_head(n - 1)
    print(n)

# Example usage
if __name__ == "__main__":
    countdown_head(5)
