# TF::Google::ComputeBackendService BackendDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#balancingmode" title="BalancingMode">BalancingMode</a>" : <i>String</i>,
    "<a href="#capacityscaler" title="CapacityScaler">CapacityScaler</a>" : <i>Double</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#group" title="Group">Group</a>" : <i>String</i>,
    "<a href="#maxconnections" title="MaxConnections">MaxConnections</a>" : <i>Double</i>,
    "<a href="#maxconnectionsperendpoint" title="MaxConnectionsPerEndpoint">MaxConnectionsPerEndpoint</a>" : <i>Double</i>,
    "<a href="#maxconnectionsperinstance" title="MaxConnectionsPerInstance">MaxConnectionsPerInstance</a>" : <i>Double</i>,
    "<a href="#maxrate" title="MaxRate">MaxRate</a>" : <i>Double</i>,
    "<a href="#maxrateperendpoint" title="MaxRatePerEndpoint">MaxRatePerEndpoint</a>" : <i>Double</i>,
    "<a href="#maxrateperinstance" title="MaxRatePerInstance">MaxRatePerInstance</a>" : <i>Double</i>,
    "<a href="#maxutilization" title="MaxUtilization">MaxUtilization</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#balancingmode" title="BalancingMode">BalancingMode</a>: <i>String</i>
<a href="#capacityscaler" title="CapacityScaler">CapacityScaler</a>: <i>Double</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#group" title="Group">Group</a>: <i>String</i>
<a href="#maxconnections" title="MaxConnections">MaxConnections</a>: <i>Double</i>
<a href="#maxconnectionsperendpoint" title="MaxConnectionsPerEndpoint">MaxConnectionsPerEndpoint</a>: <i>Double</i>
<a href="#maxconnectionsperinstance" title="MaxConnectionsPerInstance">MaxConnectionsPerInstance</a>: <i>Double</i>
<a href="#maxrate" title="MaxRate">MaxRate</a>: <i>Double</i>
<a href="#maxrateperendpoint" title="MaxRatePerEndpoint">MaxRatePerEndpoint</a>: <i>Double</i>
<a href="#maxrateperinstance" title="MaxRatePerInstance">MaxRatePerInstance</a>: <i>Double</i>
<a href="#maxutilization" title="MaxUtilization">MaxUtilization</a>: <i>Double</i>
</pre>

## Properties

#### BalancingMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapacityScaler

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConnections

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConnectionsPerEndpoint

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConnectionsPerInstance

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRatePerEndpoint

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRatePerInstance

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxUtilization

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

