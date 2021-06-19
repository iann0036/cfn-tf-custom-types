# TF::SDM::SecretStore

A SecretStore is a server where resource secrets (passwords, keys) are stored. 
 Coming soon support for HashiCorp Vault and AWS Secret Store. Contact support@strongdm.com to request access to the beta.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::SDM::SecretStore",
    "Properties" : {
        "<a href="#aws" title="Aws">Aws</a>" : <i>[ <a href="awsdefinition.md">AwsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#vaulttls" title="VaultTls">VaultTls</a>" : <i>[ <a href="vaulttlsdefinition.md">VaultTlsDefinition</a>, ... ]</i>,
        "<a href="#vaulttoken" title="VaultToken">VaultToken</a>" : <i>[ <a href="vaulttokendefinition.md">VaultTokenDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::SDM::SecretStore
Properties:
    <a href="#aws" title="Aws">Aws</a>: <i>
      - <a href="awsdefinition.md">AwsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#vaulttls" title="VaultTls">VaultTls</a>: <i>
      - <a href="vaulttlsdefinition.md">VaultTlsDefinition</a></i>
    <a href="#vaulttoken" title="VaultToken">VaultToken</a>: <i>
      - <a href="vaulttokendefinition.md">VaultTokenDefinition</a></i>
</pre>

## Properties

#### Aws

_Required_: No

_Type_: List of <a href="awsdefinition.md">AwsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VaultTls

_Required_: No

_Type_: List of <a href="vaulttlsdefinition.md">VaultTlsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VaultToken

_Required_: No

_Type_: List of <a href="vaulttokendefinition.md">VaultTokenDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

