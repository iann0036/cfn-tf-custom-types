# TF::NSXT::PolicyGatewayPolicy

This resource provides a method for the management of a Gateway Policy and its Rules.

This resource is applicable to NSX Global Manager and NSX Policy Manager.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NSXT::PolicyGatewayPolicy",
    "Properties" : {
        "<a href="#category" title="Category">Category</a>" : <i>String</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#locked" title="Locked">Locked</a>" : <i>Boolean</i>,
        "<a href="#nsxid" title="NsxId">NsxId</a>" : <i>String</i>,
        "<a href="#sequencenumber" title="SequenceNumber">SequenceNumber</a>" : <i>Double</i>,
        "<a href="#stateful" title="Stateful">Stateful</a>" : <i>Boolean</i>,
        "<a href="#tcpstrict" title="TcpStrict">TcpStrict</a>" : <i>Boolean</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="ruledefinition.md">RuleDefinition</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NSXT::PolicyGatewayPolicy
Properties:
    <a href="#category" title="Category">Category</a>: <i>String</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#locked" title="Locked">Locked</a>: <i>Boolean</i>
    <a href="#nsxid" title="NsxId">NsxId</a>: <i>String</i>
    <a href="#sequencenumber" title="SequenceNumber">SequenceNumber</a>: <i>Double</i>
    <a href="#stateful" title="Stateful">Stateful</a>: <i>Boolean</i>
    <a href="#tcpstrict" title="TcpStrict">TcpStrict</a>: <i>Boolean</i>
    <a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="ruledefinition.md">RuleDefinition</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
</pre>

## Properties

#### Category

The category to use for priority of this Gateway Policy. For local manager must be one of: `Emergency`, `SystemRules`, `SharedPreRules`, `LocalGatewayRules`, `AutoServiceRules` and `Default`. For global manager must be `SharedPreRules` or `LocalGatewayRules`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

Comments for this Gateway Policy including lock/unlock comments.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the resource.
* `destination_groups` - (Optional) Set of group paths that serve as the destination for this rule. IPs, IP ranges, or CIDRs may also be used starting in NSX-T 3.0. An empty set can be used to specify "Any".
* `destinations_excluded` - (Optional) A boolean value indicating negation of destination groups.
* `direction` - (Optional) The traffic direction for the policy. Must be one of: `IN`, `OUT` or `IN_OUT`. Defaults to `IN_OUT`.
* `disabled` - (Optional) A boolean value to indicate the rule is disabled. Defaults to `false`.
* `ip_version` - (Optional) The IP Protocol for the rule. Must be one of: `IPV4`, `IPV6` or `IPV4_IPV6`. Defaults to `IPV4_IPV6`.
* `logged` - (Optional) A boolean flag to enable packet logging.
* `notes` - (Optional) Text for additional notes on changes for the rule.
* `profiles` - (Optional) A list of context profiles for the rule. Note: due to platform issue, this setting is only supported with NSX 3.2 onwards.
* `scope` - (Required) List of policy paths where the rule is applied.
* `services` - (Optional) List of services to match.
* `source_groups` - (Optional) Set of group paths that serve as the source for this rule. IPs, IP ranges, or CIDRs may also be used starting in NSX-T 3.0. An empty set can be used to specify "Any".
* `source_excluded` - (Optional) A boolean value indicating negation of source groups.
* `log_label` - (Optional) Additional information (string) which will be propagated to the rule syslog.
* `tag` - (Optional) A list of scope + tag pairs to associate with this Rule.
* `action` - (Optional) The action for the Rule. Must be one of: `ALLOW`, `DROP` or `REJECT`. Defaults to `ALLOW`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

Display name of the resource.
* `description` - (Optional) Description of the resource.
* `destination_groups` - (Optional) Set of group paths that serve as the destination for this rule. IPs, IP ranges, or CIDRs may also be used starting in NSX-T 3.0. An empty set can be used to specify "Any".
* `destinations_excluded` - (Optional) A boolean value indicating negation of destination groups.
* `direction` - (Optional) The traffic direction for the policy. Must be one of: `IN`, `OUT` or `IN_OUT`. Defaults to `IN_OUT`.
* `disabled` - (Optional) A boolean value to indicate the rule is disabled. Defaults to `false`.
* `ip_version` - (Optional) The IP Protocol for the rule. Must be one of: `IPV4`, `IPV6` or `IPV4_IPV6`. Defaults to `IPV4_IPV6`.
* `logged` - (Optional) A boolean flag to enable packet logging.
* `notes` - (Optional) Text for additional notes on changes for the rule.
* `profiles` - (Optional) A list of context profiles for the rule. Note: due to platform issue, this setting is only supported with NSX 3.2 onwards.
* `scope` - (Required) List of policy paths where the rule is applied.
* `services` - (Optional) List of services to match.
* `source_groups` - (Optional) Set of group paths that serve as the source for this rule. IPs, IP ranges, or CIDRs may also be used starting in NSX-T 3.0. An empty set can be used to specify "Any".
* `source_excluded` - (Optional) A boolean value indicating negation of source groups.
* `log_label` - (Optional) Additional information (string) which will be propagated to the rule syslog.
* `tag` - (Optional) A list of scope + tag pairs to associate with this Rule.
* `action` - (Optional) The action for the Rule. Must be one of: `ALLOW`, `DROP` or `REJECT`. Defaults to `ALLOW`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

The domain to use for the Gateway Policy. This domain must already exist. For VMware Cloud on AWS use `cgw`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Locked

A boolean value indicating if the policy is locked. If locked, no other users can update the resource.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxId

The NSX ID of this resource. If set, this ID will be used to create the Gateway Policy resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SequenceNumber

An int value used to resolve conflicts between security policies across domains.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stateful

A boolean value to indicate if this Policy is stateful. When it is stateful, the state of the network connects are tracked and a stateful packet inspection is performed.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpStrict

A boolean value to enable/disable a 3 way TCP handshake is done before the data packets are sent.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of <a href="ruledefinition.md">RuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tagdefinition.md">TagDefinition</a>

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

#### Path

Returns the <code>Path</code> value.

#### Revision

Returns the <code>Revision</code> value.

