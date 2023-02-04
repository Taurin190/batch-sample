# Event Driven Sample

# 参考記事
VPCとSubnet。
https://qiita.com/okubot55/items/b18a5dd5166f1ec2696c

API GatewayとLambdaのサンプル。
https://dev.classmethod.jp/articles/build-httapi-with-api-gateway-by-cloud-formation/

API Gatewayでできることについて
https://aws.amazon.com/jp/api-gateway/features/#:~:text=Amazon%20API%20Gateway%20%E3%81%AF%E3%80%81%E3%83%87%E3%83%99%E3%83%AD%E3%83%83%E3%83%91%E3%83%BC,%E5%BE%93%E9%87%8F%E5%88%B6%E3%81%AE%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%81%A7%E3%81%99%E3%80%82


ELBtとAPI Gatewayの比較
https://www.l7defense.com/cyber-security/api-gateway-vs-load-balancer/
- 少ないリクエストであればAPI Gatewayの方がコストメリットはある
- リクエストが一定して多くなってくるとELBの方がコスト的には安くなる
- 認証など使用する場合にはAPI Gatewayを使うことになる

SQS作成のサンプル
https://www.yokoyan.net/entry/2020/01/21/180000

localでlambdaの実行
https://zenn.dev/denham/scraps/0169c6fedbae6b

Go言語でSQSのメッセージを取得する
https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/sqs-example-receive-message.html#sqs-example-receive-mesage