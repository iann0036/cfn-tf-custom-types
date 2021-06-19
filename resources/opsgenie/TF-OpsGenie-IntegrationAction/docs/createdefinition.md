# TF::OpsGenie::IntegrationAction CreateDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#alertactions" title="AlertActions">AlertActions</a>" : <i>[ String, ... ]</i>,
    "<a href="#alias" title="Alias">Alias</a>" : <i>String</i>,
    "<a href="#appendattachments" title="AppendAttachments">AppendAttachments</a>" : <i>Boolean</i>,
    "<a href="#custompriority" title="CustomPriority">CustomPriority</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#entity" title="Entity">Entity</a>" : <i>String</i>,
    "<a href="#extraproperties" title="ExtraProperties">ExtraProperties</a>" : <i>[ <a href="extrapropertiesdefinition.md">ExtraPropertiesDefinition</a>, ... ]</i>,
    "<a href="#ignorealertactionsfrompayload" title="IgnoreAlertActionsFromPayload">IgnoreAlertActionsFromPayload</a>" : <i>Boolean</i>,
    "<a href="#ignoreextrapropertiesfrompayload" title="IgnoreExtraPropertiesFromPayload">IgnoreExtraPropertiesFromPayload</a>" : <i>Boolean</i>,
    "<a href="#ignorerespondersfrompayload" title="IgnoreRespondersFromPayload">IgnoreRespondersFromPayload</a>" : <i>Boolean</i>,
    "<a href="#ignoretagsfrompayload" title="IgnoreTagsFromPayload">IgnoreTagsFromPayload</a>" : <i>Boolean</i>,
    "<a href="#ignoreteamsfrompayload" title="IgnoreTeamsFromPayload">IgnoreTeamsFromPayload</a>" : <i>Boolean</i>,
    "<a href="#message" title="Message">Message</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#note" title="Note">Note</a>" : <i>String</i>,
    "<a href="#order" title="Order">Order</a>" : <i>Double</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>String</i>,
    "<a href="#source" title="Source">Source</a>" : <i>String</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#user" title="User">User</a>" : <i>String</i>,
    "<a href="#filter" title="Filter">Filter</a>" : <i>[ <a href="filterdefinition.md">FilterDefinition</a>, ... ]</i>,
    "<a href="#responders" title="Responders">Responders</a>" : <i>[ <a href="respondersdefinition.md">RespondersDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#alertactions" title="AlertActions">AlertActions</a>: <i>
      - String</i>
<a href="#alias" title="Alias">Alias</a>: <i>String</i>
<a href="#appendattachments" title="AppendAttachments">AppendAttachments</a>: <i>Boolean</i>
<a href="#custompriority" title="CustomPriority">CustomPriority</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#entity" title="Entity">Entity</a>: <i>String</i>
<a href="#extraproperties" title="ExtraProperties">ExtraProperties</a>: <i>
      - <a href="extrapropertiesdefinition.md">ExtraPropertiesDefinition</a></i>
<a href="#ignorealertactionsfrompayload" title="IgnoreAlertActionsFromPayload">IgnoreAlertActionsFromPayload</a>: <i>Boolean</i>
<a href="#ignoreextrapropertiesfrompayload" title="IgnoreExtraPropertiesFromPayload">IgnoreExtraPropertiesFromPayload</a>: <i>Boolean</i>
<a href="#ignorerespondersfrompayload" title="IgnoreRespondersFromPayload">IgnoreRespondersFromPayload</a>: <i>Boolean</i>
<a href="#ignoretagsfrompayload" title="IgnoreTagsFromPayload">IgnoreTagsFromPayload</a>: <i>Boolean</i>
<a href="#ignoreteamsfrompayload" title="IgnoreTeamsFromPayload">IgnoreTeamsFromPayload</a>: <i>Boolean</i>
<a href="#message" title="Message">Message</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#note" title="Note">Note</a>: <i>String</i>
<a href="#order" title="Order">Order</a>: <i>Double</i>
<a href="#priority" title="Priority">Priority</a>: <i>String</i>
<a href="#source" title="Source">Source</a>: <i>String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#user" title="User">User</a>: <i>String</i>
<a href="#filter" title="Filter">Filter</a>: <i>
      - <a href="filterdefinition.md">FilterDefinition</a></i>
<a href="#responders" title="Responders">Responders</a>: <i>
      - <a href="respondersdefinition.md">RespondersDefinition</a></i>
</pre>

## Properties

#### AlertActions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Alias

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppendAttachments

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomPriority

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Entity

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraProperties

_Required_: No

_Type_: List of <a href="extrapropertiesdefinition.md">ExtraPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreAlertActionsFromPayload

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreExtraPropertiesFromPayload

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreRespondersFromPayload

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreTagsFromPayload

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreTeamsFromPayload

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Message

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Note

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Order

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No

_Type_: List of <a href="filterdefinition.md">FilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Responders

_Required_: No

_Type_: List of <a href="respondersdefinition.md">RespondersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

