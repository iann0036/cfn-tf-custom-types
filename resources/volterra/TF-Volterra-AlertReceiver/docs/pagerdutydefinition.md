# TF::Volterra::AlertReceiver PagerdutyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#url" title="Url">Url</a>" : <i>String</i>,
    "<a href="#routingkey" title="RoutingKey">RoutingKey</a>" : <i>[ <a href="routingkeydefinition.md">RoutingKeyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#url" title="Url">Url</a>: <i>String</i>
<a href="#routingkey" title="RoutingKey">RoutingKey</a>: <i>
      - <a href="routingkeydefinition.md">RoutingKeyDefinition</a></i>
</pre>

## Properties

#### Url

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoutingKey

_Required_: No

_Type_: List of <a href="routingkeydefinition.md">RoutingKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

