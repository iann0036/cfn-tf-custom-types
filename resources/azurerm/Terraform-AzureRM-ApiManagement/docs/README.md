# Terraform::AzureRM::ApiManagement

Manages an API Management Service.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::ApiManagement",
    "Properties" : {
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notificationsenderemail" title="NotificationSenderEmail">NotificationSenderEmail</a>" : <i>String</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>[ <a href="policy.md">Policy</a>, ... ]</i>,
        "<a href="#publisheremail" title="PublisherEmail">PublisherEmail</a>" : <i>String</i>,
        "<a href="#publishername" title="PublisherName">PublisherName</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#skuname" title="SkuName">SkuName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#additionallocation" title="AdditionalLocation">AdditionalLocation</a>" : <i>[ <a href="additionallocation.md">AdditionalLocation</a>, ... ]</i>,
        "<a href="#certificate" title="Certificate">Certificate</a>" : <i>[ <a href="certificate.md">Certificate</a>, ... ]</i>,
        "<a href="#hostnameconfiguration" title="HostnameConfiguration">HostnameConfiguration</a>" : <i>[ <a href="hostnameconfiguration.md">HostnameConfiguration</a>, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ <a href="identity.md">Identity</a>, ... ]</i>,
        "<a href="#protocols" title="Protocols">Protocols</a>" : <i>[ <a href="protocols.md">Protocols</a>, ... ]</i>,
        "<a href="#security" title="Security">Security</a>" : <i>[ <a href="security.md">Security</a>, ... ]</i>,
        "<a href="#signin" title="SignIn">SignIn</a>" : <i>[ <a href="signin.md">SignIn</a>, ... ]</i>,
        "<a href="#signup" title="SignUp">SignUp</a>" : <i>[ <a href="signup.md">SignUp</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#management" title="Management">Management</a>" : <i>[ <a href="management.md">Management</a>, ... ]</i>,
        "<a href="#portal" title="Portal">Portal</a>" : <i>[ <a href="portal.md">Portal</a>, ... ]</i>,
        "<a href="#proxy" title="Proxy">Proxy</a>" : <i>[ <a href="proxy.md">Proxy</a>, ... ]</i>,
        "<a href="#scm" title="Scm">Scm</a>" : <i>[ <a href="scm.md">Scm</a>, ... ]</i>,
        "<a href="#termsofservice" title="TermsOfService">TermsOfService</a>" : <i>[ <a href="termsofservice.md">TermsOfService</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::ApiManagement
Properties:
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notificationsenderemail" title="NotificationSenderEmail">NotificationSenderEmail</a>: <i>String</i>
    <a href="#policy" title="Policy">Policy</a>: <i>
      - <a href="policy.md">Policy</a></i>
    <a href="#publisheremail" title="PublisherEmail">PublisherEmail</a>: <i>String</i>
    <a href="#publishername" title="PublisherName">PublisherName</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#skuname" title="SkuName">SkuName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#additionallocation" title="AdditionalLocation">AdditionalLocation</a>: <i>
      - <a href="additionallocation.md">AdditionalLocation</a></i>
    <a href="#certificate" title="Certificate">Certificate</a>: <i>
      - <a href="certificate.md">Certificate</a></i>
    <a href="#hostnameconfiguration" title="HostnameConfiguration">HostnameConfiguration</a>: <i>
      - <a href="hostnameconfiguration.md">HostnameConfiguration</a></i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - <a href="identity.md">Identity</a></i>
    <a href="#protocols" title="Protocols">Protocols</a>: <i>
      - <a href="protocols.md">Protocols</a></i>
    <a href="#security" title="Security">Security</a>: <i>
      - <a href="security.md">Security</a></i>
    <a href="#signin" title="SignIn">SignIn</a>: <i>
      - <a href="signin.md">SignIn</a></i>
    <a href="#signup" title="SignUp">SignUp</a>: <i>
      - <a href="signup.md">SignUp</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#management" title="Management">Management</a>: <i>
      - <a href="management.md">Management</a></i>
    <a href="#portal" title="Portal">Portal</a>: <i>
      - <a href="portal.md">Portal</a></i>
    <a href="#proxy" title="Proxy">Proxy</a>: <i>
      - <a href="proxy.md">Proxy</a></i>
    <a href="#scm" title="Scm">Scm</a>: <i>
      - <a href="scm.md">Scm</a></i>
    <a href="#termsofservice" title="TermsOfService">TermsOfService</a>: <i>
      - <a href="termsofservice.md">TermsOfService</a></i>
</pre>

## Properties

#### Location

The Azure location where the API Management Service exists. Changing this forces a new resource to be created.

_Required_: Yes

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

_Type_: List of <a href="policy.md">Policy</a>

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

`sku_name` is a string consisting of two parts separated by an underscore(\_). The fist part is the `name`, valid values include: `Developer`, `Basic`, `Standard` and `Premium`. The second part is the `capacity` (e.g. the number of deployed units of the `sku`), which must be a positive `integer` (e.g. `Developer_1`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags assigned to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalLocation

_Required_: No

_Type_: List of <a href="additionallocation.md">AdditionalLocation</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

_Required_: No

_Type_: List of <a href="certificate.md">Certificate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostnameConfiguration

_Required_: No

_Type_: List of <a href="hostnameconfiguration.md">HostnameConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of <a href="identity.md">Identity</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocols

_Required_: No

_Type_: List of <a href="protocols.md">Protocols</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Security

_Required_: No

_Type_: List of <a href="security.md">Security</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignIn

_Required_: No

_Type_: List of <a href="signin.md">SignIn</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignUp

_Required_: No

_Type_: List of <a href="signup.md">SignUp</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Management

_Required_: No

_Type_: List of <a href="management.md">Management</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Portal

_Required_: No

_Type_: List of <a href="portal.md">Portal</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Proxy

_Required_: No

_Type_: List of <a href="proxy.md">Proxy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scm

_Required_: No

_Type_: List of <a href="scm.md">Scm</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TermsOfService

_Required_: No

_Type_: List of <a href="termsofservice.md">TermsOfService</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

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

#### PublicIpAddresses

Returns the <code>PublicIpAddresses</code> value.

#### ScmUrl

Returns the <code>ScmUrl</code> value.

