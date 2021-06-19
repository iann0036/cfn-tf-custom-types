# TF::Volterra::Discovery PublishInfoDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disable" title="Disable">Disable</a>" : <i>Boolean</i>,
    "<a href="#publishfqdns" title="PublishFqdns">PublishFqdns</a>" : <i>Boolean</i>,
    "<a href="#dnsdelegation" title="DnsDelegation">DnsDelegation</a>" : <i>[ <a href="dnsdelegationdefinition.md">DnsDelegationDefinition</a>, ... ]</i>,
    "<a href="#publish" title="Publish">Publish</a>" : <i>[ <a href="publishdefinition.md">PublishDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#disable" title="Disable">Disable</a>: <i>Boolean</i>
<a href="#publishfqdns" title="PublishFqdns">PublishFqdns</a>: <i>Boolean</i>
<a href="#dnsdelegation" title="DnsDelegation">DnsDelegation</a>: <i>
      - <a href="dnsdelegationdefinition.md">DnsDelegationDefinition</a></i>
<a href="#publish" title="Publish">Publish</a>: <i>
      - <a href="publishdefinition.md">PublishDefinition</a></i>
</pre>

## Properties

#### Disable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublishFqdns

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsDelegation

_Required_: No

_Type_: List of <a href="dnsdelegationdefinition.md">DnsDelegationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Publish

_Required_: No

_Type_: List of <a href="publishdefinition.md">PublishDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

