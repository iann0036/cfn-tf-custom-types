# TF::FortiOS::SystemDnsdatabase

Configure DNS databases.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemDnsdatabase",
    "Properties" : {
        "<a href="#allowtransfer" title="AllowTransfer">AllowTransfer</a>" : <i>String</i>,
        "<a href="#authoritative" title="Authoritative">Authoritative</a>" : <i>String</i>,
        "<a href="#contact" title="Contact">Contact</a>" : <i>String</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#forwarder" title="Forwarder">Forwarder</a>" : <i>String</i>,
        "<a href="#ipmaster" title="IpMaster">IpMaster</a>" : <i>String</i>,
        "<a href="#ipprimary" title="IpPrimary">IpPrimary</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#primaryname" title="PrimaryName">PrimaryName</a>" : <i>String</i>,
        "<a href="#rrmax" title="RrMax">RrMax</a>" : <i>Double</i>,
        "<a href="#sourceip" title="SourceIp">SourceIp</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#view" title="View">View</a>" : <i>String</i>,
        "<a href="#dnsentry" title="DnsEntry">DnsEntry</a>" : <i>[ <a href="dnsentrydefinition.md">DnsEntryDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemDnsdatabase
Properties:
    <a href="#allowtransfer" title="AllowTransfer">AllowTransfer</a>: <i>String</i>
    <a href="#authoritative" title="Authoritative">Authoritative</a>: <i>String</i>
    <a href="#contact" title="Contact">Contact</a>: <i>String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#forwarder" title="Forwarder">Forwarder</a>: <i>String</i>
    <a href="#ipmaster" title="IpMaster">IpMaster</a>: <i>String</i>
    <a href="#ipprimary" title="IpPrimary">IpPrimary</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#primaryname" title="PrimaryName">PrimaryName</a>: <i>String</i>
    <a href="#rrmax" title="RrMax">RrMax</a>: <i>Double</i>
    <a href="#sourceip" title="SourceIp">SourceIp</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#view" title="View">View</a>: <i>String</i>
    <a href="#dnsentry" title="DnsEntry">DnsEntry</a>: <i>
      - <a href="dnsentrydefinition.md">DnsEntryDefinition</a></i>
</pre>

## Properties

#### AllowTransfer

DNS zone transfer IP address list.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authoritative

Enable/disable authoritative zone. Valid values: `enable`, `disable`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Contact

Email address of the administrator for this zone.
You can specify only the username (e.g. admin) or full email address (e.g. admin@test.com)
When using a simple username, the domain of the email will be this zone.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

Domain name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Forwarder

DNS zone forwarder IP address list.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpMaster

IP address of master DNS server. Entries in this master DNS server and imported into the DNS zone.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpPrimary

IP address of primary DNS server. Entries in this primary DNS server and imported into the DNS zone.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Zone name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryName

Domain name of the default DNS server for this zone.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RrMax

Maximum number of resource records (10 - 65536, 0 means infinite).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIp

Source IP for forwarding to DNS server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable this DNS zone. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

Default time-to-live value for the entries of this DNS zone (0 - 2147483647 sec, default = 86400).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Zone type (master to manage entries directly, slave to import entries from other zones).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### View

Zone view (public to serve public clients, shadow to serve internal clients). Valid values: `shadow`, `public`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsEntry

_Required_: No

_Type_: List of <a href="dnsentrydefinition.md">DnsEntryDefinition</a>

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

