import os
import lxml
from glob import iglob

def nzb_scan(*directories):
    # helper utility taking vararg of directory paths to scan for NZB files
    for d in directories:
        prefix_path = os.path.realpath(d)
        glob_path = os.path.join(prefix_path, "*.nzb")
        # excluding 'yield from' for backwards compatibility
        for entry in iglob(glob_path):
            yield entry

class NzbTarget:
    """
    segmented file as described by NZB prior to reassembly
    """
    groups = []
    segments = []

    def __init__(self, el):
        self._elem = el

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
        tree = lxml.objectify.parse(self.nzb_path)
        root = tree.getroot()
        dtd_namespace = "".join(['{', root.nsmap[None], '}'])

        # TODO: extract <HEAD> data

        # extract files
        file_mask = dtd_namespace + "file"
        for f in root.findall(file_mask):
            target = NzbTarget(el = f)
            groups, segments = f.getchildren()
            target.groups = [g for g in groups.getchildren()]
            target.segments = [s for s in segments.getchildren()]
            self.files.append( target )


    def __repr__(self):

        TRUNCATE_AT_LENGTH = 20
        fmt_str = "<NzbFile: {} ({})>"
        basename = os.path.basename(self.nzb_path)
        title, _ = os.path.splitext(basename)

        if len(title) > TRUNCATE_AT_LENGTH:
            slice_index = TRUNCATE_AT_LENGTH - 3
            title = title[:slice_index] + '...'

        file_count = len(self.files)

        return fmt_str.format(title, file_count)
