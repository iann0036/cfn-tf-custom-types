# TF::AzureRM::CosmosdbSqlContainer

Manages a SQL Container within a Cosmos DB Account.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::CosmosdbSqlContainer",
    "Properties" : {
        "<a href="#accountname" title="AccountName">AccountName</a>" : <i>String</i>,
        "<a href="#analyticalstoragettl" title="AnalyticalStorageTtl">AnalyticalStorageTtl</a>" : <i>Double</i>,
        "<a href="#databasename" title="DatabaseName">DatabaseName</a>" : <i>String</i>,
        "<a href="#defaultttl" title="DefaultTtl">DefaultTtl</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#partitionkeypath" title="PartitionKeyPath">PartitionKeyPath</a>" : <i>String</i>,
        "<a href="#partitionkeyversion" title="PartitionKeyVersion">PartitionKeyVersion</a>" : <i>Double</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#throughput" title="Throughput">Throughput</a>" : <i>Double</i>,
        "<a href="#autoscalesettings" title="AutoscaleSettings">AutoscaleSettings</a>" : <i>[ <a href="autoscalesettingsdefinition.md">AutoscaleSettingsDefinition</a>, ... ]</i>,
        "<a href="#conflictresolutionpolicy" title="ConflictResolutionPolicy">ConflictResolutionPolicy</a>" : <i>[ <a href="conflictresolutionpolicydefinition.md">ConflictResolutionPolicyDefinition</a>, ... ]</i>,
        "<a href="#indexingpolicy" title="IndexingPolicy">IndexingPolicy</a>" : <i>[ <a href="indexingpolicydefinition.md">IndexingPolicyDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#uniquekey" title="UniqueKey">UniqueKey</a>" : <i>[ <a href="uniquekeydefinition.md">UniqueKeyDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::CosmosdbSqlContainer
Properties:
    <a href="#accountname" title="AccountName">AccountName</a>: <i>String</i>
    <a href="#analyticalstoragettl" title="AnalyticalStorageTtl">AnalyticalStorageTtl</a>: <i>Double</i>
    <a href="#databasename" title="DatabaseName">DatabaseName</a>: <i>String</i>
    <a href="#defaultttl" title="DefaultTtl">DefaultTtl</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#partitionkeypath" title="PartitionKeyPath">PartitionKeyPath</a>: <i>String</i>
    <a href="#partitionkeyversion" title="PartitionKeyVersion">PartitionKeyVersion</a>: <i>Double</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#throughput" title="Throughput">Throughput</a>: <i>Double</i>
    <a href="#autoscalesettings" title="AutoscaleSettings">AutoscaleSettings</a>: <i>
      - <a href="autoscalesettingsdefinition.md">AutoscaleSettingsDefinition</a></i>
    <a href="#conflictresolutionpolicy" title="ConflictResolutionPolicy">ConflictResolutionPolicy</a>: <i>
      - <a href="conflictresolutionpolicydefinition.md">ConflictResolutionPolicyDefinition</a></i>
    <a href="#indexingpolicy" title="IndexingPolicy">IndexingPolicy</a>: <i>
      - <a href="indexingpolicydefinition.md">IndexingPolicyDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#uniquekey" title="UniqueKey">UniqueKey</a>: <i>
      - <a href="uniquekeydefinition.md">UniqueKeyDefinition</a></i>
</pre>

## Properties

#### AccountName

The name of the Cosmos DB Account to create the container within. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnalyticalStorageTtl

The default time to live of Analytical Storage for this SQL container. If present and the value is set to `-1`, it is equal to infinity, and items don’t expire by default. If present and the value is set to some number `n` – items will expire `n` seconds after their last modified time.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseName

The name of the Cosmos DB SQL Database to create the container within. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultTtl

The default time to live of SQL container. If missing, items are not expired automatically. If present and the value is set to `-1`, it is equal to infinity, and items don’t expire by default. If present and the value is set to some number `n` – items will expire `n` seconds after their last modified time.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the Cosmos DB SQL Container. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PartitionKeyPath

Define a partition key. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PartitionKeyVersion

Define a partition key version. Changing this forces a new resource to be created. Possible values are `1 `and `2`. This should be set to `2` in order to use large partition keys.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which the Cosmos DB SQL Container is created. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Throughput

The throughput of SQL container (RU/s). Must be set in increments of `100`. The minimum value is `400`. This must be set upon container creation otherwise it cannot be updated without a manual terraform destroy-apply.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleSettings

_Required_: No

_Type_: List of <a href="autoscalesettingsdefinition.md">AutoscaleSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConflictResolutionPolicy

_Required_: No

_Type_: List of <a href="conflictresolutionpolicydefinition.md">ConflictResolutionPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IndexingPolicy

_Required_: No

_Type_: List of <a href="indexingpolicydefinition.md">IndexingPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UniqueKey

_Required_: No

_Type_: List of <a href="uniquekeydefinition.md">UniqueKeyDefinition</a>

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
