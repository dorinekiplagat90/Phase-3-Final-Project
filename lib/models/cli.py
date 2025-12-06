import click
from commands.students import students
from commands.courses import courses
from commands.enrollments import enrollments

@click.group()
def cli():
    """Student Course Registration System CLI"""
    pass

cli.add_command(students)
cli.add_command(courses)
cli.add_command(enrollments)

if __name__ == "__main__":
    cli()
