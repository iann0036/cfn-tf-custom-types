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

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxIntervalInSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxStalenessPrefix

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

