# TF::FortiOS::IcapProfile HeaderGroupDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#casesensitivity" title="CaseSensitivity">CaseSensitivity</a>" : <i>String</i>,
    "<a href="#header" title="Header">Header</a>" : <i>String</i>,
    "<a href="#headername" title="HeaderName">HeaderName</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#casesensitivity" title="CaseSensitivity">CaseSensitivity</a>: <i>String</i>
<a href="#header" title="Header">Header</a>: <i>String</i>
<a href="#headername" title="HeaderName">HeaderName</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
</pre>

## Properties

#### CaseSensitivity

Enable/disable case sensitivity when matching header. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Header

HTTP header regular expression.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderName

HTTP header.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

