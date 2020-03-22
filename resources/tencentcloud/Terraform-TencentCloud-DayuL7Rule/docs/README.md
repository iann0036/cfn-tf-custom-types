# Terraform::TencentCloud::DayuL7Rule

Use this resource to create dayu layer 7 rule

~> **NOTE:** This resource only support resource Anti-DDoS of type `bgpip`

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::DayuL7Rule",
    "Properties" : {
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#healthcheckcode" title="HealthCheckCode">HealthCheckCode</a>" : <i>Double</i>,
        "<a href="#healthcheckhealthnum" title="HealthCheckHealthNum">HealthCheckHealthNum</a>" : <i>Double</i>,
        "<a href="#healthcheckinterval" title="HealthCheckInterval">HealthCheckInterval</a>" : <i>Double</i>,
        "<a href="#healthcheckmethod" title="HealthCheckMethod">HealthCheckMethod</a>" : <i>String</i>,
        "<a href="#healthcheckpath" title="HealthCheckPath">HealthCheckPath</a>" : <i>String</i>,
        "<a href="#healthcheckswitch" title="HealthCheckSwitch">HealthCheckSwitch</a>" : <i>Boolean</i>,
        "<a href="#healthcheckunhealthnum" title="HealthCheckUnhealthNum">HealthCheckUnhealthNum</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#resourceid" title="ResourceId">ResourceId</a>" : <i>String</i>,
        "<a href="#resourcetype" title="ResourceType">ResourceType</a>" : <i>String</i>,
        "<a href="#sourcelist" title="SourceList">SourceList</a>" : <i>[ String, ... ]</i>,
        "<a href="#sourcetype" title="SourceType">SourceType</a>" : <i>Double</i>,
        "<a href="#sslid" title="SslId">SslId</a>" : <i>String</i>,
        "<a href="#switch" title="Switch">Switch</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::DayuL7Rule
Properties:
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#healthcheckcode" title="HealthCheckCode">HealthCheckCode</a>: <i>Double</i>
    <a href="#healthcheckhealthnum" title="HealthCheckHealthNum">HealthCheckHealthNum</a>: <i>Double</i>
    <a href="#healthcheckinterval" title="HealthCheckInterval">HealthCheckInterval</a>: <i>Double</i>
    <a href="#healthcheckmethod" title="HealthCheckMethod">HealthCheckMethod</a>: <i>String</i>
    <a href="#healthcheckpath" title="HealthCheckPath">HealthCheckPath</a>: <i>String</i>
    <a href="#healthcheckswitch" title="HealthCheckSwitch">HealthCheckSwitch</a>: <i>Boolean</i>
    <a href="#healthcheckunhealthnum" title="HealthCheckUnhealthNum">HealthCheckUnhealthNum</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#resourceid" title="ResourceId">ResourceId</a>: <i>String</i>
    <a href="#resourcetype" title="ResourceType">ResourceType</a>: <i>String</i>
    <a href="#sourcelist" title="SourceList">SourceList</a>: <i>
      - String</i>
    <a href="#sourcetype" title="SourceType">SourceType</a>: <i>Double</i>
    <a href="#sslid" title="SslId">SslId</a>: <i>String</i>
    <a href="#switch" title="Switch">Switch</a>: <i>Boolean</i>
</pre>

## Properties

#### Domain

Domain that the layer 7 rule works for. Valid string length ranges from 0 to 80.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckCode

HTTP Status Code. The default is 26 and value range is 1-31. 1 means the return value '1xx' is health. 2 means the return value '2xx' is health. 4 means the return value '3xx' is health. 8 means the return value '4xx' is health. 16 means the return value '5xx' is health. If you want multiple return codes to indicate health, need to add the corresponding values.

_Required_: No

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

#### HealthCheckMethod

Methods of health check. The default is 'HEAD', the available value are 'HEAD' and 'GET'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckPath

Path of health check. The default is `/`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckSwitch

Indicates whether health check is enabled. The default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckUnhealthNum

Unhealthy threshold of health check, and the default is 3. If the unhealth result is returned 3 consecutive times, indicates that the forwarding is abnormal. The value range is 2-10.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Protocol of the rule, valid values are `http`, `https`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceId

ID of the resource that the layer 7 rule works for.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceType

Type of the resource that the layer 7 rule works for, valid value is `bgpip`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceList

Source list of the rule, it can be a set of ip sources or a set of domain sources. The number of items ranges from 1 to 16.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceType

Source type, 1 for source of host, 2 for source of ip.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslId

SSL id, when the `protocol` is `https`, the field should be set with valid SSL id.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Switch

Indicate the rule will take effect or not.

_Required_: Yes

_Type_: Boolean

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

#### RuleId

Returns the <code>RuleId</code> value.

#### Status

Returns the <code>Status</code> value.

