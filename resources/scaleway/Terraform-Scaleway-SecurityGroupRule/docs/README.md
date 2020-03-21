# Terraform::Scaleway::SecurityGroupRule

**DEPRECATED**: This resource is deprecated and will be removed in `v2.0+`.
Please use `scaleway_instance_security_group_rule` instead.

Provides security group rules. This allows security group rules to be created, updated and deleted.
For additional details please refer to [API documentation](https://developer.scaleway.com/#security-groups-manage-rules).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Scaleway::SecurityGroupRule",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#direction" title="Direction">Direction</a>" : <i>String</i>,
        "<a href="#iprange" title="IpRange">IpRange</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#securitygroup" title="SecurityGroup">SecurityGroup</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Scaleway::SecurityGroupRule
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#direction" title="Direction">Direction</a>: <i>String</i>
    <a href="#iprange" title="IpRange">IpRange</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#securitygroup" title="SecurityGroup">SecurityGroup</a>: <i>String</i>
</pre>

## Properties

#### Action

action of rule (`accept`, `drop`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Direction

direction of rule (`inbound`, `outbound`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpRange

ip_range of rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

port of the rule.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

protocol of rule (`ICMP`, `TCP`, `UDP`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroup

the security group which should be associated with this rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

