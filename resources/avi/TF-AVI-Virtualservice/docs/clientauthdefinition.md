# TF::AVI::Virtualservice ClientAuthDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authprofileref" title="AuthProfileRef">AuthProfileRef</a>" : <i>String</i>,
    "<a href="#realm" title="Realm">Realm</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#requesturipath" title="RequestUriPath">RequestUriPath</a>" : <i>[ <a href="requesturipathdefinition.md">RequestUriPathDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#authprofileref" title="AuthProfileRef">AuthProfileRef</a>: <i>String</i>
<a href="#realm" title="Realm">Realm</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#requesturipath" title="RequestUriPath">RequestUriPath</a>: <i>
      - <a href="requesturipathdefinition.md">RequestUriPathDefinition</a></i>
</pre>

## Properties

#### AuthProfileRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Realm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestUriPath

_Required_: No

_Type_: List of <a href="requesturipathdefinition.md">RequestUriPathDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

