from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

class Keyvault:
  def __init__(self, name):
    self._uri = 'https://{}.vault.azure.net'.format(name)
    self.__kv_client = None

  @property
  def _kv_client(self):
    if self.__kv_client is None:
      self.__kv_client = SecretClient(
        vault_url=self._uri,
        credential=DefaultAzureCredential()
      )
    return self.__kv_client

  @property
  def _secret_list(self):
    return self._kv_client.list_properties_of_secrets()
  
  def _get_secret(self, name):
    secret = self._kv_client.get_secret
    return secret(name)

  @property
  def secrets(self):
    return map(lambda s: self._get_secret(s.name), self._secret_list)
