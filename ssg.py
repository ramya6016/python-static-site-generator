import typer
from ssg.site import Site
def main(self,source="content",dest="dist"):
    config={'config':source,'dest':dest}
    Site_instance=Site(**config)
    Site_instance.build()
typer.run(main())




