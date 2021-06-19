# TF::Thunder::VrrpVrid BladeParametersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#failoverpolicytemplate" title="FailOverPolicyTemplate">FailOverPolicyTemplate</a>" : <i>String</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#trackingoptions" title="TrackingOptions">TrackingOptions</a>" : <i>[ <a href="trackingoptionsdefinition.md">TrackingOptionsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#failoverpolicytemplate" title="FailOverPolicyTemplate">FailOverPolicyTemplate</a>: <i>String</i>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
<a href="#trackingoptions" title="TrackingOptions">TrackingOptions</a>: <i>
      - <a href="trackingoptionsdefinition.md">TrackingOptionsDefinition</a></i>
</pre>

## Properties

#### FailOverPolicyTemplate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrackingOptions

_Required_: No

_Type_: List of <a href="trackingoptionsdefinition.md">TrackingOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

