# Terraform::Datadog::LogsIndex

Provides a Datadog [Logs Index API](https://docs.datadoghq.com/api/?lang=python#logs-indexes) resource. This can be used to create and manage Datadog logs indexes.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Datadog::LogsIndex",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#exclusionfilter" title="ExclusionFilter">ExclusionFilter</a>" : <i>[ <a href="exclusionfilter.md">ExclusionFilter</a>, ... ]</i>,
        "<a href="#filter" title="Filter">Filter</a>" : <i>[ <a href="filter.md">Filter</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Datadog::LogsIndex
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#exclusionfilter" title="ExclusionFilter">ExclusionFilter</a>: <i>
      - <a href="exclusionfilter.md">ExclusionFilter</a></i>
    <a href="#filter" title="Filter">Filter</a>: <i>
      - <a href="filter.md">Filter</a></i>
</pre>

## Properties

#### Name

The name of the exclusion filter.
* `is_enabled` - (Optional, default = false) A boolean stating if the exclusion is active or not.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExclusionFilter

_Required_: No

_Type_: List of <a href="exclusionfilter.md">ExclusionFilter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No

_Type_: List of <a href="filter.md">Filter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

