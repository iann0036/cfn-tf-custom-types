# Fastly Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/fastly**. The below arguments may be included as the key/value or JSON properties in the secret:

* `api_key` - (Optional) This is the API key. It must be provided, but
  it can also be sourced from the `FASTLY_API_KEY` environment variable

* `base_url` - (Optional) This is the API server hostname. It is required
  if using a private instance of the API and otherwise defaults to the
  public Fastly production service. It can also be sourced from the
  `FASTLY_API_URL` environment variable


## Supported Resources

* [TF::Fastly::ServiceAclEntriesV1](../resources/fastly/TF-Fastly-ServiceAclEntriesV1/docs/README.md)
* [TF::Fastly::ServiceCompute](../resources/fastly/TF-Fastly-ServiceCompute/docs/README.md)
* [TF::Fastly::ServiceDictionaryItemsV1](../resources/fastly/TF-Fastly-ServiceDictionaryItemsV1/docs/README.md)
* [TF::Fastly::ServiceDynamicSnippetContentV1](../resources/fastly/TF-Fastly-ServiceDynamicSnippetContentV1/docs/README.md)
* [TF::Fastly::ServiceV1](../resources/fastly/TF-Fastly-ServiceV1/docs/README.md)
* [TF::Fastly::ServiceWafConfiguration](../resources/fastly/TF-Fastly-ServiceWafConfiguration/docs/README.md)
* [TF::Fastly::TlsActivation](../resources/fastly/TF-Fastly-TlsActivation/docs/README.md)
* [TF::Fastly::TlsCertificate](../resources/fastly/TF-Fastly-TlsCertificate/docs/README.md)
* [TF::Fastly::TlsPlatformCertificate](../resources/fastly/TF-Fastly-TlsPlatformCertificate/docs/README.md)
* [TF::Fastly::TlsPrivateKey](../resources/fastly/TF-Fastly-TlsPrivateKey/docs/README.md)
* [TF::Fastly::TlsSubscriptionValidation](../resources/fastly/TF-Fastly-TlsSubscriptionValidation/docs/README.md)
* [TF::Fastly::TlsSubscription](../resources/fastly/TF-Fastly-TlsSubscription/docs/README.md)
* [TF::Fastly::UserV1](../resources/fastly/TF-Fastly-UserV1/docs/README.md)