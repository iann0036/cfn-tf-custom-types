# TF::OCI::WaasProtectionRule

This resource provides the Protection Rule resource in Oracle Cloud Infrastructure Web Application Acceleration and Security service.

Updates the action for each specified protection rule. Requests can either be allowed, blocked, or trigger an alert if they meet the parameters of an applied rule. For more information on protection rules, see [WAF Protection Rules](https://docs.cloud.oracle.com/iaas/Content/WAF/Tasks/wafprotectionrules.htm).
This operation can update or disable protection rules depending on the structure of the request body.
Protection rules can be updated by changing the properties of the protection rule object with the rule's key specified in the key field.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::WaasProtectionRule",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#waaspolicyid" title="WaasPolicyId">WaasPolicyId</a>" : <i>String</i>,
        "<a href="#exclusions" title="Exclusions">Exclusions</a>" : <i>[ <a href="exclusionsdefinition.md">ExclusionsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::WaasProtectionRule
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#waaspolicyid" title="WaasPolicyId">WaasPolicyId</a>: <i>String</i>
    <a href="#exclusions" title="Exclusions">Exclusions</a>: <i>
      - <a href="exclusionsdefinition.md">ExclusionsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Action

(Updatable) The action to take when the traffic is detected as malicious. If unspecified, defaults to `OFF`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

(Updatable) The unique key of the protection rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaasPolicyId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the WAAS policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exclusions

_Required_: No

_Type_: List of <a href="exclusionsdefinition.md">ExclusionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Description

Returns the <code>Description</code> value.

#### Id

Returns the <code>Id</code> value.

#### Labels

Returns the <code>Labels</code> value.

#### ModSecurityRuleIds

Returns the <code>ModSecurityRuleIds</code> value.

#### Name

Returns the <code>Name</code> value.

