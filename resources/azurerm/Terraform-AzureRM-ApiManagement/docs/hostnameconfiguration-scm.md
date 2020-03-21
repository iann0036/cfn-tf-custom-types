# Terraform::AzureRM::ApiManagement HostnameConfiguration Scm

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#certificate" title="Certificate">Certificate</a>" : <i>String</i>,
    "<a href="#certificatepassword" title="CertificatePassword">CertificatePassword</a>" : <i>String</i>,
    "<a href="#hostname" title="HostName">HostName</a>" : <i>String</i>,
    "<a href="#keyvaultid" title="KeyVaultId">KeyVaultId</a>" : <i>String</i>,
    "<a href="#negotiateclientcertificate" title="NegotiateClientCertificate">NegotiateClientCertificate</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#certificate" title="Certificate">Certificate</a>: <i>String</i>
<a href="#certificatepassword" title="CertificatePassword">CertificatePassword</a>: <i>String</i>
<a href="#hostname" title="HostName">HostName</a>: <i>String</i>
<a href="#keyvaultid" title="KeyVaultId">KeyVaultId</a>: <i>String</i>
<a href="#negotiateclientcertificate" title="NegotiateClientCertificate">NegotiateClientCertificate</a>: <i>Boolean</i>
</pre>

## Properties

#### Certificate

The Base64 Encoded Certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificatePassword

The password associated with the certificate provided above.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostName

The Hostname to use for the Management API.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyVaultId

The ID of the Key Vault Secret containing the SSL Certificate, which must be should be of the type `application/x-pkcs12`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NegotiateClientCertificate

Should Client Certificate Negotiation be enabled for this Hostname? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

