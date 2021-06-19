# TF::FortiOS::ReportDataset ParametersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#datatype" title="DataType">DataType</a>" : <i>String</i>,
    "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
    "<a href="#field" title="Field">Field</a>" : <i>[ <a href="fielddefinition.md">FieldDefinition</a>, ... ]</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#datatype" title="DataType">DataType</a>: <i>String</i>
<a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
<a href="#field" title="Field">Field</a>: <i>
      - <a href="fielddefinition.md">FieldDefinition</a></i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
</pre>

## Properties

#### DataType

Data type. Valid values: `text`, `integer`, `double`, `long-integer`, `date-time`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

Display name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Field

_Required_: No

_Type_: List of <a href="fielddefinition.md">FieldDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Parameter ID (1 to number of columns in SQL result).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

