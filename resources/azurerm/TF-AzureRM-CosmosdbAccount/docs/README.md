# TF::AzureRM::CosmosdbAccount

Manages a CosmosDB (formally DocumentDB) Account.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::CosmosdbAccount",
    "Properties" : {
        "<a href="#accesskeymetadatawritesenabled" title="AccessKeyMetadataWritesEnabled">AccessKeyMetadataWritesEnabled</a>" : <i>Boolean</i>,
        "<a href="#analyticalstorageenabled" title="AnalyticalStorageEnabled">AnalyticalStorageEnabled</a>" : <i>Boolean</i>,
        "<a href="#enableautomaticfailover" title="EnableAutomaticFailover">EnableAutomaticFailover</a>" : <i>Boolean</i>,
        "<a href="#enablefreetier" title="EnableFreeTier">EnableFreeTier</a>" : <i>Boolean</i>,
        "<a href="#enablemultiplewritelocations" title="EnableMultipleWriteLocations">EnableMultipleWriteLocations</a>" : <i>Boolean</i>,
        "<a href="#iprangefilter" title="IpRangeFilter">IpRangeFilter</a>" : <i>String</i>,
        "<a href="#isvirtualnetworkfilterenabled" title="IsVirtualNetworkFilterEnabled">IsVirtualNetworkFilterEnabled</a>" : <i>Boolean</i>,
        "<a href="#keyvaultkeyid" title="KeyVaultKeyId">KeyVaultKeyId</a>" : <i>String</i>,
        "<a href="#kind" title="Kind">Kind</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#mongoserverversion" title="MongoServerVersion">MongoServerVersion</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkaclbypassforazureservices" title="NetworkAclBypassForAzureServices">NetworkAclBypassForAzureServices</a>" : <i>Boolean</i>,
        "<a href="#networkaclbypassids" title="NetworkAclBypassIds">NetworkAclBypassIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#offertype" title="OfferType">OfferType</a>" : <i>String</i>,
        "<a href="#publicnetworkaccessenabled" title="PublicNetworkAccessEnabled">PublicNetworkAccessEnabled</a>" : <i>Boolean</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#backup" title="Backup">Backup</a>" : <i>[ <a href="backupdefinition.md">BackupDefinition</a>, ... ]</i>,
        "<a href="#capabilities" title="Capabilities">Capabilities</a>" : <i>[ <a href="capabilitiesdefinition.md">CapabilitiesDefinition</a>, ... ]</i>,
        "<a href="#consistencypolicy" title="ConsistencyPolicy">ConsistencyPolicy</a>" : <i>[ <a href="consistencypolicydefinition.md">ConsistencyPolicyDefinition</a>, ... ]</i>,
        "<a href="#corsrule" title="CorsRule">CorsRule</a>" : <i>[ <a href="corsruledefinition.md">CorsRuleDefinition</a>, ... ]</i>,
        "<a href="#geolocation" title="GeoLocation">GeoLocation</a>" : <i>[ <a href="geolocationdefinition.md">GeoLocationDefinition</a>, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ <a href="identitydefinition.md">IdentityDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#virtualnetworkrule" title="VirtualNetworkRule">VirtualNetworkRule</a>" : <i>[ <a href="virtualnetworkruledefinition.md">VirtualNetworkRuleDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::CosmosdbAccount
Properties:
    <a href="#accesskeymetadatawritesenabled" title="AccessKeyMetadataWritesEnabled">AccessKeyMetadataWritesEnabled</a>: <i>Boolean</i>
    <a href="#analyticalstorageenabled" title="AnalyticalStorageEnabled">AnalyticalStorageEnabled</a>: <i>Boolean</i>
    <a href="#enableautomaticfailover" title="EnableAutomaticFailover">EnableAutomaticFailover</a>: <i>Boolean</i>
    <a href="#enablefreetier" title="EnableFreeTier">EnableFreeTier</a>: <i>Boolean</i>
    <a href="#enablemultiplewritelocations" title="EnableMultipleWriteLocations">EnableMultipleWriteLocations</a>: <i>Boolean</i>
    <a href="#iprangefilter" title="IpRangeFilter">IpRangeFilter</a>: <i>String</i>
    <a href="#isvirtualnetworkfilterenabled" title="IsVirtualNetworkFilterEnabled">IsVirtualNetworkFilterEnabled</a>: <i>Boolean</i>
    <a href="#keyvaultkeyid" title="KeyVaultKeyId">KeyVaultKeyId</a>: <i>String</i>
    <a href="#kind" title="Kind">Kind</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#mongoserverversion" title="MongoServerVersion">MongoServerVersion</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkaclbypassforazureservices" title="NetworkAclBypassForAzureServices">NetworkAclBypassForAzureServices</a>: <i>Boolean</i>
    <a href="#networkaclbypassids" title="NetworkAclBypassIds">NetworkAclBypassIds</a>: <i>
      - String</i>
    <a href="#offertype" title="OfferType">OfferType</a>: <i>String</i>
    <a href="#publicnetworkaccessenabled" title="PublicNetworkAccessEnabled">PublicNetworkAccessEnabled</a>: <i>Boolean</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#backup" title="Backup">Backup</a>: <i>
      - <a href="backupdefinition.md">BackupDefinition</a></i>
    <a href="#capabilities" title="Capabilities">Capabilities</a>: <i>
      - <a href="capabilitiesdefinition.md">CapabilitiesDefinition</a></i>
    <a href="#consistencypolicy" title="ConsistencyPolicy">ConsistencyPolicy</a>: <i>
      - <a href="consistencypolicydefinition.md">ConsistencyPolicyDefinition</a></i>
    <a href="#corsrule" title="CorsRule">CorsRule</a>: <i>
      - <a href="corsruledefinition.md">CorsRuleDefinition</a></i>
    <a href="#geolocation" title="GeoLocation">GeoLocation</a>: <i>
      - <a href="geolocationdefinition.md">GeoLocationDefinition</a></i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - <a href="identitydefinition.md">IdentityDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#virtualnetworkrule" title="VirtualNetworkRule">VirtualNetworkRule</a>: <i>
      - <a href="virtualnetworkruledefinition.md">VirtualNetworkRuleDefinition</a></i>
</pre>

## Properties

#### AccessKeyMetadataWritesEnabled

Is write operations on metadata resources (databases, containers, throughput) via account keys enabled? Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnalyticalStorageEnabled

Enable Analytical Storage option for this Cosmos DB account. Defaults to `false`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAutomaticFailover

Enable automatic fail over for this Cosmos DB account.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableFreeTier

Enable Free Tier pricing option for this Cosmos DB account. Defaults to `false`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableMultipleWriteLocations

Enable multi-master support for this Cosmos DB account.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpRangeFilter

CosmosDB Firewall Support: This value specifies the set of IP addresses or IP address ranges in CIDR form to be included as the allowed list of client IP's for a given database account. IP addresses/ranges must be comma separated and must not contain any spaces.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsVirtualNetworkFilterEnabled

Enables virtual network filtering for this Cosmos DB account.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyVaultKeyId

A versionless Key Vault Key ID for CMK encryption. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kind

Specifies the Kind of CosmosDB to create - possible values are `GlobalDocumentDB` and `MongoDB`. Defaults to `GlobalDocumentDB`. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MongoServerVersion

The Server Version of a MongoDB account. Possible values are `4.0`, `3.6`, and `3.2`. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the CosmosDB Account. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkAclBypassForAzureServices

If azure services can bypass ACLs. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkAclBypassIds

The list of resource Ids for Network Acl Bypass for this Cosmos DB account.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OfferType

Specifies the Offer Type to use for this CosmosDB Account - currently this can only be set to `Standard`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicNetworkAccessEnabled

Whether or not public network access is allowed for this CosmosDB account.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which the CosmosDB Account is created. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backup

_Required_: No

_Type_: List of <a href="backupdefinition.md">BackupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Capabilities

_Required_: No

_Type_: List of <a href="capabilitiesdefinition.md">CapabilitiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsistencyPolicy

_Required_: No

_Type_: List of <a href="consistencypolicydefinition.md">ConsistencyPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CorsRule

_Required_: No

_Type_: List of <a href="corsruledefinition.md">CorsRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeoLocation

_Required_: No

_Type_: List of <a href="geolocationdefinition.md">GeoLocationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of <a href="identitydefinition.md">IdentityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetworkRule

_Required_: No

_Type_: List of <a href="virtualnetworkruledefinition.md">VirtualNetworkRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ConnectionStrings

Returns the <code>ConnectionStrings</code> value.

#### Endpoint

Returns the <code>Endpoint</code> value.

#### Id

Returns the <code>Id</code> value.

#### PrimaryKey

Returns the <code>PrimaryKey</code> value.

#### PrimaryMasterKey

Returns the <code>PrimaryMasterKey</code> value.

#### PrimaryReadonlyKey

Returns the <code>PrimaryReadonlyKey</code> value.

#### PrimaryReadonlyMasterKey

Returns the <code>PrimaryReadonlyMasterKey</code> value.

#### ReadEndpoints

Returns the <code>ReadEndpoints</code> value.

#### SecondaryKey

Returns the <code>SecondaryKey</code> value.

#### SecondaryMasterKey

Returns the <code>SecondaryMasterKey</code> value.

#### SecondaryReadonlyKey

Returns the <code>SecondaryReadonlyKey</code> value.

#### SecondaryReadonlyMasterKey

Returns the <code>SecondaryReadonlyMasterKey</code> value.

#### WriteEndpoints

Returns the <code>WriteEndpoints</code> value.

