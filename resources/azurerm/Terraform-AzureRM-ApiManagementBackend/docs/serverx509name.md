# Terraform::AzureRM::ApiManagementBackend ServerX509Name

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#issuercertificatethumbprint" title="IssuerCertificateThumbprint">IssuerCertificateThumbprint</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#issuercertificatethumbprint" title="IssuerCertificateThumbprint">IssuerCertificateThumbprint</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### IssuerCertificateThumbprint

The thumbprint for the issuer of the certificate.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The common name of the certificate.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

