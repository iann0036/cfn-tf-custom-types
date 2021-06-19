# TF::OpsGenie::NotificationPolicy

Manages a Notification Policy within Opsgenie.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OpsGenie::NotificationPolicy",
    "Properties" : {
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#policydescription" title="PolicyDescription">PolicyDescription</a>" : <i>String</i>,
        "<a href="#suppress" title="Suppress">Suppress</a>" : <i>Boolean</i>,
        "<a href="#teamid" title="TeamId">TeamId</a>" : <i>String</i>,
        "<a href="#autocloseaction" title="AutoCloseAction">AutoCloseAction</a>" : <i>[ <a href="autocloseactiondefinition.md">AutoCloseActionDefinition</a>, ... ]</i>,
        "<a href="#autorestartaction" title="AutoRestartAction">AutoRestartAction</a>" : <i>[ <a href="autorestartactiondefinition.md">AutoRestartActionDefinition</a>, ... ]</i>,
        "<a href="#deduplicationaction" title="DeDuplicationAction">DeDuplicationAction</a>" : <i>[ <a href="deduplicationactiondefinition.md">DeDuplicationActionDefinition</a>, ... ]</i>,
        "<a href="#delayaction" title="DelayAction">DelayAction</a>" : <i>[ <a href="delayactiondefinition.md">DelayActionDefinition</a>, ... ]</i>,
        "<a href="#filter" title="Filter">Filter</a>" : <i>[ <a href="filterdefinition.md">FilterDefinition</a>, ... ]</i>,
        "<a href="#timerestriction" title="TimeRestriction">TimeRestriction</a>" : <i>[ <a href="timerestrictiondefinition.md">TimeRestrictionDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OpsGenie::NotificationPolicy
Properties:
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#policydescription" title="PolicyDescription">PolicyDescription</a>: <i>String</i>
    <a href="#suppress" title="Suppress">Suppress</a>: <i>Boolean</i>
    <a href="#teamid" title="TeamId">TeamId</a>: <i>String</i>
    <a href="#autocloseaction" title="AutoCloseAction">AutoCloseAction</a>: <i>
      - <a href="autocloseactiondefinition.md">AutoCloseActionDefinition</a></i>
    <a href="#autorestartaction" title="AutoRestartAction">AutoRestartAction</a>: <i>
      - <a href="autorestartactiondefinition.md">AutoRestartActionDefinition</a></i>
    <a href="#deduplicationaction" title="DeDuplicationAction">DeDuplicationAction</a>: <i>
      - <a href="deduplicationactiondefinition.md">DeDuplicationActionDefinition</a></i>
    <a href="#delayaction" title="DelayAction">DelayAction</a>: <i>
      - <a href="delayactiondefinition.md">DelayActionDefinition</a></i>
    <a href="#filter" title="Filter">Filter</a>: <i>
      - <a href="filterdefinition.md">FilterDefinition</a></i>
    <a href="#timerestriction" title="TimeRestriction">TimeRestriction</a>: <i>
      - <a href="timerestrictiondefinition.md">TimeRestrictionDefinition</a></i>
</pre>

## Properties

#### Enabled

If policy should be enabled. Default: `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the notification policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyDescription

Description of the policy. This can be max 512 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Suppress

Suppress value of the policy. Values are: `true`, `false`. Default: `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TeamId

Id of team that this policy belons to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoCloseAction

_Required_: No

_Type_: List of <a href="autocloseactiondefinition.md">AutoCloseActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoRestartAction

_Required_: No

_Type_: List of <a href="autorestartactiondefinition.md">AutoRestartActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeDuplicationAction

_Required_: No

_Type_: List of <a href="deduplicationactiondefinition.md">DeDuplicationActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DelayAction

_Required_: No

_Type_: List of <a href="delayactiondefinition.md">DelayActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No

_Type_: List of <a href="filterdefinition.md">FilterDefinition</a>

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

