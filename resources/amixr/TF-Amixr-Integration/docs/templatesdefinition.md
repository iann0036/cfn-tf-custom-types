# TF::Amixr::Integration TemplatesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#groupingkey" title="GroupingKey">GroupingKey</a>" : <i>String</i>,
    "<a href="#resolvesignal" title="ResolveSignal">ResolveSignal</a>" : <i>String</i>,
    "<a href="#slack" title="Slack">Slack</a>" : <i>[ <a href="slackdefinition.md">SlackDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#groupingkey" title="GroupingKey">GroupingKey</a>: <i>String</i>
<a href="#resolvesignal" title="ResolveSignal">ResolveSignal</a>: <i>String</i>
<a href="#slack" title="Slack">Slack</a>: <i>
      - <a href="slackdefinition.md">SlackDefinition</a></i>
</pre>

## Properties

#### GroupingKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResolveSignal

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slack

_Required_: No

_Type_: List of <a href="slackdefinition.md">SlackDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

