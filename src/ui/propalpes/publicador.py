import pulsar
import avro.schema
from avro.io import DatumWriter, BinaryEncoder
import io
client = pulsar.Client('pulsar://localhost:6650')
producer = client.create_producer('topic-comando-crear-compania')


# Define Avro schema
avro_schema_str = '''
{
    "type": "record",
    "name": "ComandoCrearCompania",
    "fields": [
        {
            "name": "data",
            "type": [
                "null",
                {
                    "type": "record",
                    "name": "ComandoCrearCompaniaPayload",
                    "fields": [
                        {
                            "name": "nombre",
                            "type": [
                                "null",
                                "string"
                            ]
                        },
                        {
                            "name": "email",
                            "type": [
                                "null",
                                "string"
                            ]
                        },
                        {
                            "name": "identificacion",
                            "type": [
                                "null",
                                "string"
                            ]
                        },
                        {
                            "name": "fecha_creacion",
                            "type": [
                                "null",
                                "string"
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}
'''
avro_schema = avro.schema.parse(avro_schema_str)

#for i in range(1):
print(f'Hola-Pulsar')
    #producer.send(('Hola-Pulsar-%d' % i).encode('utf-8'))
payload = {
  "data": {
    "nombre": "Nombre de la compañía6",
    "email": "correo@compania.com6",
    "identificacion": "identificador_de_la_compania6",
    "fecha_creacion": "1709515009893"
  }
}
bytes_writer = io.BytesIO()
encoder = BinaryEncoder(bytes_writer)
writer = DatumWriter(avro_schema)
writer.write(payload, encoder)
serialized_message = bytes_writer.getvalue()

producer.send(serialized_message)

client.close()