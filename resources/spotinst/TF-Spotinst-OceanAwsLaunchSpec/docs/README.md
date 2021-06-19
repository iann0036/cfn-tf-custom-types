# TF::Spotinst::OceanAwsLaunchSpec

Manages a Spotinst Ocean AWS [Virtual Node Group](https://docs.spot.io/ocean/features/launch-specifications) resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Spotinst::OceanAwsLaunchSpec",
    "Properties" : {
        "<a href="#associatepublicipaddress" title="AssociatePublicIpAddress">AssociatePublicIpAddress</a>" : <i>Boolean</i>,
        "<a href="#iaminstanceprofile" title="IamInstanceProfile">IamInstanceProfile</a>" : <i>String</i>,
        "<a href="#imageid" title="ImageId">ImageId</a>" : <i>String</i>,
        "<a href="#instancetypes" title="InstanceTypes">InstanceTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#oceanid" title="OceanId">OceanId</a>" : <i>String</i>,
        "<a href="#restrictscaledown" title="RestrictScaleDown">RestrictScaleDown</a>" : <i>Boolean</i>,
        "<a href="#rootvolumesize" title="RootVolumeSize">RootVolumeSize</a>" : <i>Double</i>,
        "<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#subnetids" title="SubnetIds">SubnetIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#autoscaleheadrooms" title="AutoscaleHeadrooms">AutoscaleHeadrooms</a>" : <i>[ <a href="autoscaleheadroomsdefinition.md">AutoscaleHeadroomsDefinition</a>, ... ]</i>,
        "<a href="#blockdevicemappings" title="BlockDeviceMappings">BlockDeviceMappings</a>" : <i>[ <a href="blockdevicemappingsdefinition.md">BlockDeviceMappingsDefinition</a>, ... ]</i>,
        "<a href="#createoptions" title="CreateOptions">CreateOptions</a>" : <i>[ <a href="createoptionsdefinition.md">CreateOptionsDefinition</a>, ... ]</i>,
        "<a href="#elasticippool" title="ElasticIpPool">ElasticIpPool</a>" : <i>[ <a href="elasticippooldefinition.md">ElasticIpPoolDefinition</a>, ... ]</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#resourcelimits" title="ResourceLimits">ResourceLimits</a>" : <i>[ <a href="resourcelimitsdefinition.md">ResourceLimitsDefinition</a>, ... ]</i>,
        "<a href="#strategy" title="Strategy">Strategy</a>" : <i>[ <a href="strategydefinition.md">StrategyDefinition</a>, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#taints" title="Taints">Taints</a>" : <i>[ <a href="taintsdefinition.md">TaintsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Spotinst::OceanAwsLaunchSpec
Properties:
    <a href="#associatepublicipaddress" title="AssociatePublicIpAddress">AssociatePublicIpAddress</a>: <i>Boolean</i>
    <a href="#iaminstanceprofile" title="IamInstanceProfile">IamInstanceProfile</a>: <i>String</i>
    <a href="#imageid" title="ImageId">ImageId</a>: <i>String</i>
    <a href="#instancetypes" title="InstanceTypes">InstanceTypes</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#oceanid" title="OceanId">OceanId</a>: <i>String</i>
    <a href="#restrictscaledown" title="RestrictScaleDown">RestrictScaleDown</a>: <i>Boolean</i>
    <a href="#rootvolumesize" title="RootVolumeSize">RootVolumeSize</a>: <i>Double</i>
    <a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>: <i>
      - String</i>
    <a href="#subnetids" title="SubnetIds">SubnetIds</a>: <i>
      - String</i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#autoscaleheadrooms" title="AutoscaleHeadrooms">AutoscaleHeadrooms</a>: <i>
      - <a href="autoscaleheadroomsdefinition.md">AutoscaleHeadroomsDefinition</a></i>
    <a href="#blockdevicemappings" title="BlockDeviceMappings">BlockDeviceMappings</a>: <i>
      - <a href="blockdevicemappingsdefinition.md">BlockDeviceMappingsDefinition</a></i>
    <a href="#createoptions" title="CreateOptions">CreateOptions</a>: <i>
      - <a href="createoptionsdefinition.md">CreateOptionsDefinition</a></i>
    <a href="#elasticippool" title="ElasticIpPool">ElasticIpPool</a>: <i>
      - <a href="elasticippooldefinition.md">ElasticIpPoolDefinition</a></i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#resourcelimits" title="ResourceLimits">ResourceLimits</a>: <i>
      - <a href="resourcelimitsdefinition.md">ResourceLimitsDefinition</a></i>
    <a href="#strategy" title="Strategy">Strategy</a>: <i>
      - <a href="strategydefinition.md">StrategyDefinition</a></i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#taints" title="Taints">Taints</a>: <i>
      - <a href="taintsdefinition.md">TaintsDefinition</a></i>
</pre>

## Properties

#### AssociatePublicIpAddress

Configure public IP address allocation.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamInstanceProfile

The ARN or name of an IAM instance profile to associate with launched instances.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageId

ID of the image used to launch the instances.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTypes

A list of instance types allowed to be provisioned for pods pending under the specified launch specification. The list overrides the list defined for the cluster.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Virtual Node Group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OceanId

The ID of the Ocean cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestrictScaleDown

Boolean. When set to `True`, nodes will be treated as if all pods running have the restrict-scale-down label. Therefore, Ocean will not scale nodes down unless empty.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootVolumeSize

Set root volume size (in GB).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroups

Optionally adds security group IDs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetIds

A list of subnet IDs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

Base64-encoded MIME user data to make available to the instances.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleHeadrooms

_Required_: No

_Type_: List of <a href="autoscaleheadroomsdefinition.md">AutoscaleHeadroomsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockDeviceMappings

_Required_: No

_Type_: List of <a href="blockdevicemappingsdefinition.md">BlockDeviceMappingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateOptions

_Required_: No

_Type_: List of <a href="createoptionsdefinition.md">CreateOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticIpPool

_Required_: No

_Type_: List of <a href="elasticippooldefinition.md">ElasticIpPoolDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceLimits

_Required_: No

_Type_: List of <a href="resourcelimitsdefinition.md">ResourceLimitsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Strategy

_Required_: No

_Type_: List of <a href="strategydefinition.md">StrategyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Taints

_Required_: No

_Type_: List of <a href="taintsdefinition.md">TaintsDefinition</a>

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

