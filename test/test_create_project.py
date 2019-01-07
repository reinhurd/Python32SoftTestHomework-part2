from model.project import Project
import random
import string


def random_projectname(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_create_project(app):
    # assert app.session.is_logged_in_as('administrator')
    username = "administrator"
    password = "root"
    old_projects = app.soap.get_project_list(username, password)
    project = Project(name=random_projectname("project_", 4))
    app.project.create(project)
    new_projects = app.soap.get_project_list(username, password)
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
