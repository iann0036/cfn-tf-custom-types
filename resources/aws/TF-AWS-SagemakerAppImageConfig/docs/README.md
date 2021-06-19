# TF::AWS::SagemakerAppImageConfig

Provides a Sagemaker App Image Config resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::SagemakerAppImageConfig",
    "Properties" : {
        "<a href="#appimageconfigname" title="AppImageConfigName">AppImageConfigName</a>" : <i>String</i>,
        "<a href="#kernelgatewayimageconfig" title="KernelGatewayImageConfig">KernelGatewayImageConfig</a>" : <i>[ <a href="kernelgatewayimageconfigdefinition.md">KernelGatewayImageConfigDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::SagemakerAppImageConfig
Properties:
    <a href="#appimageconfigname" title="AppImageConfigName">AppImageConfigName</a>: <i>String</i>
    <a href="#kernelgatewayimageconfig" title="KernelGatewayImageConfig">KernelGatewayImageConfig</a>: <i>
      - <a href="kernelgatewayimageconfigdefinition.md">KernelGatewayImageConfigDefinition</a></i>
</pre>

## Properties

#### AppImageConfigName

The name of the App Image Config.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KernelGatewayImageConfig

_Required_: No

_Type_: List of <a href="kernelgatewayimageconfigdefinition.md">KernelGatewayImageConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

