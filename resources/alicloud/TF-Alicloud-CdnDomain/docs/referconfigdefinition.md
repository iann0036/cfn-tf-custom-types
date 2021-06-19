# TF::Alicloud::CdnDomain ReferConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowempty" title="AllowEmpty">AllowEmpty</a>" : <i>String</i>,
    "<a href="#referlist" title="ReferList">ReferList</a>" : <i>[ String, ... ]</i>,
    "<a href="#refertype" title="ReferType">ReferType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#allowempty" title="AllowEmpty">AllowEmpty</a>: <i>String</i>
<a href="#referlist" title="ReferList">ReferList</a>: <i>
      - String</i>
<a href="#refertype" title="ReferType">ReferType</a>: <i>String</i>
</pre>

## Properties

#### AllowEmpty

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReferList

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReferType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

