# Terraform::TencentCloud::GaapHttpRule

Provides a resource to create a forward rule of layer7 listener.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::GaapHttpRule",
    "Properties" : {
        "<a href="#connecttimeout" title="ConnectTimeout">ConnectTimeout</a>" : <i>Double</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#forwardhost" title="ForwardHost">ForwardHost</a>" : <i>String</i>,
        "<a href="#healthcheck" title="HealthCheck">HealthCheck</a>" : <i>Boolean</i>,
        "<a href="#healthcheckmethod" title="HealthCheckMethod">HealthCheckMethod</a>" : <i>String</i>,
        "<a href="#healthcheckpath" title="HealthCheckPath">HealthCheckPath</a>" : <i>String</i>,
        "<a href="#healthcheckstatuscodes" title="HealthCheckStatusCodes">HealthCheckStatusCodes</a>" : <i>[ Double, ... ]</i>,
        "<a href="#interval" title="Interval">Interval</a>" : <i>Double</i>,
        "<a href="#listenerid" title="ListenerId">ListenerId</a>" : <i>String</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>,
        "<a href="#realservertype" title="RealserverType">RealserverType</a>" : <i>String</i>,
        "<a href="#scheduler" title="Scheduler">Scheduler</a>" : <i>String</i>,
        "<a href="#realservers" title="Realservers">Realservers</a>" : <i>[ <a href="realservers.md">Realservers</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::GaapHttpRule
Properties:
    <a href="#connecttimeout" title="ConnectTimeout">ConnectTimeout</a>: <i>Double</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#forwardhost" title="ForwardHost">ForwardHost</a>: <i>String</i>
    <a href="#healthcheck" title="HealthCheck">HealthCheck</a>: <i>Boolean</i>
    <a href="#healthcheckmethod" title="HealthCheckMethod">HealthCheckMethod</a>: <i>String</i>
    <a href="#healthcheckpath" title="HealthCheckPath">HealthCheckPath</a>: <i>String</i>
    <a href="#healthcheckstatuscodes" title="HealthCheckStatusCodes">HealthCheckStatusCodes</a>: <i>
      - Double</i>
    <a href="#interval" title="Interval">Interval</a>: <i>Double</i>
    <a href="#listenerid" title="ListenerId">ListenerId</a>: <i>String</i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
    <a href="#realservertype" title="RealserverType">RealserverType</a>: <i>String</i>
    <a href="#scheduler" title="Scheduler">Scheduler</a>: <i>String</i>
    <a href="#realservers" title="Realservers">Realservers</a>: <i>
      - <a href="realservers.md">Realservers</a></i>
</pre>

## Properties

#### ConnectTimeout

Timeout of the health check response, default value is 2s.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

Forward domain of the forward rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardHost

The default value of requested host which is forwarded to the realserver by the listener is `default`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheck

Indicates whether health check is enable.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckMethod

Method of the health check, the available values includes `GET` and `HEAD`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckPath

Path of health check. Maximum length is 80.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckStatusCodes

Return code of confirmed normal, the available values include `100`, `200`, `300`, `400` and `500`.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interval

Interval of the health check, default value is 5s.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListenerId

ID of the layer7 listener.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

Path of the forward rule. Maximum length is 80.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RealserverType

Type of the realserver, the available values include `IP` and `DOMAIN`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scheduler

Scheduling policy of the forward rule, default value is `rr`, the available values include `rr`, `wrr` and `lc`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Realservers

_Required_: No

_Type_: List of <a href="realservers.md">Realservers</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

