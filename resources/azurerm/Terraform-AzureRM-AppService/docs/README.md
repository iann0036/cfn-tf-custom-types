# Terraform::AzureRM::AppService

CloudFormation equivalent of azurerm_app_service

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::AppService",
    "Properties" : {
        "<a href="#appserviceplanid" title="AppServicePlanId">AppServicePlanId</a>" : <i>String</i>,
        "<a href="#appsettings" title="AppSettings">AppSettings</a>" : <i>[ &lt;a href=&#34;appsettings.md&#34;&gt;AppSettings&lt;/a&gt;, ... ]</i>,
        "<a href="#clientaffinityenabled" title="ClientAffinityEnabled">ClientAffinityEnabled</a>" : <i>Boolean</i>,
        "<a href="#clientcertenabled" title="ClientCertEnabled">ClientCertEnabled</a>" : <i>Boolean</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#httpsonly" title="HttpsOnly">HttpsOnly</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#authsettings" title="AuthSettings">AuthSettings</a>" : <i>[ &lt;a href=&#34;authsettings.md&#34;&gt;AuthSettings&lt;/a&gt;, ... ]</i>,
        "<a href="#backup" title="Backup">Backup</a>" : <i>[ &lt;a href=&#34;backup.md&#34;&gt;Backup&lt;/a&gt;, ... ]</i>,
        "<a href="#connectionstring" title="ConnectionString">ConnectionString</a>" : <i>[ &lt;a href=&#34;connectionstring.md&#34;&gt;ConnectionString&lt;/a&gt;, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ &lt;a href=&#34;identity.md&#34;&gt;Identity&lt;/a&gt;, ... ]</i>,
        "<a href="#logs" title="Logs">Logs</a>" : <i>[ &lt;a href=&#34;logs.md&#34;&gt;Logs&lt;/a&gt;, ... ]</i>,
        "<a href="#siteconfig" title="SiteConfig">SiteConfig</a>" : <i>[ &lt;a href=&#34;siteconfig.md&#34;&gt;SiteConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#storageaccount" title="StorageAccount">StorageAccount</a>" : <i>[ &lt;a href=&#34;storageaccount.md&#34;&gt;StorageAccount&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#activedirectory" title="ActiveDirectory">ActiveDirectory</a>" : <i>[ &lt;a href=&#34;activedirectory.md&#34;&gt;ActiveDirectory&lt;/a&gt;, ... ]</i>,
        "<a href="#facebook" title="Facebook">Facebook</a>" : <i>[ &lt;a href=&#34;facebook.md&#34;&gt;Facebook&lt;/a&gt;, ... ]</i>,
        "<a href="#google" title="Google">Google</a>" : <i>[ &lt;a href=&#34;google.md&#34;&gt;Google&lt;/a&gt;, ... ]</i>,
        "<a href="#microsoft" title="Microsoft">Microsoft</a>" : <i>[ &lt;a href=&#34;microsoft.md&#34;&gt;Microsoft&lt;/a&gt;, ... ]</i>,
        "<a href="#twitter" title="Twitter">Twitter</a>" : <i>[ &lt;a href=&#34;twitter.md&#34;&gt;Twitter&lt;/a&gt;, ... ]</i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>[ &lt;a href=&#34;schedule.md&#34;&gt;Schedule&lt;/a&gt;, ... ]</i>,
        "<a href="#applicationlogs" title="ApplicationLogs">ApplicationLogs</a>" : <i>[ &lt;a href=&#34;applicationlogs.md&#34;&gt;ApplicationLogs&lt;/a&gt;, ... ]</i>,
        "<a href="#httplogs" title="HttpLogs">HttpLogs</a>" : <i>[ &lt;a href=&#34;httplogs.md&#34;&gt;HttpLogs&lt;/a&gt;, ... ]</i>,
        "<a href="#cors" title="Cors">Cors</a>" : <i>[ &lt;a href=&#34;cors.md&#34;&gt;Cors&lt;/a&gt;, ... ]</i>,
        "<a href="#azureblobstorage" title="AzureBlobStorage">AzureBlobStorage</a>" : <i>[ &lt;a href=&#34;azureblobstorage.md&#34;&gt;AzureBlobStorage&lt;/a&gt;, ... ]</i>,
        "<a href="#filesystem" title="FileSystem">FileSystem</a>" : <i>[ &lt;a href=&#34;filesystem.md&#34;&gt;FileSystem&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::AppService
Properties:
    <a href="#appserviceplanid" title="AppServicePlanId">AppServicePlanId</a>: <i>String</i>
    <a href="#appsettings" title="AppSettings">AppSettings</a>: <i>
      - &lt;a href=&#34;appsettings.md&#34;&gt;AppSettings&lt;/a&gt;</i>
    <a href="#clientaffinityenabled" title="ClientAffinityEnabled">ClientAffinityEnabled</a>: <i>Boolean</i>
    <a href="#clientcertenabled" title="ClientCertEnabled">ClientCertEnabled</a>: <i>Boolean</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#httpsonly" title="HttpsOnly">HttpsOnly</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#authsettings" title="AuthSettings">AuthSettings</a>: <i>
      - &lt;a href=&#34;authsettings.md&#34;&gt;AuthSettings&lt;/a&gt;</i>
    <a href="#backup" title="Backup">Backup</a>: <i>
      - &lt;a href=&#34;backup.md&#34;&gt;Backup&lt;/a&gt;</i>
    <a href="#connectionstring" title="ConnectionString">ConnectionString</a>: <i>
      - &lt;a href=&#34;connectionstring.md&#34;&gt;ConnectionString&lt;/a&gt;</i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - &lt;a href=&#34;identity.md&#34;&gt;Identity&lt;/a&gt;</i>
    <a href="#logs" title="Logs">Logs</a>: <i>
      - &lt;a href=&#34;logs.md&#34;&gt;Logs&lt;/a&gt;</i>
    <a href="#siteconfig" title="SiteConfig">SiteConfig</a>: <i>
      - &lt;a href=&#34;siteconfig.md&#34;&gt;SiteConfig&lt;/a&gt;</i>
    <a href="#storageaccount" title="StorageAccount">StorageAccount</a>: <i>
      - &lt;a href=&#34;storageaccount.md&#34;&gt;StorageAccount&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#activedirectory" title="ActiveDirectory">ActiveDirectory</a>: <i>
      - &lt;a href=&#34;activedirectory.md&#34;&gt;ActiveDirectory&lt;/a&gt;</i>
    <a href="#facebook" title="Facebook">Facebook</a>: <i>
      - &lt;a href=&#34;facebook.md&#34;&gt;Facebook&lt;/a&gt;</i>
    <a href="#google" title="Google">Google</a>: <i>
      - &lt;a href=&#34;google.md&#34;&gt;Google&lt;/a&gt;</i>
    <a href="#microsoft" title="Microsoft">Microsoft</a>: <i>
      - &lt;a href=&#34;microsoft.md&#34;&gt;Microsoft&lt;/a&gt;</i>
    <a href="#twitter" title="Twitter">Twitter</a>: <i>
      - &lt;a href=&#34;twitter.md&#34;&gt;Twitter&lt;/a&gt;</i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>
      - &lt;a href=&#34;schedule.md&#34;&gt;Schedule&lt;/a&gt;</i>
    <a href="#applicationlogs" title="ApplicationLogs">ApplicationLogs</a>: <i>
      - &lt;a href=&#34;applicationlogs.md&#34;&gt;ApplicationLogs&lt;/a&gt;</i>
    <a href="#httplogs" title="HttpLogs">HttpLogs</a>: <i>
      - &lt;a href=&#34;httplogs.md&#34;&gt;HttpLogs&lt;/a&gt;</i>
    <a href="#cors" title="Cors">Cors</a>: <i>
      - &lt;a href=&#34;cors.md&#34;&gt;Cors&lt;/a&gt;</i>
    <a href="#azureblobstorage" title="AzureBlobStorage">AzureBlobStorage</a>: <i>
      - &lt;a href=&#34;azureblobstorage.md&#34;&gt;AzureBlobStorage&lt;/a&gt;</i>
    <a href="#filesystem" title="FileSystem">FileSystem</a>: <i>
      - &lt;a href=&#34;filesystem.md&#34;&gt;FileSystem&lt;/a&gt;</i>
</pre>

## Properties

#### AppServicePlanId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppSettings

_Required_: No

_Type_: List of &lt;a href=&#34;appsettings.md&#34;&gt;AppSettings&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientAffinityEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCertEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsOnly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthSettings

_Required_: No

_Type_: List of &lt;a href=&#34;authsettings.md&#34;&gt;AuthSettings&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backup

_Required_: No

_Type_: List of &lt;a href=&#34;backup.md&#34;&gt;Backup&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionString

_Required_: No

_Type_: List of &lt;a href=&#34;connectionstring.md&#34;&gt;ConnectionString&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of &lt;a href=&#34;identity.md&#34;&gt;Identity&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logs

_Required_: No

_Type_: List of &lt;a href=&#34;logs.md&#34;&gt;Logs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SiteConfig

_Required_: No

_Type_: List of &lt;a href=&#34;siteconfig.md&#34;&gt;SiteConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccount

_Required_: No

_Type_: List of &lt;a href=&#34;storageaccount.md&#34;&gt;StorageAccount&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActiveDirectory

_Required_: No

_Type_: List of &lt;a href=&#34;activedirectory.md&#34;&gt;ActiveDirectory&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Facebook

_Required_: No

_Type_: List of &lt;a href=&#34;facebook.md&#34;&gt;Facebook&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Google

_Required_: No

_Type_: List of &lt;a href=&#34;google.md&#34;&gt;Google&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Microsoft

_Required_: No

_Type_: List of &lt;a href=&#34;microsoft.md&#34;&gt;Microsoft&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Twitter

_Required_: No

_Type_: List of &lt;a href=&#34;twitter.md&#34;&gt;Twitter&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

_Required_: No

_Type_: List of &lt;a href=&#34;schedule.md&#34;&gt;Schedule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationLogs

_Required_: No

_Type_: List of &lt;a href=&#34;applicationlogs.md&#34;&gt;ApplicationLogs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpLogs

_Required_: No

_Type_: List of &lt;a href=&#34;httplogs.md&#34;&gt;HttpLogs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cors

_Required_: No

_Type_: List of &lt;a href=&#34;cors.md&#34;&gt;Cors&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureBlobStorage

_Required_: No

_Type_: List of &lt;a href=&#34;azureblobstorage.md&#34;&gt;AzureBlobStorage&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileSystem

_Required_: No

_Type_: List of &lt;a href=&#34;filesystem.md&#34;&gt;FileSystem&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DefaultSiteHostname

Returns the &lt;code&gt;DefaultSiteHostname&lt;/code&gt; value.

#### OutboundIpAddresses

Returns the &lt;code&gt;OutboundIpAddresses&lt;/code&gt; value.

#### PossibleOutboundIpAddresses

Returns the &lt;code&gt;PossibleOutboundIpAddresses&lt;/code&gt; value.

#### SiteCredential

Returns the &lt;code&gt;SiteCredential&lt;/code&gt; value.

#### SourceControl

Returns the &lt;code&gt;SourceControl&lt;/code&gt; value.

