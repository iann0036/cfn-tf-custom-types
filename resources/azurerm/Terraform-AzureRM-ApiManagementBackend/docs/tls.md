# Terraform::AzureRM::ApiManagementBackend Tls

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#validatecertificatechain" title="ValidateCertificateChain">ValidateCertificateChain</a>" : <i>Boolean</i>,
    "<a href="#validatecertificatename" title="ValidateCertificateName">ValidateCertificateName</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#validatecertificatechain" title="ValidateCertificateChain">ValidateCertificateChain</a>: <i>Boolean</i>
<a href="#validatecertificatename" title="ValidateCertificateName">ValidateCertificateName</a>: <i>Boolean</i>
</pre>

## Properties

#### ValidateCertificateChain

Flag indicating whether SSL certificate chain validation should be done when using self-signed certificates for the backend host.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidateCertificateName

Flag indicating whether SSL certificate name validation should be done when using self-signed certificates for the backend host.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

