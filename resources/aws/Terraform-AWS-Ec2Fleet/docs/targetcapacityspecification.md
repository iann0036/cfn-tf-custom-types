# Terraform::AWS::Ec2Fleet TargetCapacitySpecification

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaulttargetcapacitytype" title="DefaultTargetCapacityType">DefaultTargetCapacityType</a>" : <i>String</i>,
    "<a href="#ondemandtargetcapacity" title="OnDemandTargetCapacity">OnDemandTargetCapacity</a>" : <i>Double</i>,
    "<a href="#spottargetcapacity" title="SpotTargetCapacity">SpotTargetCapacity</a>" : <i>Double</i>,
    "<a href="#totaltargetcapacity" title="TotalTargetCapacity">TotalTargetCapacity</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#defaulttargetcapacitytype" title="DefaultTargetCapacityType">DefaultTargetCapacityType</a>: <i>String</i>
<a href="#ondemandtargetcapacity" title="OnDemandTargetCapacity">OnDemandTargetCapacity</a>: <i>Double</i>
<a href="#spottargetcapacity" title="SpotTargetCapacity">SpotTargetCapacity</a>: <i>Double</i>
<a href="#totaltargetcapacity" title="TotalTargetCapacity">TotalTargetCapacity</a>: <i>Double</i>
</pre>

## Properties

#### DefaultTargetCapacityType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnDemandTargetCapacity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotTargetCapacity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TotalTargetCapacity

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

