# TF::AzureRM::AppService

Manages an App Service (within an App Service Plan).

-> **Note:** When using Slots - the `app_settings`, `connection_string` and `site_config` blocks on the `azurerm_app_service` resource will be overwritten when promoting a Slot using the `azurerm_app_service_active_slot` resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::AppService",
    "Properties" : {
        "<a href="#appserviceplanid" title="AppServicePlanId">AppServicePlanId</a>" : <i>String</i>,
        "<a href="#appsettings" title="AppSettings">AppSettings</a>" : <i>[ <a href="appsettingsdefinition.md">AppSettingsDefinition</a>, ... ]</i>,
        "<a href="#clientaffinityenabled" title="ClientAffinityEnabled">ClientAffinityEnabled</a>" : <i>Boolean</i>,
        "<a href="#clientcertenabled" title="ClientCertEnabled">ClientCertEnabled</a>" : <i>Boolean</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#httpsonly" title="HttpsOnly">HttpsOnly</a>" : <i>Boolean</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#authsettings" title="AuthSettings">AuthSettings</a>" : <i>[ <a href="authsettingsdefinition.md">AuthSettingsDefinition</a>, ... ]</i>,
        "<a href="#backup" title="Backup">Backup</a>" : <i>[ <a href="backupdefinition.md">BackupDefinition</a>, ... ]</i>,
        "<a href="#connectionstring" title="ConnectionString">ConnectionString</a>" : <i>[ <a href="connectionstringdefinition.md">ConnectionStringDefinition</a>, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ <a href="identitydefinition.md">IdentityDefinition</a>, ... ]</i>,
        "<a href="#logs" title="Logs">Logs</a>" : <i>[ <a href="logsdefinition.md">LogsDefinition</a>, ... ]</i>,
        "<a href="#siteconfig" title="SiteConfig">SiteConfig</a>" : <i>[ <a href="siteconfigdefinition.md">SiteConfigDefinition</a>, ... ]</i>,
        "<a href="#sourcecontrol" title="SourceControl">SourceControl</a>" : <i>[ <a href="sourcecontroldefinition.md">SourceControlDefinition</a>, ... ]</i>,
        "<a href="#storageaccount" title="StorageAccount">StorageAccount</a>" : <i>[ <a href="storageaccountdefinition.md">StorageAccountDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::AppService
Properties:
    <a href="#appserviceplanid" title="AppServicePlanId">AppServicePlanId</a>: <i>String</i>
    <a href="#appsettings" title="AppSettings">AppSettings</a>: <i>
      - <a href="appsettingsdefinition.md">AppSettingsDefinition</a></i>
    <a href="#clientaffinityenabled" title="ClientAffinityEnabled">ClientAffinityEnabled</a>: <i>Boolean</i>
    <a href="#clientcertenabled" title="ClientCertEnabled">ClientCertEnabled</a>: <i>Boolean</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#httpsonly" title="HttpsOnly">HttpsOnly</a>: <i>Boolean</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#authsettings" title="AuthSettings">AuthSettings</a>: <i>
      - <a href="authsettingsdefinition.md">AuthSettingsDefinition</a></i>
    <a href="#backup" title="Backup">Backup</a>: <i>
      - <a href="backupdefinition.md">BackupDefinition</a></i>
    <a href="#connectionstring" title="ConnectionString">ConnectionString</a>: <i>
      - <a href="connectionstringdefinition.md">ConnectionStringDefinition</a></i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - <a href="identitydefinition.md">IdentityDefinition</a></i>
    <a href="#logs" title="Logs">Logs</a>: <i>
      - <a href="logsdefinition.md">LogsDefinition</a></i>
    <a href="#siteconfig" title="SiteConfig">SiteConfig</a>: <i>
      - <a href="siteconfigdefinition.md">SiteConfigDefinition</a></i>
    <a href="#sourcecontrol" title="SourceControl">SourceControl</a>: <i>
      - <a href="sourcecontroldefinition.md">SourceControlDefinition</a></i>
    <a href="#storageaccount" title="StorageAccount">StorageAccount</a>: <i>
      - <a href="storageaccountdefinition.md">StorageAccountDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AppServicePlanId

The ID of the App Service Plan within which to create this App Service.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppSettings

A key-value pair of App Settings.

_Required_: No

_Type_: List of <a href="appsettingsdefinition.md">AppSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientAffinityEnabled

Should the App Service send session affinity cookies, which route client requests in the same session to the same instance?.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCertEnabled

Does the App Service require client certificates for incoming requests? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Is the App Service Enabled?.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsOnly

Can the App Service only be accessed via HTTPS? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the App Service. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to create the App Service.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthSettings

_Required_: No

_Type_: List of <a href="authsettingsdefinition.md">AuthSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backup

_Required_: No

_Type_: List of <a href="backupdefinition.md">BackupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionString

_Required_: No

_Type_: List of <a href="connectionstringdefinition.md">ConnectionStringDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of <a href="identitydefinition.md">IdentityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logs

_Required_: No

_Type_: List of <a href="logsdefinition.md">LogsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SiteConfig

_Required_: No

_Type_: List of <a href="siteconfigdefinition.md">SiteConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceControl

_Required_: No

_Type_: List of <a href="sourcecontroldefinition.md">SourceControlDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccount

_Required_: No

_Type_: List of <a href="storageaccountdefinition.md">StorageAccountDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CustomDomainVerificationId

Returns the <code>CustomDomainVerificationId</code> value.

#### DefaultSiteHostname

Returns the <code>DefaultSiteHostname</code> value.

#### Id

Returns the <code>Id</code> value.

#### OutboundIpAddressList

Returns the <code>OutboundIpAddressList</code> value.

#### OutboundIpAddresses

Returns the <code>OutboundIpAddresses</code> value.

#### PossibleOutboundIpAddressList

Returns the <code>PossibleOutboundIpAddressList</code> value.

#### PossibleOutboundIpAddresses

Returns the <code>PossibleOutboundIpAddresses</code> value.

#### SiteCredential

Returns the <code>SiteCredential</code> value.

