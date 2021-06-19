# TF::NSXT::PolicySecurityPolicy

This resource provides a method for the management of Security Policy and rules under it.

This resource is applicable to NSX Global Manager, NSX Policy Manager and VMC.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NSXT::PolicySecurityPolicy",
    "Properties" : {
        "<a href="#category" title="Category">Category</a>" : <i>String</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#locked" title="Locked">Locked</a>" : <i>Boolean</i>,
        "<a href="#nsxid" title="NsxId">NsxId</a>" : <i>String</i>,
        "<a href="#scope" title="Scope">Scope</a>" : <i>[ String, ... ]</i>,
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
Type: TF::NSXT::PolicySecurityPolicy
Properties:
    <a href="#category" title="Category">Category</a>: <i>String</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#locked" title="Locked">Locked</a>: <i>Boolean</i>
    <a href="#nsxid" title="NsxId">NsxId</a>: <i>String</i>
    <a href="#scope" title="Scope">Scope</a>: <i>
      - String</i>
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

Category of this policy. For local manager must be one of `Ethernet`, `Emergency`, `Infrastructure`, `Environment`, `Application`. For global manager must be one of: `Infrastructure`, `Environment`, `Application`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

Comments for security policy lock/unlock.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the resource.
* `action` - (Optional) Rule action, one of `ALLOW`, `DROP`, `REJECT` and `JUMP_TO_APPLICATION`. Default is `ALLOW`. `JUMP_TO_APPLICATION` is only applicable in `Environment` category.
* `destination_groups` - (Optional) Set of group paths that serve as the destination for this rule. IPs, IP ranges, or CIDRs may also be used starting in NSX-T 3.0. An empty set can be used to specify "Any".
* `source_groups` - (Optional) Set of group paths that serve as the source for this rule. IPs, IP ranges, or CIDRs may also be used starting in NSX-T 3.0. An empty set can be used to specify "Any".
* `destinations_excluded` - (Optional) A boolean value indicating negation of destination groups.
* `sources_excluded` - (Optional) A boolean value indicating negation of source groups.
* `direction` - (Optional) Traffic direction, one of `IN`, `OUT` or `IN_OUT`. Default is `IN_OUT`.
* `disabled` - (Optional) Flag to disable this rule. Default is false.
* `ip_version` - (Optional) Version of IP protocol, one of `IPV4`, `IPV6`, `IPV4_IPV6`. Default is `IPV4_IPV6`.
* `logged` - (Optional) Flag to enable packet logging. Default is false.
* `notes` - (Optional) Additional notes on changes.
* `profiles` - (Optional) Set of profile paths relevant for this rule.
* `scope` - (Optional) Set of policy object paths where the rule is applied.
* `services` - (Optional) Set of service paths to match.
* `log_label` - (Optional) Additional information (string) which will be propagated to the rule syslog.
* `tag` - (Optional) A list of scope + tag pairs to associate with this Rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

Display name of the resource.
* `description` - (Optional) Description of the resource.
* `action` - (Optional) Rule action, one of `ALLOW`, `DROP`, `REJECT` and `JUMP_TO_APPLICATION`. Default is `ALLOW`. `JUMP_TO_APPLICATION` is only applicable in `Environment` category.
* `destination_groups` - (Optional) Set of group paths that serve as the destination for this rule. IPs, IP ranges, or CIDRs may also be used starting in NSX-T 3.0. An empty set can be used to specify "Any".
* `source_groups` - (Optional) Set of group paths that serve as the source for this rule. IPs, IP ranges, or CIDRs may also be used starting in NSX-T 3.0. An empty set can be used to specify "Any".
* `destinations_excluded` - (Optional) A boolean value indicating negation of destination groups.
* `sources_excluded` - (Optional) A boolean value indicating negation of source groups.
* `direction` - (Optional) Traffic direction, one of `IN`, `OUT` or `IN_OUT`. Default is `IN_OUT`.
* `disabled` - (Optional) Flag to disable this rule. Default is false.
* `ip_version` - (Optional) Version of IP protocol, one of `IPV4`, `IPV6`, `IPV4_IPV6`. Default is `IPV4_IPV6`.
* `logged` - (Optional) Flag to enable packet logging. Default is false.
* `notes` - (Optional) Additional notes on changes.
* `profiles` - (Optional) Set of profile paths relevant for this rule.
* `scope` - (Optional) Set of policy object paths where the rule is applied.
* `services` - (Optional) Set of service paths to match.
* `log_label` - (Optional) Additional information (string) which will be propagated to the rule syslog.
* `tag` - (Optional) A list of scope + tag pairs to associate with this Rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

The domain to use for the resource. This domain must already exist. For VMware Cloud on AWS use `cgw`. For Global Manager, please use site id for this field. If not specified, this field is default to `default`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Locked

Indicates whether a security policy should be locked. If locked by a user, no other user would be able to modify this policy.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxId

The NSX ID of this resource. If set, this ID will be used to create the resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

Set of policy object paths where the rule is applied.
* `services` - (Optional) Set of service paths to match.
* `log_label` - (Optional) Additional information (string) which will be propagated to the rule syslog.
* `tag` - (Optional) A list of scope + tag pairs to associate with this Rule.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SequenceNumber

This field is used to resolve conflicts between security policies across domains.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stateful

If true, state of the network connects are tracked and a stateful packet inspection is performed. Default is true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpStrict

Ensures that a 3 way TCP handshake is done before the data packets are sent. Default is false.

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

