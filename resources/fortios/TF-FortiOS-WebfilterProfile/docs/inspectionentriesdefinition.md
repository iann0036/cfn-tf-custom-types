# TF::FortiOS::WebfilterProfile InspectionEntriesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#fortiguardcategory" title="FortiguardCategory">FortiguardCategory</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#fortiguardcategory" title="FortiguardCategory">FortiguardCategory</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### Action

Action to be taken upon an AntiPhishing match. Valid values: `exempt`, `log`, `block`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FortiguardCategory

FortiGuard category to match.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Inspection target name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

