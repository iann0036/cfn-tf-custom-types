# TF::AVI::Applicationprofile

The ApplicationProfile resource allows the creation and management of Avi ApplicationProfile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Applicationprofile",
    "Properties" : {
        "<a href="#cloudconfigcksum" title="CloudConfigCksum">CloudConfigCksum</a>" : <i>String</i>,
        "<a href="#createdby" title="CreatedBy">CreatedBy</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#preserveclientip" title="PreserveClientIp">PreserveClientIp</a>" : <i>Boolean</i>,
        "<a href="#preserveclientport" title="PreserveClientPort">PreserveClientPort</a>" : <i>Boolean</i>,
        "<a href="#preservedestipport" title="PreserveDestIpPort">PreserveDestIpPort</a>" : <i>Boolean</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#dnsserviceprofile" title="DnsServiceProfile">DnsServiceProfile</a>" : <i>[ <a href="dnsserviceprofiledefinition.md">DnsServiceProfileDefinition</a>, ... ]</i>,
        "<a href="#dosrlprofile" title="DosRlProfile">DosRlProfile</a>" : <i>[ <a href="dosrlprofiledefinition.md">DosRlProfileDefinition</a>, ... ]</i>,
        "<a href="#httpprofile" title="HttpProfile">HttpProfile</a>" : <i>[ <a href="httpprofiledefinition.md">HttpProfileDefinition</a>, ... ]</i>,
        "<a href="#markers" title="Markers">Markers</a>" : <i>[ <a href="markersdefinition.md">MarkersDefinition</a>, ... ]</i>,
        "<a href="#sipserviceprofile" title="SipServiceProfile">SipServiceProfile</a>" : <i>[ <a href="sipserviceprofiledefinition.md">SipServiceProfileDefinition</a>, ... ]</i>,
        "<a href="#tcpappprofile" title="TcpAppProfile">TcpAppProfile</a>" : <i>[ <a href="tcpappprofiledefinition.md">TcpAppProfileDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Applicationprofile
Properties:
    <a href="#cloudconfigcksum" title="CloudConfigCksum">CloudConfigCksum</a>: <i>String</i>
    <a href="#createdby" title="CreatedBy">CreatedBy</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#preserveclientip" title="PreserveClientIp">PreserveClientIp</a>: <i>Boolean</i>
    <a href="#preserveclientport" title="PreserveClientPort">PreserveClientPort</a>: <i>Boolean</i>
    <a href="#preservedestipport" title="PreserveDestIpPort">PreserveDestIpPort</a>: <i>Boolean</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#dnsserviceprofile" title="DnsServiceProfile">DnsServiceProfile</a>: <i>
      - <a href="dnsserviceprofiledefinition.md">DnsServiceProfileDefinition</a></i>
    <a href="#dosrlprofile" title="DosRlProfile">DosRlProfile</a>: <i>
      - <a href="dosrlprofiledefinition.md">DosRlProfileDefinition</a></i>
    <a href="#httpprofile" title="HttpProfile">HttpProfile</a>: <i>
      - <a href="httpprofiledefinition.md">HttpProfileDefinition</a></i>
    <a href="#markers" title="Markers">Markers</a>: <i>
      - <a href="markersdefinition.md">MarkersDefinition</a></i>
    <a href="#sipserviceprofile" title="SipServiceProfile">SipServiceProfile</a>: <i>
      - <a href="sipserviceprofiledefinition.md">SipServiceProfileDefinition</a></i>
    <a href="#tcpappprofile" title="TcpAppProfile">TcpAppProfile</a>: <i>
      - <a href="tcpappprofiledefinition.md">TcpAppProfileDefinition</a></i>
</pre>

## Properties

#### CloudConfigCksum

Checksum of application profiles. Internally set by cloud connector. Field introduced in 17.2.14, 18.1.5, 18.2.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreatedBy

Name of the application profile creator. Field introduced in 17.2.14, 18.1.5, 18.2.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

User defined description for the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the application profile.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreserveClientIp

Specifies if client ip needs to be preserved for backend connection. Not compatible with connection multiplexing.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreserveClientPort

Specifies if we need to preserve client port while preserving client ip for backend connections. Field introduced in 17.2.7.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreserveDestIpPort

Specifies if destination ip and port needs to be preserved for backend connection. Field introduced in 20.1.1. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

It is a reference to an object of type tenant.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Specifies which application layer proxy is enabled for the virtual service. Enum options - APPLICATION_PROFILE_TYPE_L4, APPLICATION_PROFILE_TYPE_HTTP, APPLICATION_PROFILE_TYPE_SYSLOG, APPLICATION_PROFILE_TYPE_DNS, APPLICATION_PROFILE_TYPE_SSL, APPLICATION_PROFILE_TYPE_SIP. Allowed in basic(allowed values- application_profile_type_l4,application_profile_type_http) edition, essentials(allowed values- application_profile_type_l4) edition, enterprise edition.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsServiceProfile

_Required_: No

_Type_: List of <a href="dnsserviceprofiledefinition.md">DnsServiceProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DosRlProfile

_Required_: No

_Type_: List of <a href="dosrlprofiledefinition.md">DosRlProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpProfile

_Required_: No

_Type_: List of <a href="httpprofiledefinition.md">HttpProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Markers

_Required_: No

_Type_: List of <a href="markersdefinition.md">MarkersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SipServiceProfile

_Required_: No

_Type_: List of <a href="sipserviceprofiledefinition.md">SipServiceProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpAppProfile

_Required_: No

_Type_: List of <a href="tcpappprofiledefinition.md">TcpAppProfileDefinition</a>

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

