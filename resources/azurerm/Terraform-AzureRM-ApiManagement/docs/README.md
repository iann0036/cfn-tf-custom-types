# Terraform::AzureRM::ApiManagement

CloudFormation equivalent of azurerm_api_management

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::ApiManagement",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#gatewayregionalurl" title="GatewayRegionalUrl">GatewayRegionalUrl</a>" : <i>String</i>,
        "<a href="#gatewayurl" title="GatewayUrl">GatewayUrl</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#managementapiurl" title="ManagementApiUrl">ManagementApiUrl</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notificationsenderemail" title="NotificationSenderEmail">NotificationSenderEmail</a>" : <i>String</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>[ &lt;a href=&#34;policy.md&#34;&gt;Policy&lt;/a&gt;, ... ]</i>,
        "<a href="#portalurl" title="PortalUrl">PortalUrl</a>" : <i>String</i>,
        "<a href="#publicipaddresses" title="PublicIpAddresses">PublicIpAddresses</a>" : <i>[ String, ... ]</i>,
        "<a href="#publisheremail" title="PublisherEmail">PublisherEmail</a>" : <i>String</i>,
        "<a href="#publishername" title="PublisherName">PublisherName</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#scmurl" title="ScmUrl">ScmUrl</a>" : <i>String</i>,
        "<a href="#skuname" title="SkuName">SkuName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#additionallocation" title="AdditionalLocation">AdditionalLocation</a>" : <i>[ &lt;a href=&#34;additionallocation.md&#34;&gt;AdditionalLocation&lt;/a&gt;, ... ]</i>,
        "<a href="#certificate" title="Certificate">Certificate</a>" : <i>[ &lt;a href=&#34;certificate.md&#34;&gt;Certificate&lt;/a&gt;, ... ]</i>,
        "<a href="#hostnameconfiguration" title="HostnameConfiguration">HostnameConfiguration</a>" : <i>[ &lt;a href=&#34;hostnameconfiguration.md&#34;&gt;HostnameConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ &lt;a href=&#34;identity.md&#34;&gt;Identity&lt;/a&gt;, ... ]</i>,
        "<a href="#protocols" title="Protocols">Protocols</a>" : <i>[ &lt;a href=&#34;protocols.md&#34;&gt;Protocols&lt;/a&gt;, ... ]</i>,
        "<a href="#security" title="Security">Security</a>" : <i>[ &lt;a href=&#34;security.md&#34;&gt;Security&lt;/a&gt;, ... ]</i>,
        "<a href="#signin" title="SignIn">SignIn</a>" : <i>[ &lt;a href=&#34;signin.md&#34;&gt;SignIn&lt;/a&gt;, ... ]</i>,
        "<a href="#signup" title="SignUp">SignUp</a>" : <i>[ &lt;a href=&#34;signup.md&#34;&gt;SignUp&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#management" title="Management">Management</a>" : <i>[ &lt;a href=&#34;management.md&#34;&gt;Management&lt;/a&gt;, ... ]</i>,
        "<a href="#portal" title="Portal">Portal</a>" : <i>[ &lt;a href=&#34;portal.md&#34;&gt;Portal&lt;/a&gt;, ... ]</i>,
        "<a href="#proxy" title="Proxy">Proxy</a>" : <i>[ &lt;a href=&#34;proxy.md&#34;&gt;Proxy&lt;/a&gt;, ... ]</i>,
        "<a href="#scm" title="Scm">Scm</a>" : <i>[ &lt;a href=&#34;scm.md&#34;&gt;Scm&lt;/a&gt;, ... ]</i>,
        "<a href="#termsofservice" title="TermsOfService">TermsOfService</a>" : <i>[ &lt;a href=&#34;termsofservice.md&#34;&gt;TermsOfService&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::ApiManagement
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#gatewayregionalurl" title="GatewayRegionalUrl">GatewayRegionalUrl</a>: <i>String</i>
    <a href="#gatewayurl" title="GatewayUrl">GatewayUrl</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#managementapiurl" title="ManagementApiUrl">ManagementApiUrl</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notificationsenderemail" title="NotificationSenderEmail">NotificationSenderEmail</a>: <i>String</i>
    <a href="#policy" title="Policy">Policy</a>: <i>
      - &lt;a href=&#34;policy.md&#34;&gt;Policy&lt;/a&gt;</i>
    <a href="#portalurl" title="PortalUrl">PortalUrl</a>: <i>String</i>
    <a href="#publicipaddresses" title="PublicIpAddresses">PublicIpAddresses</a>: <i>
      - String</i>
    <a href="#publisheremail" title="PublisherEmail">PublisherEmail</a>: <i>String</i>
    <a href="#publishername" title="PublisherName">PublisherName</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#scmurl" title="ScmUrl">ScmUrl</a>: <i>String</i>
    <a href="#skuname" title="SkuName">SkuName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#additionallocation" title="AdditionalLocation">AdditionalLocation</a>: <i>
      - &lt;a href=&#34;additionallocation.md&#34;&gt;AdditionalLocation&lt;/a&gt;</i>
    <a href="#certificate" title="Certificate">Certificate</a>: <i>
      - &lt;a href=&#34;certificate.md&#34;&gt;Certificate&lt;/a&gt;</i>
    <a href="#hostnameconfiguration" title="HostnameConfiguration">HostnameConfiguration</a>: <i>
      - &lt;a href=&#34;hostnameconfiguration.md&#34;&gt;HostnameConfiguration&lt;/a&gt;</i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - &lt;a href=&#34;identity.md&#34;&gt;Identity&lt;/a&gt;</i>
    <a href="#protocols" title="Protocols">Protocols</a>: <i>
      - &lt;a href=&#34;protocols.md&#34;&gt;Protocols&lt;/a&gt;</i>
    <a href="#security" title="Security">Security</a>: <i>
      - &lt;a href=&#34;security.md&#34;&gt;Security&lt;/a&gt;</i>
    <a href="#signin" title="SignIn">SignIn</a>: <i>
      - &lt;a href=&#34;signin.md&#34;&gt;SignIn&lt;/a&gt;</i>
    <a href="#signup" title="SignUp">SignUp</a>: <i>
      - &lt;a href=&#34;signup.md&#34;&gt;SignUp&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#management" title="Management">Management</a>: <i>
      - &lt;a href=&#34;management.md&#34;&gt;Management&lt;/a&gt;</i>
    <a href="#portal" title="Portal">Portal</a>: <i>
      - &lt;a href=&#34;portal.md&#34;&gt;Portal&lt;/a&gt;</i>
    <a href="#proxy" title="Proxy">Proxy</a>: <i>
      - &lt;a href=&#34;proxy.md&#34;&gt;Proxy&lt;/a&gt;</i>
    <a href="#scm" title="Scm">Scm</a>: <i>
      - &lt;a href=&#34;scm.md&#34;&gt;Scm&lt;/a&gt;</i>
    <a href="#termsofservice" title="TermsOfService">TermsOfService</a>: <i>
      - &lt;a href=&#34;termsofservice.md&#34;&gt;TermsOfService&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayRegionalUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagementApiUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationSenderEmail

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

