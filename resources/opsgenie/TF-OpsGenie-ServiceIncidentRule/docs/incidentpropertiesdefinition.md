# TF::OpsGenie::ServiceIncidentRule IncidentPropertiesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#details" title="Details">Details</a>" : <i>[ <a href="detailsdefinition.md">DetailsDefinition</a>, ... ]</i>,
    "<a href="#message" title="Message">Message</a>" : <i>String</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>String</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
    "<a href="#stakeholderproperties" title="StakeholderProperties">StakeholderProperties</a>" : <i>[ <a href="stakeholderpropertiesdefinition.md">StakeholderPropertiesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#details" title="Details">Details</a>: <i>
      - <a href="detailsdefinition.md">DetailsDefinition</a></i>
<a href="#message" title="Message">Message</a>: <i>String</i>
<a href="#priority" title="Priority">Priority</a>: <i>String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
<a href="#stakeholderproperties" title="StakeholderProperties">StakeholderProperties</a>: <i>
      - <a href="stakeholderpropertiesdefinition.md">StakeholderPropertiesDefinition</a></i>
</pre>

## Properties

#### Description

Description field of the incident rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Details

Map of key-value pairs to use as custom properties of the alert.

_Required_: No

_Type_: List of <a href="detailsdefinition.md">DetailsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Message

Message of the related incident rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

Priority level of the alert. Possible values are `P1`, `P2`, `P3`, `P4` and `P5`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Tags of the alert.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StakeholderProperties

_Required_: No

_Type_: List of <a href="stakeholderpropertiesdefinition.md">StakeholderPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

