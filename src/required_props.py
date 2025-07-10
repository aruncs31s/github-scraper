# To Store required Props 
class rProps:
    def __init__(self):
        self.title = ""
        self.description = ""
        self.main = dict({
            "id": 1,  
            "content": "", # this will be the full description
            "imgCard": "",
            "imgMain": "",
            "imgAlt": ""
        })
        self.tabs ="""
        - id: "tabs-with-card-item-1"
          dataTab: "#tabs-with-card-1"
          title: "Description"
        - id: "tabs-with-card-item-2"
          dataTab: "#tabs-with-card-2"
          title: "Specifications"
        - id: "tabs-with-card-item-3"
          dataTab: "#tabs-with-card-3"
          title: "Blueprints"
        """
        self.longDescription = {
            "title": "",
            "subTitle": "",
            "btnTitle": "Contact sales to learn more",
            "btnURL": "#"
        }
        self.descriptionList = []
        self.specificationsLeft = []
        self.tableData = []
        self.blueprints = {
            "first": "",
            "second": ""
        }
    def check_all_filled(self):
        if not self.title or not self.description or not self.main['content'] or not self.main['imgCard'] or not self.main['imgMain'] or not self.main['imgAlt']:
            return False
        if not self.longDescription['title'] or not self.longDescription['subTitle']:
            return False
        if not self.descriptionList or not self.specificationsLeft or not self.tableData:
            return False
        if not self.blueprints['first'] or not self.blueprints['second']:
            return False
        return True