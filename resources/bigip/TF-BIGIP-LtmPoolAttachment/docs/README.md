# TF::BIGIP::LtmPoolAttachment

`bigip_ltm_pool_attachment` Manages nodes membership in pools

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::BIGIP::LtmPoolAttachment",
    "Properties" : {
        "<a href="#connectionlimit" title="ConnectionLimit">ConnectionLimit</a>" : <i>Double</i>,
        "<a href="#connectionratelimit" title="ConnectionRateLimit">ConnectionRateLimit</a>" : <i>String</i>,
        "<a href="#dynamicratio" title="DynamicRatio">DynamicRatio</a>" : <i>Double</i>,
        "<a href="#fqdnautopopulate" title="FqdnAutopopulate">FqdnAutopopulate</a>" : <i>String</i>,
        "<a href="#node" title="Node">Node</a>" : <i>String</i>,
        "<a href="#pool" title="Pool">Pool</a>" : <i>String</i>,
        "<a href="#prioritygroup" title="PriorityGroup">PriorityGroup</a>" : <i>Double</i>,
        "<a href="#ratio" title="Ratio">Ratio</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::BIGIP::LtmPoolAttachment
Properties:
    <a href="#connectionlimit" title="ConnectionLimit">ConnectionLimit</a>: <i>Double</i>
    <a href="#connectionratelimit" title="ConnectionRateLimit">ConnectionRateLimit</a>: <i>String</i>
    <a href="#dynamicratio" title="DynamicRatio">DynamicRatio</a>: <i>Double</i>
    <a href="#fqdnautopopulate" title="FqdnAutopopulate">FqdnAutopopulate</a>: <i>String</i>
    <a href="#node" title="Node">Node</a>: <i>String</i>
    <a href="#pool" title="Pool">Pool</a>: <i>String</i>
    <a href="#prioritygroup" title="PriorityGroup">PriorityGroup</a>: <i>Double</i>
    <a href="#ratio" title="Ratio">Ratio</a>: <i>Double</i>
</pre>

## Properties

#### ConnectionLimit

Specifies a maximum established connection limit for a pool member or node.The default is 0, meaning that there is no limit to the number of connections.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionRateLimit

Specifies the maximum number of connections-per-second allowed for a pool member,The default is 0.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicRatio

Specifies the fixed ratio value used for a node during ratio load balancing.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FqdnAutopopulate

Specifies whether the system automatically creates ephemeral nodes using the IP addresses returned by the resolution of a DNS query for a node defined by an FQDN. The default is enabled.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Node

Pool member address/fqdn with service port, (ex: `1.1.1.1:80/www.google.com:80`). (Note: Member will be in same partition of Pool).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pool

Name of the pool to which members should be attached,it should be "full path".The full path is the combination of the partition + name of the pool.(For example `/Common/my-pool`) or partition + directory + name of the pool (For example `/Common/test/my-pool`).When including directory in fullpath we have to make sure it is created in the given partition before using it.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PriorityGroup

Specifies a number representing the priority group for the pool member. The default is 0, meaning that the member has no priority.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ratio

"Specifies the ratio weight to assign to the pool member. Valid values range from 1 through 65535. The default is 1, which means that each pool member has an equal ratio proportion.".

_Required_: No

_Type_: Double

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

