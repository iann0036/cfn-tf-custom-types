# TF::AWS::Kinesisanalyticsv2Application FlinkRunConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allownonrestoredstate" title="AllowNonRestoredState">AllowNonRestoredState</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#allownonrestoredstate" title="AllowNonRestoredState">AllowNonRestoredState</a>: <i>Boolean</i>
</pre>

## Properties

#### AllowNonRestoredState

When restoring from a snapshot, specifies whether the runtime is allowed to skip a state that cannot be mapped to the new program. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

