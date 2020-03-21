# Terraform::Spotinst::ElastigroupAws

CloudFormation equivalent of spotinst_elastigroup_aws

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Spotinst::ElastigroupAws",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
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
        "<a href="#utilizereservedinstances" title="UtilizeReservedInstances">UtilizeReservedInstances</a>" : <i>Boolean</i>,
        "<a href="#waitforcapacity" title="WaitForCapacity">WaitForCapacity</a>" : <i>Double</i>,
        "<a href="#waitforcapacitytimeout" title="WaitForCapacityTimeout">WaitForCapacityTimeout</a>" : <i>Double</i>,
        "<a href="#ebsblockdevice" title="EbsBlockDevice">EbsBlockDevice</a>" : <i>[ &lt;a href=&#34;ebsblockdevice.md&#34;&gt;EbsBlockDevice&lt;/a&gt;, ... ]</i>,
        "<a href="#ephemeralblockdevice" title="EphemeralBlockDevice">EphemeralBlockDevice</a>" : <i>[ &lt;a href=&#34;ephemeralblockdevice.md&#34;&gt;EphemeralBlockDevice&lt;/a&gt;, ... ]</i>,
        "<a href="#instancetypesweights" title="InstanceTypesWeights">InstanceTypesWeights</a>" : <i>[ &lt;a href=&#34;instancetypesweights.md&#34;&gt;InstanceTypesWeights&lt;/a&gt;, ... ]</i>,
        "<a href="#integrationbeanstalk" title="IntegrationBeanstalk">IntegrationBeanstalk</a>" : <i>[ &lt;a href=&#34;integrationbeanstalk.md&#34;&gt;IntegrationBeanstalk&lt;/a&gt;, ... ]</i>,
        "<a href="#integrationcodedeploy" title="IntegrationCodedeploy">IntegrationCodedeploy</a>" : <i>[ &lt;a href=&#34;integrationcodedeploy.md&#34;&gt;IntegrationCodedeploy&lt;/a&gt;, ... ]</i>,
        "<a href="#integrationdockerswarm" title="IntegrationDockerSwarm">IntegrationDockerSwarm</a>" : <i>[ &lt;a href=&#34;integrationdockerswarm.md&#34;&gt;IntegrationDockerSwarm&lt;/a&gt;, ... ]</i>,
        "<a href="#integrationecs" title="IntegrationEcs">IntegrationEcs</a>" : <i>[ &lt;a href=&#34;integrationecs.md&#34;&gt;IntegrationEcs&lt;/a&gt;, ... ]</i>,
        "<a href="#integrationgitlab" title="IntegrationGitlab">IntegrationGitlab</a>" : <i>[ &lt;a href=&#34;integrationgitlab.md&#34;&gt;IntegrationGitlab&lt;/a&gt;, ... ]</i>,
        "<a href="#integrationkubernetes" title="IntegrationKubernetes">IntegrationKubernetes</a>" : <i>[ &lt;a href=&#34;integrationkubernetes.md&#34;&gt;IntegrationKubernetes&lt;/a&gt;, ... ]</i>,
        "<a href="#integrationmesosphere" title="IntegrationMesosphere">IntegrationMesosphere</a>" : <i>[ &lt;a href=&#34;integrationmesosphere.md&#34;&gt;IntegrationMesosphere&lt;/a&gt;, ... ]</i>,
        "<a href="#integrationmultairuntime" title="IntegrationMultaiRuntime">IntegrationMultaiRuntime</a>" : <i>[ &lt;a href=&#34;integrationmultairuntime.md&#34;&gt;IntegrationMultaiRuntime&lt;/a&gt;, ... ]</i>,
        "<a href="#integrationnomad" title="IntegrationNomad">IntegrationNomad</a>" : <i>[ &lt;a href=&#34;integrationnomad.md&#34;&gt;IntegrationNomad&lt;/a&gt;, ... ]</i>,
        "<a href="#integrationrancher" title="IntegrationRancher">IntegrationRancher</a>" : <i>[ &lt;a href=&#34;integrationrancher.md&#34;&gt;IntegrationRancher&lt;/a&gt;, ... ]</i>,
        "<a href="#integrationroute53" title="IntegrationRoute53">IntegrationRoute53</a>" : <i>[ &lt;a href=&#34;integrationroute53.md&#34;&gt;IntegrationRoute53&lt;/a&gt;, ... ]</i>,
        "<a href="#multaitargetsets" title="MultaiTargetSets">MultaiTargetSets</a>" : <i>[ &lt;a href=&#34;multaitargetsets.md&#34;&gt;MultaiTargetSets&lt;/a&gt;, ... ]</i>,
        "<a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>" : <i>[ &lt;a href=&#34;networkinterface.md&#34;&gt;NetworkInterface&lt;/a&gt;, ... ]</i>,
        "<a href="#reverttospot" title="RevertToSpot">RevertToSpot</a>" : <i>[ &lt;a href=&#34;reverttospot.md&#34;&gt;RevertToSpot&lt;/a&gt;, ... ]</i>,
        "<a href="#scalingdownpolicy" title="ScalingDownPolicy">ScalingDownPolicy</a>" : <i>[ &lt;a href=&#34;scalingdownpolicy.md&#34;&gt;ScalingDownPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#scalingstrategy" title="ScalingStrategy">ScalingStrategy</a>" : <i>[ &lt;a href=&#34;scalingstrategy.md&#34;&gt;ScalingStrategy&lt;/a&gt;, ... ]</i>,
        "<a href="#scalingtargetpolicy" title="ScalingTargetPolicy">ScalingTargetPolicy</a>" : <i>[ &lt;a href=&#34;scalingtargetpolicy.md&#34;&gt;ScalingTargetPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#scalinguppolicy" title="ScalingUpPolicy">ScalingUpPolicy</a>" : <i>[ &lt;a href=&#34;scalinguppolicy.md&#34;&gt;ScalingUpPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#scheduledtask" title="ScheduledTask">ScheduledTask</a>" : <i>[ &lt;a href=&#34;scheduledtask.md&#34;&gt;ScheduledTask&lt;/a&gt;, ... ]</i>,
        "<a href="#signal" title="Signal">Signal</a>" : <i>[ &lt;a href=&#34;signal.md&#34;&gt;Signal&lt;/a&gt;, ... ]</i>,
        "<a href="#statefuldeallocation" title="StatefulDeallocation">StatefulDeallocation</a>" : <i>[ &lt;a href=&#34;statefuldeallocation.md&#34;&gt;StatefulDeallocation&lt;/a&gt;, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#updatepolicy" title="UpdatePolicy">UpdatePolicy</a>" : <i>[ &lt;a href=&#34;updatepolicy.md&#34;&gt;UpdatePolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#deploymentpreferences" title="DeploymentPreferences">DeploymentPreferences</a>" : <i>[ &lt;a href=&#34;deploymentpreferences.md&#34;&gt;DeploymentPreferences&lt;/a&gt;, ... ]</i>,
        "<a href="#managedactions" title="ManagedActions">ManagedActions</a>" : <i>[ &lt;a href=&#34;managedactions.md&#34;&gt;ManagedActions&lt;/a&gt;, ... ]</i>,
        "<a href="#deploymentgroups" title="DeploymentGroups">DeploymentGroups</a>" : <i>[ &lt;a href=&#34;deploymentgroups.md&#34;&gt;DeploymentGroups&lt;/a&gt;, ... ]</i>,
        "<a href="#autoscaledown" title="AutoscaleDown">AutoscaleDown</a>" : <i>[ &lt;a href=&#34;autoscaledown.md&#34;&gt;AutoscaleDown&lt;/a&gt;, ... ]</i>,
        "<a href="#autoscaleheadroom" title="AutoscaleHeadroom">AutoscaleHeadroom</a>" : <i>[ &lt;a href=&#34;autoscaleheadroom.md&#34;&gt;AutoscaleHeadroom&lt;/a&gt;, ... ]</i>,
        "<a href="#autoscaleattributes" title="AutoscaleAttributes">AutoscaleAttributes</a>" : <i>[ &lt;a href=&#34;autoscaleattributes.md&#34;&gt;AutoscaleAttributes&lt;/a&gt;, ... ]</i>,
        "<a href="#runner" title="Runner">Runner</a>" : <i>[ &lt;a href=&#34;runner.md&#34;&gt;Runner&lt;/a&gt;, ... ]</i>,
        "<a href="#autoscalelabels" title="AutoscaleLabels">AutoscaleLabels</a>" : <i>[ &lt;a href=&#34;autoscalelabels.md&#34;&gt;AutoscaleLabels&lt;/a&gt;, ... ]</i>,
        "<a href="#autoscaleconstraints" title="AutoscaleConstraints">AutoscaleConstraints</a>" : <i>[ &lt;a href=&#34;autoscaleconstraints.md&#34;&gt;AutoscaleConstraints&lt;/a&gt;, ... ]</i>,
        "<a href="#domains" title="Domains">Domains</a>" : <i>[ &lt;a href=&#34;domains.md&#34;&gt;Domains&lt;/a&gt;, ... ]</i>,
        "<a href="#dimensions" title="Dimensions">Dimensions</a>" : <i>[ &lt;a href=&#34;dimensions.md&#34;&gt;Dimensions&lt;/a&gt;, ... ]</i>,
        "<a href="#rollconfig" title="RollConfig">RollConfig</a>" : <i>[ &lt;a href=&#34;rollconfig.md&#34;&gt;RollConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#strategy" title="Strategy">Strategy</a>" : <i>[ &lt;a href=&#34;strategy.md&#34;&gt;Strategy&lt;/a&gt;, ... ]</i>,
        "<a href="#platformupdate" title="PlatformUpdate">PlatformUpdate</a>" : <i>[ &lt;a href=&#34;platformupdate.md&#34;&gt;PlatformUpdate&lt;/a&gt;, ... ]</i>,
        "<a href="#recordsets" title="RecordSets">RecordSets</a>" : <i>[ &lt;a href=&#34;recordsets.md&#34;&gt;RecordSets&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Spotinst::ElastigroupAws
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
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
    <a href="#utilizereservedinstances" title="UtilizeReservedInstances">UtilizeReservedInstances</a>: <i>Boolean</i>
    <a href="#waitforcapacity" title="WaitForCapacity">WaitForCapacity</a>: <i>Double</i>
    <a href="#waitforcapacitytimeout" title="WaitForCapacityTimeout">WaitForCapacityTimeout</a>: <i>Double</i>
    <a href="#ebsblockdevice" title="EbsBlockDevice">EbsBlockDevice</a>: <i>
      - &lt;a href=&#34;ebsblockdevice.md&#34;&gt;EbsBlockDevice&lt;/a&gt;</i>
    <a href="#ephemeralblockdevice" title="EphemeralBlockDevice">EphemeralBlockDevice</a>: <i>
      - &lt;a href=&#34;ephemeralblockdevice.md&#34;&gt;EphemeralBlockDevice&lt;/a&gt;</i>
    <a href="#instancetypesweights" title="InstanceTypesWeights">InstanceTypesWeights</a>: <i>
      - &lt;a href=&#34;instancetypesweights.md&#34;&gt;InstanceTypesWeights&lt;/a&gt;</i>
    <a href="#integrationbeanstalk" title="IntegrationBeanstalk">IntegrationBeanstalk</a>: <i>
      - &lt;a href=&#34;integrationbeanstalk.md&#34;&gt;IntegrationBeanstalk&lt;/a&gt;</i>
    <a href="#integrationcodedeploy" title="IntegrationCodedeploy">IntegrationCodedeploy</a>: <i>
      - &lt;a href=&#34;integrationcodedeploy.md&#34;&gt;IntegrationCodedeploy&lt;/a&gt;</i>
    <a href="#integrationdockerswarm" title="IntegrationDockerSwarm">IntegrationDockerSwarm</a>: <i>
      - &lt;a href=&#34;integrationdockerswarm.md&#34;&gt;IntegrationDockerSwarm&lt;/a&gt;</i>
    <a href="#integrationecs" title="IntegrationEcs">IntegrationEcs</a>: <i>
      - &lt;a href=&#34;integrationecs.md&#34;&gt;IntegrationEcs&lt;/a&gt;</i>
    <a href="#integrationgitlab" title="IntegrationGitlab">IntegrationGitlab</a>: <i>
      - &lt;a href=&#34;integrationgitlab.md&#34;&gt;IntegrationGitlab&lt;/a&gt;</i>
    <a href="#integrationkubernetes" title="IntegrationKubernetes">IntegrationKubernetes</a>: <i>
      - &lt;a href=&#34;integrationkubernetes.md&#34;&gt;IntegrationKubernetes&lt;/a&gt;</i>
    <a href="#integrationmesosphere" title="IntegrationMesosphere">IntegrationMesosphere</a>: <i>
      - &lt;a href=&#34;integrationmesosphere.md&#34;&gt;IntegrationMesosphere&lt;/a&gt;</i>
    <a href="#integrationmultairuntime" title="IntegrationMultaiRuntime">IntegrationMultaiRuntime</a>: <i>
      - &lt;a href=&#34;integrationmultairuntime.md&#34;&gt;IntegrationMultaiRuntime&lt;/a&gt;</i>
    <a href="#integrationnomad" title="IntegrationNomad">IntegrationNomad</a>: <i>
      - &lt;a href=&#34;integrationnomad.md&#34;&gt;IntegrationNomad&lt;/a&gt;</i>
    <a href="#integrationrancher" title="IntegrationRancher">IntegrationRancher</a>: <i>
      - &lt;a href=&#34;integrationrancher.md&#34;&gt;IntegrationRancher&lt;/a&gt;</i>
    <a href="#integrationroute53" title="IntegrationRoute53">IntegrationRoute53</a>: <i>
      - &lt;a href=&#34;integrationroute53.md&#34;&gt;IntegrationRoute53&lt;/a&gt;</i>
    <a href="#multaitargetsets" title="MultaiTargetSets">MultaiTargetSets</a>: <i>
      - &lt;a href=&#34;multaitargetsets.md&#34;&gt;MultaiTargetSets&lt;/a&gt;</i>
    <a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>: <i>
      - &lt;a href=&#34;networkinterface.md&#34;&gt;NetworkInterface&lt;/a&gt;</i>
    <a href="#reverttospot" title="RevertToSpot">RevertToSpot</a>: <i>
      - &lt;a href=&#34;reverttospot.md&#34;&gt;RevertToSpot&lt;/a&gt;</i>
    <a href="#scalingdownpolicy" title="ScalingDownPolicy">ScalingDownPolicy</a>: <i>
      - &lt;a href=&#34;scalingdownpolicy.md&#34;&gt;ScalingDownPolicy&lt;/a&gt;</i>
    <a href="#scalingstrategy" title="ScalingStrategy">ScalingStrategy</a>: <i>
      - &lt;a href=&#34;scalingstrategy.md&#34;&gt;ScalingStrategy&lt;/a&gt;</i>
    <a href="#scalingtargetpolicy" title="ScalingTargetPolicy">ScalingTargetPolicy</a>: <i>
      - &lt;a href=&#34;scalingtargetpolicy.md&#34;&gt;ScalingTargetPolicy&lt;/a&gt;</i>
    <a href="#scalinguppolicy" title="ScalingUpPolicy">ScalingUpPolicy</a>: <i>
      - &lt;a href=&#34;scalinguppolicy.md&#34;&gt;ScalingUpPolicy&lt;/a&gt;</i>
    <a href="#scheduledtask" title="ScheduledTask">ScheduledTask</a>: <i>
      - &lt;a href=&#34;scheduledtask.md&#34;&gt;ScheduledTask&lt;/a&gt;</i>
    <a href="#signal" title="Signal">Signal</a>: <i>
      - &lt;a href=&#34;signal.md&#34;&gt;Signal&lt;/a&gt;</i>
    <a href="#statefuldeallocation" title="StatefulDeallocation">StatefulDeallocation</a>: <i>
      - &lt;a href=&#34;statefuldeallocation.md&#34;&gt;StatefulDeallocation&lt;/a&gt;</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#updatepolicy" title="UpdatePolicy">UpdatePolicy</a>: <i>
      - &lt;a href=&#34;updatepolicy.md&#34;&gt;UpdatePolicy&lt;/a&gt;</i>
    <a href="#deploymentpreferences" title="DeploymentPreferences">DeploymentPreferences</a>: <i>
      - &lt;a href=&#34;deploymentpreferences.md&#34;&gt;DeploymentPreferences&lt;/a&gt;</i>
    <a href="#managedactions" title="ManagedActions">ManagedActions</a>: <i>
      - &lt;a href=&#34;managedactions.md&#34;&gt;ManagedActions&lt;/a&gt;</i>
    <a href="#deploymentgroups" title="DeploymentGroups">DeploymentGroups</a>: <i>
      - &lt;a href=&#34;deploymentgroups.md&#34;&gt;DeploymentGroups&lt;/a&gt;</i>
    <a href="#autoscaledown" title="AutoscaleDown">AutoscaleDown</a>: <i>
      - &lt;a href=&#34;autoscaledown.md&#34;&gt;AutoscaleDown&lt;/a&gt;</i>
    <a href="#autoscaleheadroom" title="AutoscaleHeadroom">AutoscaleHeadroom</a>: <i>
      - &lt;a href=&#34;autoscaleheadroom.md&#34;&gt;AutoscaleHeadroom&lt;/a&gt;</i>
    <a href="#autoscaleattributes" title="AutoscaleAttributes">AutoscaleAttributes</a>: <i>
      - &lt;a href=&#34;autoscaleattributes.md&#34;&gt;AutoscaleAttributes&lt;/a&gt;</i>
    <a href="#runner" title="Runner">Runner</a>: <i>
      - &lt;a href=&#34;runner.md&#34;&gt;Runner&lt;/a&gt;</i>
    <a href="#autoscalelabels" title="AutoscaleLabels">AutoscaleLabels</a>: <i>
      - &lt;a href=&#34;autoscalelabels.md&#34;&gt;AutoscaleLabels&lt;/a&gt;</i>
    <a href="#autoscaleconstraints" title="AutoscaleConstraints">AutoscaleConstraints</a>: <i>
      - &lt;a href=&#34;autoscaleconstraints.md&#34;&gt;AutoscaleConstraints&lt;/a&gt;</i>
    <a href="#domains" title="Domains">Domains</a>: <i>
      - &lt;a href=&#34;domains.md&#34;&gt;Domains&lt;/a&gt;</i>
    <a href="#dimensions" title="Dimensions">Dimensions</a>: <i>
      - &lt;a href=&#34;dimensions.md&#34;&gt;Dimensions&lt;/a&gt;</i>
    <a href="#rollconfig" title="RollConfig">RollConfig</a>: <i>
      - &lt;a href=&#34;rollconfig.md&#34;&gt;RollConfig&lt;/a&gt;</i>
    <a href="#strategy" title="Strategy">Strategy</a>: <i>
      - &lt;a href=&#34;strategy.md&#34;&gt;Strategy&lt;/a&gt;</i>
    <a href="#platformupdate" title="PlatformUpdate">PlatformUpdate</a>: <i>
      - &lt;a href=&#34;platformupdate.md&#34;&gt;PlatformUpdate&lt;/a&gt;</i>
    <a href="#recordsets" title="RecordSets">RecordSets</a>: <i>
      - &lt;a href=&#34;recordsets.md&#34;&gt;RecordSets&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZones

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockDevicesMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapacityUnit

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuCredits

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredCapacity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrainingTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsOptimized

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticIps

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticLoadBalancers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableMonitoring

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FallbackToOndemand

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckGracePeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckUnhealthyDurationBeforeReplacement

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamInstanceProfile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTypesOndemand

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTypesPreferredSpot

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTypesSpot

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifetimePeriod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OndemandCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Orientation

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

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredAvailabilityZones

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIps

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Product

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroups

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShutdownScript

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotPercentage

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroupArns

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UtilizeReservedInstances

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForCapacity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForCapacityTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsBlockDevice

_Required_: No

_Type_: List of &lt;a href=&#34;ebsblockdevice.md&#34;&gt;EbsBlockDevice&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EphemeralBlockDevice

_Required_: No

_Type_: List of &lt;a href=&#34;ephemeralblockdevice.md&#34;&gt;EphemeralBlockDevice&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTypesWeights

_Required_: No

_Type_: List of &lt;a href=&#34;instancetypesweights.md&#34;&gt;InstanceTypesWeights&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationBeanstalk

_Required_: No

_Type_: List of &lt;a href=&#34;integrationbeanstalk.md&#34;&gt;IntegrationBeanstalk&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationCodedeploy

_Required_: No

_Type_: List of &lt;a href=&#34;integrationcodedeploy.md&#34;&gt;IntegrationCodedeploy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationDockerSwarm

_Required_: No

_Type_: List of &lt;a href=&#34;integrationdockerswarm.md&#34;&gt;IntegrationDockerSwarm&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationEcs

_Required_: No

_Type_: List of &lt;a href=&#34;integrationecs.md&#34;&gt;IntegrationEcs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationGitlab

_Required_: No

_Type_: List of &lt;a href=&#34;integrationgitlab.md&#34;&gt;IntegrationGitlab&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationKubernetes

_Required_: No

_Type_: List of &lt;a href=&#34;integrationkubernetes.md&#34;&gt;IntegrationKubernetes&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationMesosphere

_Required_: No

_Type_: List of &lt;a href=&#34;integrationmesosphere.md&#34;&gt;IntegrationMesosphere&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationMultaiRuntime

_Required_: No

_Type_: List of &lt;a href=&#34;integrationmultairuntime.md&#34;&gt;IntegrationMultaiRuntime&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationNomad

_Required_: No

_Type_: List of &lt;a href=&#34;integrationnomad.md&#34;&gt;IntegrationNomad&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationRancher

_Required_: No

_Type_: List of &lt;a href=&#34;integrationrancher.md&#34;&gt;IntegrationRancher&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationRoute53

_Required_: No

_Type_: List of &lt;a href=&#34;integrationroute53.md&#34;&gt;IntegrationRoute53&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultaiTargetSets

_Required_: No

_Type_: List of &lt;a href=&#34;multaitargetsets.md&#34;&gt;MultaiTargetSets&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterface

_Required_: No

_Type_: List of &lt;a href=&#34;networkinterface.md&#34;&gt;NetworkInterface&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RevertToSpot

_Required_: No

_Type_: List of &lt;a href=&#34;reverttospot.md&#34;&gt;RevertToSpot&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingDownPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;scalingdownpolicy.md&#34;&gt;ScalingDownPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingStrategy

_Required_: No

_Type_: List of &lt;a href=&#34;scalingstrategy.md&#34;&gt;ScalingStrategy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingTargetPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;scalingtargetpolicy.md&#34;&gt;ScalingTargetPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingUpPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;scalinguppolicy.md&#34;&gt;ScalingUpPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduledTask

_Required_: No

_Type_: List of &lt;a href=&#34;scheduledtask.md&#34;&gt;ScheduledTask&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Signal

_Required_: No

_Type_: List of &lt;a href=&#34;signal.md&#34;&gt;Signal&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatefulDeallocation

_Required_: No

_Type_: List of &lt;a href=&#34;statefuldeallocation.md&#34;&gt;StatefulDeallocation&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdatePolicy

_Required_: No

_Type_: List of &lt;a href=&#34;updatepolicy.md&#34;&gt;UpdatePolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentPreferences

_Required_: No

_Type_: List of &lt;a href=&#34;deploymentpreferences.md&#34;&gt;DeploymentPreferences&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedActions

_Required_: No

_Type_: List of &lt;a href=&#34;managedactions.md&#34;&gt;ManagedActions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentGroups

_Required_: No

_Type_: List of &lt;a href=&#34;deploymentgroups.md&#34;&gt;DeploymentGroups&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleDown

_Required_: No

_Type_: List of &lt;a href=&#34;autoscaledown.md&#34;&gt;AutoscaleDown&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleHeadroom

_Required_: No

_Type_: List of &lt;a href=&#34;autoscaleheadroom.md&#34;&gt;AutoscaleHeadroom&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleAttributes

_Required_: No

_Type_: List of &lt;a href=&#34;autoscaleattributes.md&#34;&gt;AutoscaleAttributes&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Runner

_Required_: No

_Type_: List of &lt;a href=&#34;runner.md&#34;&gt;Runner&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleLabels

_Required_: No

_Type_: List of &lt;a href=&#34;autoscalelabels.md&#34;&gt;AutoscaleLabels&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleConstraints

_Required_: No

_Type_: List of &lt;a href=&#34;autoscaleconstraints.md&#34;&gt;AutoscaleConstraints&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domains

_Required_: No

_Type_: List of &lt;a href=&#34;domains.md&#34;&gt;Domains&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dimensions

_Required_: No

_Type_: List of &lt;a href=&#34;dimensions.md&#34;&gt;Dimensions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RollConfig

_Required_: No

_Type_: List of &lt;a href=&#34;rollconfig.md&#34;&gt;RollConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Strategy

_Required_: No

_Type_: List of &lt;a href=&#34;strategy.md&#34;&gt;Strategy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlatformUpdate

_Required_: No

_Type_: List of &lt;a href=&#34;platformupdate.md&#34;&gt;PlatformUpdate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecordSets

_Required_: No

_Type_: List of &lt;a href=&#34;recordsets.md&#34;&gt;RecordSets&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

