# TF::AWS::EmrInstanceFleet

Provides an Elastic MapReduce Cluster Instance Fleet configuration.
See [Amazon Elastic MapReduce Documentation](https://aws.amazon.com/documentation/emr/) for more information.

~> **NOTE:** At this time, Instance Fleets cannot be destroyed through the API nor
web interface. Instance Fleets are destroyed when the EMR Cluster is destroyed.
Terraform will resize any Instance Fleet to zero when destroying the resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::EmrInstanceFleet",
    "Properties" : {
        "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#targetondemandcapacity" title="TargetOnDemandCapacity">TargetOnDemandCapacity</a>" : <i>Double</i>,
        "<a href="#targetspotcapacity" title="TargetSpotCapacity">TargetSpotCapacity</a>" : <i>Double</i>,
        "<a href="#instancetypeconfigs" title="InstanceTypeConfigs">InstanceTypeConfigs</a>" : <i>[ <a href="instancetypeconfigsdefinition.md">InstanceTypeConfigsDefinition</a>, ... ]</i>,
        "<a href="#launchspecifications" title="LaunchSpecifications">LaunchSpecifications</a>" : <i>[ <a href="launchspecificationsdefinition.md">LaunchSpecificationsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::EmrInstanceFleet
Properties:
    <a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#targetondemandcapacity" title="TargetOnDemandCapacity">TargetOnDemandCapacity</a>: <i>Double</i>
    <a href="#targetspotcapacity" title="TargetSpotCapacity">TargetSpotCapacity</a>: <i>Double</i>
    <a href="#instancetypeconfigs" title="InstanceTypeConfigs">InstanceTypeConfigs</a>: <i>
      - <a href="instancetypeconfigsdefinition.md">InstanceTypeConfigsDefinition</a></i>
    <a href="#launchspecifications" title="LaunchSpecifications">LaunchSpecifications</a>: <i>
      - <a href="launchspecificationsdefinition.md">LaunchSpecificationsDefinition</a></i>
</pre>

## Properties

#### ClusterId

ID of the EMR Cluster to attach to. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Friendly name given to the instance fleet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetOnDemandCapacity

The target capacity of On-Demand units for the instance fleet, which determines how many On-Demand instances to provision.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetSpotCapacity

The target capacity of Spot units for the instance fleet, which determines how many Spot instances to provision.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTypeConfigs

_Required_: No

_Type_: List of <a href="instancetypeconfigsdefinition.md">InstanceTypeConfigsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchSpecifications

_Required_: No

_Type_: List of <a href="launchspecificationsdefinition.md">LaunchSpecificationsDefinition</a>

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

#### ProvisionedOnDemandCapacity

Returns the <code>ProvisionedOnDemandCapacity</code> value.

#### ProvisionedSpotCapacity

Returns the <code>ProvisionedSpotCapacity</code> value.

