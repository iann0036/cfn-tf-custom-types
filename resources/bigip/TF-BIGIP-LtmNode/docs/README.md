# TF::BIGIP::LtmNode

`bigip_ltm_node` Manages a node configuration

For resources should be named with their "full path".The full path is the combination of the partition + name of the resource( example: /Common/my-node ) or partition + Direcroty + nameof the resource ( example: /Common/test/my-node ).When including directory in fullpath we have to make sure it is created in the given partition before using it.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::BIGIP::LtmNode",
    "Properties" : {
        "<a href="#address" title="Address">Address</a>" : <i>String</i>,
        "<a href="#connectionlimit" title="ConnectionLimit">ConnectionLimit</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dynamicratio" title="DynamicRatio">DynamicRatio</a>" : <i>Double</i>,
        "<a href="#monitor" title="Monitor">Monitor</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ratelimit" title="RateLimit">RateLimit</a>" : <i>String</i>,
        "<a href="#ratio" title="Ratio">Ratio</a>" : <i>Double</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#fqdn" title="Fqdn">Fqdn</a>" : <i>[ <a href="fqdndefinition.md">FqdnDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::BIGIP::LtmNode
Properties:
    <a href="#address" title="Address">Address</a>: <i>String</i>
    <a href="#connectionlimit" title="ConnectionLimit">ConnectionLimit</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dynamicratio" title="DynamicRatio">DynamicRatio</a>: <i>Double</i>
    <a href="#monitor" title="Monitor">Monitor</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ratelimit" title="RateLimit">RateLimit</a>: <i>String</i>
    <a href="#ratio" title="Ratio">Ratio</a>: <i>Double</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#fqdn" title="Fqdn">Fqdn</a>: <i>
      - <a href="fqdndefinition.md">FqdnDefinition</a></i>
</pre>

## Properties

#### Address

IP or hostname of the node.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionLimit

Specifies the maximum number of connections allowed for the node or node address.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

User-defined description give ltm_node.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicRatio

Specifies the fixed ratio value used for a node during ratio load balancing.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Monitor

specifies the name of the monitor or monitor rule that you want to associate with the node.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the node.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateLimit

Specifies the maximum number of connections per second allowed for a node or node address. The default value is 'disabled'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ratio

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

Default is "user-up" you can set to "user-down" if you want to disable.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fqdn

_Required_: No

_Type_: List of <a href="fqdndefinition.md">FqdnDefinition</a>

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

