# Terraform::AWS::AutoscalingGroup InstancesDistribution

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ondemandallocationstrategy" title="OnDemandAllocationStrategy">OnDemandAllocationStrategy</a>" : <i>String</i>,
    "<a href="#ondemandbasecapacity" title="OnDemandBaseCapacity">OnDemandBaseCapacity</a>" : <i>Double</i>,
    "<a href="#ondemandpercentageabovebasecapacity" title="OnDemandPercentageAboveBaseCapacity">OnDemandPercentageAboveBaseCapacity</a>" : <i>Double</i>,
    "<a href="#spotallocationstrategy" title="SpotAllocationStrategy">SpotAllocationStrategy</a>" : <i>String</i>,
    "<a href="#spotinstancepools" title="SpotInstancePools">SpotInstancePools</a>" : <i>Double</i>,
    "<a href="#spotmaxprice" title="SpotMaxPrice">SpotMaxPrice</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#ondemandallocationstrategy" title="OnDemandAllocationStrategy">OnDemandAllocationStrategy</a>: <i>String</i>
<a href="#ondemandbasecapacity" title="OnDemandBaseCapacity">OnDemandBaseCapacity</a>: <i>Double</i>
<a href="#ondemandpercentageabovebasecapacity" title="OnDemandPercentageAboveBaseCapacity">OnDemandPercentageAboveBaseCapacity</a>: <i>Double</i>
<a href="#spotallocationstrategy" title="SpotAllocationStrategy">SpotAllocationStrategy</a>: <i>String</i>
<a href="#spotinstancepools" title="SpotInstancePools">SpotInstancePools</a>: <i>Double</i>
<a href="#spotmaxprice" title="SpotMaxPrice">SpotMaxPrice</a>: <i>String</i>
</pre>

## Properties

#### OnDemandAllocationStrategy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnDemandBaseCapacity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnDemandPercentageAboveBaseCapacity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotAllocationStrategy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotInstancePools

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotMaxPrice

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

