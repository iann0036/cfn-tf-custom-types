# TF::AVI::Authprofile SamlDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#idp" title="Idp">Idp</a>" : <i>[ <a href="idpdefinition.md">IdpDefinition</a>, ... ]</i>,
    "<a href="#sp" title="Sp">Sp</a>" : <i>[ <a href="spdefinition.md">SpDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#idp" title="Idp">Idp</a>: <i>
      - <a href="idpdefinition.md">IdpDefinition</a></i>
<a href="#sp" title="Sp">Sp</a>: <i>
      - <a href="spdefinition.md">SpDefinition</a></i>
</pre>

## Properties

#### Idp

_Required_: No

_Type_: List of <a href="idpdefinition.md">IdpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sp

_Required_: No

_Type_: List of <a href="spdefinition.md">SpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

