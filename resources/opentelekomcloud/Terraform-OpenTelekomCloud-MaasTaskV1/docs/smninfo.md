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

Specifies the management console language used by the
current users. Users can select en-us.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopicUrn

Specifies the SMN message topic URN bound to a migration
task.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggerConditions

Specifies the trigger conditions of sending messages
using SMN. The value depending on the state of a migration task. The migration task
status can be SUCCESS or FAIL.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

