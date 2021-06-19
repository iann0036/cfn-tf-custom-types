# Venafi Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/venafi**. The below arguments may be included as the key/value or JSON properties in the secret:

* `zone` - (Required, string) Application Name and Issuing 
Template API Alias (e.g. "Business App\Enterprise CIT") for Venafi Cloud or policy folder for Venafi Platform.

* `url` - (Optional, string) Venafi URL (e.g. "https://tpp.venafi.example").

* `access_token` - (Optional, string) authentication token for the 'hashicorp-terraform-by-venafi' API Application (applies only to Venafi Platform).

* `api_key` - (Optional, string) REST API key for authentication (applies only to Venafi Cloud).

* `tpp_username` [DEPRECATED] - (Optional, string) WebSDK account username for authentication (applies only to Venafi Platform).

* `tpp_password` [DEPRECATED] - (Optional, string) WebSDK account password for authentication (applies only to Venafi Platform).

* `trust_bundle` - (Optional, string) PEM trust bundle for Venafi Platform server certificate (e.g. "${file("bundle.pem")}" ).

* `dev_mode` - (Optional, boolean) When "true" will test the provider without connecting to Venafi Platform or Venafi Cloud.


## Supported Resources

* [TF::Venafi::Certificate](../resources/venafi/TF-Venafi-Certificate/docs/README.md)
* [TF::Venafi::Policy](../resources/venafi/TF-Venafi-Policy/docs/README.md)