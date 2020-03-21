# Terraform::Consul::KeyPrefix

CloudFormation equivalent of consul_key_prefix

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Consul::KeyPrefix",
    "Properties" : {
        "<a href="#datacenter" title="Datacenter">Datacenter</a>" : <i>String</i>,
        "<a href="#pathprefix" title="PathPrefix">PathPrefix</a>" : <i>String</i>,
        "<a href="#subkeys" title="Subkeys">Subkeys</a>" : <i>[ <a href="subkeys.md">Subkeys</a>, ... ]</i>,
        "<a href="#token" title="Token">Token</a>" : <i>String</i>,
        "<a href="#subkey" title="Subkey">Subkey</a>" : <i>[ <a href="subkey.md">Subkey</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Consul::KeyPrefix
Properties:
    <a href="#datacenter" title="Datacenter">Datacenter</a>: <i>String</i>
    <a href="#pathprefix" title="PathPrefix">PathPrefix</a>: <i>String</i>
    <a href="#subkeys" title="Subkeys">Subkeys</a>: <i>
      - <a href="subkeys.md">Subkeys</a></i>
    <a href="#token" title="Token">Token</a>: <i>String</i>
    <a href="#subkey" title="Subkey">Subkey</a>: <i>
      - <a href="subkey.md">Subkey</a></i>
</pre>

## Properties

#### Datacenter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathPrefix

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subkeys

_Required_: No

_Type_: List of <a href="subkeys.md">Subkeys</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Token

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subkey

_Required_: No

_Type_: List of <a href="subkey.md">Subkey</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

