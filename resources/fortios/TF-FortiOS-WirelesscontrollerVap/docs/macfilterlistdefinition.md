# TF::FortiOS::WirelesscontrollerVap MacFilterListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#mac" title="Mac">Mac</a>" : <i>String</i>,
    "<a href="#macfilterpolicy" title="MacFilterPolicy">MacFilterPolicy</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#mac" title="Mac">Mac</a>: <i>String</i>
<a href="#macfilterpolicy" title="MacFilterPolicy">MacFilterPolicy</a>: <i>String</i>
</pre>

## Properties

#### Id

ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mac

MAC address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacFilterPolicy

Deny or allow the client with this MAC address. Valid values: `allow`, `deny`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

