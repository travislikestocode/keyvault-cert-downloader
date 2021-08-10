class LocalSecret:
  def __init__(self, filename, version):
    self._filename = filename
    self._version = version

  @property
  def filename(self):
    return self._filename
  
  @property
  def name(self):
    return self._filename.split('.')[0]
  
  @property
  def version(self):
    return self._version
