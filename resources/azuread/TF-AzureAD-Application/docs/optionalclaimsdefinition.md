# TF::AzureAD::Application OptionalClaimsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accesstoken" title="AccessToken">AccessToken</a>" : <i>[ <a href="accesstokendefinition.md">AccessTokenDefinition</a>, ... ]</i>,
    "<a href="#idtoken" title="IdToken">IdToken</a>" : <i>[ <a href="idtokendefinition.md">IdTokenDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#accesstoken" title="AccessToken">AccessToken</a>: <i>
      - <a href="accesstokendefinition.md">AccessTokenDefinition</a></i>
<a href="#idtoken" title="IdToken">IdToken</a>: <i>
      - <a href="idtokendefinition.md">IdTokenDefinition</a></i>
</pre>

## Properties

#### AccessToken

_Required_: No

_Type_: List of <a href="accesstokendefinition.md">AccessTokenDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdToken

_Required_: No

_Type_: List of <a href="idtokendefinition.md">IdTokenDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

