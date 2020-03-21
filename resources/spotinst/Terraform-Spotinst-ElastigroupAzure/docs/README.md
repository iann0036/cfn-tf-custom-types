# Terraform::Spotinst::ElastigroupAzure

CloudFormation equivalent of spotinst_elastigroup_azure

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Spotinst::ElastigroupAzure",
    "Properties" : {
        "<a href="#customdata" title="CustomData">CustomData</a>" : <i>String</i>,
        "<a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>" : <i>Double</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#lowprioritysizes" title="LowPrioritySizes">LowPrioritySizes</a>" : <i>[ String, ... ]</i>,
        "<a href="#maxsize" title="MaxSize">MaxSize</a>" : <i>Double</i>,
        "<a href="#minsize" title="MinSize">MinSize</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#odsizes" title="OdSizes">OdSizes</a>" : <i>[ String, ... ]</i>,
        "<a href="#product" title="Product">Product</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#shutdownscript" title="ShutdownScript">ShutdownScript</a>" : <i>String</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#healthcheck" title="HealthCheck">HealthCheck</a>" : <i>[ &lt;a href=&#34;healthcheck.md&#34;&gt;HealthCheck&lt;/a&gt;, ... ]</i>,
        "<a href="#image" title="Image">Image</a>" : <i>[ &lt;a href=&#34;image.md&#34;&gt;Image&lt;/a&gt;, ... ]</i>,
        "<a href="#integrationkubernetes" title="IntegrationKubernetes">IntegrationKubernetes</a>" : <i>[ &lt;a href=&#34;integrationkubernetes.md&#34;&gt;IntegrationKubernetes&lt;/a&gt;, ... ]</i>,
        "<a href="#integrationmultairuntime" title="IntegrationMultaiRuntime">IntegrationMultaiRuntime</a>" : <i>[ &lt;a href=&#34;integrationmultairuntime.md&#34;&gt;IntegrationMultaiRuntime&lt;/a&gt;, ... ]</i>,
        "<a href="#loadbalancers" title="LoadBalancers">LoadBalancers</a>" : <i>[ &lt;a href=&#34;loadbalancers.md&#34;&gt;LoadBalancers&lt;/a&gt;, ... ]</i>,
        "<a href="#login" title="Login">Login</a>" : <i>[ &lt;a href=&#34;login.md&#34;&gt;Login&lt;/a&gt;, ... ]</i>,
        "<a href="#managedserviceidentities" title="ManagedServiceIdentities">ManagedServiceIdentities</a>" : <i>[ &lt;a href=&#34;managedserviceidentities.md&#34;&gt;ManagedServiceIdentities&lt;/a&gt;, ... ]</i>,
        "<a href="#network" title="Network">Network</a>" : <i>[ &lt;a href=&#34;network.md&#34;&gt;Network&lt;/a&gt;, ... ]</i>,
        "<a href="#scalingdownpolicy" title="ScalingDownPolicy">ScalingDownPolicy</a>" : <i>[ &lt;a href=&#34;scalingdownpolicy.md&#34;&gt;ScalingDownPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#scalinguppolicy" title="ScalingUpPolicy">ScalingUpPolicy</a>" : <i>[ &lt;a href=&#34;scalinguppolicy.md&#34;&gt;ScalingUpPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#scheduledtask" title="ScheduledTask">ScheduledTask</a>" : <i>[ &lt;a href=&#34;scheduledtask.md&#34;&gt;ScheduledTask&lt;/a&gt;, ... ]</i>,
        "<a href="#strategy" title="Strategy">Strategy</a>" : <i>[ &lt;a href=&#34;strategy.md&#34;&gt;Strategy&lt;/a&gt;, ... ]</i>,
        "<a href="#updatepolicy" title="UpdatePolicy">UpdatePolicy</a>" : <i>[ &lt;a href=&#34;updatepolicy.md&#34;&gt;UpdatePolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#custom" title="Custom">Custom</a>" : <i>[ &lt;a href=&#34;custom.md&#34;&gt;Custom&lt;/a&gt;, ... ]</i>,
        "<a href="#marketplace" title="Marketplace">Marketplace</a>" : <i>[ &lt;a href=&#34;marketplace.md&#34;&gt;Marketplace&lt;/a&gt;, ... ]</i>,
        "<a href="#additionalipconfigs" title="AdditionalIpConfigs">AdditionalIpConfigs</a>" : <i>[ &lt;a href=&#34;additionalipconfigs.md&#34;&gt;AdditionalIpConfigs&lt;/a&gt;, ... ]</i>,
        "<a href="#dimensions" title="Dimensions">Dimensions</a>" : <i>[ &lt;a href=&#34;dimensions.md&#34;&gt;Dimensions&lt;/a&gt;, ... ]</i>,
        "<a href="#rollconfig" title="RollConfig">RollConfig</a>" : <i>[ &lt;a href=&#34;rollconfig.md&#34;&gt;RollConfig&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Spotinst::ElastigroupAzure
Properties:
    <a href="#customdata" title="CustomData">CustomData</a>: <i>String</i>
    <a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>: <i>Double</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#lowprioritysizes" title="LowPrioritySizes">LowPrioritySizes</a>: <i>
      - String</i>
    <a href="#maxsize" title="MaxSize">MaxSize</a>: <i>Double</i>
    <a href="#minsize" title="MinSize">MinSize</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#odsizes" title="OdSizes">OdSizes</a>: <i>
      - String</i>
    <a href="#product" title="Product">Product</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#shutdownscript" title="ShutdownScript">ShutdownScript</a>: <i>String</i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#healthcheck" title="HealthCheck">HealthCheck</a>: <i>
      - &lt;a href=&#34;healthcheck.md&#34;&gt;HealthCheck&lt;/a&gt;</i>
    <a href="#image" title="Image">Image</a>: <i>
      - &lt;a href=&#34;image.md&#34;&gt;Image&lt;/a&gt;</i>
    <a href="#integrationkubernetes" title="IntegrationKubernetes">IntegrationKubernetes</a>: <i>
      - &lt;a href=&#34;integrationkubernetes.md&#34;&gt;IntegrationKubernetes&lt;/a&gt;</i>
    <a href="#integrationmultairuntime" title="IntegrationMultaiRuntime">IntegrationMultaiRuntime</a>: <i>
      - &lt;a href=&#34;integrationmultairuntime.md&#34;&gt;IntegrationMultaiRuntime&lt;/a&gt;</i>
    <a href="#loadbalancers" title="LoadBalancers">LoadBalancers</a>: <i>
      - &lt;a href=&#34;loadbalancers.md&#34;&gt;LoadBalancers&lt;/a&gt;</i>
    <a href="#login" title="Login">Login</a>: <i>
      - &lt;a href=&#34;login.md&#34;&gt;Login&lt;/a&gt;</i>
    <a href="#managedserviceidentities" title="ManagedServiceIdentities">ManagedServiceIdentities</a>: <i>
      - &lt;a href=&#34;managedserviceidentities.md&#34;&gt;ManagedServiceIdentities&lt;/a&gt;</i>
    <a href="#network" title="Network">Network</a>: <i>
      - &lt;a href=&#34;network.md&#34;&gt;Network&lt;/a&gt;</i>
    <a href="#scalingdownpolicy" title="ScalingDownPolicy">ScalingDownPolicy</a>: <i>
      - &lt;a href=&#34;scalingdownpolicy.md&#34;&gt;ScalingDownPolicy&lt;/a&gt;</i>
    <a href="#scalinguppolicy" title="ScalingUpPolicy">ScalingUpPolicy</a>: <i>
      - &lt;a href=&#34;scalinguppolicy.md&#34;&gt;ScalingUpPolicy&lt;/a&gt;</i>
    <a href="#scheduledtask" title="ScheduledTask">ScheduledTask</a>: <i>
      - &lt;a href=&#34;scheduledtask.md&#34;&gt;ScheduledTask&lt;/a&gt;</i>
    <a href="#strategy" title="Strategy">Strategy</a>: <i>
      - &lt;a href=&#34;strategy.md&#34;&gt;Strategy&lt;/a&gt;</i>
    <a href="#updatepolicy" title="UpdatePolicy">UpdatePolicy</a>: <i>
      - &lt;a href=&#34;updatepolicy.md&#34;&gt;UpdatePolicy&lt;/a&gt;</i>
    <a href="#custom" title="Custom">Custom</a>: <i>
      - &lt;a href=&#34;custom.md&#34;&gt;Custom&lt;/a&gt;</i>
    <a href="#marketplace" title="Marketplace">Marketplace</a>: <i>
      - &lt;a href=&#34;marketplace.md&#34;&gt;Marketplace&lt;/a&gt;</i>
    <a href="#additionalipconfigs" title="AdditionalIpConfigs">AdditionalIpConfigs</a>: <i>
      - &lt;a href=&#34;additionalipconfigs.md&#34;&gt;AdditionalIpConfigs&lt;/a&gt;</i>
    <a href="#dimensions" title="Dimensions">Dimensions</a>: <i>
      - &lt;a href=&#34;dimensions.md&#34;&gt;Dimensions&lt;/a&gt;</i>
    <a href="#rollconfig" title="RollConfig">RollConfig</a>: <i>
      - &lt;a href=&#34;rollconfig.md&#34;&gt;RollConfig&lt;/a&gt;</i>
</pre>

## Properties

#### CustomData

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredCapacity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LowPrioritySizes

_Required_: Yes

_Type_: List of String

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

#### OdSizes

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Product

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShutdownScript

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheck

_Required_: No

_Type_: List of &lt;a href=&#34;healthcheck.md&#34;&gt;HealthCheck&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

_Required_: No

_Type_: List of &lt;a href=&#34;image.md&#34;&gt;Image&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationKubernetes

_Required_: No

_Type_: List of &lt;a href=&#34;integrationkubernetes.md&#34;&gt;IntegrationKubernetes&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationMultaiRuntime

_Required_: No

_Type_: List of &lt;a href=&#34;integrationmultairuntime.md&#34;&gt;IntegrationMultaiRuntime&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancers

_Required_: No

_Type_: List of &lt;a href=&#34;loadbalancers.md&#34;&gt;LoadBalancers&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Login

_Required_: No

_Type_: List of &lt;a href=&#34;login.md&#34;&gt;Login&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedServiceIdentities

_Required_: No

_Type_: List of &lt;a href=&#34;managedserviceidentities.md&#34;&gt;ManagedServiceIdentities&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: List of &lt;a href=&#34;network.md&#34;&gt;Network&lt;/a&gt;

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

#### Strategy

_Required_: No

_Type_: List of &lt;a href=&#34;strategy.md&#34;&gt;Strategy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdatePolicy

_Required_: No

_Type_: List of &lt;a href=&#34;updatepolicy.md&#34;&gt;UpdatePolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Custom

_Required_: No

_Type_: List of &lt;a href=&#34;custom.md&#34;&gt;Custom&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Marketplace

_Required_: No

_Type_: List of &lt;a href=&#34;marketplace.md&#34;&gt;Marketplace&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalIpConfigs

_Required_: No

_Type_: List of &lt;a href=&#34;additionalipconfigs.md&#34;&gt;AdditionalIpConfigs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dimensions

_Required_: No

_Type_: List of &lt;a href=&#34;dimensions.md&#34;&gt;Dimensions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RollConfig

_Required_: No

_Type_: List of &lt;a href=&#34;rollconfig.md&#34;&gt;RollConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

