# TF::Spotinst::MultaiTargetSet HealthCheckDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#healthythreshold" title="HealthyThreshold">HealthyThreshold</a>" : <i>Double</i>,
    "<a href="#interval" title="Interval">Interval</a>" : <i>Double</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
    "<a href="#unhealthythreshold" title="UnhealthyThreshold">UnhealthyThreshold</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#healthythreshold" title="HealthyThreshold">HealthyThreshold</a>: <i>Double</i>
<a href="#interval" title="Interval">Interval</a>: <i>Double</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
<a href="#unhealthythreshold" title="UnhealthyThreshold">UnhealthyThreshold</a>: <i>Double</i>
</pre>

## Properties

#### HealthyThreshold

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interval

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnhealthyThreshold

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

