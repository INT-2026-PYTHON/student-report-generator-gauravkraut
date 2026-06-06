"""gradebook.reports — build a printable report from grade records."""

# TODO: use a RELATIVE import to pull from the sibling stats module.
# from .stats import average_per_student, subjects_offered, top_scorer, passing_students


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    # TODO: implement
    pass
from .stats import average_per_student, subjects_offered, top_scorer, passing_students
def format_report(records):
    report =""
    report+="Total Records: "+str(len(records))+"\n"
    report+="Subjects: "+str(subjects_offered(records))+"\n"
    report+="Average Scores:\n"
    avg = average_per_student(records)
    for name in avg:
        report+=name+ " : "+str(avg[name])+"\n"
    top = top_scorer(records)
    report += "Top Scorer: " + str(top) + "\n"
    report += "Passing Students: "
    report += str(passing_students(records))
    return report