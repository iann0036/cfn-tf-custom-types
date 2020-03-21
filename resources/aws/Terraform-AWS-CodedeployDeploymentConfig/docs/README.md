# Terraform::AWS::CodedeployDeploymentConfig

CloudFormation equivalent of aws_codedeploy_deployment_config

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::CodedeployDeploymentConfig",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#computeplatform" title="ComputePlatform">ComputePlatform</a>" : <i>String</i>,
        "<a href="#deploymentconfigid" title="DeploymentConfigId">DeploymentConfigId</a>" : <i>String</i>,
        "<a href="#deploymentconfigname" title="DeploymentConfigName">DeploymentConfigName</a>" : <i>String</i>,
        "<a href="#minimumhealthyhosts" title="MinimumHealthyHosts">MinimumHealthyHosts</a>" : <i>[ &lt;a href=&#34;minimumhealthyhosts.md&#34;&gt;MinimumHealthyHosts&lt;/a&gt;, ... ]</i>,
        "<a href="#trafficroutingconfig" title="TrafficRoutingConfig">TrafficRoutingConfig</a>" : <i>[ &lt;a href=&#34;trafficroutingconfig.md&#34;&gt;TrafficRoutingConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#timebasedcanary" title="TimeBasedCanary">TimeBasedCanary</a>" : <i>[ &lt;a href=&#34;timebasedcanary.md&#34;&gt;TimeBasedCanary&lt;/a&gt;, ... ]</i>,
        "<a href="#timebasedlinear" title="TimeBasedLinear">TimeBasedLinear</a>" : <i>[ &lt;a href=&#34;timebasedlinear.md&#34;&gt;TimeBasedLinear&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::CodedeployDeploymentConfig
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#computeplatform" title="ComputePlatform">ComputePlatform</a>: <i>String</i>
    <a href="#deploymentconfigid" title="DeploymentConfigId">DeploymentConfigId</a>: <i>String</i>
    <a href="#deploymentconfigname" title="DeploymentConfigName">DeploymentConfigName</a>: <i>String</i>
    <a href="#minimumhealthyhosts" title="MinimumHealthyHosts">MinimumHealthyHosts</a>: <i>
      - &lt;a href=&#34;minimumhealthyhosts.md&#34;&gt;MinimumHealthyHosts&lt;/a&gt;</i>
    <a href="#trafficroutingconfig" title="TrafficRoutingConfig">TrafficRoutingConfig</a>: <i>
      - &lt;a href=&#34;trafficroutingconfig.md&#34;&gt;TrafficRoutingConfig&lt;/a&gt;</i>
    <a href="#timebasedcanary" title="TimeBasedCanary">TimeBasedCanary</a>: <i>
      - &lt;a href=&#34;timebasedcanary.md&#34;&gt;TimeBasedCanary&lt;/a&gt;</i>
    <a href="#timebasedlinear" title="TimeBasedLinear">TimeBasedLinear</a>: <i>
      - &lt;a href=&#34;timebasedlinear.md&#34;&gt;TimeBasedLinear&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComputePlatform

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentConfigId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentConfigName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinimumHealthyHosts

_Required_: No

_Type_: List of &lt;a href=&#34;minimumhealthyhosts.md&#34;&gt;MinimumHealthyHosts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficRoutingConfig

_Required_: No

_Type_: List of &lt;a href=&#34;trafficroutingconfig.md&#34;&gt;TrafficRoutingConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeBasedCanary

_Required_: No

_Type_: List of &lt;a href=&#34;timebasedcanary.md&#34;&gt;TimeBasedCanary&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeBasedLinear

_Required_: No

_Type_: List of &lt;a href=&#34;timebasedlinear.md&#34;&gt;TimeBasedLinear&lt;/a&gt;

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

Returns the &lt;code&gt;DeploymentConfigId&lt;/code&gt; value.

