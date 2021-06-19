# NS1 Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/ns1**. The below arguments may be included as the key/value or JSON properties in the secret:

* `apikey` - (Required) NS1 API token.
* `version` - (Optional, but recommended if you don't like surprises) From
  output of `terraform init`.
* `endpoint` - (Optional) NS1 API endpoint. For managed clients, this normally
  should not be set.
* `ignore_ssl` - (Optional) This normally does not need to be set.
* `enable_ddi` - (Optional) This sets the permission schema to a DDI-compatible schema. 
Users of the managed SaaS product should not need to set this.
Users of DDI should set this to true if managing teams, users, or API keys through this provider.
* `rate_limit_parallelism` - (Optional) Integer for alternative rate limit and parallelism strategy (Terraform default value is 10).
    NS1 uses a token-based method for rate limiting API requests. Details of which can be found here: https://help.ns1.com/hc/en-us/articles/360020250573-About-API-rate-limiting.
    
    By default, the NS1 provider uses the "sleep" strategy of the underlying [NS1 Go SDK](https://github.com/ns1/ns1-go) for handling the NS1 API rate limit:
    an operation waits after every API request for a time equal to the rate limit period of that request type divided by the corresponding tokens renaming.
    
    Furthermore, the default behaviour of Terraform uses ten concurrent operations.
    This means that the provider will burst through available request tokens, gradually slowing until it reaches an equilibrium point where the ten operations wait long enough between requests to replenish ten tokens.
    However, if there are other concurrent uses of the API this can lead to the tokens being entirely depleted when a Terraform operation makes a new request.
    This results in a 429 response which will cause the entire Terraform process to fail.
    
    If you encounter this scenario, or believe you are likely to, then you can set the rate_limit_parallelism to enable an alternative rate limiting strategy.
    Here the Terraform operations will burst through all available tokens until they reach a point where the remaining limit is less, or equal, to the value set;
    after this point an operation will wait for the time it would take to replenish an equal number of tokens.
    
    Setting this to a value of 60 represents a good balance between optimising for performance and reducing the risk of a 429 response.
    If you still encounter issues then you can increase this value: we would recommend you do so in increments of 20.
    
    Note: We recommend that you do not set the -parallelism=n option when you run terraform apply so that it is uses the default number of ten.
    An increase in this value will lead to an increased risk of encountering a 429 response.


## Supported Resources

* [TF::NS1::Apikey](../resources/ns1/TF-NS1-Apikey/docs/README.md)
* [TF::NS1::Datafeed](../resources/ns1/TF-NS1-Datafeed/docs/README.md)
* [TF::NS1::Datasource](../resources/ns1/TF-NS1-Datasource/docs/README.md)
* [TF::NS1::Monitoringjob](../resources/ns1/TF-NS1-Monitoringjob/docs/README.md)
* [TF::NS1::Notifylist](../resources/ns1/TF-NS1-Notifylist/docs/README.md)
* [TF::NS1::Record](../resources/ns1/TF-NS1-Record/docs/README.md)
* [TF::NS1::Team](../resources/ns1/TF-NS1-Team/docs/README.md)
* [TF::NS1::User](../resources/ns1/TF-NS1-User/docs/README.md)
* [TF::NS1::Zone](../resources/ns1/TF-NS1-Zone/docs/README.md)