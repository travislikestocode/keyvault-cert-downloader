from os import listdir, path
from os.path import isfile, join

class Files:
  def __init__(self, dir):
    self.dir = dir

  @property
  def file_names(self):
    return [f for f in listdir(
      self.dir) if isfile(
        join(self.dir, f)
      )]

  @classmethod
  def make_filename(cls, cert_name, ext):
    return cert_name + ext

  def output_file(self, filename, value):
    _fullpath = path.join(self.dir, filename)

    with open(_fullpath, 'w') as writer:
      writer.write(value)
