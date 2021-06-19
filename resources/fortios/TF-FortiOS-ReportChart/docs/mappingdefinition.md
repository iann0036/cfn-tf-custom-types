# TF::FortiOS::ReportChart MappingDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#displayname" title="Displayname">Displayname</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#op" title="Op">Op</a>" : <i>String</i>,
    "<a href="#value1" title="Value1">Value1</a>" : <i>String</i>,
    "<a href="#value2" title="Value2">Value2</a>" : <i>String</i>,
    "<a href="#valuetype" title="ValueType">ValueType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#displayname" title="Displayname">Displayname</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#op" title="Op">Op</a>: <i>String</i>
<a href="#value1" title="Value1">Value1</a>: <i>String</i>
<a href="#value2" title="Value2">Value2</a>: <i>String</i>
<a href="#valuetype" title="ValueType">ValueType</a>: <i>String</i>
</pre>

## Properties

#### Displayname

Display name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Op

Comparision operater. Valid values: `none`, `greater`, `greater-equal`, `less`, `less-equal`, `equal`, `between`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value1

Value 1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value2

Value 2.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValueType

Value type. Valid values: `integer`, `string`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

