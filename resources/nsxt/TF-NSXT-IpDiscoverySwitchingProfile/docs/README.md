# TF::NSXT::IpDiscoverySwitchingProfile

Provides a resource to configure IP discovery switching profile on NSX-T manager

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NSXT::IpDiscoverySwitchingProfile",
    "Properties" : {
        "<a href="#arpbindingslimit" title="ArpBindingsLimit">ArpBindingsLimit</a>" : <i>Double</i>,
        "<a href="#arpsnoopingenabled" title="ArpSnoopingEnabled">ArpSnoopingEnabled</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dhcpsnoopingenabled" title="DhcpSnoopingEnabled">DhcpSnoopingEnabled</a>" : <i>Boolean</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#vmtoolsenabled" title="VmToolsEnabled">VmToolsEnabled</a>" : <i>Boolean</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NSXT::IpDiscoverySwitchingProfile
Properties:
    <a href="#arpbindingslimit" title="ArpBindingsLimit">ArpBindingsLimit</a>: <i>Double</i>
    <a href="#arpsnoopingenabled" title="ArpSnoopingEnabled">ArpSnoopingEnabled</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dhcpsnoopingenabled" title="DhcpSnoopingEnabled">DhcpSnoopingEnabled</a>: <i>Boolean</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#vmtoolsenabled" title="VmToolsEnabled">VmToolsEnabled</a>: <i>Boolean</i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
</pre>

## Properties

#### ArpBindingsLimit

Limit for the amount of ARP bindings.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArpSnoopingEnabled

A boolean flag iIndicates whether ARP snooping is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of this resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpSnoopingEnabled

A boolean flag iIndicates whether DHCP snooping is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The display name of this resource. Defaults to ID if not set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmToolsEnabled

A boolean flag iIndicates whether VM tools will be enabled. This option is only supported on ESX where vm-tools is installed.

_Required_: No

_Type_: Boolean

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

#### Revision

Returns the <code>Revision</code> value.

