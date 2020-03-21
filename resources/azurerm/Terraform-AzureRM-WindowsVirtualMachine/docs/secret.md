# Terraform::AzureRM::WindowsVirtualMachine Secret

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#keyvaultid" title="KeyVaultId">KeyVaultId</a>" : <i>String</i>,
    "<a href="#certificate" title="Certificate">Certificate</a>" : <i>[ <a href="secret-certificate.md">Certificate</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#keyvaultid" title="KeyVaultId">KeyVaultId</a>: <i>String</i>
<a href="#certificate" title="Certificate">Certificate</a>: <i>
      - <a href="secret-certificate.md">Certificate</a></i>
</pre>

## Properties

#### KeyVaultId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

_Required_: No

_Type_: List of <a href="secret-certificate.md">Certificate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

