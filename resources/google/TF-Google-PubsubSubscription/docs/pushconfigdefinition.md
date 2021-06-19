# TF::Google::PubsubSubscription PushConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#attributes" title="Attributes">Attributes</a>" : <i>[ <a href="attributesdefinition.md">AttributesDefinition</a>, ... ]</i>,
    "<a href="#pushendpoint" title="PushEndpoint">PushEndpoint</a>" : <i>String</i>,
    "<a href="#oidctoken" title="OidcToken">OidcToken</a>" : <i>[ <a href="oidctokendefinition.md">OidcTokenDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#attributes" title="Attributes">Attributes</a>: <i>
      - <a href="attributesdefinition.md">AttributesDefinition</a></i>
<a href="#pushendpoint" title="PushEndpoint">PushEndpoint</a>: <i>String</i>
<a href="#oidctoken" title="OidcToken">OidcToken</a>: <i>
      - <a href="oidctokendefinition.md">OidcTokenDefinition</a></i>
</pre>

## Properties

#### Attributes

_Required_: No

_Type_: List of <a href="attributesdefinition.md">AttributesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PushEndpoint

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OidcToken

_Required_: No

_Type_: List of <a href="oidctokendefinition.md">OidcTokenDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

