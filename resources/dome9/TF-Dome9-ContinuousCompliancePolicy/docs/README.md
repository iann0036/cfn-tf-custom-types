# TF::Dome9::ContinuousCompliancePolicy

This  resource is used to  create and modify compliance policies in Dome9 for continuous compliance assessments. A continuous compliance policy is the combination of a Rule Bundle applied to a specific cloud account.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Dome9::ContinuousCompliancePolicy",
    "Properties" : {
        "<a href="#notificationids" title="NotificationIds">NotificationIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#rulesetid" title="RulesetId">RulesetId</a>" : <i>Double</i>,
        "<a href="#targetid" title="TargetId">TargetId</a>" : <i>String</i>,
        "<a href="#targettype" title="TargetType">TargetType</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Dome9::ContinuousCompliancePolicy
Properties:
    <a href="#notificationids" title="NotificationIds">NotificationIds</a>: <i>
      - String</i>
    <a href="#rulesetid" title="RulesetId">RulesetId</a>: <i>Double</i>
    <a href="#targetid" title="TargetId">TargetId</a>: <i>String</i>
    <a href="#targettype" title="TargetType">TargetType</a>: <i>String</i>
</pre>

## Properties

#### NotificationIds

The notification policy id's for the policy [list].

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RulesetId

The bundle id for the bundle that will be used in the policy.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetId

The cloud account id.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetType

The cloud account provider ("Aws", "Azure", "Gcp", "Kubernetes", "OrganizationalUnit").

_Required_: Yes

_Type_: String

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

