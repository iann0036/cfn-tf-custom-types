# Terraform::OpenTelekomCloud::MaasTaskV1 SmnInfo

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#language" title="Language">Language</a>" : <i>String</i>,
    "<a href="#topicurn" title="TopicUrn">TopicUrn</a>" : <i>String</i>,
    "<a href="#triggerconditions" title="TriggerConditions">TriggerConditions</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#language" title="Language">Language</a>: <i>String</i>
<a href="#topicurn" title="TopicUrn">TopicUrn</a>: <i>String</i>
<a href="#triggerconditions" title="TriggerConditions">TriggerConditions</a>: <i>
      - String</i>
</pre>

## Properties

#### Language

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopicUrn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggerConditions

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

