# TF::FortiOS::EndpointcontrolFctems

Configure FortiClient Enterprise Management Server (EMS) entries.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::EndpointcontrolFctems",
    "Properties" : {
        "<a href="#adminpassword" title="AdminPassword">AdminPassword</a>" : <i>String</i>,
        "<a href="#adminusername" title="AdminUsername">AdminUsername</a>" : <i>String</i>,
        "<a href="#calltimeout" title="CallTimeout">CallTimeout</a>" : <i>Double</i>,
        "<a href="#certificate" title="Certificate">Certificate</a>" : <i>String</i>,
        "<a href="#cloudservertype" title="CloudServerType">CloudServerType</a>" : <i>String</i>,
        "<a href="#fortinetonecloudauthentication" title="FortinetoneCloudAuthentication">FortinetoneCloudAuthentication</a>" : <i>String</i>,
        "<a href="#httpsport" title="HttpsPort">HttpsPort</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pullavatars" title="PullAvatars">PullAvatars</a>" : <i>String</i>,
        "<a href="#pullsysinfo" title="PullSysinfo">PullSysinfo</a>" : <i>String</i>,
        "<a href="#pulltags" title="PullTags">PullTags</a>" : <i>String</i>,
        "<a href="#pullvulnerabilities" title="PullVulnerabilities">PullVulnerabilities</a>" : <i>String</i>,
        "<a href="#serialnumber" title="SerialNumber">SerialNumber</a>" : <i>String</i>,
        "<a href="#server" title="Server">Server</a>" : <i>String</i>,
        "<a href="#sourceip" title="SourceIp">SourceIp</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::EndpointcontrolFctems
Properties:
    <a href="#adminpassword" title="AdminPassword">AdminPassword</a>: <i>String</i>
    <a href="#adminusername" title="AdminUsername">AdminUsername</a>: <i>String</i>
    <a href="#calltimeout" title="CallTimeout">CallTimeout</a>: <i>Double</i>
    <a href="#certificate" title="Certificate">Certificate</a>: <i>String</i>
    <a href="#cloudservertype" title="CloudServerType">CloudServerType</a>: <i>String</i>
    <a href="#fortinetonecloudauthentication" title="FortinetoneCloudAuthentication">FortinetoneCloudAuthentication</a>: <i>String</i>
    <a href="#httpsport" title="HttpsPort">HttpsPort</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pullavatars" title="PullAvatars">PullAvatars</a>: <i>String</i>
    <a href="#pullsysinfo" title="PullSysinfo">PullSysinfo</a>: <i>String</i>
    <a href="#pulltags" title="PullTags">PullTags</a>: <i>String</i>
    <a href="#pullvulnerabilities" title="PullVulnerabilities">PullVulnerabilities</a>: <i>String</i>
    <a href="#serialnumber" title="SerialNumber">SerialNumber</a>: <i>String</i>
    <a href="#server" title="Server">Server</a>: <i>String</i>
    <a href="#sourceip" title="SourceIp">SourceIp</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### AdminPassword

FortiClient EMS admin password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminUsername

FortiClient EMS admin username.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CallTimeout

FortiClient EMS call timeout in milliseconds (500 - 30000 milliseconds, default = 5000).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

FortiClient EMS certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudServerType

Cloud server type. Valid values: `production`, `alpha`, `beta`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FortinetoneCloudAuthentication

Enable/disable authentication of FortiClient EMS Cloud through FortiCloud account. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsPort

FortiClient EMS HTTPS access port number. (1 - 65535, default: 443).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

FortiClient Enterprise Management Server (EMS) name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PullAvatars

Enable/disable pulling avatars from EMS. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PullSysinfo

Enable/disable pulling SysInfo from EMS. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PullTags

Enable/disable pulling FortiClient user tags from EMS. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PullVulnerabilities

Enable/disable pulling vulnerabilities from EMS. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SerialNumber

FortiClient EMS Serial Number.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Server

FortiClient EMS FQDN or IPv4 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIp

REST API call source IP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

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

