# Terraform::AzureRM::WindowsVirtualMachine WinrmListener

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#certificateurl" title="CertificateUrl">CertificateUrl</a>" : <i>String</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#certificateurl" title="CertificateUrl">CertificateUrl</a>: <i>String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
</pre>

## Properties

#### CertificateUrl

The Secret URL of a Key Vault Certificate, which must be specified when `protocol` is set to `Https`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

