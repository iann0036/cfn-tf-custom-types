# Terraform::Spotinst::ElastigroupGcp

CloudFormation equivalent of spotinst_elastigroup_gcp

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Spotinst::ElastigroupGcp",
    "Properties" : {
        "<a href="#autohealing" title="AutoHealing">AutoHealing</a>" : <i>Boolean</i>,
        "<a href="#availabilityzones" title="AvailabilityZones">AvailabilityZones</a>" : <i>[ String, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>" : <i>Double</i>,
        "<a href="#drainingtimeout" title="DrainingTimeout">DrainingTimeout</a>" : <i>Double</i>,
        "<a href="#fallbacktoondemand" title="FallbackToOndemand">FallbackToOndemand</a>" : <i>Boolean</i>,
        "<a href="#healthcheckgraceperiod" title="HealthCheckGracePeriod">HealthCheckGracePeriod</a>" : <i>Double</i>,
        "<a href="#healthchecktype" title="HealthCheckType">HealthCheckType</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#instancetypesondemand" title="InstanceTypesOndemand">InstanceTypesOndemand</a>" : <i>String</i>,
        "<a href="#instancetypespreemptible" title="InstanceTypesPreemptible">InstanceTypesPreemptible</a>" : <i>[ String, ... ]</i>,
        "<a href="#ipforwarding" title="IpForwarding">IpForwarding</a>" : <i>Boolean</i>,
        "<a href="#maxsize" title="MaxSize">MaxSize</a>" : <i>Double</i>,
        "<a href="#minsize" title="MinSize">MinSize</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ondemandcount" title="OndemandCount">OndemandCount</a>" : <i>Double</i>,
        "<a href="#preemptiblepercentage" title="PreemptiblePercentage">PreemptiblePercentage</a>" : <i>Double</i>,
        "<a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>" : <i>String</i>,
        "<a href="#shutdownscript" title="ShutdownScript">ShutdownScript</a>" : <i>String</i>,
        "<a href="#startupscript" title="StartupScript">StartupScript</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#unhealthyduration" title="UnhealthyDuration">UnhealthyDuration</a>" : <i>Double</i>,
        "<a href="#backendservices" title="BackendServices">BackendServices</a>" : <i>[ &lt;a href=&#34;backendservices.md&#34;&gt;BackendServices&lt;/a&gt;, ... ]</i>,
        "<a href="#disk" title="Disk">Disk</a>" : <i>[ &lt;a href=&#34;disk.md&#34;&gt;Disk&lt;/a&gt;, ... ]</i>,
        "<a href="#gpu" title="Gpu">Gpu</a>" : <i>[ &lt;a href=&#34;gpu.md&#34;&gt;Gpu&lt;/a&gt;, ... ]</i>,
        "<a href="#instancetypescustom" title="InstanceTypesCustom">InstanceTypesCustom</a>" : <i>[ &lt;a href=&#34;instancetypescustom.md&#34;&gt;InstanceTypesCustom&lt;/a&gt;, ... ]</i>,
        "<a href="#integrationdockerswarm" title="IntegrationDockerSwarm">IntegrationDockerSwarm</a>" : <i>[ &lt;a href=&#34;integrationdockerswarm.md&#34;&gt;IntegrationDockerSwarm&lt;/a&gt;, ... ]</i>,
        "<a href="#integrationgke" title="IntegrationGke">IntegrationGke</a>" : <i>[ &lt;a href=&#34;integrationgke.md&#34;&gt;IntegrationGke&lt;/a&gt;, ... ]</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;, ... ]</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;, ... ]</i>,
        "<a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>" : <i>[ &lt;a href=&#34;networkinterface.md&#34;&gt;NetworkInterface&lt;/a&gt;, ... ]</i>,
        "<a href="#scalingdownpolicy" title="ScalingDownPolicy">ScalingDownPolicy</a>" : <i>[ &lt;a href=&#34;scalingdownpolicy.md&#34;&gt;ScalingDownPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#scalinguppolicy" title="ScalingUpPolicy">ScalingUpPolicy</a>" : <i>[ &lt;a href=&#34;scalinguppolicy.md&#34;&gt;ScalingUpPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#scheduledtask" title="ScheduledTask">ScheduledTask</a>" : <i>[ &lt;a href=&#34;scheduledtask.md&#34;&gt;ScheduledTask&lt;/a&gt;, ... ]</i>,
        "<a href="#subnets" title="Subnets">Subnets</a>" : <i>[ &lt;a href=&#34;subnets.md&#34;&gt;Subnets&lt;/a&gt;, ... ]</i>,
        "<a href="#namedports" title="NamedPorts">NamedPorts</a>" : <i>[ &lt;a href=&#34;namedports.md&#34;&gt;NamedPorts&lt;/a&gt;, ... ]</i>,
        "<a href="#initializeparams" title="InitializeParams">InitializeParams</a>" : <i>[ &lt;a href=&#34;initializeparams.md&#34;&gt;InitializeParams&lt;/a&gt;, ... ]</i>,
        "<a href="#autoscaledown" title="AutoscaleDown">AutoscaleDown</a>" : <i>[ &lt;a href=&#34;autoscaledown.md&#34;&gt;AutoscaleDown&lt;/a&gt;, ... ]</i>,
        "<a href="#autoscaleheadroom" title="AutoscaleHeadroom">AutoscaleHeadroom</a>" : <i>[ &lt;a href=&#34;autoscaleheadroom.md&#34;&gt;AutoscaleHeadroom&lt;/a&gt;, ... ]</i>,
        "<a href="#autoscalelabels" title="AutoscaleLabels">AutoscaleLabels</a>" : <i>[ &lt;a href=&#34;autoscalelabels.md&#34;&gt;AutoscaleLabels&lt;/a&gt;, ... ]</i>,
        "<a href="#accessconfigs" title="AccessConfigs">AccessConfigs</a>" : <i>[ &lt;a href=&#34;accessconfigs.md&#34;&gt;AccessConfigs&lt;/a&gt;, ... ]</i>,
        "<a href="#aliasipranges" title="AliasIpRanges">AliasIpRanges</a>" : <i>[ &lt;a href=&#34;aliasipranges.md&#34;&gt;AliasIpRanges&lt;/a&gt;, ... ]</i>,
        "<a href="#dimensions" title="Dimensions">Dimensions</a>" : <i>[ &lt;a href=&#34;dimensions.md&#34;&gt;Dimensions&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Spotinst::ElastigroupGcp
Properties:
    <a href="#autohealing" title="AutoHealing">AutoHealing</a>: <i>Boolean</i>
    <a href="#availabilityzones" title="AvailabilityZones">AvailabilityZones</a>: <i>
      - String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>: <i>Double</i>
    <a href="#drainingtimeout" title="DrainingTimeout">DrainingTimeout</a>: <i>Double</i>
    <a href="#fallbacktoondemand" title="FallbackToOndemand">FallbackToOndemand</a>: <i>Boolean</i>
    <a href="#healthcheckgraceperiod" title="HealthCheckGracePeriod">HealthCheckGracePeriod</a>: <i>Double</i>
    <a href="#healthchecktype" title="HealthCheckType">HealthCheckType</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#instancetypesondemand" title="InstanceTypesOndemand">InstanceTypesOndemand</a>: <i>String</i>
    <a href="#instancetypespreemptible" title="InstanceTypesPreemptible">InstanceTypesPreemptible</a>: <i>
      - String</i>
    <a href="#ipforwarding" title="IpForwarding">IpForwarding</a>: <i>Boolean</i>
    <a href="#maxsize" title="MaxSize">MaxSize</a>: <i>Double</i>
    <a href="#minsize" title="MinSize">MinSize</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ondemandcount" title="OndemandCount">OndemandCount</a>: <i>Double</i>
    <a href="#preemptiblepercentage" title="PreemptiblePercentage">PreemptiblePercentage</a>: <i>Double</i>
    <a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>: <i>String</i>
    <a href="#shutdownscript" title="ShutdownScript">ShutdownScript</a>: <i>String</i>
    <a href="#startupscript" title="StartupScript">StartupScript</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#unhealthyduration" title="UnhealthyDuration">UnhealthyDuration</a>: <i>Double</i>
    <a href="#backendservices" title="BackendServices">BackendServices</a>: <i>
      - &lt;a href=&#34;backendservices.md&#34;&gt;BackendServices&lt;/a&gt;</i>
    <a href="#disk" title="Disk">Disk</a>: <i>
      - &lt;a href=&#34;disk.md&#34;&gt;Disk&lt;/a&gt;</i>
    <a href="#gpu" title="Gpu">Gpu</a>: <i>
      - &lt;a href=&#34;gpu.md&#34;&gt;Gpu&lt;/a&gt;</i>
    <a href="#instancetypescustom" title="InstanceTypesCustom">InstanceTypesCustom</a>: <i>
      - &lt;a href=&#34;instancetypescustom.md&#34;&gt;InstanceTypesCustom&lt;/a&gt;</i>
    <a href="#integrationdockerswarm" title="IntegrationDockerSwarm">IntegrationDockerSwarm</a>: <i>
      - &lt;a href=&#34;integrationdockerswarm.md&#34;&gt;IntegrationDockerSwarm&lt;/a&gt;</i>
    <a href="#integrationgke" title="IntegrationGke">IntegrationGke</a>: <i>
      - &lt;a href=&#34;integrationgke.md&#34;&gt;IntegrationGke&lt;/a&gt;</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;</i>
    <a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>: <i>
      - &lt;a href=&#34;networkinterface.md&#34;&gt;NetworkInterface&lt;/a&gt;</i>
    <a href="#scalingdownpolicy" title="ScalingDownPolicy">ScalingDownPolicy</a>: <i>
      - &lt;a href=&#34;scalingdownpolicy.md&#34;&gt;ScalingDownPolicy&lt;/a&gt;</i>
    <a href="#scalinguppolicy" title="ScalingUpPolicy">ScalingUpPolicy</a>: <i>
      - &lt;a href=&#34;scalinguppolicy.md&#34;&gt;ScalingUpPolicy&lt;/a&gt;</i>
    <a href="#scheduledtask" title="ScheduledTask">ScheduledTask</a>: <i>
      - &lt;a href=&#34;scheduledtask.md&#34;&gt;ScheduledTask&lt;/a&gt;</i>
    <a href="#subnets" title="Subnets">Subnets</a>: <i>
      - &lt;a href=&#34;subnets.md&#34;&gt;Subnets&lt;/a&gt;</i>
    <a href="#namedports" title="NamedPorts">NamedPorts</a>: <i>
      - &lt;a href=&#34;namedports.md&#34;&gt;NamedPorts&lt;/a&gt;</i>
    <a href="#initializeparams" title="InitializeParams">InitializeParams</a>: <i>
      - &lt;a href=&#34;initializeparams.md&#34;&gt;InitializeParams&lt;/a&gt;</i>
    <a href="#autoscaledown" title="AutoscaleDown">AutoscaleDown</a>: <i>
      - &lt;a href=&#34;autoscaledown.md&#34;&gt;AutoscaleDown&lt;/a&gt;</i>
    <a href="#autoscaleheadroom" title="AutoscaleHeadroom">AutoscaleHeadroom</a>: <i>
      - &lt;a href=&#34;autoscaleheadroom.md&#34;&gt;AutoscaleHeadroom&lt;/a&gt;</i>
    <a href="#autoscalelabels" title="AutoscaleLabels">AutoscaleLabels</a>: <i>
      - &lt;a href=&#34;autoscalelabels.md&#34;&gt;AutoscaleLabels&lt;/a&gt;</i>
    <a href="#accessconfigs" title="AccessConfigs">AccessConfigs</a>: <i>
      - &lt;a href=&#34;accessconfigs.md&#34;&gt;AccessConfigs&lt;/a&gt;</i>
    <a href="#aliasipranges" title="AliasIpRanges">AliasIpRanges</a>: <i>
      - &lt;a href=&#34;aliasipranges.md&#34;&gt;AliasIpRanges&lt;/a&gt;</i>
    <a href="#dimensions" title="Dimensions">Dimensions</a>: <i>
      - &lt;a href=&#34;dimensions.md&#34;&gt;Dimensions&lt;/a&gt;</i>
</pre>

## Properties

#### AutoHealing

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZones

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredCapacity

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrainingTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FallbackToOndemand

_Required_: No

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

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTypesOndemand

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTypesPreemptible

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpForwarding

_Required_: No

_Type_: Boolean

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

#### PreemptiblePercentage

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccount

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShutdownScript

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartupScript

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnhealthyDuration

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackendServices

_Required_: No

_Type_: List of &lt;a href=&#34;backendservices.md&#34;&gt;BackendServices&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disk

_Required_: No

_Type_: List of &lt;a href=&#34;disk.md&#34;&gt;Disk&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gpu

_Required_: No

_Type_: List of &lt;a href=&#34;gpu.md&#34;&gt;Gpu&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTypesCustom

_Required_: No

_Type_: List of &lt;a href=&#34;instancetypescustom.md&#34;&gt;InstanceTypesCustom&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationDockerSwarm

_Required_: No

_Type_: List of &lt;a href=&#34;integrationdockerswarm.md&#34;&gt;IntegrationDockerSwarm&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationGke

_Required_: No

_Type_: List of &lt;a href=&#34;integrationgke.md&#34;&gt;IntegrationGke&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterface

_Required_: No

_Type_: List of &lt;a href=&#34;networkinterface.md&#34;&gt;NetworkInterface&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingDownPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;scalingdownpolicy.md&#34;&gt;ScalingDownPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingUpPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;scalinguppolicy.md&#34;&gt;ScalingUpPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduledTask

_Required_: No

_Type_: List of &lt;a href=&#34;scheduledtask.md&#34;&gt;ScheduledTask&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnets

_Required_: No

_Type_: List of &lt;a href=&#34;subnets.md&#34;&gt;Subnets&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamedPorts

_Required_: No

_Type_: List of &lt;a href=&#34;namedports.md&#34;&gt;NamedPorts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitializeParams

_Required_: No

_Type_: List of &lt;a href=&#34;initializeparams.md&#34;&gt;InitializeParams&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleDown

_Required_: No

_Type_: List of &lt;a href=&#34;autoscaledown.md&#34;&gt;AutoscaleDown&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleHeadroom

_Required_: No

_Type_: List of &lt;a href=&#34;autoscaleheadroom.md&#34;&gt;AutoscaleHeadroom&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleLabels

_Required_: No

_Type_: List of &lt;a href=&#34;autoscalelabels.md&#34;&gt;AutoscaleLabels&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessConfigs

_Required_: No

_Type_: List of &lt;a href=&#34;accessconfigs.md&#34;&gt;AccessConfigs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AliasIpRanges

_Required_: No

_Type_: List of &lt;a href=&#34;aliasipranges.md&#34;&gt;AliasIpRanges&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dimensions

_Required_: No

_Type_: List of &lt;a href=&#34;dimensions.md&#34;&gt;Dimensions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

