# Terraform::NSXT::FirewallSection

This resource provides a way to configure a firewall section on the NSX manager. A firewall section is a collection of firewall rules that are grouped together.
Order of firewall sections can be controlled with 'insert_before' attribute.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NSXT::FirewallSection",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#insertbefore" title="InsertBefore">InsertBefore</a>" : <i>String</i>,
        "<a href="#sectiontype" title="SectionType">SectionType</a>" : <i>String</i>,
        "<a href="#stateful" title="Stateful">Stateful</a>" : <i>Boolean</i>,
        "<a href="#appliedto" title="AppliedTo">AppliedTo</a>" : <i>[ <a href="appliedto.md">AppliedTo</a>, ... ]</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="rule.md">Rule</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tag.md">Tag</a>, ... ]</i>,
        "<a href="#destination" title="Destination">Destination</a>" : <i>[ <a href="destination.md">Destination</a>, ... ]</i>,
        "<a href="#service" title="Service">Service</a>" : <i>[ <a href="service.md">Service</a>, ... ]</i>,
        "<a href="#source" title="Source">Source</a>" : <i>[ <a href="source.md">Source</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NSXT::FirewallSection
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#insertbefore" title="InsertBefore">InsertBefore</a>: <i>String</i>
    <a href="#sectiontype" title="SectionType">SectionType</a>: <i>String</i>
    <a href="#stateful" title="Stateful">Stateful</a>: <i>Boolean</i>
    <a href="#appliedto" title="AppliedTo">AppliedTo</a>: <i>
      - <a href="appliedto.md">AppliedTo</a></i>
    <a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="rule.md">Rule</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tag.md">Tag</a></i>
    <a href="#destination" title="Destination">Destination</a>: <i>
      - <a href="destination.md">Destination</a></i>
    <a href="#service" title="Service">Service</a>: <i>
      - <a href="service.md">Service</a></i>
    <a href="#source" title="Source">Source</a>: <i>
      - <a href="source.md">Source</a></i>
</pre>

## Properties

#### Description

Description of this rule.
* `action` - (Required) Action enforced on the packets which matches the firewall rule. [Allowed values: "ALLOW", "DROP", "REJECT"]
* `applied_to` - (Optional) List of objects where rule will be enforced. The section level field overrides this one. Null will be treated as any. [Supported target types: "LogicalPort", "LogicalSwitch", "NSGroup", "LogicalRouterPort"]
* `destination` - (Optional) List of the destinations. Null will be treated as any. [Allowed target types: "IPSet", "LogicalPort", "LogicalSwitch", "NSGroup", "MACSet" (depending on the section type)]
* `destinations_excluded` - (Optional) When this boolean flag is set to true, the rule destinations will be negated.
* `direction` - (Optional) Rule direction in case of stateless firewall rules. This will only considered if section level parameter is set to stateless. Default to IN_OUT if not specified. [Allowed values: "IN", "OUT", "IN_OUT"]
* `disabled` - (Optional) Flag to disable rule. Disabled will only be persisted but never provisioned/realized.
* `ip_protocol` - (Optional) Type of IP packet that should be matched while enforcing the rule. [allowed values: "IPV4", "IPV6", "IPV4_IPV6"]
* `logged` - (Optional) Flag to enable packet logging. Default is disabled.
* `notes` - (Optional) User notes specific to the rule.
* `rule_tag` - (Optional) User level field which will be printed in CLI and packet logs.
* `service` - (Optional) List of the services. Null will be treated as any. [Allowed target types: "NSService", "NSServiceGroup"]
* `source` - (Optional) List of sources. Null will be treated as any. [Allowed target types: "IPSet", "LogicalPort", "LogicalSwitch", "NSGroup", "MACSet" (depending on the section type)]
* `sources_excluded` - (Optional) When this boolean flag is set to true, the rule sources will be negated.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The display name of this rule. Defaults to ID if not set.
* `description` - (Optional) Description of this rule.
* `action` - (Required) Action enforced on the packets which matches the firewall rule. [Allowed values: "ALLOW", "DROP", "REJECT"]
* `applied_to` - (Optional) List of objects where rule will be enforced. The section level field overrides this one. Null will be treated as any. [Supported target types: "LogicalPort", "LogicalSwitch", "NSGroup", "LogicalRouterPort"]
* `destination` - (Optional) List of the destinations. Null will be treated as any. [Allowed target types: "IPSet", "LogicalPort", "LogicalSwitch", "NSGroup", "MACSet" (depending on the section type)]
* `destinations_excluded` - (Optional) When this boolean flag is set to true, the rule destinations will be negated.
* `direction` - (Optional) Rule direction in case of stateless firewall rules. This will only considered if section level parameter is set to stateless. Default to IN_OUT if not specified. [Allowed values: "IN", "OUT", "IN_OUT"]
* `disabled` - (Optional) Flag to disable rule. Disabled will only be persisted but never provisioned/realized.
* `ip_protocol` - (Optional) Type of IP packet that should be matched while enforcing the rule. [allowed values: "IPV4", "IPV6", "IPV4_IPV6"]
* `logged` - (Optional) Flag to enable packet logging. Default is disabled.
* `notes` - (Optional) User notes specific to the rule.
* `rule_tag` - (Optional) User level field which will be printed in CLI and packet logs.
* `service` - (Optional) List of the services. Null will be treated as any. [Allowed target types: "NSService", "NSServiceGroup"]
* `source` - (Optional) List of sources. Null will be treated as any. [Allowed target types: "IPSet", "LogicalPort", "LogicalSwitch", "NSGroup", "MACSet" (depending on the section type)]
* `sources_excluded` - (Optional) When this boolean flag is set to true, the rule sources will be negated.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsertBefore

Firewall section id that should come immediately after this one. It is user responsibility to use this attribute in consistent manner (for example, if same value would be set in two separate sections, the outcome would depend on order of creation). Changing this attribute would force recreation of the firewall section.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SectionType

Type of the rules which a section can contain. Either LAYER2 or LAYER3. Only homogeneous sections are supported.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stateful

Stateful or Stateless nature of firewall section is enforced on all rules inside the section. Layer3 sections can be stateful or stateless. Layer2 sections can only be stateless.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppliedTo

_Required_: No

_Type_: List of <a href="appliedto.md">AppliedTo</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of <a href="rule.md">Rule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tag.md">Tag</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: No

_Type_: List of <a href="destination.md">Destination</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: No

_Type_: List of <a href="service.md">Service</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

_Type_: List of <a href="source.md">Source</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### IsDefault

Returns the <code>IsDefault</code> value.

#### Revision

Returns the <code>Revision</code> value.

