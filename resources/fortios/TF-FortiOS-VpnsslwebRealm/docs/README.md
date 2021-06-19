# TF::FortiOS::VpnsslwebRealm

CloudFormation equivalent of fortios_vpnsslweb_realm

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::VpnsslwebRealm",
    "Properties" : {
        "<a href="#loginpage" title="LoginPage">LoginPage</a>" : <i>String</i>,
        "<a href="#maxconcurrentuser" title="MaxConcurrentUser">MaxConcurrentUser</a>" : <i>Double</i>,
        "<a href="#nasip" title="NasIp">NasIp</a>" : <i>String</i>,
        "<a href="#radiusport" title="RadiusPort">RadiusPort</a>" : <i>Double</i>,
        "<a href="#radiusserver" title="RadiusServer">RadiusServer</a>" : <i>String</i>,
        "<a href="#urlpath" title="UrlPath">UrlPath</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#virtualhost" title="VirtualHost">VirtualHost</a>" : <i>String</i>,
        "<a href="#virtualhostonly" title="VirtualHostOnly">VirtualHostOnly</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::VpnsslwebRealm
Properties:
    <a href="#loginpage" title="LoginPage">LoginPage</a>: <i>String</i>
    <a href="#maxconcurrentuser" title="MaxConcurrentUser">MaxConcurrentUser</a>: <i>Double</i>
    <a href="#nasip" title="NasIp">NasIp</a>: <i>String</i>
    <a href="#radiusport" title="RadiusPort">RadiusPort</a>: <i>Double</i>
    <a href="#radiusserver" title="RadiusServer">RadiusServer</a>: <i>String</i>
    <a href="#urlpath" title="UrlPath">UrlPath</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#virtualhost" title="VirtualHost">VirtualHost</a>: <i>String</i>
    <a href="#virtualhostonly" title="VirtualHostOnly">VirtualHostOnly</a>: <i>String</i>
</pre>

## Properties

#### LoginPage

Replacement HTML for SSL-VPN login page.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConcurrentUser

Maximum concurrent users (0 - 65535, 0 means unlimited).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NasIp

IP address used as a NAS-IP to communicate with the RADIUS server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RadiusPort

RADIUS service port number (0 - 65535, 0 means user.radius.radius-port).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RadiusServer

RADIUS server associated with realm.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlPath

URL path to access SSL-VPN login page.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualHost

Virtual host name for realm.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualHostOnly

Enable/disable enforcement of virtual host method for SSL-VPN client access. Valid values: `enable`, `disable`.

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

