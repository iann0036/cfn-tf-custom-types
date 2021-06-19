# TF::GoogleBeta::GoogleCloudSchedulerJob PubsubTargetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#attributes" title="Attributes">Attributes</a>" : <i>[ <a href="attributesdefinition.md">AttributesDefinition</a>, ... ]</i>,
    "<a href="#data" title="Data">Data</a>" : <i>String</i>,
    "<a href="#topicname" title="TopicName">TopicName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#attributes" title="Attributes">Attributes</a>: <i>
      - <a href="attributesdefinition.md">AttributesDefinition</a></i>
<a href="#data" title="Data">Data</a>: <i>String</i>
<a href="#topicname" title="TopicName">TopicName</a>: <i>String</i>
</pre>

## Properties

#### Attributes

_Required_: No

_Type_: List of <a href="attributesdefinition.md">AttributesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Data

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopicName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

