# TF::GoogleBeta::GoogleMonitoringSlo BasicSliDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#location" title="Location">Location</a>" : <i>[ String, ... ]</i>,
    "<a href="#method" title="Method">Method</a>" : <i>[ String, ... ]</i>,
    "<a href="#version" title="Version">Version</a>" : <i>[ String, ... ]</i>,
    "<a href="#availability" title="Availability">Availability</a>" : <i>[ <a href="availabilitydefinition.md">AvailabilityDefinition</a>, ... ]</i>,
    "<a href="#latency" title="Latency">Latency</a>" : <i>[ <a href="latencydefinition.md">LatencyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#location" title="Location">Location</a>: <i>
      - String</i>
<a href="#method" title="Method">Method</a>: <i>
      - String</i>
<a href="#version" title="Version">Version</a>: <i>
      - String</i>
<a href="#availability" title="Availability">Availability</a>: <i>
      - <a href="availabilitydefinition.md">AvailabilityDefinition</a></i>
<a href="#latency" title="Latency">Latency</a>: <i>
      - <a href="latencydefinition.md">LatencyDefinition</a></i>
</pre>

## Properties

#### Location

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Method

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Availability

_Required_: No

_Type_: List of <a href="availabilitydefinition.md">AvailabilityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Latency

_Required_: No

_Type_: List of <a href="latencydefinition.md">LatencyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

