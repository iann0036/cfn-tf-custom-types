# TF::Alicloud::GaEndpointGroup

CloudFormation equivalent of alicloud_ga_endpoint_group

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::GaEndpointGroup",
    "Properties" : {
        "<a href="#acceleratorid" title="AcceleratorId">AcceleratorId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#endpointgroupregion" title="EndpointGroupRegion">EndpointGroupRegion</a>" : <i>String</i>,
        "<a href="#endpointgrouptype" title="EndpointGroupType">EndpointGroupType</a>" : <i>String</i>,
        "<a href="#endpointrequestprotocol" title="EndpointRequestProtocol">EndpointRequestProtocol</a>" : <i>String</i>,
        "<a href="#healthcheckintervalseconds" title="HealthCheckIntervalSeconds">HealthCheckIntervalSeconds</a>" : <i>Double</i>,
        "<a href="#healthcheckpath" title="HealthCheckPath">HealthCheckPath</a>" : <i>String</i>,
        "<a href="#healthcheckport" title="HealthCheckPort">HealthCheckPort</a>" : <i>Double</i>,
        "<a href="#healthcheckprotocol" title="HealthCheckProtocol">HealthCheckProtocol</a>" : <i>String</i>,
        "<a href="#listenerid" title="ListenerId">ListenerId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#thresholdcount" title="ThresholdCount">ThresholdCount</a>" : <i>Double</i>,
        "<a href="#trafficpercentage" title="TrafficPercentage">TrafficPercentage</a>" : <i>Double</i>,
        "<a href="#endpointconfigurations" title="EndpointConfigurations">EndpointConfigurations</a>" : <i>[ <a href="endpointconfigurationsdefinition.md">EndpointConfigurationsDefinition</a>, ... ]</i>,
        "<a href="#portoverrides" title="PortOverrides">PortOverrides</a>" : <i>[ <a href="portoverridesdefinition.md">PortOverridesDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::GaEndpointGroup
Properties:
    <a href="#acceleratorid" title="AcceleratorId">AcceleratorId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#endpointgroupregion" title="EndpointGroupRegion">EndpointGroupRegion</a>: <i>String</i>
    <a href="#endpointgrouptype" title="EndpointGroupType">EndpointGroupType</a>: <i>String</i>
    <a href="#endpointrequestprotocol" title="EndpointRequestProtocol">EndpointRequestProtocol</a>: <i>String</i>
    <a href="#healthcheckintervalseconds" title="HealthCheckIntervalSeconds">HealthCheckIntervalSeconds</a>: <i>Double</i>
    <a href="#healthcheckpath" title="HealthCheckPath">HealthCheckPath</a>: <i>String</i>
    <a href="#healthcheckport" title="HealthCheckPort">HealthCheckPort</a>: <i>Double</i>
    <a href="#healthcheckprotocol" title="HealthCheckProtocol">HealthCheckProtocol</a>: <i>String</i>
    <a href="#listenerid" title="ListenerId">ListenerId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#thresholdcount" title="ThresholdCount">ThresholdCount</a>: <i>Double</i>
    <a href="#trafficpercentage" title="TrafficPercentage">TrafficPercentage</a>: <i>Double</i>
    <a href="#endpointconfigurations" title="EndpointConfigurations">EndpointConfigurations</a>: <i>
      - <a href="endpointconfigurationsdefinition.md">EndpointConfigurationsDefinition</a></i>
    <a href="#portoverrides" title="PortOverrides">PortOverrides</a>: <i>
      - <a href="portoverridesdefinition.md">PortOverridesDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AcceleratorId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointGroupRegion

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointGroupType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointRequestProtocol

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

#### ListenerId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficPercentage

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointConfigurations

_Required_: No

_Type_: List of <a href="endpointconfigurationsdefinition.md">EndpointConfigurationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortOverrides

_Required_: No

_Type_: List of <a href="portoverridesdefinition.md">PortOverridesDefinition</a>

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

#### Status

Returns the <code>Status</code> value.

