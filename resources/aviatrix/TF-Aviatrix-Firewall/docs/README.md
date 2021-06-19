# TF::Aviatrix::Firewall

The **aviatrix_firewall** resource allows the creation and management of [Aviatrix Stateful Firewall](https://docs.aviatrix.com/HowTos/stateful_firewall_faq.html) policies.

~> **NOTE on Firewall and Firewall Policy resources:** Terraform currently provides both a standalone Firewall Policy resource and a Firewall resource with policies defined in-line. At this time, you cannot use a Firewall resource with in-line rules in conjunction with any Firewall Policy resources. Doing so will cause a conflict of policy settings and will overwrite policies. In order to use the **aviatrix_firewall_policy** resource, `manage_firewall_policies` must be set to false in this resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::Firewall",
    "Properties" : {
        "<a href="#baselogenabled" title="BaseLogEnabled">BaseLogEnabled</a>" : <i>Boolean</i>,
        "<a href="#basepolicy" title="BasePolicy">BasePolicy</a>" : <i>String</i>,
        "<a href="#gwname" title="GwName">GwName</a>" : <i>String</i>,
        "<a href="#managefirewallpolicies" title="ManageFirewallPolicies">ManageFirewallPolicies</a>" : <i>Boolean</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>[ <a href="policydefinition.md">PolicyDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::Firewall
Properties:
    <a href="#baselogenabled" title="BaseLogEnabled">BaseLogEnabled</a>: <i>Boolean</i>
    <a href="#basepolicy" title="BasePolicy">BasePolicy</a>: <i>String</i>
    <a href="#gwname" title="GwName">GwName</a>: <i>String</i>
    <a href="#managefirewallpolicies" title="ManageFirewallPolicies">ManageFirewallPolicies</a>: <i>Boolean</i>
    <a href="#policy" title="Policy">Policy</a>: <i>
      - <a href="policydefinition.md">PolicyDefinition</a></i>
</pre>

## Properties

#### BaseLogEnabled

Indicates whether enable logging or not. Valid Values: true, false. Default value: false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BasePolicy

New base policy. Valid Values: "allow-all", "deny-all". Default value: "deny-all".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GwName

Gateway name to attach firewall policy to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManageFirewallPolicies

Enable to manage firewall policies via in-line rules. If false, policies must be managed using `aviatrix_firewall_policy` resources. Default: true. Valid values: true, false. Available in provider version R2.17+.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

_Required_: No

_Type_: List of <a href="policydefinition.md">PolicyDefinition</a>

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

