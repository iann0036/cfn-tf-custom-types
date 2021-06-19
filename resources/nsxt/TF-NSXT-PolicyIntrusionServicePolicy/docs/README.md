# TF::NSXT::PolicyIntrusionServicePolicy

This resource provides a method for the management of Intrusion Service (IDS) Policy and rules under it.

This resource is applicable to NSX Policy Manager and VMC (NSX version 3.1.0 and up).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NSXT::PolicyIntrusionServicePolicy",
    "Properties" : {
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#locked" title="Locked">Locked</a>" : <i>Boolean</i>,
        "<a href="#nsxid" title="NsxId">NsxId</a>" : <i>String</i>,
        "<a href="#sequencenumber" title="SequenceNumber">SequenceNumber</a>" : <i>Double</i>,
        "<a href="#stateful" title="Stateful">Stateful</a>" : <i>Boolean</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="ruledefinition.md">RuleDefinition</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NSXT::PolicyIntrusionServicePolicy
Properties:
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#locked" title="Locked">Locked</a>: <i>Boolean</i>
    <a href="#nsxid" title="NsxId">NsxId</a>: <i>String</i>
    <a href="#sequencenumber" title="SequenceNumber">SequenceNumber</a>: <i>Double</i>
    <a href="#stateful" title="Stateful">Stateful</a>: <i>Boolean</i>
    <a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="ruledefinition.md">RuleDefinition</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
</pre>

## Properties

#### Comments

Comments for IDS policy lock/unlock.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the resource.
* `action` - (Optional) Rule action, one of `DETECT`, `DETECT_PREVENT`. Default is `DETECT`.
* `destination_groups` - (Optional) Set of group paths that serve as destination for this rule.
* `source_groups` - (Optional) Set of group paths that serve as source for this rule.
* `destinations_excluded` - (Optional) A boolean value indicating negation of destination groups.
* `sources_excluded` - (Optional) A boolean value indicating negation of source groups.
* `direction` - (Optional) Traffic direction, one of `IN`, `OUT` or `IN_OUT`. Default is `IN_OUT`.
* `disabled` - (Optional) Flag to disable this rule. Default is false.
* `ip_version` - (Optional) Version of IP protocol, one of `IPV4`, `IPV6`, `IPV4_IPV6`. Default is `IPV4_IPV6`.
* `logged` - (Optional) Flag to enable packet logging. Default is false.
* `notes` - (Optional) Additional notes on changes.
* `ids_profiles` - (Required) Set of IDS profile paths relevant for this rule.
* `services` - (Optional) Set of service paths to match.
* `log_label` - (Optional) Additional information (string) which will be propagated to the rule syslog.
* `tag` - (Optional) A list of scope + tag pairs to associate with this Rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

Display name of the resource.
* `description` - (Optional) Description of the resource.
* `action` - (Optional) Rule action, one of `DETECT`, `DETECT_PREVENT`. Default is `DETECT`.
* `destination_groups` - (Optional) Set of group paths that serve as destination for this rule.
* `source_groups` - (Optional) Set of group paths that serve as source for this rule.
* `destinations_excluded` - (Optional) A boolean value indicating negation of destination groups.
* `sources_excluded` - (Optional) A boolean value indicating negation of source groups.
* `direction` - (Optional) Traffic direction, one of `IN`, `OUT` or `IN_OUT`. Default is `IN_OUT`.
* `disabled` - (Optional) Flag to disable this rule. Default is false.
* `ip_version` - (Optional) Version of IP protocol, one of `IPV4`, `IPV6`, `IPV4_IPV6`. Default is `IPV4_IPV6`.
* `logged` - (Optional) Flag to enable packet logging. Default is false.
* `notes` - (Optional) Additional notes on changes.
* `ids_profiles` - (Required) Set of IDS profile paths relevant for this rule.
* `services` - (Optional) Set of service paths to match.
* `log_label` - (Optional) Additional information (string) which will be propagated to the rule syslog.
* `tag` - (Optional) A list of scope + tag pairs to associate with this Rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

The domain to use for the resource. This domain must already exist. For VMware Cloud on AWS use `cgw`. If not specified, this field is default to `default`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Locked

Indicates whether the policy should be locked. If locked by a user, no other user would be able to modify this policy.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxId

The NSX ID of this resource. If set, this ID will be used to create the resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SequenceNumber

This field is used to resolve conflicts between IDS policies across domains.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stateful

If true, state of the network connects are tracked and a stateful packet inspection is performed. Default is true.

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

