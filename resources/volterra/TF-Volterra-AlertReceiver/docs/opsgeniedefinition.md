# TF::Volterra::AlertReceiver OpsgenieDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#url" title="Url">Url</a>" : <i>String</i>,
    "<a href="#apikey" title="ApiKey">ApiKey</a>" : <i>[ <a href="apikeydefinition.md">ApiKeyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#url" title="Url">Url</a>: <i>String</i>
<a href="#apikey" title="ApiKey">ApiKey</a>: <i>
      - <a href="apikeydefinition.md">ApiKeyDefinition</a></i>
</pre>

## Properties

#### Url

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiKey

_Required_: No

_Type_: List of <a href="apikeydefinition.md">ApiKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

