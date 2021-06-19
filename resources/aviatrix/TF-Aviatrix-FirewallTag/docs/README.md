# TF::Aviatrix::FirewallTag

The **aviatrix_firewall_tag** resource allows the creation and management of [Aviatrix Stateful Firewall tags](https://docs.aviatrix.com/HowTos/tag_firewall.html) for tag-based security for gateways.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::FirewallTag",
    "Properties" : {
        "<a href="#firewalltag" title="FirewallTag">FirewallTag</a>" : <i>String</i>,
        "<a href="#cidrlist" title="CidrList">CidrList</a>" : <i>[ <a href="cidrlistdefinition.md">CidrListDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::FirewallTag
Properties:
    <a href="#firewalltag" title="FirewallTag">FirewallTag</a>: <i>String</i>
    <a href="#cidrlist" title="CidrList">CidrList</a>: <i>
      - <a href="cidrlistdefinition.md">CidrListDefinition</a></i>
</pre>

## Properties

#### FirewallTag

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CidrList

_Required_: No

_Type_: List of <a href="cidrlistdefinition.md">CidrListDefinition</a>

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

