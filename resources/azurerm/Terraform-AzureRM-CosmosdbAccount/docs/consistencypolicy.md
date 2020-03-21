# Terraform::AzureRM::CosmosdbAccount ConsistencyPolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#consistencylevel" title="ConsistencyLevel">ConsistencyLevel</a>" : <i>String</i>,
    "<a href="#maxintervalinseconds" title="MaxIntervalInSeconds">MaxIntervalInSeconds</a>" : <i>Double</i>,
    "<a href="#maxstalenessprefix" title="MaxStalenessPrefix">MaxStalenessPrefix</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#consistencylevel" title="ConsistencyLevel">ConsistencyLevel</a>: <i>String</i>
<a href="#maxintervalinseconds" title="MaxIntervalInSeconds">MaxIntervalInSeconds</a>: <i>Double</i>
<a href="#maxstalenessprefix" title="MaxStalenessPrefix">MaxStalenessPrefix</a>: <i>Double</i>
</pre>

## Properties

#### ConsistencyLevel

The Consistency Level to use for this CosmosDB Account - can be either `BoundedStaleness`, `Eventual`, `Session`, `Strong` or `ConsistentPrefix`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxIntervalInSeconds

When used with the Bounded Staleness consistency level, this value represents the time amount of staleness (in seconds) tolerated. Accepted range for this value is `5` - `86400` (1 day). Defaults to `5`. Required when `consistency_level` is set to `BoundedStaleness`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxStalenessPrefix

When used with the Bounded Staleness consistency level, this value represents the number of stale requests tolerated. Accepted range for this value is `10` – `2147483647`. Defaults to `100`. Required when `consistency_level` is set to `BoundedStaleness`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

