# TF::AzureRM::ContainerRegistry

Manages an Azure Container Registry.

~> **Note:** All arguments including the access key will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::ContainerRegistry",
    "Properties" : {
        "<a href="#adminenabled" title="AdminEnabled">AdminEnabled</a>" : <i>Boolean</i>,
        "<a href="#encryption" title="Encryption">Encryption</a>" : <i>[ <a href="encryptiondefinition.md">EncryptionDefinition</a>, ... ]</i>,
        "<a href="#georeplicationlocations" title="GeoreplicationLocations">GeoreplicationLocations</a>" : <i>[ String, ... ]</i>,
        "<a href="#georeplications" title="Georeplications">Georeplications</a>" : <i>[ <a href="georeplicationsdefinition2.md">GeoreplicationsDefinition2</a>, ... ]</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkruleset" title="NetworkRuleSet">NetworkRuleSet</a>" : <i>[ <a href="networkrulesetdefinition3.md">NetworkRuleSetDefinition3</a>, ... ]</i>,
        "<a href="#publicnetworkaccessenabled" title="PublicNetworkAccessEnabled">PublicNetworkAccessEnabled</a>" : <i>Boolean</i>,
        "<a href="#quarantinepolicyenabled" title="QuarantinePolicyEnabled">QuarantinePolicyEnabled</a>" : <i>Boolean</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#retentionpolicy" title="RetentionPolicy">RetentionPolicy</a>" : <i>[ <a href="retentionpolicydefinition.md">RetentionPolicyDefinition</a>, ... ]</i>,
        "<a href="#sku" title="Sku">Sku</a>" : <i>String</i>,
        "<a href="#storageaccountid" title="StorageAccountId">StorageAccountId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="georeplicationsdefinition.md">GeoreplicationsDefinition</a>, ... ]</i>,
        "<a href="#trustpolicy" title="TrustPolicy">TrustPolicy</a>" : <i>[ <a href="trustpolicydefinition.md">TrustPolicyDefinition</a>, ... ]</i>,
        "<a href="#zoneredundancyenabled" title="ZoneRedundancyEnabled">ZoneRedundancyEnabled</a>" : <i>Boolean</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ <a href="identitydefinition.md">IdentityDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::ContainerRegistry
Properties:
    <a href="#adminenabled" title="AdminEnabled">AdminEnabled</a>: <i>Boolean</i>
    <a href="#encryption" title="Encryption">Encryption</a>: <i>
      - <a href="encryptiondefinition.md">EncryptionDefinition</a></i>
    <a href="#georeplicationlocations" title="GeoreplicationLocations">GeoreplicationLocations</a>: <i>
      - String</i>
    <a href="#georeplications" title="Georeplications">Georeplications</a>: <i>
      - <a href="georeplicationsdefinition2.md">GeoreplicationsDefinition2</a></i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkruleset" title="NetworkRuleSet">NetworkRuleSet</a>: <i>
      - <a href="networkrulesetdefinition3.md">NetworkRuleSetDefinition3</a></i>
    <a href="#publicnetworkaccessenabled" title="PublicNetworkAccessEnabled">PublicNetworkAccessEnabled</a>: <i>Boolean</i>
    <a href="#quarantinepolicyenabled" title="QuarantinePolicyEnabled">QuarantinePolicyEnabled</a>: <i>Boolean</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#retentionpolicy" title="RetentionPolicy">RetentionPolicy</a>: <i>
      - <a href="retentionpolicydefinition.md">RetentionPolicyDefinition</a></i>
    <a href="#sku" title="Sku">Sku</a>: <i>String</i>
    <a href="#storageaccountid" title="StorageAccountId">StorageAccountId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="georeplicationsdefinition.md">GeoreplicationsDefinition</a></i>
    <a href="#trustpolicy" title="TrustPolicy">TrustPolicy</a>: <i>
      - <a href="trustpolicydefinition.md">TrustPolicyDefinition</a></i>
    <a href="#zoneredundancyenabled" title="ZoneRedundancyEnabled">ZoneRedundancyEnabled</a>: <i>Boolean</i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - <a href="identitydefinition.md">IdentityDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AdminEnabled

Specifies whether the admin user is enabled. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encryption

An `encryption` block as documented below.

_Required_: No

_Type_: List of <a href="encryptiondefinition.md">EncryptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeoreplicationLocations

A list of Azure locations where the container registry should be geo-replicated.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Georeplications

A `georeplications` block as documented below.

_Required_: No

_Type_: List of <a href="georeplicationsdefinition2.md">GeoreplicationsDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the Container Registry. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkRuleSet

A `network_rule_set` block as documented below.

_Required_: No

_Type_: List of <a href="networkrulesetdefinition3.md">NetworkRuleSetDefinition3</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicNetworkAccessEnabled

Whether public network access is allowed for the container registry. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuarantinePolicyEnabled

Boolean value that indicates whether quarantine policy is enabled. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to create the Container Registry. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionPolicy

A `retention_policy` block as documented below.

_Required_: No

_Type_: List of <a href="retentionpolicydefinition.md">RetentionPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sku

The SKU name of the container registry. Possible values are  `Basic`, `Standard` and `Premium`. `Classic` (which was previously `Basic`) is supported only for existing resources.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountId

The ID of a Storage Account which must be located in the same Azure Region as the Container Registry.  Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="georeplicationsdefinition.md">GeoreplicationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrustPolicy

A `trust_policy` block as documented below.

_Required_: No

_Type_: List of <a href="trustpolicydefinition.md">TrustPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneRedundancyEnabled

Whether zone redundancy is enabled for this Container Registry? Changing this forces a new resource to be created. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of <a href="identitydefinition.md">IdentityDefinition</a>

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

#### AdminPassword

Returns the <code>AdminPassword</code> value.

#### AdminUsername

Returns the <code>AdminUsername</code> value.

#### Id

Returns the <code>Id</code> value.

#### LoginServer

Returns the <code>LoginServer</code> value.

