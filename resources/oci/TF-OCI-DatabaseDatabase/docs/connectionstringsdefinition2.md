# TF::OCI::DatabaseDatabase ConnectionStringsDefinition2

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allconnectionstrings" title="AllConnectionStrings">AllConnectionStrings</a>" : <i>[ <a href="connectionstringsdefinition.md">ConnectionStringsDefinition</a>, ... ]</i>,
    "<a href="#cdbdefault" title="CdbDefault">CdbDefault</a>" : <i>String</i>,
    "<a href="#cdbipdefault" title="CdbIpDefault">CdbIpDefault</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#allconnectionstrings" title="AllConnectionStrings">AllConnectionStrings</a>: <i>
      - <a href="connectionstringsdefinition.md">ConnectionStringsDefinition</a></i>
<a href="#cdbdefault" title="CdbDefault">CdbDefault</a>: <i>String</i>
<a href="#cdbipdefault" title="CdbIpDefault">CdbIpDefault</a>: <i>String</i>
</pre>

## Properties

#### AllConnectionStrings

_Required_: No

_Type_: List of <a href="connectionstringsdefinition.md">ConnectionStringsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CdbDefault

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CdbIpDefault

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

