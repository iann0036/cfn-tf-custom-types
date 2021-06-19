# TF::AWS::CodedeployDeploymentConfig

Provides a CodeDeploy deployment config for an application

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::CodedeployDeploymentConfig",
    "Properties" : {
        "<a href="#computeplatform" title="ComputePlatform">ComputePlatform</a>" : <i>String</i>,
        "<a href="#deploymentconfigname" title="DeploymentConfigName">DeploymentConfigName</a>" : <i>String</i>,
        "<a href="#minimumhealthyhosts" title="MinimumHealthyHosts">MinimumHealthyHosts</a>" : <i>[ <a href="minimumhealthyhostsdefinition.md">MinimumHealthyHostsDefinition</a>, ... ]</i>,
        "<a href="#trafficroutingconfig" title="TrafficRoutingConfig">TrafficRoutingConfig</a>" : <i>[ <a href="trafficroutingconfigdefinition.md">TrafficRoutingConfigDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::CodedeployDeploymentConfig
Properties:
    <a href="#computeplatform" title="ComputePlatform">ComputePlatform</a>: <i>String</i>
    <a href="#deploymentconfigname" title="DeploymentConfigName">DeploymentConfigName</a>: <i>String</i>
    <a href="#minimumhealthyhosts" title="MinimumHealthyHosts">MinimumHealthyHosts</a>: <i>
      - <a href="minimumhealthyhostsdefinition.md">MinimumHealthyHostsDefinition</a></i>
    <a href="#trafficroutingconfig" title="TrafficRoutingConfig">TrafficRoutingConfig</a>: <i>
      - <a href="trafficroutingconfigdefinition.md">TrafficRoutingConfigDefinition</a></i>
</pre>

## Properties

#### ComputePlatform

The compute platform can be `Server`, `Lambda`, or `ECS`. Default is `Server`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentConfigName

The name of the deployment config.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinimumHealthyHosts

_Required_: No

_Type_: List of <a href="minimumhealthyhostsdefinition.md">MinimumHealthyHostsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficRoutingConfig

_Required_: No

_Type_: List of <a href="trafficroutingconfigdefinition.md">TrafficRoutingConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DeploymentConfigId

Returns the <code>DeploymentConfigId</code> value.

#### Id

Returns the <code>Id</code> value.

