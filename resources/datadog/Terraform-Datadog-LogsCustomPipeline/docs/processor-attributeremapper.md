# Terraform::Datadog::LogsCustomPipeline Processor AttributeRemapper

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#overrideonconflict" title="OverrideOnConflict">OverrideOnConflict</a>" : <i>Boolean</i>,
    "<a href="#preservesource" title="PreserveSource">PreserveSource</a>" : <i>Boolean</i>,
    "<a href="#sourcetype" title="SourceType">SourceType</a>" : <i>String</i>,
    "<a href="#sources" title="Sources">Sources</a>" : <i>[ String, ... ]</i>,
    "<a href="#target" title="Target">Target</a>" : <i>String</i>,
    "<a href="#targettype" title="TargetType">TargetType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#overrideonconflict" title="OverrideOnConflict">OverrideOnConflict</a>: <i>Boolean</i>
<a href="#preservesource" title="PreserveSource">PreserveSource</a>: <i>Boolean</i>
<a href="#sourcetype" title="SourceType">SourceType</a>: <i>String</i>
<a href="#sources" title="Sources">Sources</a>: <i>
      - String</i>
<a href="#target" title="Target">Target</a>: <i>String</i>
<a href="#targettype" title="TargetType">TargetType</a>: <i>String</i>
</pre>

## Properties

#### IsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideOnConflict

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreserveSource

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sources

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

