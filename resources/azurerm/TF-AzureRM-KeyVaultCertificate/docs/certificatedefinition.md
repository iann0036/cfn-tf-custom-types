# TF::AzureRM::KeyVaultCertificate CertificateDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#contents" title="Contents">Contents</a>" : <i>String</i>,
    "<a href="#password" title="Password">Password</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#contents" title="Contents">Contents</a>: <i>String</i>
<a href="#password" title="Password">Password</a>: <i>String</i>
</pre>

## Properties

#### Contents

The base64-encoded certificate contents. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

The password associated with the certificate. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

