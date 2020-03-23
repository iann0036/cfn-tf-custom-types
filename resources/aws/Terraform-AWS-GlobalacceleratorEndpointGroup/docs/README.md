# Terraform::AWS::GlobalacceleratorEndpointGroup

Provides a Global Accelerator endpoint group.

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

The time—10 seconds or 30 seconds—between each health check for an endpoint. The default value is 30.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckPath

If the protocol is HTTP/S, then this specifies the path that is the destination for health check targets. The default value is slash (/).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckPort

The port that AWS Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default port is the listener port that this endpoint group is associated with. If listener port is a list of ports, Global Accelerator uses the first port in the list.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckProtocol

The protocol that AWS Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default value is TCP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListenerArn

The Amazon Resource Name (ARN) of the listener.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdCount

The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficDialPercentage

The percentage of traffic to send to an AWS Region. Additional traffic is distributed to other endpoint groups for this listener. The default value is 100.

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

