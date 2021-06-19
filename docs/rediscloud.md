# Redis Enterprise Cloud Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/rediscloud**. The below arguments may be included as the key/value or JSON properties in the secret:

* `url` - (Optional) This is the URL of Redis Enterprise Cloud and will default to `https://api.redislabs.com/v1`. 

* `api_key` - (Optional) This is the Redis Enterprise Cloud API key.

* `secret_key` - (Optional) This is the Redis Enterprise Cloud API secret key.


## Supported Resources

* [TF::RedisCloud::CloudAccount](../resources/rediscloud/TF-RedisCloud-CloudAccount/docs/README.md)
* [TF::RedisCloud::SubscriptionPeering](../resources/rediscloud/TF-RedisCloud-SubscriptionPeering/docs/README.md)
* [TF::RedisCloud::Subscription](../resources/rediscloud/TF-RedisCloud-Subscription/docs/README.md)