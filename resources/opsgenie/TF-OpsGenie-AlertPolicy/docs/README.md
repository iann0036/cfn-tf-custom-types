# TF::OpsGenie::AlertPolicy

Manages a Alert Policy within Opsgenie.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OpsGenie::AlertPolicy",
    "Properties" : {
        "<a href="#actions" title="Actions">Actions</a>" : <i>[ String, ... ]</i>,
        "<a href="#alertdescription" title="AlertDescription">AlertDescription</a>" : <i>String</i>,
        "<a href="#alias" title="Alias">Alias</a>" : <i>String</i>,
        "<a href="#continuepolicy" title="ContinuePolicy">ContinuePolicy</a>" : <i>Boolean</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#entity" title="Entity">Entity</a>" : <i>String</i>,
        "<a href="#ignoreoriginalactions" title="IgnoreOriginalActions">IgnoreOriginalActions</a>" : <i>Boolean</i>,
        "<a href="#ignoreoriginaldetails" title="IgnoreOriginalDetails">IgnoreOriginalDetails</a>" : <i>Boolean</i>,
        "<a href="#ignoreoriginalresponders" title="IgnoreOriginalResponders">IgnoreOriginalResponders</a>" : <i>Boolean</i>,
        "<a href="#ignoreoriginaltags" title="IgnoreOriginalTags">IgnoreOriginalTags</a>" : <i>Boolean</i>,
        "<a href="#message" title="Message">Message</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#policydescription" title="PolicyDescription">PolicyDescription</a>" : <i>String</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>String</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#teamid" title="TeamId">TeamId</a>" : <i>String</i>,
        "<a href="#filter" title="Filter">Filter</a>" : <i>[ <a href="filterdefinition.md">FilterDefinition</a>, ... ]</i>,
        "<a href="#responders" title="Responders">Responders</a>" : <i>[ <a href="respondersdefinition.md">RespondersDefinition</a>, ... ]</i>,
        "<a href="#timerestriction" title="TimeRestriction">TimeRestriction</a>" : <i>[ <a href="timerestrictiondefinition.md">TimeRestrictionDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OpsGenie::AlertPolicy
Properties:
    <a href="#actions" title="Actions">Actions</a>: <i>
      - String</i>
    <a href="#alertdescription" title="AlertDescription">AlertDescription</a>: <i>String</i>
    <a href="#alias" title="Alias">Alias</a>: <i>String</i>
    <a href="#continuepolicy" title="ContinuePolicy">ContinuePolicy</a>: <i>Boolean</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#entity" title="Entity">Entity</a>: <i>String</i>
    <a href="#ignoreoriginalactions" title="IgnoreOriginalActions">IgnoreOriginalActions</a>: <i>Boolean</i>
    <a href="#ignoreoriginaldetails" title="IgnoreOriginalDetails">IgnoreOriginalDetails</a>: <i>Boolean</i>
    <a href="#ignoreoriginalresponders" title="IgnoreOriginalResponders">IgnoreOriginalResponders</a>: <i>Boolean</i>
    <a href="#ignoreoriginaltags" title="IgnoreOriginalTags">IgnoreOriginalTags</a>: <i>Boolean</i>
    <a href="#message" title="Message">Message</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#policydescription" title="PolicyDescription">PolicyDescription</a>: <i>String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>String</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#teamid" title="TeamId">TeamId</a>: <i>String</i>
    <a href="#filter" title="Filter">Filter</a>: <i>
      - <a href="filterdefinition.md">FilterDefinition</a></i>
    <a href="#responders" title="Responders">Responders</a>: <i>
      - <a href="respondersdefinition.md">RespondersDefinition</a></i>
    <a href="#timerestriction" title="TimeRestriction">TimeRestriction</a>: <i>
      - <a href="timerestrictiondefinition.md">TimeRestrictionDefinition</a></i>
</pre>

## Properties

#### Actions

Actions to add to the alerts original actions value as a list of strings. If `ignore_original_actions` field is set to `true`, this will replace the original actions.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertDescription

Description of the alert. You can use `{{description}}` to refer to the original alert description. Default: `{{description}}`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Alias

Alias of the alert. You can use `{{alias}}` to refer to the original alias. Default: `{{alias}}`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContinuePolicy

It will trigger other modify policies if set to `true`. Default: `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

If policy should be enabled. Default: `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Entity

Entity field of the alert. You can use `{{entity}}` to refer to the original entity. Default: `{{entity}}`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreOriginalActions

If set to `true`, policy will ignore the original actions of the alert. Default: `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreOriginalDetails

If set to `true`, policy will ignore the original details of the alert. Default: `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreOriginalResponders

If set to `true`, policy will ignore the original responders of the alert. Default: `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreOriginalTags

If set to `true`, policy will ignore the original tags of the alert. Default: `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Message

Message of the alerts.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the alert policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyDescription

Description of the policy. This can be max 512 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

Priority of the alert. Should be one of `P1`, `P2`, `P3`, `P4`, or `P5`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

Source field of the alert. You can use `{{source}}` to refer to the original source. Default: `{{source}}`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Tags to add to the alerts original tags value as a list of strings. If `ignore_original_responders` field is set to `true`, this will replace the original responders.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TeamId

Id of team that this policy belongs to.

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

#### TimeRestriction

_Required_: No

_Type_: List of <a href="timerestrictiondefinition.md">TimeRestrictionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

