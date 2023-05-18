if __name__ == "__main__":
    import time

    pbcl = 50 # Progress bar character length
    pbpa = 120 # Progress bar progress amount (units)
    pbpr = 300 # Progress bar progress rate (ms / unit)

    for cp in range(pbpa + 1): # For every unit of current progress made

        fcc = int((pbcl * cp) / pbpa) # Filled character count
        ucc = pbcl - fcc # Unfilled character count

        # Print out the progress bar
        print(f"\r[{'■' * fcc}{'-' * ucc}] {(100 * cp) / pbpa :.2f}%", end="")
        time.sleep(pbpr / 1000) # Wait for pbpr miliseconds

    print("") # Jump to a new line
