import os
from lxml import objectify

def scan_folder(dir_path):
    nzb_dir = os.path.realpath(dir_path)
    nzbs = [f for f in os.listdir(nzb_dir) if f.endswith(".nzb")]
    for nzb in nzbs:
        yield os.path.join(nzb_dir, nzb)

class NzbTarget:
    groups = []
    segments = []

    def __init__(self, elem):
        self._elem = elem

    @property
    def attrib(self):
        return self._elem.attrib

    def __repr__(self):
        fmt_str = "<NzbTarget: {} groups, {} segments>"
        return fmt_str.format(len(self.groups),
                              len(self.segments))

class NzbFile(object):

    def __init__(self, nzb_path):
        self.nzb_path = os.path.realpath(nzb_path)
        self.files = []

        self.load()

    def load(self):
        tree = objectify.parse(self.nzb_path)
        root = tree.getroot()
        dtd_namespace = "".join(['{', root.nsmap[None], '}'])

        # TODO: extract <HEAD> data

        # extract files
        file_mask = dtd_namespace + "file"
        for f in root.findall(file_mask):
            target = NzbTarget(elem = f)
            groups, segments = f.getchildren()
            target.groups = [g for g in groups.getchildren()]
            target.segments = [s for s in segments.getchildren()]
            self.files.append( target )

    def __repr__(self):
        return os.path.basename(self.nzb_path)
