# Terraform::Spotinst::OceanAws

Provides a Spotinst Ocean AWS resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Spotinst::OceanAws",
    "Properties" : {
        "<a href="#associatepublicipaddress" title="AssociatePublicIpAddress">AssociatePublicIpAddress</a>" : <i>Boolean</i>,
        "<a href="#blacklist" title="Blacklist">Blacklist</a>" : <i>[ String, ... ]</i>,
        "<a href="#controllerid" title="ControllerId">ControllerId</a>" : <i>String</i>,
        "<a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>" : <i>Double</i>,
        "<a href="#drainingtimeout" title="DrainingTimeout">DrainingTimeout</a>" : <i>Double</i>,
        "<a href="#ebsoptimized" title="EbsOptimized">EbsOptimized</a>" : <i>Boolean</i>,
        "<a href="#fallbacktoondemand" title="FallbackToOndemand">FallbackToOndemand</a>" : <i>Boolean</i>,
        "<a href="#iaminstanceprofile" title="IamInstanceProfile">IamInstanceProfile</a>" : <i>String</i>,
        "<a href="#imageid" title="ImageId">ImageId</a>" : <i>String</i>,
        "<a href="#keyname" title="KeyName">KeyName</a>" : <i>String</i>,
        "<a href="#maxsize" title="MaxSize">MaxSize</a>" : <i>Double</i>,
        "<a href="#minsize" title="MinSize">MinSize</a>" : <i>Double</i>,
        "<a href="#monitoring" title="Monitoring">Monitoring</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#rootvolumesize" title="RootVolumeSize">RootVolumeSize</a>" : <i>Double</i>,
        "<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#spotpercentage" title="SpotPercentage">SpotPercentage</a>" : <i>Double</i>,
        "<a href="#subnetids" title="SubnetIds">SubnetIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#utilizereservedinstances" title="UtilizeReservedInstances">UtilizeReservedInstances</a>" : <i>Boolean</i>,
        "<a href="#whitelist" title="Whitelist">Whitelist</a>" : <i>[ String, ... ]</i>,
        "<a href="#autoscaler" title="Autoscaler">Autoscaler</a>" : <i>[ <a href="autoscaler.md">Autoscaler</a>, ... ]</i>,
        "<a href="#loadbalancers" title="LoadBalancers">LoadBalancers</a>" : <i>[ <a href="loadbalancers.md">LoadBalancers</a>, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#updatepolicy" title="UpdatePolicy">UpdatePolicy</a>" : <i>[ <a href="updatepolicy.md">UpdatePolicy</a>, ... ]</i>,
        "<a href="#autoscaledown" title="AutoscaleDown">AutoscaleDown</a>" : <i>[ <a href="autoscaledown.md">AutoscaleDown</a>, ... ]</i>,
        "<a href="#autoscaleheadroom" title="AutoscaleHeadroom">AutoscaleHeadroom</a>" : <i>[ <a href="autoscaleheadroom.md">AutoscaleHeadroom</a>, ... ]</i>,
        "<a href="#resourcelimits" title="ResourceLimits">ResourceLimits</a>" : <i>[ <a href="resourcelimits.md">ResourceLimits</a>, ... ]</i>,
        "<a href="#rollconfig" title="RollConfig">RollConfig</a>" : <i>[ <a href="rollconfig.md">RollConfig</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Spotinst::OceanAws
Properties:
    <a href="#associatepublicipaddress" title="AssociatePublicIpAddress">AssociatePublicIpAddress</a>: <i>Boolean</i>
    <a href="#blacklist" title="Blacklist">Blacklist</a>: <i>
      - String</i>
    <a href="#controllerid" title="ControllerId">ControllerId</a>: <i>String</i>
    <a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>: <i>Double</i>
    <a href="#drainingtimeout" title="DrainingTimeout">DrainingTimeout</a>: <i>Double</i>
    <a href="#ebsoptimized" title="EbsOptimized">EbsOptimized</a>: <i>Boolean</i>
    <a href="#fallbacktoondemand" title="FallbackToOndemand">FallbackToOndemand</a>: <i>Boolean</i>
    <a href="#iaminstanceprofile" title="IamInstanceProfile">IamInstanceProfile</a>: <i>String</i>
    <a href="#imageid" title="ImageId">ImageId</a>: <i>String</i>
    <a href="#keyname" title="KeyName">KeyName</a>: <i>String</i>
    <a href="#maxsize" title="MaxSize">MaxSize</a>: <i>Double</i>
    <a href="#minsize" title="MinSize">MinSize</a>: <i>Double</i>
    <a href="#monitoring" title="Monitoring">Monitoring</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#rootvolumesize" title="RootVolumeSize">RootVolumeSize</a>: <i>Double</i>
    <a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>: <i>
      - String</i>
    <a href="#spotpercentage" title="SpotPercentage">SpotPercentage</a>: <i>Double</i>
    <a href="#subnetids" title="SubnetIds">SubnetIds</a>: <i>
      - String</i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#utilizereservedinstances" title="UtilizeReservedInstances">UtilizeReservedInstances</a>: <i>Boolean</i>
    <a href="#whitelist" title="Whitelist">Whitelist</a>: <i>
      - String</i>
    <a href="#autoscaler" title="Autoscaler">Autoscaler</a>: <i>
      - <a href="autoscaler.md">Autoscaler</a></i>
    <a href="#loadbalancers" title="LoadBalancers">LoadBalancers</a>: <i>
      - <a href="loadbalancers.md">LoadBalancers</a></i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#updatepolicy" title="UpdatePolicy">UpdatePolicy</a>: <i>
      - <a href="updatepolicy.md">UpdatePolicy</a></i>
    <a href="#autoscaledown" title="AutoscaleDown">AutoscaleDown</a>: <i>
      - <a href="autoscaledown.md">AutoscaleDown</a></i>
    <a href="#autoscaleheadroom" title="AutoscaleHeadroom">AutoscaleHeadroom</a>: <i>
      - <a href="autoscaleheadroom.md">AutoscaleHeadroom</a></i>
    <a href="#resourcelimits" title="ResourceLimits">ResourceLimits</a>: <i>
      - <a href="resourcelimits.md">ResourceLimits</a></i>
    <a href="#rollconfig" title="RollConfig">RollConfig</a>: <i>
      - <a href="rollconfig.md">RollConfig</a></i>
</pre>

## Properties

#### AssociatePublicIpAddress

Configure public IP address allocation.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Blacklist

Instance types not allowed in the Ocean cluster. Cannot be configured if `whitelist` is configured.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControllerId

The ocean cluster identifier. Example: `ocean.k8s`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredCapacity

The number of instances to launch and maintain in the cluster.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrainingTimeout

The time in seconds, the instance is allowed to run while detached from the ELB. This is to allow the instance time to be drained from incoming TCP connections before terminating it, during a scale down operation.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsOptimized

Enable EBS optimized for cluster. Flag will enable optimized capacity for high bandwidth connectivity to the EB service for non EBS optimized instance types. For instances that are EBS optimized this flag will be ignored.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FallbackToOndemand

If not Spot instance markets are available, enable Ocean to launch On-Demand instances instead.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamInstanceProfile

The instance profile iam role.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageId

ID of the image used to launch the instances.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyName

The key pair to attach the instances.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSize

The upper limit of instances the cluster can scale up to.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinSize

The lower limit of instances the cluster can scale down to.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Monitoring

Enable detailed monitoring for cluster. Flag will enable Cloud Watch detailed detailed monitoring (one minute increments). Note: there are additional hourly costs for this service based on the region used.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Required if type is set to CLASSIC
* `type` - (Required) Can be set to CLASSIC or TARGET_GROUP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region the cluster will run in.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootVolumeSize

The size (in Gb) to allocate for the root volume. Minimum `20`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroups

One or more security group ids.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotPercentage

The percentage of Spot instances the cluster should maintain. Min 0, max 100.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetIds

A comma-separated list of subnet identifiers for the Ocean cluster. Subnet IDs should be configured with auto assign public ip.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

Base64-encoded MIME user data to make available to the instances.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UtilizeReservedInstances

If Reserved instances exist, OCean will utilize them before launching Spot instances.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Whitelist

Instance types allowed in the Ocean cluster. Cannot be configured if `blacklist` is configured.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Autoscaler

_Required_: No

_Type_: List of <a href="autoscaler.md">Autoscaler</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancers

_Required_: No

_Type_: List of <a href="loadbalancers.md">LoadBalancers</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdatePolicy

_Required_: No

_Type_: List of <a href="updatepolicy.md">UpdatePolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleDown

_Required_: No

_Type_: List of <a href="autoscaledown.md">AutoscaleDown</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleHeadroom

_Required_: No

_Type_: List of <a href="autoscaleheadroom.md">AutoscaleHeadroom</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceLimits

_Required_: No

_Type_: List of <a href="resourcelimits.md">ResourceLimits</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RollConfig

_Required_: No

_Type_: List of <a href="rollconfig.md">RollConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

