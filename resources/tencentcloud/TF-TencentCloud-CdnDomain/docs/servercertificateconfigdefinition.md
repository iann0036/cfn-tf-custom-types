# TF::TencentCloud::CdnDomain ServerCertificateConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#certificatecontent" title="CertificateContent">CertificateContent</a>" : <i>String</i>,
    "<a href="#certificateid" title="CertificateId">CertificateId</a>" : <i>String</i>,
    "<a href="#message" title="Message">Message</a>" : <i>String</i>,
    "<a href="#privatekey" title="PrivateKey">PrivateKey</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#certificatecontent" title="CertificateContent">CertificateContent</a>: <i>String</i>
<a href="#certificateid" title="CertificateId">CertificateId</a>: <i>String</i>
<a href="#message" title="Message">Message</a>: <i>String</i>
<a href="#privatekey" title="PrivateKey">PrivateKey</a>: <i>String</i>
</pre>

## Properties

#### CertificateContent

Server certificate information. This is required when uploading an external certificate, which should contain the complete certificate chain.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateId

Server certificate ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Message

Certificate remarks.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKey

Server key information. This is required when uploading an external certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

