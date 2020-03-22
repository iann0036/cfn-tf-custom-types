# Terraform::AWS::GlobalacceleratorEndpointGroup

CloudFormation equivalent of aws_globalaccelerator_endpoint_group

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::GlobalacceleratorEndpointGroup",
    "Properties" : {
        "<a href="#endpointgroupregion" title="EndpointGroupRegion">EndpointGroupRegion</a>" : <i>String</i>,
        "<a href="#healthcheckintervalseconds" title="HealthCheckIntervalSeconds">HealthCheckIntervalSeconds</a>" : <i>Double</i>,
        "<a href="#healthcheckpath" title="HealthCheckPath">HealthCheckPath</a>" : <i>String</i>,
        "<a href="#healthcheckport" title="HealthCheckPort">HealthCheckPort</a>" : <i>Double</i>,
        "<a href="#healthcheckprotocol" title="HealthCheckProtocol">HealthCheckProtocol</a>" : <i>String</i>,
        "<a href="#listenerarn" title="ListenerArn">ListenerArn</a>" : <i>String</i>,
        "<a href="#thresholdcount" title="ThresholdCount">ThresholdCount</a>" : <i>Double</i>,
        "<a href="#trafficdialpercentage" title="TrafficDialPercentage">TrafficDialPercentage</a>" : <i>Double</i>,
        "<a href="#endpointconfiguration" title="EndpointConfiguration">EndpointConfiguration</a>" : <i>[ <a href="endpointconfiguration.md">EndpointConfiguration</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::GlobalacceleratorEndpointGroup
Properties:
    <a href="#endpointgroupregion" title="EndpointGroupRegion">EndpointGroupRegion</a>: <i>String</i>
    <a href="#healthcheckintervalseconds" title="HealthCheckIntervalSeconds">HealthCheckIntervalSeconds</a>: <i>Double</i>
    <a href="#healthcheckpath" title="HealthCheckPath">HealthCheckPath</a>: <i>String</i>
    <a href="#healthcheckport" title="HealthCheckPort">HealthCheckPort</a>: <i>Double</i>
    <a href="#healthcheckprotocol" title="HealthCheckProtocol">HealthCheckProtocol</a>: <i>String</i>
    <a href="#listenerarn" title="ListenerArn">ListenerArn</a>: <i>String</i>
    <a href="#thresholdcount" title="ThresholdCount">ThresholdCount</a>: <i>Double</i>
    <a href="#trafficdialpercentage" title="TrafficDialPercentage">TrafficDialPercentage</a>: <i>Double</i>
    <a href="#endpointconfiguration" title="EndpointConfiguration">EndpointConfiguration</a>: <i>
      - <a href="endpointconfiguration.md">EndpointConfiguration</a></i>
</pre>

## Properties

#### EndpointGroupRegion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckIntervalSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckPort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckProtocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListenerArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficDialPercentage

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointConfiguration

_Required_: No

_Type_: List of <a href="endpointconfiguration.md">EndpointConfiguration</a>

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

