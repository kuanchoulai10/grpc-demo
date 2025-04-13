import grpc
import prediction_pb2
import prediction_pb2_grpc

def run():
    # 建立 gRPC channel
    channel = grpc.insecure_channel('localhost:50051')

    # 建立 stub（代理 client）
    stub = prediction_pb2_grpc.ModelServiceStub(channel)

    # 準備 request
    request = prediction_pb2.PredictRequest(
        user_id="kc",
        features=[1.0, 2.0, 3.0, 4.0]
    )

    # 呼叫 Predict 方法
    response = stub.Predict(request)
    print(f"預測分數: {response.score}")

if __name__ == '__main__':
    run()
