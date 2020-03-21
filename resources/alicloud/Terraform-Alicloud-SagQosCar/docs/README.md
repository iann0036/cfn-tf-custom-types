# Terraform::Alicloud::SagQosCar

Provides a Sag qos car resource. 
You need to create a QoS car to set priorities, rate limits, and quintuple rules for different messages.

For information about Sag Qos Car and how to use it, see [What is Qos Car](https://www.alibabacloud.com/help/doc-detail/140065.htm).

-> **NOTE:** Available in 1.60.0+

-> **NOTE:** Only the following regions support. [`cn-shanghai`, `cn-shanghai-finance-1`, `cn-hongkong`, `ap-southeast-1`, `ap-southeast-2`, `ap-southeast-3`, `ap-southeast-5`, `ap-northeast-1`, `eu-central-1`]

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::SagQosCar",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#limittype" title="LimitType">LimitType</a>" : <i>String</i>,
        "<a href="#maxbandwidthabs" title="MaxBandwidthAbs">MaxBandwidthAbs</a>" : <i>Double</i>,
        "<a href="#maxbandwidthpercent" title="MaxBandwidthPercent">MaxBandwidthPercent</a>" : <i>Double</i>,
        "<a href="#minbandwidthabs" title="MinBandwidthAbs">MinBandwidthAbs</a>" : <i>Double</i>,
        "<a href="#minbandwidthpercent" title="MinBandwidthPercent">MinBandwidthPercent</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#percentsourcetype" title="PercentSourceType">PercentSourceType</a>" : <i>String</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
        "<a href="#qosid" title="QosId">QosId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::SagQosCar
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#limittype" title="LimitType">LimitType</a>: <i>String</i>
    <a href="#maxbandwidthabs" title="MaxBandwidthAbs">MaxBandwidthAbs</a>: <i>Double</i>
    <a href="#maxbandwidthpercent" title="MaxBandwidthPercent">MaxBandwidthPercent</a>: <i>Double</i>
    <a href="#minbandwidthabs" title="MinBandwidthAbs">MinBandwidthAbs</a>: <i>Double</i>
    <a href="#minbandwidthpercent" title="MinBandwidthPercent">MinBandwidthPercent</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#percentsourcetype" title="PercentSourceType">PercentSourceType</a>: <i>String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>Double</i>
    <a href="#qosid" title="QosId">QosId</a>: <i>String</i>
</pre>

## Properties

#### Description

The description of the QoS speed limiting rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitType

The speed limiting method. Valid values: Absolute, Percent.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxBandwidthAbs

The maximum bandwidth allowed for the stream specified in the quintuple rule. This parameter is required when the value of the LimitType is Absolute.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxBandwidthPercent

The maximum bandwidth percentage allowed for the stream specified in the quintuple rule. It is based on the maximum upstream bandwidth you set for the associated Smart Access Gateway (SAG) instance.This parameter is required when the value of the LimitType parameter is Percent.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinBandwidthAbs

The minimum bandwidth allowed for the stream specified in the quintuple rule. This parameter is required when the value of the LimitType parameter is Absolute.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinBandwidthPercent

The minimum bandwidth percentage allowed for the stream specified in the quintuple rule. It is based on the maximum upstream bandwidth you set for the associated SAG instance.This parameter is required when the value of the LimitType parameter is Percent.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the QoS speed limiting rule..

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PercentSourceType

The bandwidth type when the speed is limited based on percentage. Valid values: CcnBandwidth, InternetUpBandwidth.The default value is InternetUpBandwidth.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

The priority of the specified stream.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QosId

The instance ID of the QoS.

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

