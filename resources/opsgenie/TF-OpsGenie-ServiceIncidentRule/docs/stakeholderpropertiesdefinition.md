# TF::OpsGenie::ServiceIncidentRule StakeholderPropertiesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#enable" title="Enable">Enable</a>" : <i>Boolean</i>,
    "<a href="#message" title="Message">Message</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#enable" title="Enable">Enable</a>: <i>Boolean</i>
<a href="#message" title="Message">Message</a>: <i>String</i>
</pre>

## Properties

#### Description

Description that is generally used to provide a detailed information about the alert.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enable

Option to enable stakeholder notifications.Default value is true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Message

Message that is to be passed to audience that is generally used to provide a content information about the alert.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

