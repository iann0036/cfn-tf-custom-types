# TF::CheckPoint::ManagementHost

This resource allows you to add/update/delete Check Point Host.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CheckPoint::ManagementHost",
    "Properties" : {
        "<a href="#color" title="Color">Color</a>" : <i>String</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#ignoreerrors" title="IgnoreErrors">IgnoreErrors</a>" : <i>Boolean</i>,
        "<a href="#ignorewarnings" title="IgnoreWarnings">IgnoreWarnings</a>" : <i>Boolean</i>,
        "<a href="#ipv4address" title="Ipv4Address">Ipv4Address</a>" : <i>String</i>,
        "<a href="#ipv6address" title="Ipv6Address">Ipv6Address</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#natsettings" title="NatSettings">NatSettings</a>" : <i>[ <a href="natsettingsdefinition.md">NatSettingsDefinition</a>, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#hostservers" title="HostServers">HostServers</a>" : <i>[ <a href="hostserversdefinition.md">HostServersDefinition</a>, ... ]</i>,
        "<a href="#interfaces" title="Interfaces">Interfaces</a>" : <i>[ <a href="interfacesdefinition.md">InterfacesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CheckPoint::ManagementHost
Properties:
    <a href="#color" title="Color">Color</a>: <i>String</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#ignoreerrors" title="IgnoreErrors">IgnoreErrors</a>: <i>Boolean</i>
    <a href="#ignorewarnings" title="IgnoreWarnings">IgnoreWarnings</a>: <i>Boolean</i>
    <a href="#ipv4address" title="Ipv4Address">Ipv4Address</a>: <i>String</i>
    <a href="#ipv6address" title="Ipv6Address">Ipv6Address</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#natsettings" title="NatSettings">NatSettings</a>: <i>
      - <a href="natsettingsdefinition.md">NatSettingsDefinition</a></i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#hostservers" title="HostServers">HostServers</a>: <i>
      - <a href="hostserversdefinition.md">HostServersDefinition</a></i>
    <a href="#interfaces" title="Interfaces">Interfaces</a>: <i>
      - <a href="interfacesdefinition.md">InterfacesDefinition</a></i>
</pre>

## Properties

#### Color

Color of the object. Should be one of existing colors.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

Comments string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreErrors

Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreWarnings

Apply changes ignoring warnings.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4Address

IPv4 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Address

IPv6 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Object name. Should be unique in the domain.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NatSettings

NAT settings. NAT settings blocks are documented below.

_Required_: No

_Type_: List of <a href="natsettingsdefinition.md">NatSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Collection of tag identifiers.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostServers

_Required_: No

_Type_: List of <a href="hostserversdefinition.md">HostServersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interfaces

_Required_: No

_Type_: List of <a href="interfacesdefinition.md">InterfacesDefinition</a>

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

