# Terraform::AzureRM::WindowsVirtualMachine Secret

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#keyvaultid" title="KeyVaultId">KeyVaultId</a>" : <i>String</i>,
    "<a href="#certificate" title="Certificate">Certificate</a>" : <i>[ &lt;a href=&#34;secret-certificate.md&#34;&gt;Certificate&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#keyvaultid" title="KeyVaultId">KeyVaultId</a>: <i>String</i>
<a href="#certificate" title="Certificate">Certificate</a>: <i>
      - &lt;a href=&#34;secret-certificate.md&#34;&gt;Certificate&lt;/a&gt;</i>
</pre>

## Properties

#### KeyVaultId

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

_Required_: No
_Type_: List of &lt;a href=&#34;secret-certificate.md&#34;&gt;Certificate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

