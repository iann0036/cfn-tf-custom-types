# TF::Nomad::SchedulerConfig

Manages scheduler configuration of the Nomad cluster.

~> **Warning:** destroying this resource will not have any effect in the
cluster configuration, since there's no clear definition of what a destroy
action should do. The cluster will be left as-is and only the state reference
will be removed.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Nomad::SchedulerConfig",
    "Properties" : {
        "<a href="#memoryoversubscriptionenabled" title="MemoryOversubscriptionEnabled">MemoryOversubscriptionEnabled</a>" : <i>Boolean</i>,
        "<a href="#preemptionconfig" title="PreemptionConfig">PreemptionConfig</a>" : <i>[ <a href="preemptionconfigdefinition.md">PreemptionConfigDefinition</a>, ... ]</i>,
        "<a href="#scheduleralgorithm" title="SchedulerAlgorithm">SchedulerAlgorithm</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Nomad::SchedulerConfig
Properties:
    <a href="#memoryoversubscriptionenabled" title="MemoryOversubscriptionEnabled">MemoryOversubscriptionEnabled</a>: <i>Boolean</i>
    <a href="#preemptionconfig" title="PreemptionConfig">PreemptionConfig</a>: <i>
      - <a href="preemptionconfigdefinition.md">PreemptionConfigDefinition</a></i>
    <a href="#scheduleralgorithm" title="SchedulerAlgorithm">SchedulerAlgorithm</a>: <i>String</i>
</pre>

## Properties

#### MemoryOversubscriptionEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreemptionConfig

_Required_: No

_Type_: List of <a href="preemptionconfigdefinition.md">PreemptionConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchedulerAlgorithm

_Required_: No

_Type_: String

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

