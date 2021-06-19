# TF::AzureRM::ApiManagement CertificateDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#certificatepassword" title="CertificatePassword">CertificatePassword</a>" : <i>String</i>,
    "<a href="#encodedcertificate" title="EncodedCertificate">EncodedCertificate</a>" : <i>String</i>,
    "<a href="#storename" title="StoreName">StoreName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#certificatepassword" title="CertificatePassword">CertificatePassword</a>: <i>String</i>
<a href="#encodedcertificate" title="EncodedCertificate">EncodedCertificate</a>: <i>String</i>
<a href="#storename" title="StoreName">StoreName</a>: <i>String</i>
</pre>

## Properties

#### CertificatePassword

The password for the certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncodedCertificate

The Base64 Encoded PFX or Base64 Encoded X.509 Certificate.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StoreName

The name of the Certificate Store where this certificate should be stored. Possible values are `CertificateAuthority` and `Root`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

