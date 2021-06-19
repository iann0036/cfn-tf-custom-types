# Amixr Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/amixr**. The below arguments may be included as the key/value or JSON properties in the secret:

* `token` - (Required) The authorization token. See [API Documentation](https://api-docs.amixr.io/#authentication) for more information.


## Supported Resources

* [TF::Amixr::Escalation](../resources/amixr/TF-Amixr-Escalation/docs/README.md)
* [TF::Amixr::Integration](../resources/amixr/TF-Amixr-Integration/docs/README.md)
* [TF::Amixr::OnCallShift](../resources/amixr/TF-Amixr-OnCallShift/docs/README.md)
* [TF::Amixr::Route](../resources/amixr/TF-Amixr-Route/docs/README.md)
* [TF::Amixr::Schedule](../resources/amixr/TF-Amixr-Schedule/docs/README.md)