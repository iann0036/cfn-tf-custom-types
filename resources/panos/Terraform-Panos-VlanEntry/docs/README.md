# Terraform::Panos::VlanEntry

This resource allows you to add/update/delete an interface in a VLAN.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::VlanEntry",
    "Properties" : {
        "<a href="#interface" title="Interface">Interface</a>" : <i>String</i>,
        "<a href="#macaddresses" title="MacAddresses">MacAddresses</a>" : <i>[ String, ... ]</i>,
        "<a href="#vlan" title="Vlan">Vlan</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::VlanEntry
Properties:
    <a href="#interface" title="Interface">Interface</a>: <i>String</i>
    <a href="#macaddresses" title="MacAddresses">MacAddresses</a>: <i>
      - String</i>
    <a href="#vlan" title="Vlan">Vlan</a>: <i>String</i>
</pre>

## Properties

#### Interface

The interface's name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacAddresses

List of MAC addresses that should go with this entry.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vlan

The VLAN's name.

_Required_: Yes

_Type_: String

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

#### LiveMacAddresses

Returns the <code>LiveMacAddresses</code> value.

