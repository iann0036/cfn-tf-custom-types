# TF::Volterra::HttpLoadbalancer HeadersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#checknotpresent" title="CheckNotPresent">CheckNotPresent</a>" : <i>Boolean</i>,
    "<a href="#checkpresent" title="CheckPresent">CheckPresent</a>" : <i>Boolean</i>,
    "<a href="#invertmatcher" title="InvertMatcher">InvertMatcher</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#presence" title="Presence">Presence</a>" : <i>Boolean</i>,
    "<a href="#item" title="Item">Item</a>" : <i>[ <a href="itemdefinition.md">ItemDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#checknotpresent" title="CheckNotPresent">CheckNotPresent</a>: <i>Boolean</i>
<a href="#checkpresent" title="CheckPresent">CheckPresent</a>: <i>Boolean</i>
<a href="#invertmatcher" title="InvertMatcher">InvertMatcher</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#presence" title="Presence">Presence</a>: <i>Boolean</i>
<a href="#item" title="Item">Item</a>: <i>
      - <a href="itemdefinition.md">ItemDefinition</a></i>
</pre>

## Properties

#### CheckNotPresent

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckPresent

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InvertMatcher

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Presence

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Item

_Required_: No

_Type_: List of <a href="itemdefinition.md">ItemDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

