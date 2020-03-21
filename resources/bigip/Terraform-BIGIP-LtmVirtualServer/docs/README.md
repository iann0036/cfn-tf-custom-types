# Terraform::BIGIP::LtmVirtualServer

`bigip_ltm_virtual_server` Configures Virtual Server

For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::BIGIP::LtmVirtualServer",
    "Properties" : {
        "<a href="#clientprofiles" title="ClientProfiles">ClientProfiles</a>" : <i>[ String, ... ]</i>,
        "<a href="#defaultpersistenceprofile" title="DefaultPersistenceProfile">DefaultPersistenceProfile</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#destination" title="Destination">Destination</a>" : <i>String</i>,
        "<a href="#fallbackpersistenceprofile" title="FallbackPersistenceProfile">FallbackPersistenceProfile</a>" : <i>String</i>,
        "<a href="#ipprotocol" title="IpProtocol">IpProtocol</a>" : <i>String</i>,
        "<a href="#irules" title="Irules">Irules</a>" : <i>[ String, ... ]</i>,
        "<a href="#mask" title="Mask">Mask</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#persistenceprofiles" title="PersistenceProfiles">PersistenceProfiles</a>" : <i>[ String, ... ]</i>,
        "<a href="#policies" title="Policies">Policies</a>" : <i>[ String, ... ]</i>,
        "<a href="#pool" title="Pool">Pool</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#profiles" title="Profiles">Profiles</a>" : <i>[ String, ... ]</i>,
        "<a href="#serverprofiles" title="ServerProfiles">ServerProfiles</a>" : <i>[ String, ... ]</i>,
        "<a href="#snatpool" title="Snatpool">Snatpool</a>" : <i>String</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>,
        "<a href="#sourceaddresstranslation" title="SourceAddressTranslation">SourceAddressTranslation</a>" : <i>String</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#translateaddress" title="TranslateAddress">TranslateAddress</a>" : <i>String</i>,
        "<a href="#translateport" title="TranslatePort">TranslatePort</a>" : <i>String</i>,
        "<a href="#vlans" title="Vlans">Vlans</a>" : <i>[ String, ... ]</i>,
        "<a href="#vlansenabled" title="VlansEnabled">VlansEnabled</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::BIGIP::LtmVirtualServer
Properties:
    <a href="#clientprofiles" title="ClientProfiles">ClientProfiles</a>: <i>
      - String</i>
    <a href="#defaultpersistenceprofile" title="DefaultPersistenceProfile">DefaultPersistenceProfile</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#destination" title="Destination">Destination</a>: <i>String</i>
    <a href="#fallbackpersistenceprofile" title="FallbackPersistenceProfile">FallbackPersistenceProfile</a>: <i>String</i>
    <a href="#ipprotocol" title="IpProtocol">IpProtocol</a>: <i>String</i>
    <a href="#irules" title="Irules">Irules</a>: <i>
      - String</i>
    <a href="#mask" title="Mask">Mask</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#persistenceprofiles" title="PersistenceProfiles">PersistenceProfiles</a>: <i>
      - String</i>
    <a href="#policies" title="Policies">Policies</a>: <i>
      - String</i>
    <a href="#pool" title="Pool">Pool</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#profiles" title="Profiles">Profiles</a>: <i>
      - String</i>
    <a href="#serverprofiles" title="ServerProfiles">ServerProfiles</a>: <i>
      - String</i>
    <a href="#snatpool" title="Snatpool">Snatpool</a>: <i>String</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
    <a href="#sourceaddresstranslation" title="SourceAddressTranslation">SourceAddressTranslation</a>: <i>String</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#translateaddress" title="TranslateAddress">TranslateAddress</a>: <i>String</i>
    <a href="#translateport" title="TranslatePort">TranslatePort</a>: <i>String</i>
    <a href="#vlans" title="Vlans">Vlans</a>: <i>
      - String</i>
    <a href="#vlansenabled" title="VlansEnabled">VlansEnabled</a>: <i>Boolean</i>
</pre>

## Properties

#### ClientProfiles

List of client context profiles associated on the virtual server. Not mutually exclusive with profiles and server_profiles.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultPersistenceProfile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of Virtual server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

Destination IP.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FallbackPersistenceProfile

Specifies a fallback persistence profile for the Virtual Server to use when the default persistence profile is not available.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpProtocol

Specify the IP protocol to use with the the virtual server (all, tcp, or udp are valid).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Irules

The iRules list you want run on this virtual server. iRules help automate the intercepting, processing, and routing of application traffic.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mask

Mask can either be in CIDR notation or decimal, i.e.: 24 or 255.255.255.0. A CIDR mask of 0 is the same as 0.0.0.0.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the virtual server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistenceProfiles

List of persistence profiles associated with the Virtual Server.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policies

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pool

Default pool name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Listen port for the virtual server.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Profiles

List of profiles associated both client and server contexts on the virtual server. This includes protocol, ssl, http, etc.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerProfiles

List of server context profiles associated on the virtual server. Not mutually exclusive with profiles and client_profiles.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Snatpool

Specifies the name of an existing SNAT pool that you want the virtual server to use to implement selective and intelligent SNATs. DEPRECATED - see Virtual Server Property Groups source-address-translation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

Specifies an IP address or network from which the virtual server will accept traffic.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAddressTranslation

Can be either omitted for none or the values automap or snat.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TranslateAddress

Enables or disables address translation for the virtual server. Turn address translation off for a virtual server if you want to use the virtual server to load balance connections to any address. This option is useful when the system is load balancing devices that have the same IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TranslatePort

Enables or disables port translation. Turn port translation off for a virtual server if you want to use the virtual server to load balance connections to any service.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vlans

The virtual server is enabled/disabled on this set of VLANs. See vlans-disabled and vlans-enabled.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlansEnabled

Enables the virtual server on the VLANs specified by the VLANs option.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

