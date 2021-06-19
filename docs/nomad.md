# Nomad Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/nomad**. The below arguments may be included as the key/value or JSON properties in the secret:

* `name` - (Required) The name of the header.
* `value` - (Required) The value of the header.

An example using the `headers` configuration block with repeated blocks and
headers: 
```hcl
provider "nomad" {
  headers {
    name = "Test-Header-1"
    value = "a"
  }
  headers {
    name = "Test-header-1"
    value = "b"
  }
  headers {
    name = "test-header-2"
    value = "c"
  }
}
```


## Supported Resources

* [TF::Nomad::AclPolicy](../resources/nomad/TF-Nomad-AclPolicy/docs/README.md)
* [TF::Nomad::AclToken](../resources/nomad/TF-Nomad-AclToken/docs/README.md)
* [TF::Nomad::ExternalVolume](../resources/nomad/TF-Nomad-ExternalVolume/docs/README.md)
* [TF::Nomad::Job](../resources/nomad/TF-Nomad-Job/docs/README.md)
* [TF::Nomad::Namespace](../resources/nomad/TF-Nomad-Namespace/docs/README.md)
* [TF::Nomad::QuotaSpecification](../resources/nomad/TF-Nomad-QuotaSpecification/docs/README.md)
* [TF::Nomad::SchedulerConfig](../resources/nomad/TF-Nomad-SchedulerConfig/docs/README.md)
* [TF::Nomad::SentinelPolicy](../resources/nomad/TF-Nomad-SentinelPolicy/docs/README.md)
* [TF::Nomad::Volume](../resources/nomad/TF-Nomad-Volume/docs/README.md)