# TF::GoogleBeta::GoogleAccessContextManagerServicePerimeter IngressFromDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#identities" title="Identities">Identities</a>" : <i>[ String, ... ]</i>,
    "<a href="#identitytype" title="IdentityType">IdentityType</a>" : <i>String</i>,
    "<a href="#sources" title="Sources">Sources</a>" : <i>[ <a href="sourcesdefinition.md">SourcesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#identities" title="Identities">Identities</a>: <i>
      - String</i>
<a href="#identitytype" title="IdentityType">IdentityType</a>: <i>String</i>
<a href="#sources" title="Sources">Sources</a>: <i>
      - <a href="sourcesdefinition.md">SourcesDefinition</a></i>
</pre>

## Properties

#### Identities

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdentityType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sources

_Required_: No

_Type_: List of <a href="sourcesdefinition.md">SourcesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

