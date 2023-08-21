import pytest
import subprocess


def main():
    subprocess.run(["python", "tests/ui.py"])


if __name__ == "__main__":
    main()
