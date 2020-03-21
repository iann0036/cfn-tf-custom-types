# Terraform::AzureRM::KeyVaultCertificate CertificatePolicy SecretProperties

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#contenttype" title="ContentType">ContentType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#contenttype" title="ContentType">ContentType</a>: <i>String</i>
</pre>

## Properties

#### ContentType

The Content-Type of the Certificate, such as `application/x-pkcs12` for a PFX or `application/x-pem-file` for a PEM. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

