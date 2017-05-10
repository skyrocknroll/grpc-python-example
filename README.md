# grpc-python-example
grpc python example

### Install grpc python dependencies
```bash
python -m pip install --upgrade pip
pip install grpcio
python -m pip install grpcio-tools
```
### generate stubs from proto files
```bash
cd generated
python -m grpc_tools.protoc -I ../protobuf/ --python_out=. --grpc_python_out=. ../protobuf/Hello.proto
```
