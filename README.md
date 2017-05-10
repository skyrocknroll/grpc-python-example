# grpc-python-example
grpc python example

```bash
cd generated
python -m grpc_tools.protoc -I ../protobuf/ --python_out=. --grpc_python_out=. ../protobuf/Hello.proto
```