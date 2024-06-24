import random
import subprocess


def run(nums: list[int]) -> int:
    return sum(nums)


cases_amount: int = 1000

min_inp_size: int = 1
max_inp_size: int = 10
min_inp: int = -100
max_inp: int = 100

filepath = f"data/tests/q1.tst"

print("Started generating cases...")

with open(filepath, "w") as f:
    f.write(f"[Cases]\n{cases_amount}")


with open(filepath, "a") as f:
    for i in range(cases_amount):
        inp_amount: int = random.randint(min_inp_size, max_inp_size)

        inp: list[int] = [random.randint(min_inp, max_inp) for _ in range(inp_amount)]

        inp_str: str = "[" + ", ".join(map(str, inp)) + "]"

        output: str = str(run(inp))

        f.write(f"\n|Case|\n{inp_amount + 1}\n{len(output.split("\n"))}")
        f.write(f"\n[Input]\n{inp_str}")
        f.write(f"\n[Output]\n{output}")

        print(
            f"Generated case {i+1}/{cases_amount} ({(i + 1) / cases_amount * 100:.2f}%)"
        )
    print("Finished generating cases.")
