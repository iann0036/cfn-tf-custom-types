# Terraform::Consul::Keys

The `consul_keys` resource writes sets of individual values into Consul.
This is a powerful way to expose infrastructure details to clients.

This resource manages individual keys, and thus it can create, update
and delete the keys explicitly given. However, it is not able to detect
and remove additional keys that have been added by non-Terraform means.
To manage *all* keys sharing a common prefix, and thus have Terraform
remove errant keys not present in the configuration, consider using the
`consul_key_prefix` resource instead.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Consul::Keys",
    "Properties" : {
        "<a href="#datacenter" title="Datacenter">Datacenter</a>" : <i>String</i>,
        "<a href="#token" title="Token">Token</a>" : <i>String</i>,
        "<a href="#key" title="Key">Key</a>" : <i>[ <a href="key.md">Key</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Consul::Keys
Properties:
    <a href="#datacenter" title="Datacenter">Datacenter</a>: <i>String</i>
    <a href="#token" title="Token">Token</a>: <i>String</i>
    <a href="#key" title="Key">Key</a>: <i>
      - <a href="key.md">Key</a></i>
</pre>

## Properties

#### Datacenter

The datacenter to use. This overrides the
agent's default datacenter and the datacenter in the provider setup.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Token

The ACL token to use. This overrides the
token that the agent provides by default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

_Required_: No

_Type_: List of <a href="key.md">Key</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### Var

Returns the <code>Var</code> value.

