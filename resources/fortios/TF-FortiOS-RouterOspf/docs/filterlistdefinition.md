# TF::FortiOS::RouterOspf FilterListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#direction" title="Direction">Direction</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#list" title="List">List</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#direction" title="Direction">Direction</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#list" title="List">List</a>: <i>String</i>
</pre>

## Properties

#### Direction

Direction. Valid values: `in`, `out`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Filter list entry ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### List

Access-list or prefix-list name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

