# Terraform::TencentCloud::DayuL4Rule

Use this resource to create dayu layer 4 rule

~> **NOTE:** This resource only support resource Anti-DDoS of type `bgpip` and `net`

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::DayuL4Rule",
    "Properties" : {
        "<a href="#dport" title="DPort">DPort</a>" : <i>Double</i>,
        "<a href="#healthcheckhealthnum" title="HealthCheckHealthNum">HealthCheckHealthNum</a>" : <i>Double</i>,
        "<a href="#healthcheckinterval" title="HealthCheckInterval">HealthCheckInterval</a>" : <i>Double</i>,
        "<a href="#healthcheckswitch" title="HealthCheckSwitch">HealthCheckSwitch</a>" : <i>Boolean</i>,
        "<a href="#healthchecktimeout" title="HealthCheckTimeout">HealthCheckTimeout</a>" : <i>Double</i>,
        "<a href="#healthcheckunhealthnum" title="HealthCheckUnhealthNum">HealthCheckUnhealthNum</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#resourceid" title="ResourceId">ResourceId</a>" : <i>String</i>,
        "<a href="#resourcetype" title="ResourceType">ResourceType</a>" : <i>String</i>,
        "<a href="#sport" title="SPort">SPort</a>" : <i>Double</i>,
        "<a href="#sessionswitch" title="SessionSwitch">SessionSwitch</a>" : <i>Boolean</i>,
        "<a href="#sessiontime" title="SessionTime">SessionTime</a>" : <i>Double</i>,
        "<a href="#sourcetype" title="SourceType">SourceType</a>" : <i>Double</i>,
        "<a href="#sourcelist" title="SourceList">SourceList</a>" : <i>[ <a href="sourcelist.md">SourceList</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::DayuL4Rule
Properties:
    <a href="#dport" title="DPort">DPort</a>: <i>Double</i>
    <a href="#healthcheckhealthnum" title="HealthCheckHealthNum">HealthCheckHealthNum</a>: <i>Double</i>
    <a href="#healthcheckinterval" title="HealthCheckInterval">HealthCheckInterval</a>: <i>Double</i>
    <a href="#healthcheckswitch" title="HealthCheckSwitch">HealthCheckSwitch</a>: <i>Boolean</i>
    <a href="#healthchecktimeout" title="HealthCheckTimeout">HealthCheckTimeout</a>: <i>Double</i>
    <a href="#healthcheckunhealthnum" title="HealthCheckUnhealthNum">HealthCheckUnhealthNum</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#resourceid" title="ResourceId">ResourceId</a>: <i>String</i>
    <a href="#resourcetype" title="ResourceType">ResourceType</a>: <i>String</i>
    <a href="#sport" title="SPort">SPort</a>: <i>Double</i>
    <a href="#sessionswitch" title="SessionSwitch">SessionSwitch</a>: <i>Boolean</i>
    <a href="#sessiontime" title="SessionTime">SessionTime</a>: <i>Double</i>
    <a href="#sourcetype" title="SourceType">SourceType</a>: <i>Double</i>
    <a href="#sourcelist" title="SourceList">SourceList</a>: <i>
      - <a href="sourcelist.md">SourceList</a></i>
</pre>

## Properties

#### DPort

The destination port of the L4 rule.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckHealthNum

Health threshold of health check, and the default is 3. If a success result is returned for the health check 3 consecutive times, indicates that the forwarding is normal. The value range is 2-10.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckInterval

Interval time of health check. The value range is 10-60 sec, and the default is 15 sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckSwitch

Indicates whether health check is enabled. The default is `false`. Only valid when source list has more than one source item.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckTimeout

HTTP Status Code. The default is 26 and value range is 2-60.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckUnhealthNum

Unhealthy threshold of health check, and the default is 3. If the unhealthy result is returned 3 consecutive times, indicates that the forwarding is abnormal. The value range is 2-10.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the rule. When the `resource_type` is `net`, this field should be set with valid domain.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Protocol of the rule, valid values are `http`, `https`. When `source_type` is 1(host source), the value of this field can only set with `tcp`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceId

ID of the resource that the layer 4 rule works for.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceType

Type of the resource that the layer 4 rule works for, valid values are `bgpip` and `net`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SPort

The source port of the L4 rule.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionSwitch

Indicate that the session will keep or not, and default value is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionTime

Session keep time, only valid when `session_switch` is true, the available value ranges from 1 to 300 and unit is second.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceType

Source type, 1 for source of host, 2 for source of ip.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceList

_Required_: No

_Type_: List of <a href="sourcelist.md">SourceList</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### LbType

Returns the <code>LbType</code> value.

#### RuleId

Returns the <code>RuleId</code> value.

