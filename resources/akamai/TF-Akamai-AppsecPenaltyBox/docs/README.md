# TF::Akamai::AppsecPenaltyBox

Use the `akamai_appsec_penalty_box` resource to update the penalty box settings for a given security policy.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Akamai::AppsecPenaltyBox",
    "Properties" : {
        "<a href="#configid" title="ConfigId">ConfigId</a>" : <i>Double</i>,
        "<a href="#penaltyboxaction" title="PenaltyBoxAction">PenaltyBoxAction</a>" : <i>String</i>,
        "<a href="#penaltyboxprotection" title="PenaltyBoxProtection">PenaltyBoxProtection</a>" : <i>Boolean</i>,
        "<a href="#securitypolicyid" title="SecurityPolicyId">SecurityPolicyId</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Akamai::AppsecPenaltyBox
Properties:
    <a href="#configid" title="ConfigId">ConfigId</a>: <i>Double</i>
    <a href="#penaltyboxaction" title="PenaltyBoxAction">PenaltyBoxAction</a>: <i>String</i>
    <a href="#penaltyboxprotection" title="PenaltyBoxProtection">PenaltyBoxProtection</a>: <i>Boolean</i>
    <a href="#securitypolicyid" title="SecurityPolicyId">SecurityPolicyId</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>Double</i>
</pre>

## Properties

#### ConfigId

The ID of the security configuration to use.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PenaltyBoxAction

The action to take when penalty box protection is triggered: `alert` to record the trigger event, `deny` to block the request, `deny_custom_{custom_deny_id}` to execute a custom deny action, or `none` to take no action. Ignored if `penalty_box_protection` is set to `false`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PenaltyBoxProtection

A boolean value indicating whether to enable penalty box protection.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityPolicyId

The ID of the security policy to use.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

The version number of the security configuration to use.

_Required_: Yes

_Type_: Double

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

