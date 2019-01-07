from model.project import Project
import random
import string


def random_projectname(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_del_some_project(app):
    assert app.session.is_logged_in_as('administrator')
    if len(app.project.get_project_list()) == 0:
        app.project.create(Project(name=random_projectname("project_", 4)))
    old_project = app.project.get_project_list()
    project = random.choice(old_project)
    app.project.del_project_by_id(project.id)
    new_project = app.project.get_project_list()
    assert len(old_project) - 1 == len(new_project)
    old_project.remove(project)
    assert old_project == new_project
