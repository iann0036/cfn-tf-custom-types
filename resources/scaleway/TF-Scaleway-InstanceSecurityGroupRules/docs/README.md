# TF::Scaleway::InstanceSecurityGroupRules

Creates and manages Scaleway Compute Instance security group rules. For more information, see [the documentation](https://developers.scaleway.com/en/products/instance/api/#security-groups-8d7f89).

This resource can be used to externalize rules from a `scaleway_instance_security_group` to solve circular dependency problems. When using this resource do not forget to set `external_rules = true` on the security group.

~> **Warning:** In order to guaranty rules order in a given security group only one scaleway_instance_security_group_rules is allowed per security group.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Scaleway::InstanceSecurityGroupRules",
    "Properties" : {
        "<a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>" : <i>String</i>,
        "<a href="#inboundrule" title="InboundRule">InboundRule</a>" : <i>[ <a href="inboundruledefinition.md">InboundRuleDefinition</a>, ... ]</i>,
        "<a href="#outboundrule" title="OutboundRule">OutboundRule</a>" : <i>[ <a href="outboundruledefinition.md">OutboundRuleDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Scaleway::InstanceSecurityGroupRules
Properties:
    <a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>: <i>String</i>
    <a href="#inboundrule" title="InboundRule">InboundRule</a>: <i>
      - <a href="inboundruledefinition.md">InboundRuleDefinition</a></i>
    <a href="#outboundrule" title="OutboundRule">OutboundRule</a>: <i>
      - <a href="outboundruledefinition.md">OutboundRuleDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### SecurityGroupId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InboundRule

_Required_: No

_Type_: List of <a href="inboundruledefinition.md">InboundRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutboundRule

_Required_: No

_Type_: List of <a href="outboundruledefinition.md">OutboundRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

