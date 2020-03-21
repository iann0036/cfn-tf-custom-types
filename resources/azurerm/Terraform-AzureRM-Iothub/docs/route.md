# Terraform::AzureRM::Iothub Route

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#condition" title="Condition">Condition</a>" : <i>String</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#endpointnames" title="EndpointNames">EndpointNames</a>" : <i>[ String, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#source" title="Source">Source</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#condition" title="Condition">Condition</a>: <i>String</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#endpointnames" title="EndpointNames">EndpointNames</a>: <i>
      - String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#source" title="Source">Source</a>: <i>String</i>
</pre>

## Properties

#### Condition

The condition that is evaluated to apply the routing rule. If no condition is provided, it evaluates to true by default. For grammar, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Used to specify whether a route is enabled.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointNames

The list of endpoints to which messages that satisfy the condition are routed.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the route.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

The source that the routing rule is to be applied to, such as `DeviceMessages`. Possible values include: `RoutingSourceInvalid`, `RoutingSourceDeviceMessages`, `RoutingSourceTwinChangeEvents`, `RoutingSourceDeviceLifecycleEvents`, `RoutingSourceDeviceJobLifecycleEvents`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

