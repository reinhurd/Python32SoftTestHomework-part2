from model.project import Project
import random
import string


def random_projectname(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_create_project(app):
    assert app.session.is_logged_in_as('administrator')
    old_project = app.project.get_project_list()
    project = Project(name=random_projectname("project_", 4))
    app.project.create(project)
    new_project = app.project.get_project_list()
    assert len(old_project) + 1 == len(new_project)
    old_project.append(project)
    assert sorted(old_project, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)
