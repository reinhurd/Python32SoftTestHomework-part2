from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            wd.get("http://localhost/mantisbt-1.2.20/manage_proj_page.php")

    def create(self, group):
        wd = self.app.wd
        self.open_project_page()
        # init group creation
        wd.find_element_by_css_selector('input[value="Create New Project"]').click()
        # fill group form
        self.enter_text(group)
        # submit group creation
        wd.find_element_by_css_selector('input[value="Add Project"]').click()
        #self.return_to_groups_page()


    def enter_text(self, project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)

    def get_project_list(self):
        wd = self.app.wd
        self.open_project_page()
        self.project_cache = []
        for element in wd.find_elements_by_xpath("//td/a[contains(@href,'manage_proj_edit_page.php?project_id=')]"):
            text = element.text
            id = element.get_attribute("href").replace(
                'http://localhost/mantisbt-1.2.20/manage_proj_edit_page.php?project_id=',
                ''
            )
            self.project_cache.append(Project(name=text, id=id))
        return list(self.project_cache)


    def del_project_by_id(self, id):
        wd = self.app.wd
        self.open_project_page()
        self.enter_to_project_page_by_id(id)
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()
        ##On version 1.2.20 need click on another button to proceed
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()
        self.project_cache = None


    def enter_to_project_page_by_id(self, id):
        wd = self.app.wd
        wd.get(self.app.baseurl+'manage_proj_edit_page.php?project_id='+id)


    ## Old code from adressbook tests
    #
    # def del_first_group(self):
    #     self.del_group_by_index(0)
    #     self.group_cache = None
    #
    # def select_group_by_index(self, index):
    #     wd = self.app.wd
    #     wd.find_elements_by_name("selected[]")[index].click()
    #
    # def select_group_by_id(self, id):
    #     wd = self.app.wd
    #     wd.find_element_by_css_selector("input[value='%s']" % id).click()
    #
    # def del_group_by_index(self, index):
    #     wd = self.app.wd
    #     self.open_group_page()
    #     self.select_group_by_index(index)
    #     wd.find_element_by_name("delete").click()
    #     self.return_to_groups_page()
    #     self.group_cache = None
    #
    # def del_group_by_id(self, id):
    #     wd = self.app.wd
    #     self.open_group_page()
    #     self.select_group_by_id(id)
    #     wd.find_element_by_name("delete").click()
    #     self.return_to_groups_page()
    #     self.group_cache = None
    #
    # def mod_first_group(self, group):
    #     self.mod_group_by_index(0, group)
    #     self.group_cache = None
    #
    # def mod_group_by_index(self, index, group):
    #     wd = self.app.wd
    #     self.open_group_page()
    #     self.select_group_by_index(index)
    #     wd.find_element_by_name("edit").click()
    #     self.enter_text(group)
    #     wd.find_element_by_name("update").click()
    #     self.return_to_groups_page()
    #     self.group_cache = None
    #
    # def mod_group_by_id(self, id, group):
    #     wd = self.app.wd
    #     self.open_group_page()
    #     self.select_group_by_id(id)
    #     wd.find_element_by_name("edit").click()
    #     self.enter_text(group)
    #     wd.find_element_by_name("update").click()
    #     self.return_to_groups_page()
    #     self.group_cache = None
    #
    # def count(self):
    #     wd = self.app.wd
    #     self.open_group_page()
    #     return len(wd.find_elements_by_name("selected[]"))
    #
    # group_cache = None

