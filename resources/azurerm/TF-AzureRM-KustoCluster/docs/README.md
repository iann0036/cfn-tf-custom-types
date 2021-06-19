# TF::AzureRM::KustoCluster

Manages a Kusto (also known as Azure Data Explorer) Cluster

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::KustoCluster",
    "Properties" : {
        "<a href="#doubleencryptionenabled" title="DoubleEncryptionEnabled">DoubleEncryptionEnabled</a>" : <i>Boolean</i>,
        "<a href="#enablediskencryption" title="EnableDiskEncryption">EnableDiskEncryption</a>" : <i>Boolean</i>,
        "<a href="#enablepurge" title="EnablePurge">EnablePurge</a>" : <i>Boolean</i>,
        "<a href="#enablestreamingingest" title="EnableStreamingIngest">EnableStreamingIngest</a>" : <i>Boolean</i>,
        "<a href="#engine" title="Engine">Engine</a>" : <i>String</i>,
        "<a href="#languageextensions" title="LanguageExtensions">LanguageExtensions</a>" : <i>[ String, ... ]</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#trustedexternaltenants" title="TrustedExternalTenants">TrustedExternalTenants</a>" : <i>[ String, ... ]</i>,
        "<a href="#zones" title="Zones">Zones</a>" : <i>[ String, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ <a href="identitydefinition.md">IdentityDefinition</a>, ... ]</i>,
        "<a href="#optimizedautoscale" title="OptimizedAutoScale">OptimizedAutoScale</a>" : <i>[ <a href="optimizedautoscaledefinition.md">OptimizedAutoScaleDefinition</a>, ... ]</i>,
        "<a href="#sku" title="Sku">Sku</a>" : <i>[ <a href="skudefinition.md">SkuDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#virtualnetworkconfiguration" title="VirtualNetworkConfiguration">VirtualNetworkConfiguration</a>" : <i>[ <a href="virtualnetworkconfigurationdefinition.md">VirtualNetworkConfigurationDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::KustoCluster
Properties:
    <a href="#doubleencryptionenabled" title="DoubleEncryptionEnabled">DoubleEncryptionEnabled</a>: <i>Boolean</i>
    <a href="#enablediskencryption" title="EnableDiskEncryption">EnableDiskEncryption</a>: <i>Boolean</i>
    <a href="#enablepurge" title="EnablePurge">EnablePurge</a>: <i>Boolean</i>
    <a href="#enablestreamingingest" title="EnableStreamingIngest">EnableStreamingIngest</a>: <i>Boolean</i>
    <a href="#engine" title="Engine">Engine</a>: <i>String</i>
    <a href="#languageextensions" title="LanguageExtensions">LanguageExtensions</a>: <i>
      - String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#trustedexternaltenants" title="TrustedExternalTenants">TrustedExternalTenants</a>: <i>
      - String</i>
    <a href="#zones" title="Zones">Zones</a>: <i>
      - String</i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - <a href="identitydefinition.md">IdentityDefinition</a></i>
    <a href="#optimizedautoscale" title="OptimizedAutoScale">OptimizedAutoScale</a>: <i>
      - <a href="optimizedautoscaledefinition.md">OptimizedAutoScaleDefinition</a></i>
    <a href="#sku" title="Sku">Sku</a>: <i>
      - <a href="skudefinition.md">SkuDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#virtualnetworkconfiguration" title="VirtualNetworkConfiguration">VirtualNetworkConfiguration</a>: <i>
      - <a href="virtualnetworkconfigurationdefinition.md">VirtualNetworkConfigurationDefinition</a></i>
</pre>

## Properties

#### DoubleEncryptionEnabled

Is the cluster's double encryption enabled? Defaults to `false`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableDiskEncryption

Specifies if the cluster's disks are encrypted.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePurge

Specifies if the purge operations are enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableStreamingIngest

Specifies if the streaming ingest is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Engine

. The engine type that should be used. Possible values are `V2` and `V3`. Defaults to `V2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LanguageExtensions

An list of `language_extensions` to enable. Valid values are: `PYTHON` and `R`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

The location where the Kusto Cluster should be created. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Kusto Cluster to create. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

Specifies the Resource Group where the Kusto Cluster should exist. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrustedExternalTenants

Specifies a list of tenant IDs that are trusted by the cluster.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zones

A list of Availability Zones in which the cluster instances should be created in. Changing this forces a new resource to be created.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of <a href="identitydefinition.md">IdentityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OptimizedAutoScale

_Required_: No

_Type_: List of <a href="optimizedautoscaledefinition.md">OptimizedAutoScaleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sku

_Required_: No

_Type_: List of <a href="skudefinition.md">SkuDefinition</a>

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

#### DataIngestionUri

Returns the <code>DataIngestionUri</code> value.

#### Id

Returns the <code>Id</code> value.

#### Uri

Returns the <code>Uri</code> value.

