# Terraform::AzureRM::AppServiceSlot

Manages an App Service Slot (within an App Service).

-> **Note:** When using Slots - the `app_settings`, `connection_string` and `site_config` blocks on the `azurerm_app_service` resource will be overwritten when promoting a Slot using the `azurerm_app_service_active_slot` resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::AppServiceSlot",
    "Properties" : {
        "<a href="#appservicename" title="AppServiceName">AppServiceName</a>" : <i>String</i>,
        "<a href="#appserviceplanid" title="AppServicePlanId">AppServicePlanId</a>" : <i>String</i>,
        "<a href="#appsettings" title="AppSettings">AppSettings</a>" : <i>[ <a href="appsettings.md">AppSettings</a>, ... ]</i>,
        "<a href="#clientaffinityenabled" title="ClientAffinityEnabled">ClientAffinityEnabled</a>" : <i>Boolean</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#httpsonly" title="HttpsOnly">HttpsOnly</a>" : <i>Boolean</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#authsettings" title="AuthSettings">AuthSettings</a>" : <i>[ <a href="authsettings.md">AuthSettings</a>, ... ]</i>,
        "<a href="#connectionstring" title="ConnectionString">ConnectionString</a>" : <i>[ <a href="connectionstring.md">ConnectionString</a>, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ <a href="identity.md">Identity</a>, ... ]</i>,
        "<a href="#logs" title="Logs">Logs</a>" : <i>[ <a href="logs.md">Logs</a>, ... ]</i>,
        "<a href="#siteconfig" title="SiteConfig">SiteConfig</a>" : <i>[ <a href="siteconfig.md">SiteConfig</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#activedirectory" title="ActiveDirectory">ActiveDirectory</a>" : <i>[ <a href="activedirectory.md">ActiveDirectory</a>, ... ]</i>,
        "<a href="#facebook" title="Facebook">Facebook</a>" : <i>[ <a href="facebook.md">Facebook</a>, ... ]</i>,
        "<a href="#google" title="Google">Google</a>" : <i>[ <a href="google.md">Google</a>, ... ]</i>,
        "<a href="#microsoft" title="Microsoft">Microsoft</a>" : <i>[ <a href="microsoft.md">Microsoft</a>, ... ]</i>,
        "<a href="#twitter" title="Twitter">Twitter</a>" : <i>[ <a href="twitter.md">Twitter</a>, ... ]</i>,
        "<a href="#applicationlogs" title="ApplicationLogs">ApplicationLogs</a>" : <i>[ <a href="applicationlogs.md">ApplicationLogs</a>, ... ]</i>,
        "<a href="#httplogs" title="HttpLogs">HttpLogs</a>" : <i>[ <a href="httplogs.md">HttpLogs</a>, ... ]</i>,
        "<a href="#cors" title="Cors">Cors</a>" : <i>[ <a href="cors.md">Cors</a>, ... ]</i>,
        "<a href="#azureblobstorage" title="AzureBlobStorage">AzureBlobStorage</a>" : <i>[ <a href="azureblobstorage.md">AzureBlobStorage</a>, ... ]</i>,
        "<a href="#filesystem" title="FileSystem">FileSystem</a>" : <i>[ <a href="filesystem.md">FileSystem</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::AppServiceSlot
Properties:
    <a href="#appservicename" title="AppServiceName">AppServiceName</a>: <i>String</i>
    <a href="#appserviceplanid" title="AppServicePlanId">AppServicePlanId</a>: <i>String</i>
    <a href="#appsettings" title="AppSettings">AppSettings</a>: <i>
      - <a href="appsettings.md">AppSettings</a></i>
    <a href="#clientaffinityenabled" title="ClientAffinityEnabled">ClientAffinityEnabled</a>: <i>Boolean</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#httpsonly" title="HttpsOnly">HttpsOnly</a>: <i>Boolean</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#authsettings" title="AuthSettings">AuthSettings</a>: <i>
      - <a href="authsettings.md">AuthSettings</a></i>
    <a href="#connectionstring" title="ConnectionString">ConnectionString</a>: <i>
      - <a href="connectionstring.md">ConnectionString</a></i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - <a href="identity.md">Identity</a></i>
    <a href="#logs" title="Logs">Logs</a>: <i>
      - <a href="logs.md">Logs</a></i>
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
    <a href="#applicationlogs" title="ApplicationLogs">ApplicationLogs</a>: <i>
      - <a href="applicationlogs.md">ApplicationLogs</a></i>
    <a href="#httplogs" title="HttpLogs">HttpLogs</a>: <i>
      - <a href="httplogs.md">HttpLogs</a></i>
    <a href="#cors" title="Cors">Cors</a>: <i>
      - <a href="cors.md">Cors</a></i>
    <a href="#azureblobstorage" title="AzureBlobStorage">AzureBlobStorage</a>: <i>
      - <a href="azureblobstorage.md">AzureBlobStorage</a></i>
    <a href="#filesystem" title="FileSystem">FileSystem</a>: <i>
      - <a href="filesystem.md">FileSystem</a></i>
</pre>

## Properties

#### AppServiceName

The name of the App Service within which to create the App Service Slot.  Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppServicePlanId

The ID of the App Service Plan within which to create this App Service Slot. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppSettings

A key-value pair of App Settings.

_Required_: No

_Type_: List of <a href="appsettings.md">AppSettings</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientAffinityEnabled

Should the App Service Slot send session affinity cookies, which route client requests in the same session to the same instance?.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Is the App Service Slot Enabled?.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsOnly

Can the App Service Slot only be accessed via HTTPS? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the App Service Slot component. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to create the App Service Slot component.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

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

#### Logs

_Required_: No

_Type_: List of <a href="logs.md">Logs</a>

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

#### ApplicationLogs

_Required_: No

_Type_: List of <a href="applicationlogs.md">ApplicationLogs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpLogs

_Required_: No

_Type_: List of <a href="httplogs.md">HttpLogs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cors

_Required_: No

_Type_: List of <a href="cors.md">Cors</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureBlobStorage

_Required_: No

_Type_: List of <a href="azureblobstorage.md">AzureBlobStorage</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileSystem

_Required_: No

_Type_: List of <a href="filesystem.md">FileSystem</a>

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

Returns the <code>DefaultSiteHostname</code> value.

#### SiteCredential

Returns the <code>SiteCredential</code> value.

