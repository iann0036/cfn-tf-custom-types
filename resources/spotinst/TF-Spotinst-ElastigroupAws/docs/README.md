# TF::Spotinst::ElastigroupAws

Provides a Spotinst AWS group resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Spotinst::ElastigroupAws",
    "Properties" : {
        "<a href="#availabilityzones" title="AvailabilityZones">AvailabilityZones</a>" : <i>[ String, ... ]</i>,
        "<a href="#blockdevicesmode" title="BlockDevicesMode">BlockDevicesMode</a>" : <i>String</i>,
        "<a href="#capacityunit" title="CapacityUnit">CapacityUnit</a>" : <i>String</i>,
        "<a href="#cpucredits" title="CpuCredits">CpuCredits</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>" : <i>Double</i>,
        "<a href="#drainingtimeout" title="DrainingTimeout">DrainingTimeout</a>" : <i>Double</i>,
        "<a href="#ebsoptimized" title="EbsOptimized">EbsOptimized</a>" : <i>Boolean</i>,
        "<a href="#elasticips" title="ElasticIps">ElasticIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#elasticloadbalancers" title="ElasticLoadBalancers">ElasticLoadBalancers</a>" : <i>[ String, ... ]</i>,
        "<a href="#enablemonitoring" title="EnableMonitoring">EnableMonitoring</a>" : <i>Boolean</i>,
        "<a href="#fallbacktoondemand" title="FallbackToOndemand">FallbackToOndemand</a>" : <i>Boolean</i>,
        "<a href="#healthcheckgraceperiod" title="HealthCheckGracePeriod">HealthCheckGracePeriod</a>" : <i>Double</i>,
        "<a href="#healthchecktype" title="HealthCheckType">HealthCheckType</a>" : <i>String</i>,
        "<a href="#healthcheckunhealthydurationbeforereplacement" title="HealthCheckUnhealthyDurationBeforeReplacement">HealthCheckUnhealthyDurationBeforeReplacement</a>" : <i>Double</i>,
        "<a href="#iaminstanceprofile" title="IamInstanceProfile">IamInstanceProfile</a>" : <i>String</i>,
        "<a href="#imageid" title="ImageId">ImageId</a>" : <i>String</i>,
        "<a href="#instancetypesondemand" title="InstanceTypesOndemand">InstanceTypesOndemand</a>" : <i>String</i>,
        "<a href="#instancetypespreferredspot" title="InstanceTypesPreferredSpot">InstanceTypesPreferredSpot</a>" : <i>[ String, ... ]</i>,
        "<a href="#instancetypesspot" title="InstanceTypesSpot">InstanceTypesSpot</a>" : <i>[ String, ... ]</i>,
        "<a href="#keyname" title="KeyName">KeyName</a>" : <i>String</i>,
        "<a href="#lifetimeperiod" title="LifetimePeriod">LifetimePeriod</a>" : <i>String</i>,
        "<a href="#maxsize" title="MaxSize">MaxSize</a>" : <i>Double</i>,
        "<a href="#minsize" title="MinSize">MinSize</a>" : <i>Double</i>,
        "<a href="#minimuminstancelifetime" title="MinimumInstanceLifetime">MinimumInstanceLifetime</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ondemandcount" title="OndemandCount">OndemandCount</a>" : <i>Double</i>,
        "<a href="#orientation" title="Orientation">Orientation</a>" : <i>String</i>,
        "<a href="#persistblockdevices" title="PersistBlockDevices">PersistBlockDevices</a>" : <i>Boolean</i>,
        "<a href="#persistprivateip" title="PersistPrivateIp">PersistPrivateIp</a>" : <i>Boolean</i>,
        "<a href="#persistrootdevice" title="PersistRootDevice">PersistRootDevice</a>" : <i>Boolean</i>,
        "<a href="#placementtenancy" title="PlacementTenancy">PlacementTenancy</a>" : <i>String</i>,
        "<a href="#preferredavailabilityzones" title="PreferredAvailabilityZones">PreferredAvailabilityZones</a>" : <i>[ String, ... ]</i>,
        "<a href="#privateips" title="PrivateIps">PrivateIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#product" title="Product">Product</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#shutdownscript" title="ShutdownScript">ShutdownScript</a>" : <i>String</i>,
        "<a href="#spotpercentage" title="SpotPercentage">SpotPercentage</a>" : <i>Double</i>,
        "<a href="#subnetids" title="SubnetIds">SubnetIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#targetgrouparns" title="TargetGroupArns">TargetGroupArns</a>" : <i>[ String, ... ]</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#utilizecommitments" title="UtilizeCommitments">UtilizeCommitments</a>" : <i>Boolean</i>,
        "<a href="#utilizereservedinstances" title="UtilizeReservedInstances">UtilizeReservedInstances</a>" : <i>Boolean</i>,
        "<a href="#waitforcapacity" title="WaitForCapacity">WaitForCapacity</a>" : <i>Double</i>,
        "<a href="#waitforcapacitytimeout" title="WaitForCapacityTimeout">WaitForCapacityTimeout</a>" : <i>Double</i>,
        "<a href="#cpuoptions" title="CpuOptions">CpuOptions</a>" : <i>[ <a href="cpuoptionsdefinition.md">CpuOptionsDefinition</a>, ... ]</i>,
        "<a href="#ebsblockdevice" title="EbsBlockDevice">EbsBlockDevice</a>" : <i>[ <a href="ebsblockdevicedefinition.md">EbsBlockDeviceDefinition</a>, ... ]</i>,
        "<a href="#ephemeralblockdevice" title="EphemeralBlockDevice">EphemeralBlockDevice</a>" : <i>[ <a href="ephemeralblockdevicedefinition.md">EphemeralBlockDeviceDefinition</a>, ... ]</i>,
        "<a href="#instancetypesweights" title="InstanceTypesWeights">InstanceTypesWeights</a>" : <i>[ <a href="instancetypesweightsdefinition.md">InstanceTypesWeightsDefinition</a>, ... ]</i>,
        "<a href="#integrationbeanstalk" title="IntegrationBeanstalk">IntegrationBeanstalk</a>" : <i>[ <a href="integrationbeanstalkdefinition.md">IntegrationBeanstalkDefinition</a>, ... ]</i>,
        "<a href="#integrationcodedeploy" title="IntegrationCodedeploy">IntegrationCodedeploy</a>" : <i>[ <a href="integrationcodedeploydefinition.md">IntegrationCodedeployDefinition</a>, ... ]</i>,
        "<a href="#integrationdockerswarm" title="IntegrationDockerSwarm">IntegrationDockerSwarm</a>" : <i>[ <a href="integrationdockerswarmdefinition.md">IntegrationDockerSwarmDefinition</a>, ... ]</i>,
        "<a href="#integrationecs" title="IntegrationEcs">IntegrationEcs</a>" : <i>[ <a href="integrationecsdefinition.md">IntegrationEcsDefinition</a>, ... ]</i>,
        "<a href="#integrationgitlab" title="IntegrationGitlab">IntegrationGitlab</a>" : <i>[ <a href="integrationgitlabdefinition.md">IntegrationGitlabDefinition</a>, ... ]</i>,
        "<a href="#integrationkubernetes" title="IntegrationKubernetes">IntegrationKubernetes</a>" : <i>[ <a href="integrationkubernetesdefinition.md">IntegrationKubernetesDefinition</a>, ... ]</i>,
        "<a href="#integrationmesosphere" title="IntegrationMesosphere">IntegrationMesosphere</a>" : <i>[ <a href="integrationmesospheredefinition.md">IntegrationMesosphereDefinition</a>, ... ]</i>,
        "<a href="#integrationmultairuntime" title="IntegrationMultaiRuntime">IntegrationMultaiRuntime</a>" : <i>[ <a href="integrationmultairuntimedefinition.md">IntegrationMultaiRuntimeDefinition</a>, ... ]</i>,
        "<a href="#integrationnomad" title="IntegrationNomad">IntegrationNomad</a>" : <i>[ <a href="integrationnomaddefinition.md">IntegrationNomadDefinition</a>, ... ]</i>,
        "<a href="#integrationrancher" title="IntegrationRancher">IntegrationRancher</a>" : <i>[ <a href="integrationrancherdefinition.md">IntegrationRancherDefinition</a>, ... ]</i>,
        "<a href="#integrationroute53" title="IntegrationRoute53">IntegrationRoute53</a>" : <i>[ <a href="integrationroute53definition.md">IntegrationRoute53Definition</a>, ... ]</i>,
        "<a href="#metadataoptions" title="MetadataOptions">MetadataOptions</a>" : <i>[ <a href="metadataoptionsdefinition.md">MetadataOptionsDefinition</a>, ... ]</i>,
        "<a href="#multaitargetsets" title="MultaiTargetSets">MultaiTargetSets</a>" : <i>[ <a href="multaitargetsetsdefinition.md">MultaiTargetSetsDefinition</a>, ... ]</i>,
        "<a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>" : <i>[ <a href="networkinterfacedefinition.md">NetworkInterfaceDefinition</a>, ... ]</i>,
        "<a href="#reverttospot" title="RevertToSpot">RevertToSpot</a>" : <i>[ <a href="reverttospotdefinition.md">RevertToSpotDefinition</a>, ... ]</i>,
        "<a href="#scalingdownpolicy" title="ScalingDownPolicy">ScalingDownPolicy</a>" : <i>[ <a href="scalingdownpolicydefinition.md">ScalingDownPolicyDefinition</a>, ... ]</i>,
        "<a href="#scalingstrategy" title="ScalingStrategy">ScalingStrategy</a>" : <i>[ <a href="scalingstrategydefinition.md">ScalingStrategyDefinition</a>, ... ]</i>,
        "<a href="#scalingtargetpolicy" title="ScalingTargetPolicy">ScalingTargetPolicy</a>" : <i>[ <a href="scalingtargetpolicydefinition.md">ScalingTargetPolicyDefinition</a>, ... ]</i>,
        "<a href="#scalinguppolicy" title="ScalingUpPolicy">ScalingUpPolicy</a>" : <i>[ <a href="scalinguppolicydefinition.md">ScalingUpPolicyDefinition</a>, ... ]</i>,
        "<a href="#scheduledtask" title="ScheduledTask">ScheduledTask</a>" : <i>[ <a href="scheduledtaskdefinition.md">ScheduledTaskDefinition</a>, ... ]</i>,
        "<a href="#signal" title="Signal">Signal</a>" : <i>[ <a href="signaldefinition.md">SignalDefinition</a>, ... ]</i>,
        "<a href="#statefuldeallocation" title="StatefulDeallocation">StatefulDeallocation</a>" : <i>[ <a href="statefuldeallocationdefinition.md">StatefulDeallocationDefinition</a>, ... ]</i>,
        "<a href="#statefulinstanceaction" title="StatefulInstanceAction">StatefulInstanceAction</a>" : <i>[ <a href="statefulinstanceactiondefinition.md">StatefulInstanceActionDefinition</a>, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#updatepolicy" title="UpdatePolicy">UpdatePolicy</a>" : <i>[ <a href="updatepolicydefinition.md">UpdatePolicyDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Spotinst::ElastigroupAws
Properties:
    <a href="#availabilityzones" title="AvailabilityZones">AvailabilityZones</a>: <i>
      - String</i>
    <a href="#blockdevicesmode" title="BlockDevicesMode">BlockDevicesMode</a>: <i>String</i>
    <a href="#capacityunit" title="CapacityUnit">CapacityUnit</a>: <i>String</i>
    <a href="#cpucredits" title="CpuCredits">CpuCredits</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>: <i>Double</i>
    <a href="#drainingtimeout" title="DrainingTimeout">DrainingTimeout</a>: <i>Double</i>
    <a href="#ebsoptimized" title="EbsOptimized">EbsOptimized</a>: <i>Boolean</i>
    <a href="#elasticips" title="ElasticIps">ElasticIps</a>: <i>
      - String</i>
    <a href="#elasticloadbalancers" title="ElasticLoadBalancers">ElasticLoadBalancers</a>: <i>
      - String</i>
    <a href="#enablemonitoring" title="EnableMonitoring">EnableMonitoring</a>: <i>Boolean</i>
    <a href="#fallbacktoondemand" title="FallbackToOndemand">FallbackToOndemand</a>: <i>Boolean</i>
    <a href="#healthcheckgraceperiod" title="HealthCheckGracePeriod">HealthCheckGracePeriod</a>: <i>Double</i>
    <a href="#healthchecktype" title="HealthCheckType">HealthCheckType</a>: <i>String</i>
    <a href="#healthcheckunhealthydurationbeforereplacement" title="HealthCheckUnhealthyDurationBeforeReplacement">HealthCheckUnhealthyDurationBeforeReplacement</a>: <i>Double</i>
    <a href="#iaminstanceprofile" title="IamInstanceProfile">IamInstanceProfile</a>: <i>String</i>
    <a href="#imageid" title="ImageId">ImageId</a>: <i>String</i>
    <a href="#instancetypesondemand" title="InstanceTypesOndemand">InstanceTypesOndemand</a>: <i>String</i>
    <a href="#instancetypespreferredspot" title="InstanceTypesPreferredSpot">InstanceTypesPreferredSpot</a>: <i>
      - String</i>
    <a href="#instancetypesspot" title="InstanceTypesSpot">InstanceTypesSpot</a>: <i>
      - String</i>
    <a href="#keyname" title="KeyName">KeyName</a>: <i>String</i>
    <a href="#lifetimeperiod" title="LifetimePeriod">LifetimePeriod</a>: <i>String</i>
    <a href="#maxsize" title="MaxSize">MaxSize</a>: <i>Double</i>
    <a href="#minsize" title="MinSize">MinSize</a>: <i>Double</i>
    <a href="#minimuminstancelifetime" title="MinimumInstanceLifetime">MinimumInstanceLifetime</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ondemandcount" title="OndemandCount">OndemandCount</a>: <i>Double</i>
    <a href="#orientation" title="Orientation">Orientation</a>: <i>String</i>
    <a href="#persistblockdevices" title="PersistBlockDevices">PersistBlockDevices</a>: <i>Boolean</i>
    <a href="#persistprivateip" title="PersistPrivateIp">PersistPrivateIp</a>: <i>Boolean</i>
    <a href="#persistrootdevice" title="PersistRootDevice">PersistRootDevice</a>: <i>Boolean</i>
    <a href="#placementtenancy" title="PlacementTenancy">PlacementTenancy</a>: <i>String</i>
    <a href="#preferredavailabilityzones" title="PreferredAvailabilityZones">PreferredAvailabilityZones</a>: <i>
      - String</i>
    <a href="#privateips" title="PrivateIps">PrivateIps</a>: <i>
      - String</i>
    <a href="#product" title="Product">Product</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>: <i>
      - String</i>
    <a href="#shutdownscript" title="ShutdownScript">ShutdownScript</a>: <i>String</i>
    <a href="#spotpercentage" title="SpotPercentage">SpotPercentage</a>: <i>Double</i>
    <a href="#subnetids" title="SubnetIds">SubnetIds</a>: <i>
      - String</i>
    <a href="#targetgrouparns" title="TargetGroupArns">TargetGroupArns</a>: <i>
      - String</i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#utilizecommitments" title="UtilizeCommitments">UtilizeCommitments</a>: <i>Boolean</i>
    <a href="#utilizereservedinstances" title="UtilizeReservedInstances">UtilizeReservedInstances</a>: <i>Boolean</i>
    <a href="#waitforcapacity" title="WaitForCapacity">WaitForCapacity</a>: <i>Double</i>
    <a href="#waitforcapacitytimeout" title="WaitForCapacityTimeout">WaitForCapacityTimeout</a>: <i>Double</i>
    <a href="#cpuoptions" title="CpuOptions">CpuOptions</a>: <i>
      - <a href="cpuoptionsdefinition.md">CpuOptionsDefinition</a></i>
    <a href="#ebsblockdevice" title="EbsBlockDevice">EbsBlockDevice</a>: <i>
      - <a href="ebsblockdevicedefinition.md">EbsBlockDeviceDefinition</a></i>
    <a href="#ephemeralblockdevice" title="EphemeralBlockDevice">EphemeralBlockDevice</a>: <i>
      - <a href="ephemeralblockdevicedefinition.md">EphemeralBlockDeviceDefinition</a></i>
    <a href="#instancetypesweights" title="InstanceTypesWeights">InstanceTypesWeights</a>: <i>
      - <a href="instancetypesweightsdefinition.md">InstanceTypesWeightsDefinition</a></i>
    <a href="#integrationbeanstalk" title="IntegrationBeanstalk">IntegrationBeanstalk</a>: <i>
      - <a href="integrationbeanstalkdefinition.md">IntegrationBeanstalkDefinition</a></i>
    <a href="#integrationcodedeploy" title="IntegrationCodedeploy">IntegrationCodedeploy</a>: <i>
      - <a href="integrationcodedeploydefinition.md">IntegrationCodedeployDefinition</a></i>
    <a href="#integrationdockerswarm" title="IntegrationDockerSwarm">IntegrationDockerSwarm</a>: <i>
      - <a href="integrationdockerswarmdefinition.md">IntegrationDockerSwarmDefinition</a></i>
    <a href="#integrationecs" title="IntegrationEcs">IntegrationEcs</a>: <i>
      - <a href="integrationecsdefinition.md">IntegrationEcsDefinition</a></i>
    <a href="#integrationgitlab" title="IntegrationGitlab">IntegrationGitlab</a>: <i>
      - <a href="integrationgitlabdefinition.md">IntegrationGitlabDefinition</a></i>
    <a href="#integrationkubernetes" title="IntegrationKubernetes">IntegrationKubernetes</a>: <i>
      - <a href="integrationkubernetesdefinition.md">IntegrationKubernetesDefinition</a></i>
    <a href="#integrationmesosphere" title="IntegrationMesosphere">IntegrationMesosphere</a>: <i>
      - <a href="integrationmesospheredefinition.md">IntegrationMesosphereDefinition</a></i>
    <a href="#integrationmultairuntime" title="IntegrationMultaiRuntime">IntegrationMultaiRuntime</a>: <i>
      - <a href="integrationmultairuntimedefinition.md">IntegrationMultaiRuntimeDefinition</a></i>
    <a href="#integrationnomad" title="IntegrationNomad">IntegrationNomad</a>: <i>
      - <a href="integrationnomaddefinition.md">IntegrationNomadDefinition</a></i>
    <a href="#integrationrancher" title="IntegrationRancher">IntegrationRancher</a>: <i>
      - <a href="integrationrancherdefinition.md">IntegrationRancherDefinition</a></i>
    <a href="#integrationroute53" title="IntegrationRoute53">IntegrationRoute53</a>: <i>
      - <a href="integrationroute53definition.md">IntegrationRoute53Definition</a></i>
    <a href="#metadataoptions" title="MetadataOptions">MetadataOptions</a>: <i>
      - <a href="metadataoptionsdefinition.md">MetadataOptionsDefinition</a></i>
    <a href="#multaitargetsets" title="MultaiTargetSets">MultaiTargetSets</a>: <i>
      - <a href="multaitargetsetsdefinition.md">MultaiTargetSetsDefinition</a></i>
    <a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>: <i>
      - <a href="networkinterfacedefinition.md">NetworkInterfaceDefinition</a></i>
    <a href="#reverttospot" title="RevertToSpot">RevertToSpot</a>: <i>
      - <a href="reverttospotdefinition.md">RevertToSpotDefinition</a></i>
    <a href="#scalingdownpolicy" title="ScalingDownPolicy">ScalingDownPolicy</a>: <i>
      - <a href="scalingdownpolicydefinition.md">ScalingDownPolicyDefinition</a></i>
    <a href="#scalingstrategy" title="ScalingStrategy">ScalingStrategy</a>: <i>
      - <a href="scalingstrategydefinition.md">ScalingStrategyDefinition</a></i>
    <a href="#scalingtargetpolicy" title="ScalingTargetPolicy">ScalingTargetPolicy</a>: <i>
      - <a href="scalingtargetpolicydefinition.md">ScalingTargetPolicyDefinition</a></i>
    <a href="#scalinguppolicy" title="ScalingUpPolicy">ScalingUpPolicy</a>: <i>
      - <a href="scalinguppolicydefinition.md">ScalingUpPolicyDefinition</a></i>
    <a href="#scheduledtask" title="ScheduledTask">ScheduledTask</a>: <i>
      - <a href="scheduledtaskdefinition.md">ScheduledTaskDefinition</a></i>
    <a href="#signal" title="Signal">Signal</a>: <i>
      - <a href="signaldefinition.md">SignalDefinition</a></i>
    <a href="#statefuldeallocation" title="StatefulDeallocation">StatefulDeallocation</a>: <i>
      - <a href="statefuldeallocationdefinition.md">StatefulDeallocationDefinition</a></i>
    <a href="#statefulinstanceaction" title="StatefulInstanceAction">StatefulInstanceAction</a>: <i>
      - <a href="statefulinstanceactiondefinition.md">StatefulInstanceActionDefinition</a></i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#updatepolicy" title="UpdatePolicy">UpdatePolicy</a>: <i>
      - <a href="updatepolicydefinition.md">UpdatePolicyDefinition</a></i>
</pre>

## Properties

#### AvailabilityZones

List of Strings of availability zones. When this parameter is set, `subnet_ids` should be left unused.
Note: `availability_zones` naming syntax follows the convention `availability-zone:subnet:placement-group-name`. For example, to set an AZ in `us-east-1` with subnet `subnet-123456` and placement group `ClusterI03`, you would set:
`availability_zones = ["us-east-1a:subnet-123456:ClusterI03"]`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockDevicesMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapacityUnit

The capacity unit to launch instances by. If not specified, when choosing the weight unit, each instance will weight as the number of its vCPUs. Valid values: `instance`, `weight`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuCredits

Controls how T3 instances are launched. Valid values: `standard`, `unlimited`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The group description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredCapacity

The desired number of instances the group should have at any time.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrainingTimeout

The time in seconds, the instance is allowed to run while detached from the ELB. This is to allow the instance time to be drained from incoming TCP connections before terminating it, during a scale down operation.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsOptimized

Enable high bandwidth connectivity between instances and AWS’s Elastic Block Store (EBS). For instance types that are EBS-optimized by default this parameter will be ignored.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticIps

A list of [AWS Elastic IP](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html) allocation IDs to associate to the group instances.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticLoadBalancers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableMonitoring

Indicates whether monitoring is enabled for the instance.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FallbackToOndemand

In a case of no Spot instances available, Elastigroup will launch on-demand instances instead.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckGracePeriod

The amount of time, in seconds, after the instance has launched to starts and check its health.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckType

The service that will perform health checks for the instance. Valid values: `"ELB"`, `"HCS"`, `"TARGET_GROUP"`, `"MLB"`, `"EC2"`, `"MULTAI_TARGET_SET"`, `"MLB_RUNTIME"`, `"K8S_NODE"`, `"NOMAD_NODE"`, `"ECS_CLUSTER_INSTANCE"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckUnhealthyDurationBeforeReplacement

The amount of time, in seconds, that we will wait before replacing an instance that is running and became unhealthy (this is only applicable for instances that were once healthy).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamInstanceProfile

The ARN or name of an IAM instance profile to associate with launched instances.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageId

The ID of the AMI used to launch the instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTypesOndemand

The type of instance determines your instance's CPU capacity, memory and storage (e.g., m1.small, c1.xlarge).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTypesPreferredSpot

Prioritize a subset of spot instance types. Must be a subset of the selected spot instance types.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTypesSpot

One or more instance types.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyName

The key name that should be used for the instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifetimePeriod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSize

The maximum number of instances the group should have at any time.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinSize

The minimum number of instances the group should have at any time.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinimumInstanceLifetime

Defines the preferred minimum instance lifetime in hours. Markets which comply with this preference will be prioritized. Optional values: 1, 3, 6, 12, 24.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The group name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OndemandCount

Number of on demand instances to launch in the group. All other instances will be spot instances. When this parameter is set the `spot_percentage` parameter is being ignored.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Orientation

Select a prediction strategy. Valid values: `balanced`, `costOriented`, `equalAzDistribution`, `availabilityOriented`. You can read more in our documentation.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistBlockDevices

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistPrivateIp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistRootDevice

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlacementTenancy

Enable dedicated tenancy. Note: There is a flat hourly fee for each region in which dedicated tenancy is used. Valid values: "default", "dedicated" .

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredAvailabilityZones

The AZs to prioritize when launching Spot instances. If no markets are available in the Preferred AZs, Spot instances are launched in the non-preferred AZs.
Note: Must be a sublist of `availability_zones` and `orientation` value must not be `"equalAzDistribution"`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIps

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Product

Operation system type. Valid values: `"Linux/UNIX"`, `"SUSE Linux"`, `"Windows"`.
For EC2 Classic instances:  `"Linux/UNIX (Amazon VPC)"`, `"SUSE Linux (Amazon VPC)"`, `"Windows (Amazon VPC)"`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The AWS region your group will be created in.
Note: This parameter is required if you specify subnets (through subnet_ids). This parameter is optional if you specify Availability Zones (through availability_zones).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroups

A list of associated security group IDS.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShutdownScript

The Base64-encoded shutdown script that executes prior to instance termination, for more information please see: [Shutdown Script](https://api.spotinst.com/integration-docs/elastigroup/concepts/compute-concepts/shutdown-scripts/).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotPercentage

The percentage of Spot instances that would spin up from the `desired_capacity` number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetIds

List of Strings of subnet identifiers.
Note: When this parameter is set, `availability_zones` should be left unused.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroupArns

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

The user data to provide when launching the instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UtilizeCommitments

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UtilizeReservedInstances

In a case of any available reserved instances, Elastigroup will utilize them first before purchasing Spot instances.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForCapacity

Minimum number of instances in a 'HEALTHY' status that is required before continuing. This is ignored when updating with blue/green deployment. Cannot exceed `desired_capacity`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForCapacityTimeout

Time (seconds) to wait for instances to report a 'HEALTHY' status. Useful for plans with multiple dependencies that take some time to initialize. Leave undefined or set to `0` to indicate no wait. This is ignored when updating with blue/green deployment.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuOptions

_Required_: No

_Type_: List of <a href="cpuoptionsdefinition.md">CpuOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsBlockDevice

_Required_: No

_Type_: List of <a href="ebsblockdevicedefinition.md">EbsBlockDeviceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EphemeralBlockDevice

_Required_: No

_Type_: List of <a href="ephemeralblockdevicedefinition.md">EphemeralBlockDeviceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTypesWeights

_Required_: No

_Type_: List of <a href="instancetypesweightsdefinition.md">InstanceTypesWeightsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationBeanstalk

_Required_: No

_Type_: List of <a href="integrationbeanstalkdefinition.md">IntegrationBeanstalkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationCodedeploy

_Required_: No

_Type_: List of <a href="integrationcodedeploydefinition.md">IntegrationCodedeployDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationDockerSwarm

_Required_: No

_Type_: List of <a href="integrationdockerswarmdefinition.md">IntegrationDockerSwarmDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationEcs

_Required_: No

_Type_: List of <a href="integrationecsdefinition.md">IntegrationEcsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationGitlab

_Required_: No

_Type_: List of <a href="integrationgitlabdefinition.md">IntegrationGitlabDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationKubernetes

_Required_: No

_Type_: List of <a href="integrationkubernetesdefinition.md">IntegrationKubernetesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationMesosphere

_Required_: No

_Type_: List of <a href="integrationmesospheredefinition.md">IntegrationMesosphereDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationMultaiRuntime

_Required_: No

_Type_: List of <a href="integrationmultairuntimedefinition.md">IntegrationMultaiRuntimeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationNomad

_Required_: No

_Type_: List of <a href="integrationnomaddefinition.md">IntegrationNomadDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationRancher

_Required_: No

_Type_: List of <a href="integrationrancherdefinition.md">IntegrationRancherDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationRoute53

_Required_: No

_Type_: List of <a href="integrationroute53definition.md">IntegrationRoute53Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetadataOptions

_Required_: No

_Type_: List of <a href="metadataoptionsdefinition.md">MetadataOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultaiTargetSets

_Required_: No

_Type_: List of <a href="multaitargetsetsdefinition.md">MultaiTargetSetsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterface

_Required_: No

_Type_: List of <a href="networkinterfacedefinition.md">NetworkInterfaceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RevertToSpot

_Required_: No

_Type_: List of <a href="reverttospotdefinition.md">RevertToSpotDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingDownPolicy

_Required_: No

_Type_: List of <a href="scalingdownpolicydefinition.md">ScalingDownPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingStrategy

_Required_: No

_Type_: List of <a href="scalingstrategydefinition.md">ScalingStrategyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingTargetPolicy

_Required_: No

_Type_: List of <a href="scalingtargetpolicydefinition.md">ScalingTargetPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingUpPolicy

_Required_: No

_Type_: List of <a href="scalinguppolicydefinition.md">ScalingUpPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduledTask

_Required_: No

_Type_: List of <a href="scheduledtaskdefinition.md">ScheduledTaskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Signal

_Required_: No

_Type_: List of <a href="signaldefinition.md">SignalDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatefulDeallocation

_Required_: No

_Type_: List of <a href="statefuldeallocationdefinition.md">StatefulDeallocationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatefulInstanceAction

_Required_: No

_Type_: List of <a href="statefulinstanceactiondefinition.md">StatefulInstanceActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdatePolicy

_Required_: No

_Type_: List of <a href="updatepolicydefinition.md">UpdatePolicyDefinition</a>

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

