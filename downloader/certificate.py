import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import pkcs12

def pkcs12_to_pem(data_b64):
  bundle_data = base64.b64decode(data_b64)
  bundle = pkcs12.load_key_and_certificates(bundle_data, None)

  # Server cert
  pem_data = bundle[1].public_bytes(
    encoding=serialization.Encoding.PEM,
  )

  # Private key
  pem_data += bundle[0].private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
  )

  # Intermediate certs
  for c in bundle[2]:
    pem_data += c.public_bytes(
    encoding=serialization.Encoding.PEM,
  )

  return pem_data
