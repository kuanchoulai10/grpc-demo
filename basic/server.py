from concurrent import futures
import grpc
import prediction_pb2
import prediction_pb2_grpc

class ModelServiceServicer(prediction_pb2_grpc.ModelServiceServicer):
    def Predict(self, request, context):
        print(f"Received features: {request.features}")
        # 模擬預測分數
        score = sum(request.features) / len(request.features)
        return prediction_pb2.PredictResponse(score=score)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    prediction_pb2_grpc.add_ModelServiceServicer_to_server(ModelServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC Server started at :50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
