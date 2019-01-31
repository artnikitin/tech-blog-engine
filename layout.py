from flask import render_template

class Layout:
    def __init__(self, image_url, heading, subheading, heading_class,
                 subheading_class, html, box_id):
        self.image_url = image_url
        self.heading = heading
        self.subheading = subheading
        self.heading_class = heading_class
        self.subheading_class = subheading_class
        self.html = html
        self.box_id = box_id

    def render(self):
        return render_template("{}".format(self.html), image_url=self.image_url, heading=self.heading,
                        subheading=self.subheading, heading_class=self.heading_class,
                        subheading_class=self.subheading_class, box_id=self.box_id)