_Required_: No

_Type_: List of &lt;a href=&#34;policy.md&#34;&gt;Policy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortalUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIpAddresses

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublisherEmail

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublisherName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScmUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkuName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalLocation

_Required_: No

_Type_: List of &lt;a href=&#34;additionallocation.md&#34;&gt;AdditionalLocation&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

_Required_: No

_Type_: List of &lt;a href=&#34;certificate.md&#34;&gt;Certificate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostnameConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;hostnameconfiguration.md&#34;&gt;HostnameConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of &lt;a href=&#34;identity.md&#34;&gt;Identity&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocols

_Required_: No

_Type_: List of &lt;a href=&#34;protocols.md&#34;&gt;Protocols&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Security

_Required_: No

_Type_: List of &lt;a href=&#34;security.md&#34;&gt;Security&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignIn

_Required_: No

_Type_: List of &lt;a href=&#34;signin.md&#34;&gt;SignIn&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignUp

_Required_: No

_Type_: List of &lt;a href=&#34;signup.md&#34;&gt;SignUp&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Management

_Required_: No

_Type_: List of &lt;a href=&#34;management.md&#34;&gt;Management&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Portal

_Required_: No

_Type_: List of &lt;a href=&#34;portal.md&#34;&gt;Portal&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Proxy

_Required_: No

_Type_: List of &lt;a href=&#34;proxy.md&#34;&gt;Proxy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scm

_Required_: No

_Type_: List of &lt;a href=&#34;scm.md&#34;&gt;Scm&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TermsOfService

_Required_: No

_Type_: List of &lt;a href=&#34;termsofservice.md&#34;&gt;TermsOfService&lt;/a&gt;

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

Returns the &lt;code&gt;GatewayRegionalUrl&lt;/code&gt; value.

#### GatewayUrl

Returns the &lt;code&gt;GatewayUrl&lt;/code&gt; value.

#### ManagementApiUrl

Returns the &lt;code&gt;ManagementApiUrl&lt;/code&gt; value.

#### PortalUrl

Returns the &lt;code&gt;PortalUrl&lt;/code&gt; value.

#### PublicIpAddresses

Returns the &lt;code&gt;PublicIpAddresses&lt;/code&gt; value.

#### ScmUrl

Returns the &lt;code&gt;ScmUrl&lt;/code&gt; value.

