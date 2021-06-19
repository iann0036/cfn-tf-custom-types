# TF::AzureRM::ApiManagement

Manages an API Management Service.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::ApiManagement",
    "Properties" : {
        "<a href="#clientcertificateenabled" title="ClientCertificateEnabled">ClientCertificateEnabled</a>" : <i>Boolean</i>,
        "<a href="#gatewaydisabled" title="GatewayDisabled">GatewayDisabled</a>" : <i>Boolean</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#minapiversion" title="MinApiVersion">MinApiVersion</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notificationsenderemail" title="NotificationSenderEmail">NotificationSenderEmail</a>" : <i>String</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>[ <a href="policydefinition.md">PolicyDefinition</a>, ... ]</i>,
        "<a href="#publisheremail" title="PublisherEmail">PublisherEmail</a>" : <i>String</i>,
        "<a href="#publishername" title="PublisherName">PublisherName</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#skuname" title="SkuName">SkuName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#virtualnetworktype" title="VirtualNetworkType">VirtualNetworkType</a>" : <i>String</i>,
        "<a href="#zones" title="Zones">Zones</a>" : <i>[ String, ... ]</i>,
        "<a href="#additionallocation" title="AdditionalLocation">AdditionalLocation</a>" : <i>[ <a href="additionallocationdefinition.md">AdditionalLocationDefinition</a>, ... ]</i>,
        "<a href="#certificate" title="Certificate">Certificate</a>" : <i>[ <a href="certificatedefinition.md">CertificateDefinition</a>, ... ]</i>,
        "<a href="#hostnameconfiguration" title="HostnameConfiguration">HostnameConfiguration</a>" : <i>[ <a href="hostnameconfigurationdefinition.md">HostnameConfigurationDefinition</a>, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ <a href="identitydefinition.md">IdentityDefinition</a>, ... ]</i>,
        "<a href="#protocols" title="Protocols">Protocols</a>" : <i>[ <a href="protocolsdefinition.md">ProtocolsDefinition</a>, ... ]</i>,
        "<a href="#security" title="Security">Security</a>" : <i>[ <a href="securitydefinition.md">SecurityDefinition</a>, ... ]</i>,
        "<a href="#signin" title="SignIn">SignIn</a>" : <i>[ <a href="signindefinition.md">SignInDefinition</a>, ... ]</i>,
        "<a href="#signup" title="SignUp">SignUp</a>" : <i>[ <a href="signupdefinition.md">SignUpDefinition</a>, ... ]</i>,
        "<a href="#tenantaccess" title="TenantAccess">TenantAccess</a>" : <i>[ <a href="tenantaccessdefinition.md">TenantAccessDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#virtualnetworkconfiguration" title="VirtualNetworkConfiguration">VirtualNetworkConfiguration</a>" : <i>[ <a href="virtualnetworkconfigurationdefinition.md">VirtualNetworkConfigurationDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::ApiManagement
Properties:
    <a href="#clientcertificateenabled" title="ClientCertificateEnabled">ClientCertificateEnabled</a>: <i>Boolean</i>
    <a href="#gatewaydisabled" title="GatewayDisabled">GatewayDisabled</a>: <i>Boolean</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#minapiversion" title="MinApiVersion">MinApiVersion</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notificationsenderemail" title="NotificationSenderEmail">NotificationSenderEmail</a>: <i>String</i>
    <a href="#policy" title="Policy">Policy</a>: <i>
      - <a href="policydefinition.md">PolicyDefinition</a></i>
    <a href="#publisheremail" title="PublisherEmail">PublisherEmail</a>: <i>String</i>
    <a href="#publishername" title="PublisherName">PublisherName</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#skuname" title="SkuName">SkuName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#virtualnetworktype" title="VirtualNetworkType">VirtualNetworkType</a>: <i>String</i>
    <a href="#zones" title="Zones">Zones</a>: <i>
      - String</i>
    <a href="#additionallocation" title="AdditionalLocation">AdditionalLocation</a>: <i>
      - <a href="additionallocationdefinition.md">AdditionalLocationDefinition</a></i>
    <a href="#certificate" title="Certificate">Certificate</a>: <i>
      - <a href="certificatedefinition.md">CertificateDefinition</a></i>
    <a href="#hostnameconfiguration" title="HostnameConfiguration">HostnameConfiguration</a>: <i>
      - <a href="hostnameconfigurationdefinition.md">HostnameConfigurationDefinition</a></i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - <a href="identitydefinition.md">IdentityDefinition</a></i>
    <a href="#protocols" title="Protocols">Protocols</a>: <i>
      - <a href="protocolsdefinition.md">ProtocolsDefinition</a></i>
    <a href="#security" title="Security">Security</a>: <i>
      - <a href="securitydefinition.md">SecurityDefinition</a></i>
    <a href="#signin" title="SignIn">SignIn</a>: <i>
      - <a href="signindefinition.md">SignInDefinition</a></i>
    <a href="#signup" title="SignUp">SignUp</a>: <i>
      - <a href="signupdefinition.md">SignUpDefinition</a></i>
    <a href="#tenantaccess" title="TenantAccess">TenantAccess</a>: <i>
      - <a href="tenantaccessdefinition.md">TenantAccessDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#virtualnetworkconfiguration" title="VirtualNetworkConfiguration">VirtualNetworkConfiguration</a>: <i>
      - <a href="virtualnetworkconfigurationdefinition.md">VirtualNetworkConfigurationDefinition</a></i>
</pre>

## Properties

#### ClientCertificateEnabled

Enforce a client certificate to be presented on each request to the gateway? This is only supported when sku type is `Consumption`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayDisabled

Disable the gateway in master region? This is only supported when `additional_location` is set.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

The Azure location where the API Management Service exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinApiVersion

The version which the control plane API calls to API Management service are limited with version equal to or newer than.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the API Management Service. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationSenderEmail

Email address from which the notification will be sent.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

A `policy` block as defined below.

_Required_: No

_Type_: List of <a href="policydefinition.md">PolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublisherEmail

The email of publisher/company.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublisherName

The name of publisher/company.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the Resource Group in which the API Management Service should be exist. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkuName

`sku_name` is a string consisting of two parts separated by an underscore(\_). The first part is the `name`, valid values include: `Consumption`, `Developer`, `Basic`, `Standard` and `Premium`. The second part is the `capacity` (e.g. the number of deployed units of the `sku`), which must be a positive `integer` (e.g. `Developer_1`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags assigned to the resource.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetworkType

The type of virtual network you want to use, valid values include: `None`, `External`, `Internal`.
> **NOTE:** Please ensure that in the subnet, inbound port 3443 is open when `virtual_network_type` is `Internal` or `External`. And please ensure other necessary ports are open according to [api management network configuration](https://docs.microsoft.com/en-us/azure/api-management/api-management-using-with-vnet#-common-network-configuration-issues).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zones

A list of availability zones.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalLocation

_Required_: No

_Type_: List of <a href="additionallocationdefinition.md">AdditionalLocationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

_Required_: No

_Type_: List of <a href="certificatedefinition.md">CertificateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostnameConfiguration

_Required_: No

_Type_: List of <a href="hostnameconfigurationdefinition.md">HostnameConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of <a href="identitydefinition.md">IdentityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocols

_Required_: No

_Type_: List of <a href="protocolsdefinition.md">ProtocolsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Security

_Required_: No

_Type_: List of <a href="securitydefinition.md">SecurityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignIn

_Required_: No

_Type_: List of <a href="signindefinition.md">SignInDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignUp

_Required_: No

_Type_: List of <a href="signupdefinition.md">SignUpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantAccess

_Required_: No

_Type_: List of <a href="tenantaccessdefinition.md">TenantAccessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetworkConfiguration

_Required_: No

_Type_: List of <a href="virtualnetworkconfigurationdefinition.md">VirtualNetworkConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DeveloperPortalUrl

Returns the <code>DeveloperPortalUrl</code> value.

#### GatewayRegionalUrl

Returns the <code>GatewayRegionalUrl</code> value.

#### GatewayUrl

Returns the <code>GatewayUrl</code> value.

#### Id

Returns the <code>Id</code> value.

#### ManagementApiUrl

Returns the <code>ManagementApiUrl</code> value.

#### PortalUrl

Returns the <code>PortalUrl</code> value.

#### PrivateIpAddresses

Returns the <code>PrivateIpAddresses</code> value.

#### PublicIpAddresses

Returns the <code>PublicIpAddresses</code> value.

#### ScmUrl

Returns the <code>ScmUrl</code> value.

