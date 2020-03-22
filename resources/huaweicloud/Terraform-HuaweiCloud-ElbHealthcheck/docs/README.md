# Terraform::HuaweiCloud::ElbHealthcheck

Manages an elastic loadbalancer healthcheck resource within huawei cloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::ElbHealthcheck",
    "Properties" : {
        "<a href="#healthcheckconnectport" title="HealthcheckConnectPort">HealthcheckConnectPort</a>" : <i>Double</i>,
        "<a href="#healthcheckinterval" title="HealthcheckInterval">HealthcheckInterval</a>" : <i>Double</i>,
        "<a href="#healthcheckprotocol" title="HealthcheckProtocol">HealthcheckProtocol</a>" : <i>String</i>,
        "<a href="#healthchecktimeout" title="HealthcheckTimeout">HealthcheckTimeout</a>" : <i>Double</i>,
        "<a href="#healthcheckuri" title="HealthcheckUri">HealthcheckUri</a>" : <i>String</i>,
        "<a href="#healthythreshold" title="HealthyThreshold">HealthyThreshold</a>" : <i>Double</i>,
        "<a href="#listenerid" title="ListenerId">ListenerId</a>" : <i>String</i>,
        "<a href="#unhealthythreshold" title="UnhealthyThreshold">UnhealthyThreshold</a>" : <i>Double</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::ElbHealthcheck
Properties:
    <a href="#healthcheckconnectport" title="HealthcheckConnectPort">HealthcheckConnectPort</a>: <i>Double</i>
    <a href="#healthcheckinterval" title="HealthcheckInterval">HealthcheckInterval</a>: <i>Double</i>
    <a href="#healthcheckprotocol" title="HealthcheckProtocol">HealthcheckProtocol</a>: <i>String</i>
    <a href="#healthchecktimeout" title="HealthcheckTimeout">HealthcheckTimeout</a>: <i>Double</i>
    <a href="#healthcheckuri" title="HealthcheckUri">HealthcheckUri</a>: <i>String</i>
    <a href="#healthythreshold" title="HealthyThreshold">HealthyThreshold</a>: <i>Double</i>
    <a href="#listenerid" title="ListenerId">ListenerId</a>: <i>String</i>
    <a href="#unhealthythreshold" title="UnhealthyThreshold">UnhealthyThreshold</a>: <i>Double</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### HealthcheckConnectPort

Specifies the port used for the health
check. The value ranges from 1 to 65535.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthcheckInterval

Specifies the maximum interval (s) for
health check. The value ranges from 1 to 5.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthcheckProtocol

Specifies the protocol used for the health
check. The value can be HTTP or TCP (case-insensitive).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthcheckTimeout

Specifies the maximum timeout duration
(s) for the health check. The value ranges from 1 to 50.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthcheckUri

Specifies the URI for health check. This parameter
is valid when healthcheck_ protocol is HTTP. The value is a string of 1 to 80
characters that must start with a slash (/) and can only contain letters, digits,
and special characters, such as -/.%?#&.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthyThreshold

Specifies the threshold at which the health
check result is success, that is, the number of consecutive successful health
checks when the health check result of the backend server changes from fail
to success. The value ranges from 1 to 10.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListenerId

Specifies the ID of the listener to which the health
check task belongs.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnhealthyThreshold

Specifies the threshold at which the health
check result is fail, that is, the number of consecutive failed health checks
when the health check result of the backend server changes from success to fail.
The value ranges from 1 to 10.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### UpdateTime

Returns the <code>UpdateTime</code> value.

