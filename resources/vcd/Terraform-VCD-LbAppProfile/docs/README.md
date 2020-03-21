# Terraform::VCD::LbAppProfile

Provides a vCloud Director Edge Gateway Load Balancer Application Profile resource. An application
profile defines the behavior of the load balancer for a particular type of network traffic. After
configuring a profile, you associate it with a virtual server. The virtual server then processes
traffic according to the values specified in the profile.

~> **Note:** This resource does not currently support attaching  Pool and Virtual
Server certificates. The `enable_pool_side_ssl` only toggles the option, but does not setup
certificates.

~> **Note:** To make load balancing work one must ensure that load balancing is enabled on edge
gateway (edge gateway must be advanced).
This depends on NSX version to work properly. Please refer to [VMware Product Interoperability
Matrices](https://www.vmware.com/resources/compatibility/sim/interop_matrix.php#interop&29=&93=) 
to check supported vCloud director and NSX for vSphere configurations.

~> **Note:** The vCloud Director API for NSX supports a subset of the operations and objects defined
in the NSX vSphere API Guide. The API supports NSX 6.2, 6.3, and 6.4.

Supported in provider *v2.4+*

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VCD::LbAppProfile",
    "Properties" : {
        "<a href="#cookiemode" title="CookieMode">CookieMode</a>" : <i>String</i>,
        "<a href="#cookiename" title="CookieName">CookieName</a>" : <i>String</i>,
        "<a href="#edgegateway" title="EdgeGateway">EdgeGateway</a>" : <i>String</i>,
        "<a href="#enablepoolsidessl" title="EnablePoolSideSsl">EnablePoolSideSsl</a>" : <i>Boolean</i>,
        "<a href="#enablesslpassthrough" title="EnableSslPassthrough">EnableSslPassthrough</a>" : <i>Boolean</i>,
        "<a href="#expiration" title="Expiration">Expiration</a>" : <i>Double</i>,
        "<a href="#httpredirecturl" title="HttpRedirectUrl">HttpRedirectUrl</a>" : <i>String</i>,
        "<a href="#insertxforwardedhttpheader" title="InsertXForwardedHttpHeader">InsertXForwardedHttpHeader</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#org" title="Org">Org</a>" : <i>String</i>,
        "<a href="#persistencemechanism" title="PersistenceMechanism">PersistenceMechanism</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#vdc" title="Vdc">Vdc</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VCD::LbAppProfile
Properties:
    <a href="#cookiemode" title="CookieMode">CookieMode</a>: <i>String</i>
    <a href="#cookiename" title="CookieName">CookieName</a>: <i>String</i>
    <a href="#edgegateway" title="EdgeGateway">EdgeGateway</a>: <i>String</i>
    <a href="#enablepoolsidessl" title="EnablePoolSideSsl">EnablePoolSideSsl</a>: <i>Boolean</i>
    <a href="#enablesslpassthrough" title="EnableSslPassthrough">EnableSslPassthrough</a>: <i>Boolean</i>
    <a href="#expiration" title="Expiration">Expiration</a>: <i>Double</i>
    <a href="#httpredirecturl" title="HttpRedirectUrl">HttpRedirectUrl</a>: <i>String</i>
    <a href="#insertxforwardedhttpheader" title="InsertXForwardedHttpHeader">InsertXForwardedHttpHeader</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#org" title="Org">Org</a>: <i>String</i>
    <a href="#persistencemechanism" title="PersistenceMechanism">PersistenceMechanism</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#vdc" title="Vdc">Vdc</a>: <i>String</i>
</pre>

## Properties

#### CookieMode

The mode by which the cookie should be inserted. One of 'insert',
'prefix', or 'appsession'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CookieName

Used to uniquely identify the session the first time a client accesses
the site. The load balancer refers to this cookie when connecting subsequent requests in the
session, so that they all go to the same virtual server. Only applies for
`persistence_mechanism` 'cookie'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EdgeGateway

The name of the edge gateway on which the application profile is to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePoolSideSsl

Enable to define the certificate, CAs, or CRLs used to
authenticate the load balancer from the server side. **Note:** This resource does not currently
support attaching Pool and Virtual Server certificates therefore this toggle only enables it. To
make it fully work certificates must be currently attached manually.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableSslPassthrough

Enable SSL authentication to be passed through to the
virtual server. Otherwise SSL authentication takes place at the destination address.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expiration

Length of time in seconds that persistence stays in effect.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpRedirectUrl

The URL to which traffic that arrives at the destination address
should be redirected. Only applies for types `http` and `https`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsertXForwardedHttpHeader

Enables 'X-Forwarded-For' header for identifying
the originating IP address of a client connecting to a Web server through the load balancer.
Only applies for types `http` and `https`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Application profile name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Org

The name of organization to use, optional if defined at provider level. Useful when connected as sysadmin working across different organisations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistenceMechanism

Persistence mechanism for the profile. One of 'cookie',
'ssl-sessionid', 'sourceip'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Protocol type used to send requests to the server. One of `tcp`, `udp`,
`http`, or `https`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdc

The name of VDC to use, optional if defined at provider level.

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

