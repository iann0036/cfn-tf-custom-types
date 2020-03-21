# Terraform::OpsGenie::TeamRoutingRule

CloudFormation equivalent of opsgenie_team_routing_rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpsGenie::TeamRoutingRule",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#order" title="Order">Order</a>" : <i>Double</i>,
        "<a href="#teamid" title="TeamId">TeamId</a>" : <i>String</i>,
        "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>,
        "<a href="#criteria" title="Criteria">Criteria</a>" : <i>[ &lt;a href=&#34;criteria.md&#34;&gt;Criteria&lt;/a&gt;, ... ]</i>,
        "<a href="#notify" title="Notify">Notify</a>" : <i>[ &lt;a href=&#34;notify.md&#34;&gt;Notify&lt;/a&gt;, ... ]</i>,
        "<a href="#timerestriction" title="TimeRestriction">TimeRestriction</a>" : <i>[ &lt;a href=&#34;timerestriction.md&#34;&gt;TimeRestriction&lt;/a&gt;, ... ]</i>,
        "<a href="#conditions" title="Conditions">Conditions</a>" : <i>[ &lt;a href=&#34;conditions.md&#34;&gt;Conditions&lt;/a&gt;, ... ]</i>,
        "<a href="#restriction" title="Restriction">Restriction</a>" : <i>[ &lt;a href=&#34;restriction.md&#34;&gt;Restriction&lt;/a&gt;, ... ]</i>,
        "<a href="#restrictions" title="Restrictions">Restrictions</a>" : <i>[ &lt;a href=&#34;restrictions.md&#34;&gt;Restrictions&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpsGenie::TeamRoutingRule
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#order" title="Order">Order</a>: <i>Double</i>
    <a href="#teamid" title="TeamId">TeamId</a>: <i>String</i>
    <a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
    <a href="#criteria" title="Criteria">Criteria</a>: <i>
      - &lt;a href=&#34;criteria.md&#34;&gt;Criteria&lt;/a&gt;</i>
    <a href="#notify" title="Notify">Notify</a>: <i>
      - &lt;a href=&#34;notify.md&#34;&gt;Notify&lt;/a&gt;</i>
    <a href="#timerestriction" title="TimeRestriction">TimeRestriction</a>: <i>
      - &lt;a href=&#34;timerestriction.md&#34;&gt;TimeRestriction&lt;/a&gt;</i>
    <a href="#conditions" title="Conditions">Conditions</a>: <i>
      - &lt;a href=&#34;conditions.md&#34;&gt;Conditions&lt;/a&gt;</i>
    <a href="#restriction" title="Restriction">Restriction</a>: <i>
      - &lt;a href=&#34;restriction.md&#34;&gt;Restriction&lt;/a&gt;</i>
    <a href="#restrictions" title="Restrictions">Restrictions</a>: <i>
      - &lt;a href=&#34;restrictions.md&#34;&gt;Restrictions&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Order

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TeamId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Criteria

_Required_: No

_Type_: List of &lt;a href=&#34;criteria.md&#34;&gt;Criteria&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notify

_Required_: No

_Type_: List of &lt;a href=&#34;notify.md&#34;&gt;Notify&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeRestriction

_Required_: No

_Type_: List of &lt;a href=&#34;timerestriction.md&#34;&gt;TimeRestriction&lt;/a&gt;

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

