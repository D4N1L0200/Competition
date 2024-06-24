import sys
import subprocess


def parse_tests(question: str) -> tuple[int, list[tuple[str, str]]]:
    filepath: str = f"data/tests/{question}.txt"
    with open(filepath, "r") as file:
        content: list[str] = file.read().split("\n")

    cases: list[tuple[str, str]] = []

    if content.pop(0) == "[Cases]":
        total_cases: int = int(content.pop(0))
    else:
        raise ValueError("Invalid file format.")

    for _ in range(total_cases):
        if content.pop(0) == "[Case]":
            input_amount: int = int(content.pop(0))
            output_amount: int = int(content.pop(0))
        else:
            raise ValueError("Invalid file format.")

        if content.pop(0) != "[Input]":
            raise ValueError("Invalid file format.")
        inputs: str = "\n".join(content[:input_amount])
        content = content[input_amount:]

        if content.pop(0) != "[Output]":
            raise ValueError("Invalid file format.")
        outputs: str = "\n".join(content[:output_amount])
        content = content[output_amount:]

        cases.append((inputs, outputs))

    return total_cases, cases


def run_test(input_data: str, expected_output: str) -> tuple[bool, str]:
    from q1 import addition

    out = str(addition(input_data))
    return out == expected_output, out

questions = ["q1", "q2"]

def main() -> None:
    if len(sys.argv) == 2:
        question = sys.argv[1]
    else:
        print("Usage: test.py <case_name>")
        return
    
    if question not in questions:
        print("Invalid question.")
        return
    
    print("Parsing tests...")
    total_cases, cases = parse_tests(question)
    print(f"Parsed {total_cases} tests")

    passed_cases: int = 0

    for i, (input_data, expected_output) in enumerate(cases):
        passed, output = run_test(input_data, expected_output)

        if passed:
            passed_cases += 1
            print(f"({i+1}) passed.")
        else:
            print(f"({i+1}) failed.")
            print(f"Expected: '{expected_output}', Got: '{output}'")

    percent: float = passed_cases / total_cases * 100
    print(f"\n{passed_cases}/{total_cases} ({percent:.2f}%) test cases passed.")
    print(
        f"{total_cases - passed_cases}/{total_cases} ({100 - percent:.2f}%) test cases failed."
    )


if __name__ == "__main__":
    main()
