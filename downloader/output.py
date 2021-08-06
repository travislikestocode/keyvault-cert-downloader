from os import listdir, path
from os.path import isfile, join
from config import config
import certificate

class Output:
  def __init__(self, dir):
    self._dir = dir

  @classmethod
  def _make_filename(cls, cert_name, ext):
    return cert_name + ext

  @property
  def _file_names(self):
    return [f for f in listdir(self._dir) if isfile(join(self._dir, f))]

  def _output_file(self, secret_name, version, value_pkcs12):
    _file_name = self._make_filename(secret_name, config['output']['ext'])
    _fullpath = path.join(self._dir, _file_name)
    _value_pem = certificate.pkcs12_to_pem(value_pkcs12)

    with open(_fullpath, 'wb') as writer:
      writer.write(_value_pem)

  @property
  def secrets(self):
    return map(lambda s: s.split('.')[0], self._file_names)

  def sync(self, kv_secrets):
    for s in kv_secrets:
      self._output_file(s.name, s.properties.version, s.value)
