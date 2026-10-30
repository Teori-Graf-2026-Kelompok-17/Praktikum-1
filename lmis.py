
from bisect import bisect_left, bisect_right


def find_lmis(numbers, mode="strict"):
    """
    Mencari Largest Monotonically Increasing Subsequence.

    mode:
    - strict: setiap elemen harus lebih besar
    - non_decreasing: elemen boleh sama
    """

    if not numbers:
        return [], []

    tails = []
    tails_index = []
    previous = [-1] * len(numbers)

    for i, value in enumerate(numbers):

        if mode == "strict":
            position = bisect_left(tails, value)
        else:
            position = bisect_right(tails, value)

        if position > 0:
            previous[i] = tails_index[position - 1]

        if position == len(tails):
            tails.append(value)
            tails_index.append(i)
        else:
            tails[position] = value
            tails_index[position] = i

    # Rekonstruksi subsequence
    result = []
    indices = []

    current = tails_index[-1]

    while current != -1:
        result.append(numbers[current])
        indices.append(current)
        current = previous[current]

    result.reverse()
    indices.reverse()

    return result, indices


def display_result(numbers, mode):
    result, indices = find_lmis(numbers, mode)

    print("\n========== HASIL LMIS ==========")
    print("Data input       :", numbers)
    print("Subsequence      :", result)
    print("Panjang LMIS     :", len(result))
    print("Indeks elemen    :", indices)
    print("Mode             :", mode)
    print("================================")


def get_numbers():
    while True:
        try:
            raw = input(
                "\nMasukkan angka dipisahkan koma: "
            )

            numbers = [
                int(item.strip())
                for item in raw.split(",")
            ]

            if not numbers:
                raise ValueError

            return numbers

        except ValueError:
            print(
                "Input tidak valid! "
                "Gunakan angka bulat yang dipisahkan koma."
            )


def main():

    example = [4, 1, 13, 7, 0, 2, 8, 11, 3]

    while True:

        print("\n================================")
        print("   LMIS - TREE APPLICATION")
        print(" Largest Increasing Subsequence")
        print("================================")
        print("1. Gunakan contoh dari PPT")
        print("2. Masukkan data sendiri")
        print("3. Keluar")
        print("================================")

        choice = input("Pilih menu (1-3): ").strip()

        if choice == "3":
            print("\nProgram selesai. Terima kasih!")
            break

        elif choice in ("1", "2"):

            if choice == "1":
                numbers = example.copy()
                print("\nData contoh:", numbers)
            else:
                numbers = get_numbers()

            print("\nPilih jenis increasing:")
            print("1. Strictly Increasing")
            print("2. Non-decreasing")

            mode_choice = input("Pilihan (1-2): ").strip()

            if mode_choice == "1":
                mode = "strict"
            elif mode_choice == "2":
                mode = "non_decreasing"
            else:
                print("Pilihan tidak valid!")
                continue

            display_result(numbers, mode)

        else:
            print("Menu tidak tersedia!")


if __name__ == "__main__":
    main()
