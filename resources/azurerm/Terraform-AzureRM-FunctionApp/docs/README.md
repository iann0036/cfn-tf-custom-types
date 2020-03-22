# Terraform::AzureRM::FunctionApp

Manages a Function App.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::FunctionApp",
    "Properties" : {
        "<a href="#appserviceplanid" title="AppServicePlanId">AppServicePlanId</a>" : <i>String</i>,
        "<a href="#appsettings" title="AppSettings">AppSettings</a>" : <i>[ <a href="appsettings.md">AppSettings</a>, ... ]</i>,
        "<a href="#clientaffinityenabled" title="ClientAffinityEnabled">ClientAffinityEnabled</a>" : <i>Boolean</i>,
        "<a href="#dailymemorytimequota" title="DailyMemoryTimeQuota">DailyMemoryTimeQuota</a>" : <i>Double</i>,
        "<a href="#enablebuiltinlogging" title="EnableBuiltinLogging">EnableBuiltinLogging</a>" : <i>Boolean</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#httpsonly" title="HttpsOnly">HttpsOnly</a>" : <i>Boolean</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ostype" title="OsType">OsType</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#storageconnectionstring" title="StorageConnectionString">StorageConnectionString</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#authsettings" title="AuthSettings">AuthSettings</a>" : <i>[ <a href="authsettings.md">AuthSettings</a>, ... ]</i>,
        "<a href="#connectionstring" title="ConnectionString">ConnectionString</a>" : <i>[ <a href="connectionstring.md">ConnectionString</a>, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ <a href="identity.md">Identity</a>, ... ]</i>,
        "<a href="#siteconfig" title="SiteConfig">SiteConfig</a>" : <i>[ <a href="siteconfig.md">SiteConfig</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#activedirectory" title="ActiveDirectory">ActiveDirectory</a>" : <i>[ <a href="activedirectory.md">ActiveDirectory</a>, ... ]</i>,
        "<a href="#facebook" title="Facebook">Facebook</a>" : <i>[ <a href="facebook.md">Facebook</a>, ... ]</i>,
        "<a href="#google" title="Google">Google</a>" : <i>[ <a href="google.md">Google</a>, ... ]</i>,
        "<a href="#microsoft" title="Microsoft">Microsoft</a>" : <i>[ <a href="microsoft.md">Microsoft</a>, ... ]</i>,
        "<a href="#twitter" title="Twitter">Twitter</a>" : <i>[ <a href="twitter.md">Twitter</a>, ... ]</i>,
        "<a href="#cors" title="Cors">Cors</a>" : <i>[ <a href="cors.md">Cors</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::FunctionApp
Properties:
    <a href="#appserviceplanid" title="AppServicePlanId">AppServicePlanId</a>: <i>String</i>
    <a href="#appsettings" title="AppSettings">AppSettings</a>: <i>
      - <a href="appsettings.md">AppSettings</a></i>
    <a href="#clientaffinityenabled" title="ClientAffinityEnabled">ClientAffinityEnabled</a>: <i>Boolean</i>
    <a href="#dailymemorytimequota" title="DailyMemoryTimeQuota">DailyMemoryTimeQuota</a>: <i>Double</i>
    <a href="#enablebuiltinlogging" title="EnableBuiltinLogging">EnableBuiltinLogging</a>: <i>Boolean</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#httpsonly" title="HttpsOnly">HttpsOnly</a>: <i>Boolean</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ostype" title="OsType">OsType</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#storageconnectionstring" title="StorageConnectionString">StorageConnectionString</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#authsettings" title="AuthSettings">AuthSettings</a>: <i>
      - <a href="authsettings.md">AuthSettings</a></i>
    <a href="#connectionstring" title="ConnectionString">ConnectionString</a>: <i>
      - <a href="connectionstring.md">ConnectionString</a></i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - <a href="identity.md">Identity</a></i>
    <a href="#siteconfig" title="SiteConfig">SiteConfig</a>: <i>
      - <a href="siteconfig.md">SiteConfig</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#activedirectory" title="ActiveDirectory">ActiveDirectory</a>: <i>
      - <a href="activedirectory.md">ActiveDirectory</a></i>
    <a href="#facebook" title="Facebook">Facebook</a>: <i>
      - <a href="facebook.md">Facebook</a></i>
    <a href="#google" title="Google">Google</a>: <i>
      - <a href="google.md">Google</a></i>
    <a href="#microsoft" title="Microsoft">Microsoft</a>: <i>
      - <a href="microsoft.md">Microsoft</a></i>
    <a href="#twitter" title="Twitter">Twitter</a>: <i>
      - <a href="twitter.md">Twitter</a></i>
    <a href="#cors" title="Cors">Cors</a>: <i>
      - <a href="cors.md">Cors</a></i>
</pre>

## Properties

#### AppServicePlanId

The ID of the App Service Plan within which to create this Function App.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppSettings

A key-value pair of App Settings.

_Required_: No

_Type_: List of <a href="appsettings.md">AppSettings</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientAffinityEnabled

Should the Function App send session affinity cookies, which route client requests in the same session to the same instance?.

_Required_: No

_Type_: Boolean

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

#### StorageConnectionString

The connection string of the backend storage account which will be used by this Function App (such as the dashboard, logs).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

The runtime version associated with the Function App. Defaults to `~1`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthSettings

_Required_: No

_Type_: List of <a href="authsettings.md">AuthSettings</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionString

_Required_: No

_Type_: List of <a href="connectionstring.md">ConnectionString</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of <a href="identity.md">Identity</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SiteConfig

_Required_: No

_Type_: List of <a href="siteconfig.md">SiteConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActiveDirectory

_Required_: No

_Type_: List of <a href="activedirectory.md">ActiveDirectory</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Facebook

_Required_: No

_Type_: List of <a href="facebook.md">Facebook</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Google

_Required_: No

_Type_: List of <a href="google.md">Google</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Microsoft

_Required_: No

_Type_: List of <a href="microsoft.md">Microsoft</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Twitter

_Required_: No

_Type_: List of <a href="twitter.md">Twitter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cors

_Required_: No

_Type_: List of <a href="cors.md">Cors</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

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

