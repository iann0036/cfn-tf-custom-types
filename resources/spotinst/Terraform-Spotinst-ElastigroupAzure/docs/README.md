# Terraform::Spotinst::ElastigroupAzure

Provides a Spotinst elastigroup Azure resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Spotinst::ElastigroupAzure",
    "Properties" : {
        "<a href="#customdata" title="CustomData">CustomData</a>" : <i>String</i>,
        "<a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>" : <i>Double</i>,
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
        "<a href="#healthcheck" title="HealthCheck">HealthCheck</a>" : <i>[ <a href="healthcheck.md">HealthCheck</a>, ... ]</i>,
        "<a href="#image" title="Image">Image</a>" : <i>[ <a href="image.md">Image</a>, ... ]</i>,
        "<a href="#integrationkubernetes" title="IntegrationKubernetes">IntegrationKubernetes</a>" : <i>[ <a href="integrationkubernetes.md">IntegrationKubernetes</a>, ... ]</i>,
        "<a href="#integrationmultairuntime" title="IntegrationMultaiRuntime">IntegrationMultaiRuntime</a>" : <i>[ <a href="integrationmultairuntime.md">IntegrationMultaiRuntime</a>, ... ]</i>,
        "<a href="#loadbalancers" title="LoadBalancers">LoadBalancers</a>" : <i>[ <a href="loadbalancers.md">LoadBalancers</a>, ... ]</i>,
        "<a href="#login" title="Login">Login</a>" : <i>[ <a href="login.md">Login</a>, ... ]</i>,
        "<a href="#managedserviceidentities" title="ManagedServiceIdentities">ManagedServiceIdentities</a>" : <i>[ <a href="managedserviceidentities.md">ManagedServiceIdentities</a>, ... ]</i>,
        "<a href="#network" title="Network">Network</a>" : <i>[ <a href="network.md">Network</a>, ... ]</i>,
        "<a href="#scalingdownpolicy" title="ScalingDownPolicy">ScalingDownPolicy</a>" : <i>[ <a href="scalingdownpolicy.md">ScalingDownPolicy</a>, ... ]</i>,
        "<a href="#scalinguppolicy" title="ScalingUpPolicy">ScalingUpPolicy</a>" : <i>[ <a href="scalinguppolicy.md">ScalingUpPolicy</a>, ... ]</i>,
        "<a href="#scheduledtask" title="ScheduledTask">ScheduledTask</a>" : <i>[ <a href="scheduledtask.md">ScheduledTask</a>, ... ]</i>,
        "<a href="#strategy" title="Strategy">Strategy</a>" : <i>[ <a href="strategy.md">Strategy</a>, ... ]</i>,
        "<a href="#updatepolicy" title="UpdatePolicy">UpdatePolicy</a>" : <i>[ <a href="updatepolicy.md">UpdatePolicy</a>, ... ]</i>,
        "<a href="#custom" title="Custom">Custom</a>" : <i>[ <a href="custom.md">Custom</a>, ... ]</i>,
        "<a href="#marketplace" title="Marketplace">Marketplace</a>" : <i>[ <a href="marketplace.md">Marketplace</a>, ... ]</i>,
        "<a href="#additionalipconfigs" title="AdditionalIpConfigs">AdditionalIpConfigs</a>" : <i>[ <a href="additionalipconfigs.md">AdditionalIpConfigs</a>, ... ]</i>,
        "<a href="#dimensions" title="Dimensions">Dimensions</a>" : <i>[ <a href="dimensions.md">Dimensions</a>, ... ]</i>,
        "<a href="#rollconfig" title="RollConfig">RollConfig</a>" : <i>[ <a href="rollconfig.md">RollConfig</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Spotinst::ElastigroupAzure
Properties:
    <a href="#customdata" title="CustomData">CustomData</a>: <i>String</i>
    <a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>: <i>Double</i>
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
      - <a href="healthcheck.md">HealthCheck</a></i>
    <a href="#image" title="Image">Image</a>: <i>
      - <a href="image.md">Image</a></i>
    <a href="#integrationkubernetes" title="IntegrationKubernetes">IntegrationKubernetes</a>: <i>
      - <a href="integrationkubernetes.md">IntegrationKubernetes</a></i>
    <a href="#integrationmultairuntime" title="IntegrationMultaiRuntime">IntegrationMultaiRuntime</a>: <i>
      - <a href="integrationmultairuntime.md">IntegrationMultaiRuntime</a></i>
    <a href="#loadbalancers" title="LoadBalancers">LoadBalancers</a>: <i>
      - <a href="loadbalancers.md">LoadBalancers</a></i>
    <a href="#login" title="Login">Login</a>: <i>
      - <a href="login.md">Login</a></i>
    <a href="#managedserviceidentities" title="ManagedServiceIdentities">ManagedServiceIdentities</a>: <i>
      - <a href="managedserviceidentities.md">ManagedServiceIdentities</a></i>
    <a href="#network" title="Network">Network</a>: <i>
      - <a href="network.md">Network</a></i>
    <a href="#scalingdownpolicy" title="ScalingDownPolicy">ScalingDownPolicy</a>: <i>
      - <a href="scalingdownpolicy.md">ScalingDownPolicy</a></i>
    <a href="#scalinguppolicy" title="ScalingUpPolicy">ScalingUpPolicy</a>: <i>
      - <a href="scalinguppolicy.md">ScalingUpPolicy</a></i>
    <a href="#scheduledtask" title="ScheduledTask">ScheduledTask</a>: <i>
      - <a href="scheduledtask.md">ScheduledTask</a></i>
    <a href="#strategy" title="Strategy">Strategy</a>: <i>
      - <a href="strategy.md">Strategy</a></i>
    <a href="#updatepolicy" title="UpdatePolicy">UpdatePolicy</a>: <i>
      - <a href="updatepolicy.md">UpdatePolicy</a></i>
    <a href="#custom" title="Custom">Custom</a>: <i>
      - <a href="custom.md">Custom</a></i>
    <a href="#marketplace" title="Marketplace">Marketplace</a>: <i>
      - <a href="marketplace.md">Marketplace</a></i>
    <a href="#additionalipconfigs" title="AdditionalIpConfigs">AdditionalIpConfigs</a>: <i>
      - <a href="additionalipconfigs.md">AdditionalIpConfigs</a></i>
    <a href="#dimensions" title="Dimensions">Dimensions</a>: <i>
      - <a href="dimensions.md">Dimensions</a></i>
    <a href="#rollconfig" title="RollConfig">RollConfig</a>: <i>
      - <a href="rollconfig.md">RollConfig</a></i>
</pre>

## Properties

#### CustomData

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredCapacity

The desired number of instances the group should have at any time.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LowPrioritySizes

Available Low-Priority sizes.

_Required_: Yes

_Type_: List of String

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

#### Name

The name of the managed identity.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OdSizes

Available On-Demand sizes.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Product

Operation system type. Valid values: `"Linux"`, `"Windows"`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region your Azure group will be created in.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The Resource Group that the user-assigned managed identity resides in.
* `name` - (Required) The name of the managed identity.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShutdownScript

Shutdown script for the group. Value should be passed as a string encoded at Base64 only.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

Base64-encoded MIME user data to make available to the instances.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheck

_Required_: No

_Type_: List of <a href="healthcheck.md">HealthCheck</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

_Required_: No

_Type_: List of <a href="image.md">Image</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationKubernetes

_Required_: No

_Type_: List of <a href="integrationkubernetes.md">IntegrationKubernetes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationMultaiRuntime

_Required_: No

_Type_: List of <a href="integrationmultairuntime.md">IntegrationMultaiRuntime</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancers

_Required_: No

_Type_: List of <a href="loadbalancers.md">LoadBalancers</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Login

_Required_: No

_Type_: List of <a href="login.md">Login</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedServiceIdentities

_Required_: No

_Type_: List of <a href="managedserviceidentities.md">ManagedServiceIdentities</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: List of <a href="network.md">Network</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingDownPolicy

_Required_: No

_Type_: List of <a href="scalingdownpolicy.md">ScalingDownPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingUpPolicy

_Required_: No

_Type_: List of <a href="scalinguppolicy.md">ScalingUpPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduledTask

_Required_: No

_Type_: List of <a href="scheduledtask.md">ScheduledTask</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Strategy

_Required_: No

_Type_: List of <a href="strategy.md">Strategy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdatePolicy

_Required_: No

_Type_: List of <a href="updatepolicy.md">UpdatePolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Custom

_Required_: No

_Type_: List of <a href="custom.md">Custom</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Marketplace

_Required_: No

_Type_: List of <a href="marketplace.md">Marketplace</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalIpConfigs

_Required_: No

_Type_: List of <a href="additionalipconfigs.md">AdditionalIpConfigs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dimensions

_Required_: No

_Type_: List of <a href="dimensions.md">Dimensions</a>

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

