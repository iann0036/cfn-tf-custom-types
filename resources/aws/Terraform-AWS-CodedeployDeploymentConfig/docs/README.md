# Terraform::AWS::CodedeployDeploymentConfig

CloudFormation equivalent of aws_codedeploy_deployment_config

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::CodedeployDeploymentConfig",
    "Properties" : {
        "<a href="#computeplatform" title="ComputePlatform">ComputePlatform</a>" : <i>String</i>,
        "<a href="#deploymentconfigname" title="DeploymentConfigName">DeploymentConfigName</a>" : <i>String</i>,
        "<a href="#minimumhealthyhosts" title="MinimumHealthyHosts">MinimumHealthyHosts</a>" : <i>[ <a href="minimumhealthyhosts.md">MinimumHealthyHosts</a>, ... ]</i>,
        "<a href="#trafficroutingconfig" title="TrafficRoutingConfig">TrafficRoutingConfig</a>" : <i>[ <a href="trafficroutingconfig.md">TrafficRoutingConfig</a>, ... ]</i>,
        "<a href="#timebasedcanary" title="TimeBasedCanary">TimeBasedCanary</a>" : <i>[ <a href="timebasedcanary.md">TimeBasedCanary</a>, ... ]</i>,
        "<a href="#timebasedlinear" title="TimeBasedLinear">TimeBasedLinear</a>" : <i>[ <a href="timebasedlinear.md">TimeBasedLinear</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::CodedeployDeploymentConfig
Properties:
    <a href="#computeplatform" title="ComputePlatform">ComputePlatform</a>: <i>String</i>
    <a href="#deploymentconfigname" title="DeploymentConfigName">DeploymentConfigName</a>: <i>String</i>
    <a href="#minimumhealthyhosts" title="MinimumHealthyHosts">MinimumHealthyHosts</a>: <i>
      - <a href="minimumhealthyhosts.md">MinimumHealthyHosts</a></i>
    <a href="#trafficroutingconfig" title="TrafficRoutingConfig">TrafficRoutingConfig</a>: <i>
      - <a href="trafficroutingconfig.md">TrafficRoutingConfig</a></i>
    <a href="#timebasedcanary" title="TimeBasedCanary">TimeBasedCanary</a>: <i>
      - <a href="timebasedcanary.md">TimeBasedCanary</a></i>
    <a href="#timebasedlinear" title="TimeBasedLinear">TimeBasedLinear</a>: <i>
      - <a href="timebasedlinear.md">TimeBasedLinear</a></i>
</pre>

## Properties

#### ComputePlatform

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentConfigName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinimumHealthyHosts

_Required_: No

_Type_: List of <a href="minimumhealthyhosts.md">MinimumHealthyHosts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficRoutingConfig

_Required_: No

_Type_: List of <a href="trafficroutingconfig.md">TrafficRoutingConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeBasedCanary

_Required_: No

_Type_: List of <a href="timebasedcanary.md">TimeBasedCanary</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeBasedLinear

_Required_: No

_Type_: List of <a href="timebasedlinear.md">TimeBasedLinear</a>

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

