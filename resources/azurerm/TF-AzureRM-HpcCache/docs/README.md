# TF::AzureRM::HpcCache

Manages a HPC Cache.

~> **Note:** During the first several months of the GA release, a request must be made to the Azure HPC Cache team to add your subscription to the access list before it can be used to create a cache instance. Fill out [this form](https://aka.ms/onboard-hpc-cache) to request access.

~> **Note:** By request of the service team the provider no longer automatically registering the `Microsoft.StorageCache` Resource Provider for this resource. To register it you can run `az provider register --namespace 'Microsoft.StorageCache'`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::HpcCache",
    "Properties" : {
        "<a href="#cachesizeingb" title="CacheSizeInGb">CacheSizeInGb</a>" : <i>Double</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#mtu" title="Mtu">Mtu</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ntpserver" title="NtpServer">NtpServer</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#rootsquashenabled" title="RootSquashEnabled">RootSquashEnabled</a>" : <i>Boolean</i>,
        "<a href="#skuname" title="SkuName">SkuName</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#defaultaccesspolicy" title="DefaultAccessPolicy">DefaultAccessPolicy</a>" : <i>[ <a href="defaultaccesspolicydefinition.md">DefaultAccessPolicyDefinition</a>, ... ]</i>,
        "<a href="#directoryactivedirectory" title="DirectoryActiveDirectory">DirectoryActiveDirectory</a>" : <i>[ <a href="directoryactivedirectorydefinition.md">DirectoryActiveDirectoryDefinition</a>, ... ]</i>,
        "<a href="#directoryflatfile" title="DirectoryFlatFile">DirectoryFlatFile</a>" : <i>[ <a href="directoryflatfiledefinition.md">DirectoryFlatFileDefinition</a>, ... ]</i>,
        "<a href="#directoryldap" title="DirectoryLdap">DirectoryLdap</a>" : <i>[ <a href="directoryldapdefinition.md">DirectoryLdapDefinition</a>, ... ]</i>,
        "<a href="#dns" title="Dns">Dns</a>" : <i>[ <a href="dnsdefinition.md">DnsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::HpcCache
Properties:
    <a href="#cachesizeingb" title="CacheSizeInGb">CacheSizeInGb</a>: <i>Double</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#mtu" title="Mtu">Mtu</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ntpserver" title="NtpServer">NtpServer</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#rootsquashenabled" title="RootSquashEnabled">RootSquashEnabled</a>: <i>Boolean</i>
    <a href="#skuname" title="SkuName">SkuName</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#defaultaccesspolicy" title="DefaultAccessPolicy">DefaultAccessPolicy</a>: <i>
      - <a href="defaultaccesspolicydefinition.md">DefaultAccessPolicyDefinition</a></i>
    <a href="#directoryactivedirectory" title="DirectoryActiveDirectory">DirectoryActiveDirectory</a>: <i>
      - <a href="directoryactivedirectorydefinition.md">DirectoryActiveDirectoryDefinition</a></i>
    <a href="#directoryflatfile" title="DirectoryFlatFile">DirectoryFlatFile</a>: <i>
      - <a href="directoryflatfiledefinition.md">DirectoryFlatFileDefinition</a></i>
    <a href="#directoryldap" title="DirectoryLdap">DirectoryLdap</a>: <i>
      - <a href="directoryldapdefinition.md">DirectoryLdapDefinition</a></i>
    <a href="#dns" title="Dns">Dns</a>: <i>
      - <a href="dnsdefinition.md">DnsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CacheSizeInGb

The size of the HPC Cache, in GB. Possible values are `3072`, `6144`, `12288`, `24576`, and `49152`. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Specifies the supported Azure Region where the HPC Cache should be created. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mtu

The IPv4 maximum transmission unit configured for the subnet of the HPC Cache. Possible values range from 576 - 1500. Defaults to 1500.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the HPC Cache. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpServer

The NTP server IP Address or FQDN for the HPC Cache. Defaults to `time.windows.com`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the Resource Group in which to create the HPC Cache. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootSquashEnabled

Whether to enable [root squash](https://docs.microsoft.com/en-us/azure/hpc-cache/access-policies#root-squash)? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkuName

The SKU of HPC Cache to use. Possible values are `Standard_2G`, `Standard_4G` and `Standard_8G`. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

The ID of the Subnet for the HPC Cache. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the HPC Cache.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultAccessPolicy

_Required_: No

_Type_: List of <a href="defaultaccesspolicydefinition.md">DefaultAccessPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DirectoryActiveDirectory

_Required_: No

_Type_: List of <a href="directoryactivedirectorydefinition.md">DirectoryActiveDirectoryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DirectoryFlatFile

_Required_: No

_Type_: List of <a href="directoryflatfiledefinition.md">DirectoryFlatFileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DirectoryLdap

_Required_: No

_Type_: List of <a href="directoryldapdefinition.md">DirectoryLdapDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dns

_Required_: No

_Type_: List of <a href="dnsdefinition.md">DnsDefinition</a>

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

#### Id

Returns the <code>Id</code> value.

#### MountAddresses

Returns the <code>MountAddresses</code> value.

