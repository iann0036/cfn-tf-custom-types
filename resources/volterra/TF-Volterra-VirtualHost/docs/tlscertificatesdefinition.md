# TF::Volterra::VirtualHost TlsCertificatesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#certificateurl" title="CertificateUrl">CertificateUrl</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#privatekey" title="PrivateKey">PrivateKey</a>" : <i>[ <a href="privatekeydefinition.md">PrivateKeyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#certificateurl" title="CertificateUrl">CertificateUrl</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#privatekey" title="PrivateKey">PrivateKey</a>: <i>
      - <a href="privatekeydefinition.md">PrivateKeyDefinition</a></i>
</pre>

## Properties

#### CertificateUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKey

_Required_: No

_Type_: List of <a href="privatekeydefinition.md">PrivateKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

