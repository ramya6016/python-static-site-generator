import typer
from ssg.site import Site
def main(self,source="content",dest="dist"):
    config={'config':source,'dest':dest}
    Site(**config).build()
typer.run(main)




