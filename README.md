# gRPC tutorial from django-grpc-framework  
[gRPC Tutorial](https://djangogrpcframework.readthedocs.io/en/latest/tutorial/building_services.html)

For a model-backed service, you could also run the model proto generator.  
`python manage.py generateproto --model blog.models.Post --fields=id,title,content --file protos/blog_proto/post.proto
`  

Generate gRPC code from project root:  
`python -m grpc_tools.protoc --proto_path=./protos --python_out=./ --grpc_python_out=./ ./protos/blog_proto/post.proto
`  
