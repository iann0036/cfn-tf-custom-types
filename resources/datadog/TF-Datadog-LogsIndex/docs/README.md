# TF::Datadog::LogsIndex

CloudFormation equivalent of datadog_logs_index

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Datadog::LogsIndex",
    "Properties" : {
        "<a href="#dailylimit" title="DailyLimit">DailyLimit</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#retentiondays" title="RetentionDays">RetentionDays</a>" : <i>String</i>,
        "<a href="#exclusionfilter" title="ExclusionFilter">ExclusionFilter</a>" : <i>[ <a href="exclusionfilterdefinition.md">ExclusionFilterDefinition</a>, ... ]</i>,
        "<a href="#filter" title="Filter">Filter</a>" : <i>[ <a href="filterdefinition.md">FilterDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Datadog::LogsIndex
Properties:
    <a href="#dailylimit" title="DailyLimit">DailyLimit</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#retentiondays" title="RetentionDays">RetentionDays</a>: <i>String</i>
    <a href="#exclusionfilter" title="ExclusionFilter">ExclusionFilter</a>: <i>
      - <a href="exclusionfilterdefinition.md">ExclusionFilterDefinition</a></i>
    <a href="#filter" title="Filter">Filter</a>: <i>
      - <a href="filterdefinition.md">FilterDefinition</a></i>
</pre>

## Properties

#### DailyLimit

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionDays

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExclusionFilter

_Required_: No

_Type_: List of <a href="exclusionfilterdefinition.md">ExclusionFilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No

_Type_: List of <a href="filterdefinition.md">FilterDefinition</a>

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

