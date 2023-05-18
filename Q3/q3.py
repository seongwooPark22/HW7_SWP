import pandas as pd
import numpy as np

def main() : 
    input_data = pd.DataFrame([[1000,25],[280,120],[900,30]], index=["store1", "store2", "store3"], columns=["unit price", "number"])
    print(input_data)
    print()

    total_added_data = input_data.copy(True)
    total_added_data["total price"] = np.multiply(total_added_data["unit price"],total_added_data["number"])
    print(total_added_data)
    print()

    top2 = total_added_data.sort_values(by="total price", ascending=False)
    print(top2[:2])


if __name__ == "__main__" :
    main()
