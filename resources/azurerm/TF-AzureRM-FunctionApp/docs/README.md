# TF::AzureRM::FunctionApp

Manages a Function App.

~> **Note:** To connect an Azure Function App and a subnet within the same region `azurerm_app_service_virtual_network_swift_connection` can be used.
For an example, check the `azurerm_app_service_virtual_network_swift_connection` documentation.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::FunctionApp",
    "Properties" : {
        "<a href="#appserviceplanid" title="AppServicePlanId">AppServicePlanId</a>" : <i>String</i>,
        "<a href="#appsettings" title="AppSettings">AppSettings</a>" : <i>[ <a href="appsettingsdefinition.md">AppSettingsDefinition</a>, ... ]</i>,
        "<a href="#clientaffinityenabled" title="ClientAffinityEnabled">ClientAffinityEnabled</a>" : <i>Boolean</i>,
        "<a href="#clientcertmode" title="ClientCertMode">ClientCertMode</a>" : <i>String</i>,
        "<a href="#dailymemorytimequota" title="DailyMemoryTimeQuota">DailyMemoryTimeQuota</a>" : <i>Double</i>,
        "<a href="#enablebuiltinlogging" title="EnableBuiltinLogging">EnableBuiltinLogging</a>" : <i>Boolean</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#httpsonly" title="HttpsOnly">HttpsOnly</a>" : <i>Boolean</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ostype" title="OsType">OsType</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#storageaccountaccesskey" title="StorageAccountAccessKey">StorageAccountAccessKey</a>" : <i>String</i>,
        "<a href="#storageaccountname" title="StorageAccountName">StorageAccountName</a>" : <i>String</i>,
        "<a href="#storageconnectionstring" title="StorageConnectionString">StorageConnectionString</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#authsettings" title="AuthSettings">AuthSettings</a>" : <i>[ <a href="authsettingsdefinition.md">AuthSettingsDefinition</a>, ... ]</i>,
        "<a href="#connectionstring" title="ConnectionString">ConnectionString</a>" : <i>[ <a href="connectionstringdefinition.md">ConnectionStringDefinition</a>, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ <a href="identitydefinition.md">IdentityDefinition</a>, ... ]</i>,
        "<a href="#siteconfig" title="SiteConfig">SiteConfig</a>" : <i>[ <a href="siteconfigdefinition.md">SiteConfigDefinition</a>, ... ]</i>,
        "<a href="#sourcecontrol" title="SourceControl">SourceControl</a>" : <i>[ <a href="sourcecontroldefinition.md">SourceControlDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::FunctionApp
Properties:
    <a href="#appserviceplanid" title="AppServicePlanId">AppServicePlanId</a>: <i>String</i>
    <a href="#appsettings" title="AppSettings">AppSettings</a>: <i>
      - <a href="appsettingsdefinition.md">AppSettingsDefinition</a></i>
    <a href="#clientaffinityenabled" title="ClientAffinityEnabled">ClientAffinityEnabled</a>: <i>Boolean</i>
    <a href="#clientcertmode" title="ClientCertMode">ClientCertMode</a>: <i>String</i>
    <a href="#dailymemorytimequota" title="DailyMemoryTimeQuota">DailyMemoryTimeQuota</a>: <i>Double</i>
    <a href="#enablebuiltinlogging" title="EnableBuiltinLogging">EnableBuiltinLogging</a>: <i>Boolean</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#httpsonly" title="HttpsOnly">HttpsOnly</a>: <i>Boolean</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ostype" title="OsType">OsType</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#storageaccountaccesskey" title="StorageAccountAccessKey">StorageAccountAccessKey</a>: <i>String</i>
    <a href="#storageaccountname" title="StorageAccountName">StorageAccountName</a>: <i>String</i>
    <a href="#storageconnectionstring" title="StorageConnectionString">StorageConnectionString</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#authsettings" title="AuthSettings">AuthSettings</a>: <i>
      - <a href="authsettingsdefinition.md">AuthSettingsDefinition</a></i>
    <a href="#connectionstring" title="ConnectionString">ConnectionString</a>: <i>
      - <a href="connectionstringdefinition.md">ConnectionStringDefinition</a></i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - <a href="identitydefinition.md">IdentityDefinition</a></i>
    <a href="#siteconfig" title="SiteConfig">SiteConfig</a>: <i>
      - <a href="siteconfigdefinition.md">SiteConfigDefinition</a></i>
    <a href="#sourcecontrol" title="SourceControl">SourceControl</a>: <i>
      - <a href="sourcecontroldefinition.md">SourceControlDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AppServicePlanId

The ID of the App Service Plan within which to create this Function App.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppSettings

A map of key-value pairs for [App Settings](https://docs.microsoft.com/en-us/azure/azure-functions/functions-app-settings) and custom values.

_Required_: No

_Type_: List of <a href="appsettingsdefinition.md">AppSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientAffinityEnabled

Should the Function App send session affinity cookies, which route client requests in the same session to the same instance?.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCertMode

The mode of the Function App's client certificates requirement for incoming requests. Possible values are `Required` and `Optional`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DailyMemoryTimeQuota

The amount of memory in gigabyte-seconds that your application is allowed to consume per day. Setting this value only affects function apps under the consumption plan. Defaults to `0`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableBuiltinLogging

Should the built-in logging of this Function App be enabled? Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Is the Function App enabled?.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsOnly

Can the Function App only be accessed via HTTPS? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the Function App. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsType

A string indicating the Operating System type for this function app.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to create the Function App.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountAccessKey

The access key which will be used to access the backend storage account for the Function App.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountName

The backend storage account name which will be used by this Function App (such as the dashboard, logs).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageConnectionString

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

The runtime version associated with the Function App. Defaults to `~1`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthSettings

_Required_: No

_Type_: List of <a href="authsettingsdefinition.md">AuthSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionString

_Required_: No

_Type_: List of <a href="connectionstringdefinition.md">ConnectionStringDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of <a href="identitydefinition.md">IdentityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SiteConfig

_Required_: No

_Type_: List of <a href="siteconfigdefinition.md">SiteConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceControl

_Required_: No

_Type_: List of <a href="sourcecontroldefinition.md">SourceControlDefinition</a>

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

#### DefaultHostname

Returns the <code>DefaultHostname</code> value.

#### Id

Returns the <code>Id</code> value.

#### Kind

Returns the <code>Kind</code> value.

#### OutboundIpAddresses

Returns the <code>OutboundIpAddresses</code> value.

#### PossibleOutboundIpAddresses

Returns the <code>PossibleOutboundIpAddresses</code> value.

#### SiteCredential

Returns the <code>SiteCredential</code> value.

