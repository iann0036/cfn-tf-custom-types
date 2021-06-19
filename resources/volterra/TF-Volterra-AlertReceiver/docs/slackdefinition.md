# TF::Volterra::AlertReceiver SlackDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#channel" title="Channel">Channel</a>" : <i>String</i>,
    "<a href="#url" title="Url">Url</a>" : <i>[ <a href="urldefinition.md">UrlDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#channel" title="Channel">Channel</a>: <i>String</i>
<a href="#url" title="Url">Url</a>: <i>
      - <a href="urldefinition.md">UrlDefinition</a></i>
</pre>

## Properties

#### Channel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

_Required_: No

_Type_: List of <a href="urldefinition.md">UrlDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

