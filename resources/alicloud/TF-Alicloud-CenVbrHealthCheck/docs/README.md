# TF::Alicloud::CenVbrHealthCheck

This topic describes how to configure the health check feature for a Cloud Enterprise Network (CEN) instance. 
After you attach a Virtual Border Router (VBR) to the CEN instance and configure the health check feature, you can monitor the network conditions of the on-premises data center connected to the VBR.

For information about CEN VBR HealthCheck and how to use it, see [Manage CEN VBR HealthCheck](https://www.alibabacloud.com/help/en/doc-detail/71141.htm).

-> **NOTE:** Available in 1.88.0+

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::CenVbrHealthCheck",
    "Properties" : {
        "<a href="#cenid" title="CenId">CenId</a>" : <i>String</i>,
        "<a href="#healthcheckinterval" title="HealthCheckInterval">HealthCheckInterval</a>" : <i>Double</i>,
        "<a href="#healthchecksourceip" title="HealthCheckSourceIp">HealthCheckSourceIp</a>" : <i>String</i>,
        "<a href="#healthchecktargetip" title="HealthCheckTargetIp">HealthCheckTargetIp</a>" : <i>String</i>,
        "<a href="#healthythreshold" title="HealthyThreshold">HealthyThreshold</a>" : <i>Double</i>,
        "<a href="#vbrinstanceid" title="VbrInstanceId">VbrInstanceId</a>" : <i>String</i>,
        "<a href="#vbrinstanceownerid" title="VbrInstanceOwnerId">VbrInstanceOwnerId</a>" : <i>Double</i>,
        "<a href="#vbrinstanceregionid" title="VbrInstanceRegionId">VbrInstanceRegionId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::CenVbrHealthCheck
Properties:
    <a href="#cenid" title="CenId">CenId</a>: <i>String</i>
    <a href="#healthcheckinterval" title="HealthCheckInterval">HealthCheckInterval</a>: <i>Double</i>
    <a href="#healthchecksourceip" title="HealthCheckSourceIp">HealthCheckSourceIp</a>: <i>String</i>
    <a href="#healthchecktargetip" title="HealthCheckTargetIp">HealthCheckTargetIp</a>: <i>String</i>
    <a href="#healthythreshold" title="HealthyThreshold">HealthyThreshold</a>: <i>Double</i>
    <a href="#vbrinstanceid" title="VbrInstanceId">VbrInstanceId</a>: <i>String</i>
    <a href="#vbrinstanceownerid" title="VbrInstanceOwnerId">VbrInstanceOwnerId</a>: <i>Double</i>
    <a href="#vbrinstanceregionid" title="VbrInstanceRegionId">VbrInstanceRegionId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CenId

The ID of the CEN instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckInterval

Specifies the interval at which the health check sends continuous detection packets. Default value: 2. Value range: 2 to 3.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckSourceIp

The source IP address of health checks.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckTargetIp

The destination IP address of health checks.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthyThreshold

Specifies the number of probe messages sent by the health check. Default value: 8. Value range: 3 to 8.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VbrInstanceId

The ID of the VBR.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VbrInstanceOwnerId

The ID of the account to which the VBR belongs.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VbrInstanceRegionId

The ID of the region to which the VBR belongs.

_Required_: Yes

_Type_: String

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

