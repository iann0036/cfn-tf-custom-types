# TF::AzureRM::ServiceFabricCluster NodeTypeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#capacities" title="Capacities">Capacities</a>" : <i>[ <a href="capacitiesdefinition.md">CapacitiesDefinition</a>, ... ]</i>,
    "<a href="#clientendpointport" title="ClientEndpointPort">ClientEndpointPort</a>" : <i>Double</i>,
    "<a href="#durabilitylevel" title="DurabilityLevel">DurabilityLevel</a>" : <i>String</i>,
    "<a href="#httpendpointport" title="HttpEndpointPort">HttpEndpointPort</a>" : <i>Double</i>,
    "<a href="#instancecount" title="InstanceCount">InstanceCount</a>" : <i>Double</i>,
    "<a href="#isprimary" title="IsPrimary">IsPrimary</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#placementproperties" title="PlacementProperties">PlacementProperties</a>" : <i>[ <a href="placementpropertiesdefinition.md">PlacementPropertiesDefinition</a>, ... ]</i>,
    "<a href="#reverseproxyendpointport" title="ReverseProxyEndpointPort">ReverseProxyEndpointPort</a>" : <i>Double</i>,
    "<a href="#applicationports" title="ApplicationPorts">ApplicationPorts</a>" : <i>[ <a href="applicationportsdefinition.md">ApplicationPortsDefinition</a>, ... ]</i>,
    "<a href="#ephemeralports" title="EphemeralPorts">EphemeralPorts</a>" : <i>[ <a href="ephemeralportsdefinition.md">EphemeralPortsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#capacities" title="Capacities">Capacities</a>: <i>
      - <a href="capacitiesdefinition.md">CapacitiesDefinition</a></i>
<a href="#clientendpointport" title="ClientEndpointPort">ClientEndpointPort</a>: <i>Double</i>
<a href="#durabilitylevel" title="DurabilityLevel">DurabilityLevel</a>: <i>String</i>
<a href="#httpendpointport" title="HttpEndpointPort">HttpEndpointPort</a>: <i>Double</i>
<a href="#instancecount" title="InstanceCount">InstanceCount</a>: <i>Double</i>
<a href="#isprimary" title="IsPrimary">IsPrimary</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#placementproperties" title="PlacementProperties">PlacementProperties</a>: <i>
      - <a href="placementpropertiesdefinition.md">PlacementPropertiesDefinition</a></i>
<a href="#reverseproxyendpointport" title="ReverseProxyEndpointPort">ReverseProxyEndpointPort</a>: <i>Double</i>
<a href="#applicationports" title="ApplicationPorts">ApplicationPorts</a>: <i>
      - <a href="applicationportsdefinition.md">ApplicationPortsDefinition</a></i>
<a href="#ephemeralports" title="EphemeralPorts">EphemeralPorts</a>: <i>
      - <a href="ephemeralportsdefinition.md">EphemeralPortsDefinition</a></i>
</pre>

## Properties

#### Capacities

The capacity tags applied to the nodes in the node type, the cluster resource manager uses these tags to understand how much resource a node has.

_Required_: No

_Type_: List of <a href="capacitiesdefinition.md">CapacitiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientEndpointPort

The Port used for the Client Endpoint for this Node Type. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DurabilityLevel

The Durability Level for this Node Type. Possible values include `Bronze`, `Gold` and `Silver`. Defaults to `Bronze`. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpEndpointPort

The Port used for the HTTP Endpoint for this Node Type. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceCount

The number of nodes for this Node Type.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsPrimary

Is this the Primary Node Type? Changing this forces a new resource to be created.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Node Type. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlacementProperties

The placement tags applied to nodes in the node type, which can be used to indicate where certain services (workload) should run.

_Required_: No

_Type_: List of <a href="placementpropertiesdefinition.md">PlacementPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReverseProxyEndpointPort

The Port used for the Reverse Proxy Endpoint  for this Node Type. Changing this will upgrade the cluster.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationPorts

_Required_: No

_Type_: List of <a href="applicationportsdefinition.md">ApplicationPortsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EphemeralPorts

_Required_: No

_Type_: List of <a href="ephemeralportsdefinition.md">EphemeralPortsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

