# DNS Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/dns**. The below arguments may be included as the key/value or JSON properties in the secret:

* `server` - (Required) The hostname or IP address of the DNS server to send updates to.
* `port` - (Optional) The target UDP port on the server where updates are sent to. Defaults to `53`.
* `transport` - (Optional) Transport to use for DNS queries. Valid values are `udp`, `udp4`, `udp6`, `tcp`, `tcp4`, or `tcp6`. Any UDP transport will retry automatically with the equivalent TCP transport in the event of a truncated response. Defaults to `udp`.
* `timeout` - (Optional) Timeout for DNS queries. Valid values are durations expressed as `500ms`, etc. or a plain number which is treated as whole seconds.
* `retries` - (Optional) How many times to retry on connection timeout. Defaults to `3`.
* `key_name` - (Optional) The name of the TSIG key used to sign the DNS update messages.
* `key_algorithm` - (Optional; Required if `key_name` is set) When using TSIG authentication, the algorithm to use for HMAC. Valid values are `hmac-md5`, `hmac-sha1`, `hmac-sha256` or `hmac-sha512`.
* `key_secret` - (Optional; Required if `key_name` is set)
    A Base64-encoded string containing the shared secret to be used for TSIG.
* `gssapi` - (Optional) A `gssapi` block (documented below). Only one `gssapi` block may be in the configuration. Conflicts with use of `key_name`, `key_algorithm` and `key_secret`.


* `realm` - (Required) The Kerberos realm or Active Directory domain.
* `username` - (Optional) The name of the user to authenticate as. If not set the current user session will be used.
* `password` - (Optional; This or `keytab` is required if `username` is set) The matching password for `username`.
* `keytab` - (Optional; This or `password` is required if `username` is set, not supported on Windows) The path to a keytab file containing a key for `username`.


## Supported Resources

* [TF::DNS::ARecordSet](../resources/dns/TF-DNS-ARecordSet/docs/README.md)
* [TF::DNS::AaaaRecordSet](../resources/dns/TF-DNS-AaaaRecordSet/docs/README.md)
* [TF::DNS::CnameRecord](../resources/dns/TF-DNS-CnameRecord/docs/README.md)
* [TF::DNS::MxRecordSet](../resources/dns/TF-DNS-MxRecordSet/docs/README.md)
* [TF::DNS::NsRecordSet](../resources/dns/TF-DNS-NsRecordSet/docs/README.md)
* [TF::DNS::PtrRecord](../resources/dns/TF-DNS-PtrRecord/docs/README.md)
* [TF::DNS::SrvRecordSet](../resources/dns/TF-DNS-SrvRecordSet/docs/README.md)
* [TF::DNS::TxtRecordSet](../resources/dns/TF-DNS-TxtRecordSet/docs/README.md)