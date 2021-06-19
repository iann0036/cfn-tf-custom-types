# TF::AWS::EmrManagedScalingPolicy ComputeLimitsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maximumcapacityunits" title="MaximumCapacityUnits">MaximumCapacityUnits</a>" : <i>Double</i>,
    "<a href="#maximumcorecapacityunits" title="MaximumCoreCapacityUnits">MaximumCoreCapacityUnits</a>" : <i>Double</i>,
    "<a href="#maximumondemandcapacityunits" title="MaximumOndemandCapacityUnits">MaximumOndemandCapacityUnits</a>" : <i>Double</i>,
    "<a href="#minimumcapacityunits" title="MinimumCapacityUnits">MinimumCapacityUnits</a>" : <i>Double</i>,
    "<a href="#unittype" title="UnitType">UnitType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#maximumcapacityunits" title="MaximumCapacityUnits">MaximumCapacityUnits</a>: <i>Double</i>
<a href="#maximumcorecapacityunits" title="MaximumCoreCapacityUnits">MaximumCoreCapacityUnits</a>: <i>Double</i>
<a href="#maximumondemandcapacityunits" title="MaximumOndemandCapacityUnits">MaximumOndemandCapacityUnits</a>: <i>Double</i>
<a href="#minimumcapacityunits" title="MinimumCapacityUnits">MinimumCapacityUnits</a>: <i>Double</i>
<a href="#unittype" title="UnitType">UnitType</a>: <i>String</i>
</pre>

## Properties

#### MaximumCapacityUnits

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumCoreCapacityUnits

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumOndemandCapacityUnits

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinimumCapacityUnits

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnitType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

