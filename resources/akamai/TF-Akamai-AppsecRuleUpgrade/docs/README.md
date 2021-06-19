# TF::Akamai::AppsecRuleUpgrade

Use the `akamai_appsec_rule_upgrade` resource to upgrade to the most recent version of the KRS rule set. Akamai periodically updates these rules to keep protections current. However, the rules you use in your security policies do not automatically upgrade to the latest version when using mode: KRS. These rules do update automatically when you have mode set to AAG. Before you upgrade, run Get upgrade details to see which rules have changed. If you want to test how these rules would operate with live traffic before committing to the upgrade, run them in evaluation mode. This applies to KRS rules only and does not allow you to make any changes to the rules themselves. The response is the same as the mode response.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Akamai::AppsecRuleUpgrade",
    "Properties" : {
        "<a href="#configid" title="ConfigId">ConfigId</a>" : <i>Double</i>,
        "<a href="#securitypolicyid" title="SecurityPolicyId">SecurityPolicyId</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Akamai::AppsecRuleUpgrade
Properties:
    <a href="#configid" title="ConfigId">ConfigId</a>: <i>Double</i>
    <a href="#securitypolicyid" title="SecurityPolicyId">SecurityPolicyId</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>Double</i>
</pre>

## Properties

#### ConfigId

The ID of the security configuration to use.

_Required_: Yes

_Type_: Double

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

#### CurrentRuleset

Returns the <code>CurrentRuleset</code> value.

#### EvalStatus

Returns the <code>EvalStatus</code> value.

#### Id

Returns the <code>Id</code> value.

#### Mode

Returns the <code>Mode</code> value.

