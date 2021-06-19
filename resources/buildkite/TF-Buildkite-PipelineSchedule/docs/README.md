# TF::Buildkite::PipelineSchedule

CloudFormation equivalent of buildkite_pipeline_schedule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Buildkite::PipelineSchedule",
    "Properties" : {
        "<a href="#branch" title="Branch">Branch</a>" : <i>String</i>,
        "<a href="#commit" title="Commit">Commit</a>" : <i>String</i>,
        "<a href="#cronline" title="Cronline">Cronline</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#env" title="Env">Env</a>" : <i>[ <a href="envdefinition.md">EnvDefinition</a>, ... ]</i>,
        "<a href="#label" title="Label">Label</a>" : <i>String</i>,
        "<a href="#message" title="Message">Message</a>" : <i>String</i>,
        "<a href="#pipelineid" title="PipelineId">PipelineId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Buildkite::PipelineSchedule
Properties:
    <a href="#branch" title="Branch">Branch</a>: <i>String</i>
    <a href="#commit" title="Commit">Commit</a>: <i>String</i>
    <a href="#cronline" title="Cronline">Cronline</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#env" title="Env">Env</a>: <i>
      - <a href="envdefinition.md">EnvDefinition</a></i>
    <a href="#label" title="Label">Label</a>: <i>String</i>
    <a href="#message" title="Message">Message</a>: <i>String</i>
    <a href="#pipelineid" title="PipelineId">PipelineId</a>: <i>String</i>
</pre>

## Properties

#### Branch

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Commit

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cronline

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Env

_Required_: No

_Type_: List of <a href="envdefinition.md">EnvDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Message

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PipelineId

_Required_: Yes

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

#### Uuid

Returns the <code>Uuid</code> value.

