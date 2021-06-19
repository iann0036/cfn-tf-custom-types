# TF::NSXT::PolicyService

This resource provides a way to configure a networking and security service which can be used within NSX Policy.

This resource is applicable to NSX Global Manager, NSX Policy Manager and VMC.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NSXT::PolicyService",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#nsxid" title="NsxId">NsxId</a>" : <i>String</i>,
        "<a href="#algorithmentry" title="AlgorithmEntry">AlgorithmEntry</a>" : <i>[ <a href="algorithmentrydefinition.md">AlgorithmEntryDefinition</a>, ... ]</i>,
        "<a href="#ethertypeentry" title="EtherTypeEntry">EtherTypeEntry</a>" : <i>[ <a href="ethertypeentrydefinition.md">EtherTypeEntryDefinition</a>, ... ]</i>,
        "<a href="#icmpentry" title="IcmpEntry">IcmpEntry</a>" : <i>[ <a href="icmpentrydefinition.md">IcmpEntryDefinition</a>, ... ]</i>,
        "<a href="#igmpentry" title="IgmpEntry">IgmpEntry</a>" : <i>[ <a href="igmpentrydefinition.md">IgmpEntryDefinition</a>, ... ]</i>,
        "<a href="#ipprotocolentry" title="IpProtocolEntry">IpProtocolEntry</a>" : <i>[ <a href="ipprotocolentrydefinition.md">IpProtocolEntryDefinition</a>, ... ]</i>,
        "<a href="#l4portsetentry" title="L4PortSetEntry">L4PortSetEntry</a>" : <i>[ <a href="l4portsetentrydefinition.md">L4PortSetEntryDefinition</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NSXT::PolicyService
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#nsxid" title="NsxId">NsxId</a>: <i>String</i>
    <a href="#algorithmentry" title="AlgorithmEntry">AlgorithmEntry</a>: <i>
      - <a href="algorithmentrydefinition.md">AlgorithmEntryDefinition</a></i>
    <a href="#ethertypeentry" title="EtherTypeEntry">EtherTypeEntry</a>: <i>
      - <a href="ethertypeentrydefinition.md">EtherTypeEntryDefinition</a></i>
    <a href="#icmpentry" title="IcmpEntry">IcmpEntry</a>: <i>
      - <a href="icmpentrydefinition.md">IcmpEntryDefinition</a></i>
    <a href="#igmpentry" title="IgmpEntry">IgmpEntry</a>: <i>
      - <a href="igmpentrydefinition.md">IgmpEntryDefinition</a></i>
    <a href="#ipprotocolentry" title="IpProtocolEntry">IpProtocolEntry</a>: <i>
      - <a href="ipprotocolentrydefinition.md">IpProtocolEntryDefinition</a></i>
    <a href="#l4portsetentry" title="L4PortSetEntry">L4PortSetEntry</a>: <i>
      - <a href="l4portsetentrydefinition.md">L4PortSetEntryDefinition</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
</pre>

## Properties

#### Description

Description of the service entry.
* `destination_port` - (Required) a single destination port.
* `source_ports` - (Optional) Set of source ports/ranges.
* `algorithm` - (Required) Algorithm one of "ORACLE_TNS", "FTP", "SUN_RPC_TCP", "SUN_RPC_UDP", "MS_RPC_TCP", "MS_RPC_UDP", "NBNS_BROADCAST", "NBDG_BROADCAST", "TFTP".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

Display name of the service entry.
* `description` - (Optional) Description of the service entry.
* `destination_port` - (Required) a single destination port.
* `source_ports` - (Optional) Set of source ports/ranges.
* `algorithm` - (Required) Algorithm one of "ORACLE_TNS", "FTP", "SUN_RPC_TCP", "SUN_RPC_UDP", "MS_RPC_TCP", "MS_RPC_UDP", "NBNS_BROADCAST", "NBDG_BROADCAST", "TFTP".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxId

The NSX ID of this resource. If set, this ID will be used to create the policy resource.
The service must contain at least 1 entry (of at least one of the types), and possibly more.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlgorithmEntry

_Required_: No

_Type_: List of <a href="algorithmentrydefinition.md">AlgorithmEntryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EtherTypeEntry

_Required_: No

_Type_: List of <a href="ethertypeentrydefinition.md">EtherTypeEntryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpEntry

_Required_: No

_Type_: List of <a href="icmpentrydefinition.md">IcmpEntryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgmpEntry

_Required_: No

_Type_: List of <a href="igmpentrydefinition.md">IgmpEntryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpProtocolEntry

_Required_: No

_Type_: List of <a href="ipprotocolentrydefinition.md">IpProtocolEntryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L4PortSetEntry

_Required_: No

_Type_: List of <a href="l4portsetentrydefinition.md">L4PortSetEntryDefinition</a>

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

