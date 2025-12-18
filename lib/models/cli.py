import click
from lib.db.database import SessionLocal
from lib.db.models import Student, Course  # Add Enrollment if needed

@click.group()
def cli():
    """Student Course Registration System CLI"""
    pass

# ---------------- Students ----------------

@cli.group()
def students():
    """Manage students (CRUD)"""
    pass

@students.command()
@click.option('--name', prompt=True)
@click.option('--email', prompt=True)
def create(name, email):
    session = SessionLocal()
    student = Student.create(session, name=name, email=email)
    click.echo(f"Created student: {student}")
    session.close()

@students.command('list')
def list_students():
    session = SessionLocal()
    for s in Student.get_all(session):
        click.echo(s)
    session.close()

@students.command()
@click.option('--id', type=int, prompt=True)
@click.option('--name', default=None)
@click.option('--email', default=None)
def update(id, name, email):
    session = SessionLocal()
    student = Student.get(session, id)
    if not student:l
        click.echo("Student not found")
        session.close()
        return
    fields = {}
    if name:
        fields['name'] = name
    if email:
        fields['email'] = email
    student.update(session, **fields)
    click.echo(f"Updated student: {student}")
    session.close()

@students.command()
@click.option('--id', type=int, prompt=True)
def delete(id):
    session = SessionLocal()
    student = Student.get(session, id)
    if not student:
        click.echo("Student not found")
        session.close()
        return
    student.delete(session)
    click.echo(f"Deleted student: {student}")
    session.close()

# ---------------- Courses ----------------

@cli.group()
def courses():
    """Manage courses (CRUD)"""
    pass

@courses.command()
@click.option('--code', prompt=True)
@click.option('--title', prompt=True)
@click.option('--credits', type=int, prompt=True)
def create(code, title, credits):
    session = SessionLocal()
    course = Course.create(session, code=code, title=title, credits=credits)
    click.echo(f"Created course: {course}")
    session.close()

@courses.command('list')
def list_courses():
    session = SessionLocal()
    for c in Course.get_all(session):
        click.echo(c)
    session.close()

@courses.command()
@click.option('--id', type=int, prompt=True)
@click.option('--code', default=None)
@click.option('--title', default=None)
@click.option('--credits', type=int, default=None)
def update(id, code, title, credits):
    session = SessionLocal()
    course = Course.get(session, id)
    if not course:
        click.echo("Course not found")
        session.close()
        return
    fields = {}
    if code:
        fields['code'] = code
    if title:
        fields['title'] = title
    if credits is not None:
        fields['credits'] = credits
    course.update(session, **fields)
    click.echo(f"Updated course: {course}")
    session.close()

@courses.command()
@click.option('--id', type=int, prompt=True)
def delete(id):
    session = SessionLocal()
    course = Course.get(session, id)
    if not course:
        click.echo("Course not found")
        session.close()
        return
    course.delete(session)
    click.echo(f"Deleted course: {course}")
    session.close()

# ---------------- Info Command ----------------

@cli.command()
def info():
    """Show information about available commands"""
    click.echo("Available commands:")
    click.echo("  students      Manage students (CRUD)")
    click.echo("  courses       Manage courses (CRUD)")
    click.echo("  enrollments   Manage enrollments (CRUD)")

# ---------------- Main ----------------

if __name__ == "__main__":
    cli()
