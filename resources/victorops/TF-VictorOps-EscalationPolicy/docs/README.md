# TF::VictorOps::EscalationPolicy

[Team Escalation Policies](https://portal.victorops.com/public/api-docs.html#/Escalation32Policies) set who is actually on-call for a given team and are the link to utilize any rotations that have been created.

Note:

    - You need to fetch an existing Rotation Group Slug through the VO public API - [GET-Rotations](https://portal.victorops.com/public/api-docs.html#!/Rotations/get_api_public_v1_teams_team_rotations) for creating an escalation policy resource from Terraform
    - Update/Delete operations on an escalation policy may fail if it involves deleting or updating a routing key (not supported in current state of the Terraform provider)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VictorOps::EscalationPolicy",
    "Properties" : {
        "<a href="#ignorecustompagingpolicies" title="IgnoreCustomPagingPolicies">IgnoreCustomPagingPolicies</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#teamid" title="TeamId">TeamId</a>" : <i>String</i>,
        "<a href="#step" title="Step">Step</a>" : <i>[ <a href="stepdefinition.md">StepDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VictorOps::EscalationPolicy
Properties:
    <a href="#ignorecustompagingpolicies" title="IgnoreCustomPagingPolicies">IgnoreCustomPagingPolicies</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#teamid" title="TeamId">TeamId</a>: <i>String</i>
    <a href="#step" title="Step">Step</a>: <i>
      - <a href="stepdefinition.md">StepDefinition</a></i>
</pre>

## Properties

#### IgnoreCustomPagingPolicies

`true`/`false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of this escalation policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TeamId

The team_id of the team for which you want to create this escalation policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Step

_Required_: No

_Type_: List of <a href="stepdefinition.md">StepDefinition</a>

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

