# Terraform::AzureRM::FrontdoorFirewallPolicy CustomRule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
    "<a href="#ratelimitdurationinminutes" title="RateLimitDurationInMinutes">RateLimitDurationInMinutes</a>" : <i>Double</i>,
    "<a href="#ratelimitthreshold" title="RateLimitThreshold">RateLimitThreshold</a>" : <i>Double</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#matchcondition" title="MatchCondition">MatchCondition</a>" : <i>[ <a href="customrule-matchcondition.md">MatchCondition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
<a href="#ratelimitdurationinminutes" title="RateLimitDurationInMinutes">RateLimitDurationInMinutes</a>: <i>Double</i>
<a href="#ratelimitthreshold" title="RateLimitThreshold">RateLimitThreshold</a>: <i>Double</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#matchcondition" title="MatchCondition">MatchCondition</a>: <i>
      - <a href="customrule-matchcondition.md">MatchCondition</a></i>
</pre>

## Properties

#### Action

The action to perform when the rule is matched. Possible values are `Allow`, `Block`, `Log`, or `Redirect`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Is the rule is enabled or disabled? Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Gets name of the resource that is unique within a policy. This name can be used to access the resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

The priority of the rule. Rules with a lower value will be evaluated before rules with a higher value. Defaults to `1`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateLimitDurationInMinutes

The rate limit duration in minutes. Defaults to `1`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateLimitThreshold

The rate limit threshold. Defaults to `10`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of rule. Possible values are `MatchRule` or `RateLimitRule`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchCondition

_Required_: No

_Type_: List of <a href="customrule-matchcondition.md">MatchCondition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

