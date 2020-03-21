# Terraform::OpsGenie::NotificationPolicy

CloudFormation equivalent of opsgenie_notification_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpsGenie::NotificationPolicy",
    "Properties" : {
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#policydescription" title="PolicyDescription">PolicyDescription</a>" : <i>String</i>,
        "<a href="#suppress" title="Suppress">Suppress</a>" : <i>Boolean</i>,
        "<a href="#teamid" title="TeamId">TeamId</a>" : <i>String</i>,
        "<a href="#autocloseaction" title="AutoCloseAction">AutoCloseAction</a>" : <i>[ &lt;a href=&#34;autocloseaction.md&#34;&gt;AutoCloseAction&lt;/a&gt;, ... ]</i>,
        "<a href="#autorestartaction" title="AutoRestartAction">AutoRestartAction</a>" : <i>[ &lt;a href=&#34;autorestartaction.md&#34;&gt;AutoRestartAction&lt;/a&gt;, ... ]</i>,
        "<a href="#deduplicationaction" title="DeDuplicationAction">DeDuplicationAction</a>" : <i>[ &lt;a href=&#34;deduplicationaction.md&#34;&gt;DeDuplicationAction&lt;/a&gt;, ... ]</i>,
        "<a href="#delayaction" title="DelayAction">DelayAction</a>" : <i>[ &lt;a href=&#34;delayaction.md&#34;&gt;DelayAction&lt;/a&gt;, ... ]</i>,
        "<a href="#filter" title="Filter">Filter</a>" : <i>[ &lt;a href=&#34;filter.md&#34;&gt;Filter&lt;/a&gt;, ... ]</i>,
        "<a href="#timerestriction" title="TimeRestriction">TimeRestriction</a>" : <i>[ &lt;a href=&#34;timerestriction.md&#34;&gt;TimeRestriction&lt;/a&gt;, ... ]</i>,
        "<a href="#duration" title="Duration">Duration</a>" : <i>[ &lt;a href=&#34;duration.md&#34;&gt;Duration&lt;/a&gt;, ... ]</i>,
        "<a href="#conditions" title="Conditions">Conditions</a>" : <i>[ &lt;a href=&#34;conditions.md&#34;&gt;Conditions&lt;/a&gt;, ... ]</i>,
        "<a href="#restriction" title="Restriction">Restriction</a>" : <i>[ &lt;a href=&#34;restriction.md&#34;&gt;Restriction&lt;/a&gt;, ... ]</i>,
        "<a href="#restrictions" title="Restrictions">Restrictions</a>" : <i>[ &lt;a href=&#34;restrictions.md&#34;&gt;Restrictions&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpsGenie::NotificationPolicy
Properties:
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#policydescription" title="PolicyDescription">PolicyDescription</a>: <i>String</i>
    <a href="#suppress" title="Suppress">Suppress</a>: <i>Boolean</i>
    <a href="#teamid" title="TeamId">TeamId</a>: <i>String</i>
    <a href="#autocloseaction" title="AutoCloseAction">AutoCloseAction</a>: <i>
      - &lt;a href=&#34;autocloseaction.md&#34;&gt;AutoCloseAction&lt;/a&gt;</i>
    <a href="#autorestartaction" title="AutoRestartAction">AutoRestartAction</a>: <i>
      - &lt;a href=&#34;autorestartaction.md&#34;&gt;AutoRestartAction&lt;/a&gt;</i>
    <a href="#deduplicationaction" title="DeDuplicationAction">DeDuplicationAction</a>: <i>
      - &lt;a href=&#34;deduplicationaction.md&#34;&gt;DeDuplicationAction&lt;/a&gt;</i>
    <a href="#delayaction" title="DelayAction">DelayAction</a>: <i>
      - &lt;a href=&#34;delayaction.md&#34;&gt;DelayAction&lt;/a&gt;</i>
    <a href="#filter" title="Filter">Filter</a>: <i>
      - &lt;a href=&#34;filter.md&#34;&gt;Filter&lt;/a&gt;</i>
    <a href="#timerestriction" title="TimeRestriction">TimeRestriction</a>: <i>
      - &lt;a href=&#34;timerestriction.md&#34;&gt;TimeRestriction&lt;/a&gt;</i>
    <a href="#duration" title="Duration">Duration</a>: <i>
      - &lt;a href=&#34;duration.md&#34;&gt;Duration&lt;/a&gt;</i>
    <a href="#conditions" title="Conditions">Conditions</a>: <i>
      - &lt;a href=&#34;conditions.md&#34;&gt;Conditions&lt;/a&gt;</i>
    <a href="#restriction" title="Restriction">Restriction</a>: <i>
      - &lt;a href=&#34;restriction.md&#34;&gt;Restriction&lt;/a&gt;</i>
    <a href="#restrictions" title="Restrictions">Restrictions</a>: <i>
      - &lt;a href=&#34;restrictions.md&#34;&gt;Restrictions&lt;/a&gt;</i>
</pre>

## Properties

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyDescription

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Suppress

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TeamId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoCloseAction

_Required_: No

_Type_: List of &lt;a href=&#34;autocloseaction.md&#34;&gt;AutoCloseAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoRestartAction

_Required_: No

_Type_: List of &lt;a href=&#34;autorestartaction.md&#34;&gt;AutoRestartAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeDuplicationAction

_Required_: No

_Type_: List of &lt;a href=&#34;deduplicationaction.md&#34;&gt;DeDuplicationAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DelayAction

_Required_: No

_Type_: List of &lt;a href=&#34;delayaction.md&#34;&gt;DelayAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No

_Type_: List of &lt;a href=&#34;filter.md&#34;&gt;Filter&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeRestriction

_Required_: No

_Type_: List of &lt;a href=&#34;timerestriction.md&#34;&gt;TimeRestriction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Duration

_Required_: No

_Type_: List of &lt;a href=&#34;duration.md&#34;&gt;Duration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Conditions

_Required_: No

_Type_: List of &lt;a href=&#34;conditions.md&#34;&gt;Conditions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Restriction

_Required_: No

_Type_: List of &lt;a href=&#34;restriction.md&#34;&gt;Restriction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Restrictions

_Required_: No

_Type_: List of &lt;a href=&#34;restrictions.md&#34;&gt;Restrictions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

