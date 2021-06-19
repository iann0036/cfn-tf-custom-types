# TF::OCI::DatabaseKeyStore TypeDetailsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#adminusername" title="AdminUsername">AdminUsername</a>" : <i>String</i>,
    "<a href="#connectionips" title="ConnectionIps">ConnectionIps</a>" : <i>[ String, ... ]</i>,
    "<a href="#secretid" title="SecretId">SecretId</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#vaultid" title="VaultId">VaultId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#adminusername" title="AdminUsername">AdminUsername</a>: <i>String</i>
<a href="#connectionips" title="ConnectionIps">ConnectionIps</a>: <i>
      - String</i>
<a href="#secretid" title="SecretId">SecretId</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#vaultid" title="VaultId">VaultId</a>: <i>String</i>
</pre>

## Properties

#### AdminUsername

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionIps

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VaultId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

