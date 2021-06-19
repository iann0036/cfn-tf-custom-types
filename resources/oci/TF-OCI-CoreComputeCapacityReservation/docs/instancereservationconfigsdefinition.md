# TF::OCI::CoreComputeCapacityReservation InstanceReservationConfigsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#faultdomain" title="FaultDomain">FaultDomain</a>" : <i>String</i>,
    "<a href="#instanceshape" title="InstanceShape">InstanceShape</a>" : <i>String</i>,
    "<a href="#reservedcount" title="ReservedCount">ReservedCount</a>" : <i>String</i>,
    "<a href="#instanceshapeconfig" title="InstanceShapeConfig">InstanceShapeConfig</a>" : <i>[ <a href="instanceshapeconfigdefinition.md">InstanceShapeConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#faultdomain" title="FaultDomain">FaultDomain</a>: <i>String</i>
<a href="#instanceshape" title="InstanceShape">InstanceShape</a>: <i>String</i>
<a href="#reservedcount" title="ReservedCount">ReservedCount</a>: <i>String</i>
<a href="#instanceshapeconfig" title="InstanceShapeConfig">InstanceShapeConfig</a>: <i>
      - <a href="instanceshapeconfigdefinition.md">InstanceShapeConfigDefinition</a></i>
</pre>

## Properties

#### FaultDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceShape

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReservedCount

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceShapeConfig

_Required_: No

_Type_: List of <a href="instanceshapeconfigdefinition.md">InstanceShapeConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

