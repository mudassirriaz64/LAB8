import csv
import re
from pathlib import Path


EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")


def is_valid_email(email: str) -> bool:
	return bool(EMAIL_PATTERN.fullmatch(email.strip()))


def safe_mark(value: str) -> int | None:
	try:
		return int(value)
	except (TypeError, ValueError):
		return None


def analyze_students(csv_path: Path) -> tuple[list[dict], list[dict], list[dict]]:
	low_marks = []
	invalid_emails = []
	processed_rows = []

	with csv_path.open("r", newline="", encoding="utf-8") as file:
		reader = csv.DictReader(file)
		for row in reader:
			name = (row.get("name") or "").strip()
			email = (row.get("email") or "").strip()
			mark = safe_mark((row.get("mark") or "").strip())

			student = {"name": name, "mark": mark, "email": email}
			processed_rows.append(student)

			if mark is not None and mark < 12:
				low_marks.append(student)

			if not is_valid_email(email):
				invalid_emails.append(student)

	return processed_rows, low_marks, invalid_emails


def write_report(report_path: Path, total: int, low_marks: list[dict], invalid_emails: list[dict]) -> None:
	lines = [
		"Student Support Office - Data Validation Report",
		"=" * 48,
		f"Total students processed: {total}",
		"",
		"Students with marks less than 12:",
	]

	if low_marks:
		for student in low_marks:
			lines.append(f"- {student['name']} (mark: {student['mark']})")
	else:
		lines.append("- None")

	lines.append("")
	lines.append("Students with invalid email format:")

	if invalid_emails:
		for student in invalid_emails:
			lines.append(f"- {student['name']} (email: {student['email']})")
	else:
		lines.append("- None")

	report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def print_results(total: int, low_marks: list[dict], invalid_emails: list[dict], report_path: Path) -> None:
	print("=== Student Data Check ===")
	print(f"Total students processed: {total}")

	print("\nStudents with marks less than 12:")
	if low_marks:
		for student in low_marks:
			print(f"- {student['name']} (mark: {student['mark']})")
	else:
		print("- None")

	print("\nStudents with invalid email format:")
	if invalid_emails:
		for student in invalid_emails:
			print(f"- {student['name']} (email: {student['email']})")
	else:
		print("- None")

	print(f"\nReport generated: {report_path}")


def main() -> None:
	csv_path = Path("students.csv")
	report_path = Path("report.txt")

	if not csv_path.exists():
		print(f"CSV file not found: {csv_path}")
		return

	processed, low_marks, invalid_emails = analyze_students(csv_path)
	write_report(report_path, len(processed), low_marks, invalid_emails)
	print_results(len(processed), low_marks, invalid_emails, report_path)


if __name__ == "__main__":
	main()
