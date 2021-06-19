# TF::AWS::Route53ResolverFirewallRule

Provides a Route 53 Resolver DNS Firewall rule resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::Route53ResolverFirewallRule",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#blockoverridednstype" title="BlockOverrideDnsType">BlockOverrideDnsType</a>" : <i>String</i>,
        "<a href="#blockoverridedomain" title="BlockOverrideDomain">BlockOverrideDomain</a>" : <i>String</i>,
        "<a href="#blockoverridettl" title="BlockOverrideTtl">BlockOverrideTtl</a>" : <i>Double</i>,
        "<a href="#blockresponse" title="BlockResponse">BlockResponse</a>" : <i>String</i>,
        "<a href="#firewalldomainlistid" title="FirewallDomainListId">FirewallDomainListId</a>" : <i>String</i>,
        "<a href="#firewallrulegroupid" title="FirewallRuleGroupId">FirewallRuleGroupId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::Route53ResolverFirewallRule
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#blockoverridednstype" title="BlockOverrideDnsType">BlockOverrideDnsType</a>: <i>String</i>
    <a href="#blockoverridedomain" title="BlockOverrideDomain">BlockOverrideDomain</a>: <i>String</i>
    <a href="#blockoverridettl" title="BlockOverrideTtl">BlockOverrideTtl</a>: <i>Double</i>
    <a href="#blockresponse" title="BlockResponse">BlockResponse</a>: <i>String</i>
    <a href="#firewalldomainlistid" title="FirewallDomainListId">FirewallDomainListId</a>: <i>String</i>
    <a href="#firewallrulegroupid" title="FirewallRuleGroupId">FirewallRuleGroupId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>Double</i>
</pre>

## Properties

#### Action

The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list. Valid values: `ALLOW`, `BLOCK`, `ALERT`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockOverrideDnsType

The DNS record's type. This determines the format of the record value that you provided in BlockOverrideDomain. Value values: `CNAME`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockOverrideDomain

The custom DNS record to send back in response to the query.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockOverrideTtl

The recommended amount of time, in seconds, for the DNS resolver or web browser to cache the provided override record. Minimum value of 0. Maximum value of 604800.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockResponse

The way that you want DNS Firewall to block the request. Valid values: `NODATA`, `NXDOMAIN`, `OVERRIDE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallDomainListId

The ID of the domain list that you want to use in the rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallRuleGroupId

The unique identifier of the firewall rule group where you want to create the rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A name that lets you identify the rule, to manage and use it.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

The setting that determines the processing order of the rule in the rule group. DNS Firewall processes the rules in a rule group by order of priority, starting from the lowest setting.

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

